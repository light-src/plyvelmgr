class Logger:

    def __init__(self, db_log_path, db_diff_log_path):
        self.filepath = db_log_path
        self.db_diff_path = db_diff_log_path

    def set_db_log(self, key, value):
        with open(self.filepath, mode='a+',encoding='utf-8') as file:
            file.write(f'set db key={key}, value={value}\n')

    def erase_db_log(self, key, value):
        with open(self.filepath, mode='a+', encoding='utf-8') as file:
            file.write(f'erase db key={key}, value={value}\n')

    def check_diff_log(self, log_txt):
        with open(self.db_diff_path, mode='a+', encoding='utf-8') as file:
            file.write(log_txt)

    def diff_start_indicator(self):
        with open(self.db_diff_path, mode='a+', encoding='utf-8') as file:
            file.write('====================================================================================')


logger = Logger('plyvelmgr.log', 'plyvelmgr_diff_check.log')


def set_db_log(key, value):
    logger.set_db_log(key, value)


def erase_db_log(key, value):
    logger.erase_db_log(key, value)


def check_diff_log(json_txt):
    logger.check_diff_log(json_txt)


def diff_log_header():
    logger.diff_start_indicator()
