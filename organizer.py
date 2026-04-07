import os
import shutil

class FileOrganizer:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def organize(self):
        for file in os.listdir(self.source):
            file_path = os.path.join(self.source, file)

            if os.path.isfile(file_path):
                if file.endswith(".jpg") or file.endswith(".png"):
                    folder = "Images"
                elif file.endswith(".pdf") or file.endswith(".txt"):
                    folder = "Documents"
                else:
                    folder = "Others"

                dest_folder = os.path.join(self.destination, folder)
                os.makedirs(dest_folder, exist_ok=True)

                shutil.move(file_path, os.path.join(dest_folder, file))
                print("Moved:", file)