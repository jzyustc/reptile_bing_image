import logging


class ReptileLog:

	def __init__(self, name: str, root_path: str, info_log_filename, error_log_filename, show_info=True, file_mode="a",
				 encode_mode="GBK"):
		# INFO : stored in root_path/info_log_filename, also show in control if show_info==True
		# Warning/Error : stored in root_path/error_log_filename

		# 创建一个logger日志对象
		self.logger = logging.getLogger(name + '_logger')
		self.logger.setLevel(logging.DEBUG)  # 设置默认的日志级别

		# vars
		self.info_log_path = root_path + "/" + info_log_filename
		self.error_log_path = root_path + "/" + error_log_filename
		self.file_mode = file_mode
		self.encode_mode = encode_mode

		# settings
		self.info_log_file_setting()
		self.error_log_file_setting()
		if show_info: self.info_log_control_setting()

	def info_log_file_setting(self):
		info_log = logging.FileHandler(self.info_log_path, mode=self.file_mode, encoding=self.encode_mode)
		info_log.setLevel(logging.INFO)
		info_log.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s:  %(message)s'))
		self.logger.addHandler(info_log)

	def info_log_control_setting(self):
		info_log = logging.StreamHandler()
		info_log.setLevel(logging.INFO)
		info_log.setFormatter(logging.Formatter('%(message)s'))
		self.logger.addHandler(info_log)

	def error_log_file_setting(self):
		err_log = logging.FileHandler(self.error_log_path, mode=self.file_mode, encoding=self.encode_mode)
		err_log.setLevel(logging.WARNING)
		err_log.setFormatter(
			logging.Formatter('%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'))
		self.logger.addHandler(err_log)

	def error_log(self, message):
		self.logger.error(message)

	def warning_log(self, message):
		self.logger.warning(message)

	def info_log(self, message):
		self.logger.info(message)
