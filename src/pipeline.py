from src.cleaning import  loadDataFrame, removeDublicate, cleanData, saveOutput
import logging
logger = logging.getLogger(__name__)
def process_all_file(files: list):
    for file in files:
        if not file["loadDataFrame"]:
            continue
        
        data = loadDataFrame(file)

        processed_data = data.copy()

        processed_data = removeDublicate(processed_data)
        processed_data = cleanData(processed_data)                
        saveOutput(processed_data, file)
        logger.info(f"Processed {len(files)} files successfully")
