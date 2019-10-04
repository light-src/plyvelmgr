import plyvel
import json
from .logger import diff_log_header, check_diff_log


def iter_size(it):
    print('checking iterator size')
    cnt = 0
    for _ in it:
        cnt += 1
    print(cnt)

    return cnt


class DatabaseManager:

    def __init__(self, path):
        self._db_path = path
        self._db = plyvel.DB(path)

    def set_value_by_key(self, key, value):
        self._db.put(bytes.fromhex(key), bytes.fromhex(value))

    def get_value_by_key(self, key):
        return self._db.get(bytes.fromhex(key))

    def erase_value_by_key(self, key):
        self._db.delete(bytes.fromhex(key))

    def compare_db(self, db_path):
        cmp_db = plyvel.DB(db_path)
        diff_log_header()

        origin_iter_size = iter_size(self._db.iterator())
        cmp_iter_size = iter_size(cmp_db.iterator())

        if origin_iter_size >= cmp_iter_size:
            std_db, compared_db = self._db, cmp_db
        else:
            std_db, compared_db = cmp_db, self._db

        db_iterator = std_db.iterator()

        print('diff_checking...')
        for key, value in db_iterator:

            if compared_db.get(key) is None or compared_db.get(key) != std_db.get(key):

                first_db_value = self._db.get(key)
                second_db_value = cmp_db.get(key)

                print('diff_detected!')

                diff_dict = {
                    'key_value': key.hex() if isinstance(key, bytes) else key,
                    f'{self._db_path} value': first_db_value.hex() if isinstance(first_db_value,
                                                                                 bytes) else first_db_value,
                    f'{db_path} value': second_db_value.hex() if isinstance(second_db_value,bytes) else second_db_value
                }

                print(key)

                log_txt = json.dumps(diff_dict, indent=4)
                check_diff_log(log_txt)

    def save_db(self):
        self._db.close()
