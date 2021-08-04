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
                lines = self.base.count('\n')

                self.base += f'\n{"  " * (lines)}|_{EMOJI_A} {directory}'

            return lines + 1
        else:
            directory = self.path.split('/')[-1]
            self.base = f'{EMOJI_A} {directory}'

            return 0

    def get_folders(self):
        folders = [folder for folder in os.listdir(self.path)
                   if os.path.isdir(os.path.join(self.path, folder))]

        return folders
    
    def get_files(self):
        files = [file for file in os.listdir(self.path)
                 if os.path.isfile(os.path.join(self.path, file))]

        return files

    def __str__(self):
        lines = self.get_base()

        folders = self.get_folders()

        for folder in folders:
            self.folder += f'\n{"  "*(lines)}|_{EMOJI_B} {folder}'

        files = self.get_files()

        for file in files:
            self.file += f'\n{"  "*(lines)}|_{EMOJI_C} {file}'

        return self.base + self.folder + self.file
