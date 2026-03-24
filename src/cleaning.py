import os
import pandas as pd
import numpy as np

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