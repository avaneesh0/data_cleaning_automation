from src.utils import fileDetail
from src.pipeline import process_all_file
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
        
def main():
    files = fileDetail()
    process_all_file(files)

if __name__ == "__main__":
    main()




   
        