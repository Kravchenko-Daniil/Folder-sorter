import os
from pathlib import Path
from itertools import chain


downloads_folder = Path("D:\Projects and Documents\Загрузки")

SUBFOLDER_NAME_TO_EXTENSIONS = {
    'video': ('mp4', 'mov', 'avi', 'mkv', 'wmv', 'mpg', 'mpeg', 'm4v', 'h264'),
    'audio': ('mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'wma'),
    'image': ('jpg', 'png', 'bmp', 'jpeg', 'svg', 'tif', 'tiff'),
    'archive': ('zip', 'rar', '7z', 'z', 'gz', 'pkg', 'deb'),
    'text': ('pdf', 'txt', 'doc', 'docx', 'rtf', 'odt'),
    'spreadsheet': ('xlsx', 'xls', 'xlsm', 'csv', 'xml', 'json'),
    'presentation': ('pptx', 'ppt'),
    'book': ('fb2', 'epub', 'mobi'),
    'gif': ('gif',),
    'python code': ('ipynb', 'py'),
    '1c bases': ('dt',),
    'exe files': ('exe',),
    'html': ('html',),
    'java code': ('java',),
    'other': ('jar', 'dat', 'q1c', 'msi', 'bp1', 'rdp')
    # 'subfolder-name': ('extension', 'another-extension')
}

EXTENSIONS = tuple(chain.from_iterable(
    (SUBFOLDER_NAME_TO_EXTENSIONS.values())))

class Sorter:
    def __init__(self, path):
        self.path = path

    def get_subfolder_name_by_extension(self, extension: str) -> str:
        for subfoler_name, tutple_of_extensions in SUBFOLDER_NAME_TO_EXTENSIONS.items():
            if extension in tutple_of_extensions:
                return subfoler_name

    def get_folders_path(self):
        fp = [f.path for f in os.scandir(self.path) if not f.is_dir()]
        return fp

    def create_subfolders(self):
        for name in SUBFOLDER_NAME_TO_EXTENSIONS.keys():
            subfolder_name = self.path / name
            if not subfolder_name.exists():
                os.mkdir(subfolder_name)

    def sorted_folders(self):
        self.create_subfolders()
        for file in self.get_folders_path():
            filepath = Path(file)
            extension = file.split('.')[-1]

            if extension in EXTENSIONS:
                os.rename(filepath, Path(self.path, self.get_subfolder_name_by_extension(extension), filepath.name))


if __name__ == "__main__":
    s = Sorter(downloads_folder)
    s.sorted_folders()
    # print(s.get_folders_path())