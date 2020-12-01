import asyncio
import json
from functools import partial
from lxml import etree
from datasets.utils.reptile_utils import *
from datasets.utils.Log import ReptileLog


class Reptile:
	image_urls_g = []

	def __init__(self, path: str, engine: str):

		if path[-1] != "/": path += "/"

		# config vars
		self.config = load_config(path, engine)
		self.urls_config = self.config.url_task
		self.urls_config_query = self.urls_config.query
		self.imgs_config = self.config.img_task

		# path vars
		self.root_path = self.config.root_path
		self.images_urls_path = self.root_path + self.config.images_urls_filename
		self.images_path = self.root_path + self.config.images_path

		# count vars for get_image_urls
		self.urls_count = 0
		self.start_count = 0

		# count vars to get_image
		self.imgs_count = 0

		# Log settings
		self.logger = ReptileLog(path.split("/", 1)[0], self.root_path, self.config.info_log_filename,
								 self.config.error_log_filename, file_mode="w", encode_mode="GBK")

	# callback of get_image_urls
	def urls_callback(self, task):

		raw_html = task.result()
		html = etree.HTML(raw_html, etree.HTMLParser())
		raw_urls = html.xpath('//a[@class="iusc"]/@m')

		# get size_list of each image
		# raw_sizes = html.xpath('//span/@data-tooltip')

		# get new urls that image size >= (512,512)
		img_urls = []
		for i in range(len(raw_urls)):
			# to make sure size larger than (512,512) instead of larger than (512,-) and (-,512)
			# size = raw_sizes[i].split(" x ")
			# if (int(size[0]) < urls_config.image_size_w_min or int(size[1]) < urls_config.image_size_h_min): continue

			url = json.loads(raw_urls[i])["murl"]

			# judge if the url is in the image_urls_g
			if not is_in_list(self.image_urls_g, url):
				img_urls.append(url)
				self.image_urls_g.append(url)

		# save to file
		if os.path.exists(self.images_urls_path):
			add_image_urls(self.images_urls_path, img_urls)
		else:
			save_image_urls(self.images_urls_path, img_urls)

		# add count
		self.urls_count += len(img_urls)
		self.logger.info_log("get id :" + str(self.urls_count) + "  number : " + str(len(img_urls)))

	# get image urls
	def get_image_urls(self, semaphore):

		#  url_async
		tasks = []
		loop = asyncio.get_event_loop()
		for i in range(self.urls_config.query_number):
			# get url
			url = self.urls_config.base_url + "?"
			start_id = self.urls_config.start + self.start_count * self.urls_config_query.count
			self.start_count += 1
			params = {
				"q": self.urls_config_query.q,
				"first": str(start_id),
				"count": self.urls_config_query.count,
				"mmasync": self.urls_config_query.mmasync,
				"qft": self.urls_config_query.qft
			}
			url = add_params_after_url(url, params)
			self.logger.info_log(url)

			# get html
			raw_html = get_text(semaphore, url, self.logger)
			task = asyncio.ensure_future(raw_html)

			# callback, get  urls
			task.add_done_callback(partial(self.urls_callback))
			tasks.append(task)
		loop.run_until_complete(asyncio.wait(tasks))

	# download images
	def get_images(self, img_urls: [str], semaphore):

		#  img_async
		tasks = []
		loop = asyncio.get_event_loop()
		for url in img_urls:
			# get save path
			ext = find_ext_in_url(url, self.imgs_config.allowed_ext)
			image_file_path = self.images_path + "/" + str(self.imgs_count + 1) + ext
			self.imgs_count += 1

			# download
			download = get_and_save_image(semaphore, url, image_file_path, self.logger)
			task = asyncio.ensure_future(download)
			tasks.append(task)
		loop.run_until_complete(asyncio.wait(tasks))

	def reptile_urls(self):

		# add limits to async number
		semaphore = asyncio.Semaphore(self.urls_config.asyn_step)

		self.get_image_urls(semaphore)
		self.logger.info_log("image urls get successfully, totally " + str(len(self.image_urls_g)))

	def reptile_imgs(self):

		if not os.path.exists(self.images_path): os.mkdir(self.images_path)

		with open(self.images_urls_path, "r")as file:
			img_urls = file.read().split("\n")[self.imgs_config.start:]

		# add limits to async number
		semaphore = asyncio.Semaphore(self.imgs_config.asyn_step)

		# find max number of download image
		max_num = min(len(img_urls),
					  self.imgs_config.download_number) if self.imgs_config.download_number != -1 else len(img_urls)

		self.logger.info_log("Image number : " + str(max_num))
		self.get_images(img_urls[:max_num], semaphore)
