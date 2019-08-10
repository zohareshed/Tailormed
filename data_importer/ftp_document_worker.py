import os


class FtpDocumentWorker:
    def __init__(self, root, suffix):
        self.root = root
        self.suffix = suffix

    def get_files(self) -> list:
        """
        This method returns all the files in the root directory with the correct suffix.
        """
        files = []
        for file in os.listdir(self.root):
            if file.endswith(f".{self.suffix}"):
                files.append(os.path.join(self.root, file))
        return files

    def move_file(self, old_file: str, new_sub_dir: str):
        """
        This method moves a file to an existent subdir
        :param old_file: file name
        :param new_sub_dir: new subdir
        :return:
        """
        full_old_path = os.path.join(self.root, old_file)
        full_new_path = os.path.join(self.root, new_sub_dir, old_file)
        os.rename(full_old_path, full_new_path)

