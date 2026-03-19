import os

directory = "data/"
def fileName():
    if os.listdir(directory):
        file = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        if file:
            ext = os.path.splitext(file[0])
            filePath = directory + file[0]
            print(filePath)
            fileInfo = {
                "fileName": file[0],
                "filePath": filePath,
                "fileExt": ext[1]
            }
            return fileInfo
        else:
            print("no file")
    else:
        print("empty")