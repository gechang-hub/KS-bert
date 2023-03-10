# -*- coding: utf-8 -*-


from nlg_yongzhuo.conf.path_config import projectdir
from logging.handlers import RotatingFileHandler
import logging
import time
import os


# log目录地址
path_logs = projectdir + '/logs'
if not os.path.exists(path_logs):
    os.mkdir(path_logs)
# 全局日志格式
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
# 定义一个日志记录器
logger = logging.getLogger("NLG_YONGZHUO")
logger.setLevel(level = logging.INFO)
# 日志文件名,为启动时的日期
log_file_name = time.strftime('%Y-%m-%d', time.localtime(time.time())) + ".log"
log_name_day = os.path.join(path_logs, log_file_name)
# 文件输出, 定义一个RotatingFileHandler，最多备份32个日志文件，每个日志文件最大32K
rHandler = RotatingFileHandler(log_name_day, maxBytes = 32*1024, backupCount = 32)
rHandler.setLevel(logging.INFO)
# 日志输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
rHandler.setFormatter(formatter)
# 控制台输出
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
# logger加到handel里边
logger.addHandler(rHandler)
logger.addHandler(console)
# 所有文件共用一个logger
def get_logger_root():
    return logging.getLogger("NLG_YONGZHUO")


if __name__ == '__main__':
    logger = get_logger_root()
    logger.info("test")
