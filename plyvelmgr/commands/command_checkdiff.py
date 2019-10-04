from ..database_manager import DatabaseManager
from .command import Command


class CommandCheckDiff(Command):

    def __init__(self, sub_parser, common_parser=None):
        self.add_parser(sub_parser=sub_parser, common_parser=common_parser)

    def add_parser(self, sub_parser, common_parser):
        name = 'checkdiff'

        parser = sub_parser.add_parser(name, parents=[common_parser])
        parser.add_argument('--cmp-db', type=str, required=True)

        parser.set_defaults(func=self.run)

    def run(self, args):
        db_path = args.db
        cmp_db_path = args.cmp_db

        db = DatabaseManager(db_path)

        db.compare_db(cmp_db_path)