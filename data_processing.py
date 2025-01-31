from constants import MIN_NOTA, MAX_NOTA, CSV_FILENAME
import pandas as pd

# Function that return the number of students
def leer_csv():
    try:
        df = pd.read_csv(CSV_FILENAME)
        return df
    except FileNotFoundError:
        print(f"El archivo {CSV_FILENAME} no se encuentra.")
        return None

def revisar_nota(nota):
    if MIN_NOTA <= nota <= MAX_NOTA:
        return "N"
    else:
        return "S"