import os
import requests
import zipfile
from io import BytesIO

# URL del dataset
URL = "https://www.kaggle.com/api/v1/datasets/download/diishasiing/revenue-for-cab-drivers/"

# Nome della cartella target per salvare il file
DATA_DIR = "data"

# Nome del file da estrarre
TARGET_FILE = "data.csv"

def download_and_extract_data(url, data_dir, target_file):
    # Crea la cartella 'data' se non esiste
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"Created directory: {data_dir}")
    
    # Scarica il file zip dal link
    print(f"Downloading data from {url}...")
    response = requests.get(url)
    if response.status_code == 200:
        print("Download successful.")
    else:
        raise Exception(f"Failed to download file: {response.status_code}")
    
    # Apri il file zip in memoria
    with zipfile.ZipFile(BytesIO(response.content)) as z:
        # Lista dei file contenuti nello zip
        files = z.namelist()
        print(f"Files in archive: {files}")
        
        # Controlla se il file target esiste nello zip
        if target_file not in files:
            raise FileNotFoundError(f"{target_file} not found in the archive.")
        
        # Estrai il file specificato
        print(f"Extracting {target_file}...")
        z.extract(target_file, data_dir)
        print(f"{target_file} extracted to {data_dir}.")
    
    # Percorso completo del file estratto
    extracted_file_path = os.path.join(data_dir, target_file)
    print(f"Data is ready at {extracted_file_path}")
    return extracted_file_path

if __name__ == "__main__":
    try:
        download_and_extract_data(URL, DATA_DIR, TARGET_FILE)
    except Exception as e:
        print(f"Error: {e}")
