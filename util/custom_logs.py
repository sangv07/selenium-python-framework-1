import inspect
import logging

def CustomLogs(log_level=logging.DEBUG):

    # Gets the name of the class / method from where this method is called
    # every class/method that call this logs will provide their name in log file to know which class/method's logs
    logger_name = inspect.stack()[1][3]
    logs = logging.getLogger(logger_name)

    # By default, log all messages
    logs.setLevel(logging.DEBUG)

    # creating file_handler
    file_handler = logging.FileHandler("automation.log", mode='w')
    file_handler.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  datefmt='%m/%d/%y %I:%M:%S %p')
    file_handler.setFormatter(formatter)
    logs.addHandler(file_handler)

    return logs

