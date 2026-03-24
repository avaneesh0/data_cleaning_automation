import os
import pandas as pd
import numpy as np
import logging
logger = logging.getLogger(__name__)

def loadCsv(path):
    df = pd.read_csv(path)
    logging.info(f"Reading file at [{path}]")
    return df

def loadExcell(path):
    df = pd.read_excel(path , engine="openpyxl")
    logging.info(f"Reading file at [{path}]")
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
        logging.info(f"Saving cleaned file at [data/processed/{file['fileName']}]")
    else:
        extention = [".xlsx", ".xlsm", ".xltx", ".xltm"]
        for ext in extention:
            if file["fileExt"] == ext:
                data.to_excel(f"data/processed/{file['fileName']}", index=False)
                logging.info(f"Saving cleaned file at [data/processed/{file['fileName']}]")
                
def removeDublicate(data: pd.DataFrame):
    data = data.drop_duplicates()
    logging.info("Dublicates removed")
    return data

def cleanData(data: pd.DataFrame):

    for col in data.columns:
        total_Null = data[col].isnull().sum()
        if total_Null > 0:
            if data[col].dtype == object:
                data[col] = data[col].fillna("Missing")
                logging.info(f"Fill {total_Null} null value in {col} with Missing")
                
            if np.issubdtype(data[col].dtype, np.number ):
                data[col] = data[col].fillna(np.mean(data[col]))
                logging.info(f"Filled {total_Null} null value in {col} with mean")
    
    logging.info("Data cleaned")
    return data