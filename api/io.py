import os


class FolderLoader:
    _root = ''
    _folders = []
    _now_index = 0

    @classmethod
    def load_path(cls, path):
        if cls.check_valid_path(path):
            files = os.listdir(path)
            folders = [x for x in files if os.path.isdir(x)]
            cls._root = path
            cls._folders = folders
            cls._now_index = 0
            return cls._folders
        else:
            return []

    @classmethod
    def get_images(cls, extensions=None):
        if extensions is None:
            extensions = ['.jpg', '.png']
        files = os.listdir(os.path.join(cls._root, cls._folders[cls._now_index]))
        files = [os.path.join(cls._root, cls._folders[cls._now_index], x) for x in files if x in extensions]
        return files

    @classmethod
    def get_txts(cls, extensions=None):
        if extensions is None:
            extensions = ['.txt', '.bat']
        files = os.listdir(os.path.join(cls._root, cls._folders[cls._now_index]))
        files = [os.path.join(cls._root, cls._folders[cls._now_index], x) for x in files if x in extensions]
        return files

    @staticmethod
    def check_valid_path(path):
        return os.path.exists(path)
