import logging


def setup_logging(log_file='./log/logging.log'):
    # 创建 Formatter 实例
    formatter = logging.Formatter('%(levelname)-8s %(message)s')
    # 创建 FileHandler 实例
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setFormatter(formatter)
    # 创建 Logger 实例
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    # 添加 FileHandler 到 Logger
    log.addHandler(file_handler)
    return log

