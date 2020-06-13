class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def write(self, text_data):
        x = open(self.file_name, "a")
        x.write(text_data)

    def read(self):
        x = open(self.file_name)
        return x.read()