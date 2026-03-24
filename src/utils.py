import os
import logging
logger = logging.getLogger(__name__)

def fileDetail():
    directory = "data/raw/"
    logging.info(f"Checking file in {directory}")
    files = [f for f in os.listdir(directory) if f != ".gitkeep"]
    
    if len(files) == 0:
        logging.info("Add file to clean data")
        
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
            
        logging.info("File info obtained")
        return fileInfo
    else:
        raise FileNotFoundError("No file")