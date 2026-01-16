import datetime
import os
import logging
import argparse

from renamefiles.renamefunctions import RenameFunctions


class Application:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        parser = argparse.ArgumentParser(description="Mass Rename Files and Keep Extension")

        parser.add_argument("-d", "--dir", help="Pass the Directory of Files you want to rename", required=True)
        parser.add_argument("-n", "--name", help="The New Name you want to use", required=True)
        parser.add_argument("-k", "--keeporgname", default=False,
                            help="Switch to keep the original name, but put the new name in front")
        args = vars(parser.parse_args())

        if args['dir']:
            self.TargetDirectory = args['dir']
        if args['name']:
            self.NewName = args['name']
        if args ['keeporgname']:
            self.KeepOriginalName = args['keeporgname']
        else:
            self.KeepOriginalName = False

    def main(self):
        try:
            RenameFunctions.rename_files_keep_extension(self.TargetDirectory, self.NewName,
                                                        keep_org_name=self.KeepOriginalName)
        except Exception as ex:
            logging.error(ex)
            exit(1)