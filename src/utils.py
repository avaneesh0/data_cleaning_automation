import os

def fileDetail():
    directory = "data/raw/"
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    if files:
        fileInfo = []
        for f in files:
            
            ext = os.path.splitext(f)
            filePath = directory + f
            
            if ext[1] in [".csv",".xlsx", ".xlsm", ".xltx", ".xltm"]:
                
                file = {
                "fileName": f,
                "filePath": filePath,
                "fileExt": ext[1],
                "loadDataFrame": True
                }
                
            else:
                
                file = {
                    "fileName": f,
                    "filePath": filePath,
                    "fileExt": ext[1],
                    "loadDataFrame": False
                }
                
            fileInfo.append(file)
        print(fileInfo)
        return fileInfo
    else:
        raise FileNotFoundError("No file")