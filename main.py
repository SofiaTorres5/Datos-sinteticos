import numpy as np
import pandas as pd

pd.set_option("display.float_format", "{:.3f}".format)
np.random.seed(42)
#=============================
#      GENERAR DATOS
#=============================
ritmo_car = np.round(np.random.normal(140, 15, 150), 3)
velocidad = np.round(np.random.normal(10, 2, 150), 3)
calorias = np.round(np.random.normal(350, 50, 150), 3)
#=============================
#     AGREGAR OUTLIERS
#=============================
ritmo_car [0] = 300
velocidad [1] = 2000
calorias [2] = 1000
#=============================
#      CREAR DATAFRAME
#=============================
try:
  datos = pd.DataFrame({
    "Ritmo Cardiaco": ritmo_car,
    "Velocidad": velocidad,
    "Calorias quemadas": calorias
  })
except Exception as e:
  print("Error:", e)
#=============================
#       GUARDAR CVS
#=============================
datos.to_csv("dataset.csv", index = False)
#=============================
#     MOSTAR RESULTADOS
#=============================
print("Dataset creado correctamente")
print(datos.head())

# =========================
# LEER EL CSV
# =========================

try:
    datos_leidos = pd.read_csv("dataset.csv")

    print("\nArchivo leído correctamente.\n")

except FileNotFoundError:
    print("Error: el archivo no existe")

# =========================
# ESTADÍSTICAS
# =========================

print("===== ESTADÍSTICAS =====\n")

print(datos_leidos.describe())

# =========================
# DETECTAR OUTLIERS
# =========================

print("\n===== DETECCIÓN DE OUTLIERS =====\n")

# Función para detectar outliers
def detectar_outliers(columna):

    media = columna.mean()

    desviacion = columna.std()

    limite_superior = media + 3 * desviacion

    limite_inferior = media - 3 * desviacion

    outliers = columna[
        (columna > limite_superior) |
        (columna < limite_inferior)
    ]

    return outliers


# Detectar outliers en cada columna
out_ritmo = detectar_outliers(datos_leidos["Ritmo Cardiaco"])

out_velocidad = detectar_outliers(datos_leidos["Velocidad"])

out_calorias = detectar_outliers(datos_leidos["Calorias Quemadas"])

print("Outliers Ritmo Cardiaco:\n")
print(out_ritmo)

print("\nOutliers Velocidad:\n")
print(out_velocidad)

print("\nOutliers Calorias Quemadas:\n")
print(out_calorias)

# =========================
# ELIMINAR OUTLIERS
# =========================

print("\n===== ELIMINANDO OUTLIERS =====\n")

datos_limpios = datos_leidos.copy()

for columna in datos_limpios.columns:

    media = datos_limpios[columna].mean()

    desviacion = datos_limpios[columna].std()

    limite_superior = media + 3 * desviacion

    limite_inferior = media - 3 * desviacion

    datos_limpios = datos_limpios[
        (datos_limpios[columna] <= limite_superior) &
        (datos_limpios[columna] >= limite_inferior)
    ]

print("Datos originales:", len(datos_leidos))

print("Datos limpios:", len(datos_limpios))

# =========================
# GUARDAR DATASET LIMPIO
# =========================

datos_limpios.to_csv(
    "dataset_limpio.csv",
    index=False
)

print("\nDataset limpio guardado correctamente.")

# =========================
# GENERAR REPORTE
# =========================

with open("reporte.txt", "w") as reporte:

    reporte.write("REPORTE DE ANALISIS\n")
    reporte.write("====================\n\n")

    reporte.write("ESTADISTICAS GENERALES\n\n")

    reporte.write(str(datos_leidos.describe()))

    reporte.write("\n\n")

    reporte.write(
        f"Cantidad datos originales: {len(datos_leidos)}\n"
    )

    reporte.write(
        f"Cantidad datos limpios: {len(datos_limpios)}\n"
    )

print("\nReporte generado correctamente.")
