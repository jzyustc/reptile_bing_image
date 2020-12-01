# -*- coding: utf-8 -*-
import random
import aiohttp
from pyhocon import ConfigFactory


def random_ip():
	a = random.randint(1, 255)
	b = random.randint(1, 255)
	c = random.randint(1, 255)
	d = random.randint(1, 255)
	return str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d)


def add_header():
	return {"Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7", "Proxy-Connection": "keep-alive",
			'User-Agent': 'Mozilla/5.0 (Windows NT 7.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
			'X-Forwarded-For': random_ip()}


async def get_text(semaphore, url: str, logger):
	try:
		async with semaphore:
			async with aiohttp.ClientSession() as session:
				async with await session.get(url=url, headers=add_header()) as response:
					page_text = await response.text()  # read()  json()
					return page_text
	except Exception as e:
		for content in e.args:
			logger.error_log(str(content))
		logger.error_log("error url : " + url)


async def get_and_save_image(semaphore, url: str, save_path: str, logger, chunk_size=1024):
	try:
		async with semaphore:
			async with aiohttp.ClientSession() as session:
				async with session.get(url, headers=add_header()) as resp:
					with open(save_path, 'wb') as file:
						while True:
							chunk = await resp.content.read(chunk_size)
							if not chunk:
								break
							file.write(chunk)
					logger.info_log(save_path + " over")
	except Exception as e:
		for content in e.args:
			logger.error_log(str(content))
		logger.error_log("error url : " + url)


def save_image_urls(file_path: str, image_urls: [str]):
	with open(file_path, "w") as file:
		for url in image_urls:
			url += '\n'
			file.write(url)
		file.close()


def add_image_urls(file_path: str, image_urls: [str]):
	with open(file_path, "a") as file:
		for url in image_urls:
			url += '\n'
			file.write(url)
		file.close()


def load_config(root_path: str, engine: str):
	return ConfigFactory.parse_file(root_path + "/reptile_" + engine + ".conf")


def add_params_after_url(url: str, params):
	for key in params:
		params_in_line = key + "=" + str(params[key]) + "&"
		url += params_in_line
	return url[:-1]


def find_ext_in_url(url: str, allowed_ext: [str]):
	for ext in allowed_ext:
		if (url.lower().find(ext) != -1): return ext
	return ".png"


def is_in_list(list: [], elem):
	return elem in list
