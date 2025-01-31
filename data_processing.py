import pandas as pd
from utils import revisar_nota
from constants import APROBADO, CSV_FILENAME

def validar_notas(df):

    df.columns = df.columns.str.strip()

    """Comprueba que las notas están en el rango permitido y corrige valores inválidos."""
    errores = df[(df["Nota_Parcial_1"] < 0) | (df["Nota_Parcial_1"] > 5) |
                 (df["Nota_Parcial_2"] < 0) | (df["Nota_Parcial_2"] > 5)]
    return df

def calcular_notas_definitivas(df):
    df["NotaDefinitiva"] = (df["Nota_Parcial_1"] + df["Nota_Parcial_2"]) / 2
    return df


def ParcialesTodosEstudiantes(df):
    print("\nNotas Definitivas de los Estudiantes:")
    print(df[["Nombre", "NotaDefinitiva"]])

def PromedioParcial(df, parcial):
    if parcial not in [1, 2]:
        print(f"Parcial {parcial} no válido. Debe ser 1 o 2.")
        return
    
    promedio = df[f"Nota_Parcial_{parcial}"].mean()
    print(f"\nPromedio del Parcial {parcial}: {promedio:.2f}")

def resultados(df):
    hombres = df[df["Sexo"] == "M"]
    mujeres = df[df["Sexo"] == "F"]

    prom_hombres = hombres["NotaDefinitiva"].mean() if not hombres.empty else 0
    prom_mujeres = mujeres["NotaDefinitiva"].mean() if not mujeres.empty else 0
    reprobados = df[df["NotaDefinitiva"] < APROBADO].shape[0]

    print("\nResultados:")
    print(f"Promedio de Notas Definitivas de Hombres: {prom_hombres:.2f}")
    print(f"Promedio de Notas Definitivas de Mujeres: {prom_mujeres:.2f}")
    print(f"Número de Estudiantes Reprobados: {reprobados}")

df = pd.read_csv(CSV_FILENAME)
df = validar_notas(df)
df = calcular_notas_definitivas(df)