import pathlib
import emoji


EMOJI_BASE = emoji.emojize(':open_file_folder:')
EMOJI_FOLDER = emoji.emojize(':file_folder:')
EMOJI_FILE = emoji.emojize(':page_facing_up:')


class Tree:
    def __init__(self, path: str, absolute: bool = False) -> None:
        self.path = pathlib.Path(path)
        self.absolute = absolute

        self._lines = 0
        self._base = []
        self._folder = []
        self._file = []

    def _space(self) -> str:
        return f'\n{"  " * self._lines}'

    def _get_base(self) -> None:
        self.path = self.path.resolve()

        if self.absolute:
            if isinstance(self.path, pathlib.WindowsPath):
                self._base.append(f'{EMOJI_BASE} {self.path.drive}')
            elif isinstance(self.path, pathlib.PosixPath):
                self._base.append(f'{EMOJI_BASE} {self.path.root}')

            directories = self.path.parts[1:]

            for directory in directories:
                self._base.append(f'{self._space()}|_{EMOJI_BASE} {directory}')
                self._lines = len(self._base) - 1
        else:
            directory = self.path.name
            self._base.append(f'{EMOJI_BASE} {directory}')

    def _get_folders(self) -> None:
        for folder in self.path.iterdir():
            if folder.is_dir():
                self._folder.append(
                    f'{self._space()}|_{EMOJI_FOLDER} {folder.name}'
                )

    def _get_files(self) -> None:
        for file in self.path.iterdir():
            if file.is_file():
                self._file.append(
                    f'{self._space()}|_{EMOJI_FILE} {file.name}'
                )

    def __str__(self) -> str:
        self._get_base()
        self._base = ''.join(self._base)

        self._get_folders()
        self._folder = ''.join(self._folder)

        self._get_files()
        self._file = ''.join(self._file)

        return self._base + self._folder + self._file
