'''
用于输出日志文件
'''
import logging
from logging.handlers import RotatingFileHandler
import os


def print2log(infotxt, maxbytes=30 * 1024 * 1024):
    '''

    :param infotxt: txt 需要写入的信息
    :param maxbytes: int 每个log文件的最大容量 默认10MB
    :return:
    '''
    # 创建一个logger
    logger = logging.getLogger()
    logger.setLevel(logging.WARNING)

    # 创建一个handler，用于写入日志文件
    log_path = os.path.join(os.getcwd(), 'Logs')
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    logfile = log_path + 'info.log'
    rh = RotatingFileHandler(filename=logfile, maxBytes=maxbytes, backupCount=3, encoding='utf-8')
    rh.setLevel(logging.WARNING)  # 输出到file的log等级的开关
    # 定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    rh.setFormatter(formatter)
    logger.addHandler(rh)
    # 创建一个handler，用于写入console
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING)  # 输出到console的log等级的开关
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    # 全部用warning等级，则全部输出
    logger.warning(infotxt)
    # 每次输出完要清内存
    logger.removeHandler(ch)
    logger.removeHandler(rh)


if __name__ == "__main__":
    infotxt = 'hello world'
    print2log(infotxt)
