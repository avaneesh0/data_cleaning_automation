## 🧹 Data Cleaning Automation

A Python-based automation tool that cleans multiple raw data files with a single command.

---

## 🚀 Overview

This project automates the data cleaning process.
Just place your raw files in the `data/raw` folder, run the script, and get cleaned data in the `data/processed` folder.

---

## 📂 Project Structure

```
DATA_CLEANING_AUTOMATION/

data/
  raw/          # Add your raw files here
  processed/    # Cleaned files will be saved here

src/
  cleaning.py
  pipeline.py
  utils.py
  validation.py

validator/      # Validation file will be there

run.py          # Main script to run the project
requirements.txt
README.md
```

---

## ⚙️ Features

* Clean multiple files automatically
* Remove duplicate records
* Clean and process data
* Save cleaned output files
* Fully automated pipeline
* Create validation report

---

## ▶️ How to Use

### 1. Clone the repository

```
git clone https://github.com/avaneesh0/data_cleaning_automation
cd DATA_CLEANING_AUTOMATION
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Add your data

Put all raw files inside:

```
data/raw/
```

### 4. Run the script

```
python run.py
```

### 5. Get output

Cleaned files will be saved in:

```
data/processed/
```

---

## 🧠 How It Works

1. Reads all files from `data/raw`
2. Processes each file through a cleaning pipeline:

   * Load data
   * Remove duplicates
   * Apply cleaning functions
3. Saves cleaned files to `data/processed`
4. Prepare validation report

---

## 🛠️ Tech Stack

* Python
* Pandas
* Numpy

---

## 📌 Notes

* This only work for files in formate CSV, Excel.
* Other format will be ignore by the algorithem

---

## 🔥 Future Improvements

* Add CLI arguments (custom input/output paths)
* Support more file formats
