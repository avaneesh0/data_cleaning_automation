import os
import pandas as pd
import numpy as np

def fileDetail():
    directory = "data/"
    file = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    if file:
        ext = os.path.splitext(file[0])
        filePath = directory + file[0]
        
        fileInfo = {
            "fileName": file[0],
            "filePath": filePath,
            "fileExt": ext[1]
        }
        print(fileInfo)
        return fileInfo
    else:
        raise FileNotFoundError("No file")

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
        data.to_csv(f"output/{file['fileName']}")
    else:
        extention = [".xlsx", ".xlsm", ".xltx", ".xltm"]
        for ext in extention:
            if file["fileExt"] == ext:
                data.to_excel(f"output/{file['fileName']}")
                
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