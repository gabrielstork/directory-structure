import os
import emoji


class Tree:
    def __init__(self, directory):
        self.directory = directory
        self.base = os.path.basename(self.directory)
        self.folder = ''
        self.file = ''

    def __str__(self):
        self.base = emoji.emojize(f':open_file_folder: {self.base}\n')

        folders = [folder for folder in os.listdir(self.directory)
                   if os.path.isdir(os.path.join(self.directory, folder))]

        files = [file for file in os.listdir(self.directory)
                 if os.path.isfile(os.path.join(self.directory, file))]

        for folder in folders:
            self.folder += emoji.emojize(f'|—:file_folder: {folder}\n')

        for file in files:
            self.file += emoji.emojize(f'|—:page_facing_up: {file}\n')

        return self.base + self.folder + self.file
