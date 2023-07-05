import os
import cv2


class FolderLoader:
    _root = ''
    _folders = []
    _now_index = 0

    @classmethod
    def load_path(cls, path):
        if cls.check_valid_path(path):
            files = os.listdir(path)
            folders = [x for x in files if os.path.isdir(os.path.join(path, x))]
            cls._root = path
            cls._folders = folders
            cls._now_index = 0
            return cls._folders
        else:
            return []

    @classmethod
    def get_images(cls, extensions=None):
        if len(cls._folders) == 0:
            return []

        if extensions is None:
            extensions = ['.jpg', '.png']
        files = os.listdir(os.path.join(cls._root, cls._folders[cls._now_index]))
        files = [os.path.join(cls._root, cls._folders[cls._now_index], x) for x in files if x in extensions]
        return files

    @classmethod
    def load_image(cls, path):
        full_path = os.path.join(cls._root, cls._folders[cls._now_index], path)
        im_bgr = cv2.imread(full_path)
        return cv2.cvtColor(im_bgr, cv2.COLOR_BGR2RGB)

    @classmethod
    def save_image(cls, image, path, filename, size):
        bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        resized = cv2.resize(bgr, size)
        cv2.imwrite(os.path.join(path, filename), resized)
        return os.path.join(path, filename)

    @classmethod
    def save_text(cls, batch):
        text_file = cls.get_txts()
        with open(text_file[0], "w") as file:
            for stub in batch:
                line = stub['filename'] + ''.join([" %.3f" % num for num in stub['coordinates']])
                line += '\n'
                file.write(line)

    @classmethod
    def get_txts(cls, extensions=None):
        if len(cls._folders) == 0:
            return []

        if extensions is None:
            extensions = '.txt'
        files = os.listdir(os.path.join(cls._root, cls._folders[cls._now_index]))
        files = [os.path.join(cls._root, cls._folders[cls._now_index], x) for x in files if extensions in x]
        return files

    @classmethod
    def change_index(cls, index):
        cls._now_index = index

    @staticmethod
    def get_contents(full_path):
        batch = []
        with open(full_path, "r") as file:
            strings = file.readlines()
            for line in strings:
                split = line.split(' ')
                filename = split[0]
                for index in reversed(range(15)):
                    del split[index]
                del split[-1]
                float_list = [int(item.split('.')[0]) for item in split]
                content = {'filename': filename, 'coordinates': float_list}
                batch.append(content)
        return batch


    @staticmethod
    def check_valid_path(path):
        return os.path.exists(path)
