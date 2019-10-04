from ..database_manager import DatabaseManager
from .command import Command


class CommandGetByKey(Command):

    def __init__(self, sub_parser, common_parser=None):
        self.add_parser(sub_parser=sub_parser, common_parser=common_parser)

    def add_parser(self, sub_parser, common_parser):
        name = 'getbykey'

        parser = sub_parser.add_parser(name, parents=[common_parser])
        parser.add_argument('--key', type=str, required=True)

        parser.set_defaults(func=self.run)

    def run(self, args):
        db_path = args.db
        key = args.key

        db = DatabaseManager(db_path)

        print(db.get_value_by_key(key))