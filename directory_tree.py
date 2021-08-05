import os
import emoji


EMOJI_A = emoji.emojize(':open_file_folder:')
EMOJI_B = emoji.emojize(':file_folder:')
EMOJI_C = emoji.emojize(':page_facing_up:')


class Tree:
    def __init__(self, path, complete=False):
        self.path = path
        self.complete = complete

        self.folder = ''
        self.file = ''

    def get_base(self):
        if self.complete:
            drive = self.path.split('/')[0]
            self.base = f'{EMOJI_A} {drive}'

            directories = self.path.split('/')[1:]

            for directory in directories:
                self.lines = self.base.count('\n')

                self.base += f'\n{"  " * (self.lines)}|_{EMOJI_A} {directory}'

            self.lines += 1
        else:
            directory = self.path.split('/')[-1]
            self.base = f'{EMOJI_A} {directory}'

            self.lines = 0

    def get_folders(self):
        folders = [folder for folder in os.listdir(self.path)
                   if os.path.isdir(os.path.join(self.path, folder))]

        for folder in folders:
            self.folder += f'\n{"  "*(self.lines)}|_{EMOJI_B} {folder}'

    def get_files(self):
        files = [file for file in os.listdir(self.path)
                 if os.path.isfile(os.path.join(self.path, file))]

        for file in files:
            self.file += f'\n{"  "*(self.lines)}|_{EMOJI_C} {file}'

    def __str__(self):
        self.get_base()
        self.get_folders()
        self.get_files()

        return self.base + self.folder + self.file
