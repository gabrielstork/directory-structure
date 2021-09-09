import pathlib
import emoji


EMOJI_BASE = emoji.emojize(':open_file_folder:')
EMOJI_FOLDER = emoji.emojize(':file_folder:')
EMOJI_FILE = emoji.emojize(':page_facing_up:')


class Tree:
    """
    A class to generate directory tree structures.

    Parameters
    ----------
    path : str
        The directory path, it can be in any valid format.
    absolute : bool, default False
        Set it to True if you want to use the absolute path.
    """
    def __init__(self, path: str, absolute: bool = False) -> None:
        self.path = pathlib.Path(path)
        self.absolute = absolute

        self._lines = 0
        self._base = []
        self._folders = []
        self._files = []
        self._tree = self._make_tree()

    def _space(self) -> str:
        """
        Return a string containing spaces according to the folder or file
        location.

        Returns:
        --------
        spaces : str
            String containing spaces.
        """
        spaces = f'\n{"  " * self._lines}'
        return spaces

    def _get_base(self) -> None:
        """
        Depending on the absolute attribute, get all or only the last folder
        of the path.
        """
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
        """
        Get all folders, in alphabetical order, from the directory content.
        """
        for folder in self.path.iterdir():
            if folder.is_dir():
                self._folders.append(
                    f'{self._space()}|_{EMOJI_FOLDER} {folder.name}'
                )

    def _get_files(self) -> None:
        """
        Get all files, in alphabetical order, from the directory content.
        """
        for file in self.path.iterdir():
            if file.is_file():
                self._files.append(
                    f'{self._space()}|_{EMOJI_FILE} {file.name}'
                )

    def _make_tree(self) -> str:
        """
        Call other private methods and then sum its joined results to make the
        directory tree structure.

        Returns:
        --------
        tree : str
            Complete directory tree structure.
        """
        self._get_base()
        self._base = ''.join(self._base)

        self._get_folders()
        self._folders = ''.join(self._folders)

        self._get_files()
        self._files = ''.join(self._files)

        tree = self._base + self._folders + self._files
        return tree

    def __str__(self) -> str:
        return self._tree
