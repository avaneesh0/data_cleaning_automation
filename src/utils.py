import os
import pandas as pd
import numpy as np

def fileDetail():
    directory = "data/raw/"
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    if files:
        fileInfo = []
        for f in files:
            ext = os.path.splitext(f)
            filePath = directory + f
            
            file = {
                "fileName": f,
                "filePath": filePath,
                "fileExt": ext[1]
            }
            fileInfo.append(file)
        print(fileInfo)
        return fileInfo
    else:
        raise FileNotFoundError("No file")

fileDetail()

def loadCsv(path):
    df = pd.read_csv(path)
    return df

def loadExcell(path):
    df = pd.read_excel(path , engine="openpyxl")
    return df

def loadDataFrame(file):
    if file["fileExt"] == ".csv":
        data = loadCsv(os.path.join("./", file["filePath"]))
        return data
    else: 
        supportedExt = [".xlsx", ".xlsm", ".xltx", ".xltm"]
        for ext in supportedExt:
            if file["fileExt"] == ext:
                data = loadExcell(os.path.join("./", file["filePath"]))
                return data
                
        try:
            data
        except:
            raise TypeError("No csv and excell file")
        
def saveOutput(data: pd.DataFrame, file: dict):
    if file["fileExt"] == ".csv":
        data.to_csv(f"data/processed/{file['fileName']}", index=False)
    else:
        extention = [".xlsx", ".xlsm", ".xltx", ".xltm"]
        for ext in extention:
            if file["fileExt"] == ext:
                data.to_excel(f"data/processed/{file['fileName']}", index=False)
                
def removeDublicate(data: pd.DataFrame):
    data = data.drop_duplicates()
    return data

def cleanData(data: pd.DataFrame):
    for col in data.columns:
        if data[col].isnull().sum() > 0:
            if data[col].dtype == object:
                data[col] = data[col].fillna("Missing")
                
            if np.issubdtype(data[col].dtype, np.number ):
                data[col] = data[col].fillna(np.mean(data[col]))
    
    return data

def process_all_file(files: list):
    for file in files:
        print(file)
        data = loadDataFrame(file)

        processed_data = data.copy()

        removeDublicate(processed_data)
        cleanData(processed_data)                
        saveOutput(processed_data, file)