import os
import emoji


EMOJI_A = emoji.emojize(':open_file_folder:')
EMOJI_B = emoji.emojize(':file_folder:')
EMOJI_C = emoji.emojize(':page_facing_up:')


class Tree:
    def __init__(self, directory, complete=False):
        self.directory = directory
        self.complete = complete

        self.base = f'{EMOJI_A} {os.path.basename(self.directory)}'
        self.folder = ''
        self.file = ''

    def get_complete_base(self):
        directories = self.directory.split('/')
        self.base = f'{EMOJI_A} {directories[0]}'

        for directory in directories[1:]:
            lines = self.base.count('\n')
            
            self.base += f'\n{"  " * (lines)}|_{EMOJI_A} {directory}'
        
        return lines + 1

    def get_folders(self):
        folders = [folder for folder in os.listdir(self.directory)
                   if os.path.isdir(os.path.join(self.directory, folder))]

        return folders
    
    def get_files(self):
        files = [file for file in os.listdir(self.directory)
                 if os.path.isfile(os.path.join(self.directory, file))]

        return files

    def __str__(self):
        if self.complete:
            lines = self.get_complete_base()
        else:
            lines = 0

        folders = self.get_folders()

        for folder in folders:
            self.folder += f'\n{"  "*(lines)}|_{EMOJI_B} {folder}'

        files = self.get_files()

        for file in files:
            self.file += f'\n{"  "*(lines)}|_{EMOJI_C} {file}'

        return self.base + self.folder + self.file
