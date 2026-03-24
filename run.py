from src.utils import fileDetail
from src.pipeline import process_all_file

        
def main():
    files = fileDetail()
    process_all_file(files)

if __name__ == "__main__":
    main()




   
        