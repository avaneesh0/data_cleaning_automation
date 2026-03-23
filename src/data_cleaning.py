import pandas as pd
import numpy as np
from utils import fileDetail, loadDataFrame, saveOutput, removeDublicate, cleanData

file = fileDetail()
data = loadDataFrame(file)

processed_data = data.copy()

removeDublicate(processed_data)
cleanData(processed_data)                
saveOutput(processed_data, file)



   
        