from ..database_manager import DatabaseManager
from ..logger import erase_db_log
from .command import Command


class CommandSetByKey(Command):

    def __init__(self, sub_parser, common_parser=None):
        self.add_parser(sub_parser=sub_parser, common_parser=common_parser)

    def add_parser(self, sub_parser, common_parser):
        name = 'setbykey'

        parser = sub_parser.add_parser(name, parents=[common_parser])
        parser.add_argument('--key', type=str, required=True)
        parser.add_argument('--value', required=True)

        parser.set_defaults(func=self.run)

    def run(self, args):
        db_path = args.db
        key = args.key
        value = args.value

        db = DatabaseManager(db_path)
        db.set_value_by_key(key, value)
        print(f'db set {key} : {value}')
        erase_db_log(key, value)

        db.save_db()
