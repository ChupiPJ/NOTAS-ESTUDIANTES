from utils import leer_csv
from data_processing import resultados, validar_notas, calcular_notas_definitivas, ParcialesTodosEstudiantes, PromedioParcial
def main(): 
    df = leer_csv()
    if df is None:
            return
    
    df = validar_notas(df)  
    df = calcular_notas_definitivas(df)

    while True:
        print("📌 MENU PRINCIPAL 📌")
        print("1️⃣ Consultar notas definitivas de todos los estudiantes")
        print("2️⃣ Calcular promedio de un parcial")
        print("3️⃣ Mostrar resultados finales")
        print("4️⃣ Salir")

        opcion = input("🔹 Elija una opción: ")
        
    
        df = validar_notas(df)  
        df = calcular_notas_definitivas(df)

        if opcion == "1":
            ParcialesTodosEstudiantes(df)

        elif opcion == "2":
            try:
                parcial = int(input("Ingrese el número del parcial (1 o 2): "))
                PromedioParcial(df, parcial)
            except ValueError:
                print("❌ Debe ingresar un número entero.")
            
        elif opcion == "3":
            resultados(df)
        
        elif opcion == "4":
            print("\n👋 Saliendo del programa...")
            break

        else:
            print("❌ Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()