import logging
import os

def get_logger(name="selenium-test", log_file="logs/test.log"):
    logger = logging.getLogger(name)
    if not logger.handlers:  # tránh thêm handler nhiều lần
        logger.setLevel(logging.INFO)

        # Log ra console
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(ch)

        # Tạo thư mục logs nếu chưa có
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

        # Log ra file
        fh = logging.FileHandler(log_file, encoding="utf-8")
        fh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(fh)

    return logger
