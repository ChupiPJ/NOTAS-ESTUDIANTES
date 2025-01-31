import pandas as pd
from utils import revisar_nota
from constants import APROBADO, CSV_FILENAME

def validar_notas(df):

    df.columns = df.columns.str.strip()

    """Comprueba que las notas están en el rango permitido y corrige valores inválidos."""
    errores = df[(df["Nota_Parcial_1"] < 0) | (df["Nota_Parcial_1"] > 5) |
                 (df["Nota_Parcial_2"] < 0) | (df["Nota_Parcial_2"] > 5)]
    
    if not errores.empty:
        print("⚠ Se han encontrado notas inválidas:")
        print(errores)

        df.loc[df["Nota_Parcial_1"] < 0, "Nota_Parcial_1"] = 0
        df.loc[df["Nota_Parcial_1"] > 5, "Nota_Parcial_1"] = 5
        df.loc[df["Nota_Parcial_2"] < 0, "Nota_Parcial_2"] = 0
        df.loc[df["Nota_Parcial_2"] > 5, "Nota_Parcial_2"] = 5

        print("\n✅ Notas corregidas automáticamente dentro del rango permitido.")

    else:
        print("✅ Todos los parciales tienen valores válidos.")

    return df  # Retornar el DataFrame corregido

# Ejecutar validación
df = pd.read_csv(CSV_FILENAME)
validar_notas(df)