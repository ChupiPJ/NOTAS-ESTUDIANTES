# 📊 Gestión de Notas de Estudiantes

Este es un programa en **Python** que permite procesar, validar y analizar las notas de los estudiantes de un curso, utilizando **Pandas** para manipular los datos desde un archivo **CSV**.

---

## 🚀 Características
<details>
  <summary><strong>📌 Ver características</strong></summary>

✔ Carga de datos desde un archivo CSV 📂  
✔ Validación automática de notas 🔍  
✔ Cálculo de promedios de parciales 📈  
✔ Generación de estadísticas de aprobación/reprobación ✅❌  
✔ Interfaz de menú interactiva en consola 🖥  

</details>

---

## 📜 Requisitos
<details>
  <summary><strong>⚙️ Ver requisitos</strong></summary>

Antes de ejecutar el programa, asegúrate de tener:

✔ **Python 3.8+** instalado 🐍  
✔ **Librerías necesarias** instaladas con el siguiente comando:

```sh
pip install pandas
```

</details>

---

## 🔧 Uso del Programa
Ejecuta el siguiente comando en la terminal:

```sh
python main.py
```

📌 Al iniciar, verás el siguiente **menú interactivo**:

```
📌 MENU PRINCIPAL 📌
0️⃣ Cargar datos
1️⃣ Consultar notas definitivas de todos los estudiantes
2️⃣ Calcular promedio de un parcial
3️⃣ Mostrar resultados finales
4️⃣ Salir
🔹 Elija una opción:
```

---

## 📂 Estructura del Proyecto
```
📂 Proyecto
 ┣ 📜 main.py               # Archivo principal (menú interactivo)
 ┣ 📜 data_processing.py     # Funciones para procesar datos
 ┣ 📜 utils.py               # Funciones auxiliares
 ┣ 📜 constants.py           # Constantes del proyecto
 ┣ 📜 notas_estudiantes.csv  # Archivo de datos de los estudiantes
 ┗ 📜 README.md              # Documentación del proyecto
```

---

## 📖 Funcionalidades del Menú

<details>
  <summary><strong>0️⃣ Cargar datos</strong> 📂</summary>
  Esta opción lee el archivo **CSV** con los datos de los estudiantes y valida que las notas estén en el rango permitido (0.0 - 5.0).
</details>

<details>
  <summary><strong>1️⃣ Consultar notas definitivas</strong> 📋</summary>
  Muestra la lista de todos los estudiantes con su **nota definitiva** calculada a partir del promedio de los dos parciales.
</details>

<details>
  <summary><strong>2️⃣ Calcular promedio de un parcial</strong> 📊</summary>
  Permite calcular el promedio del parcial **1** o **2** para todo el grupo.
</details>

<details>
  <summary><strong>3️⃣ Mostrar resultados finales</strong> 📈</summary>
  Muestra estadísticas como:
  - Promedio de notas definitivas de hombres y mujeres.
  - Cantidad de estudiantes reprobados.
</details>

<details>
  <summary><strong>4️⃣ Salir</strong> ❌</summary>
  Cierra el programa.
</details>

---

### ✨ **Autor**
Desarrollado por **[Chupi]** 🖥🚀  