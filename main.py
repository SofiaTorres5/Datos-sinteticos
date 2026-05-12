import numpy as np
import pandas as pd

pd.set_option("display.float_format", "{:.3f}".format)

ritmo_car = np.round(np.random.normal(140, 15, 150), 3)
velocidad = np.round(np.random.normal(10, 2, 150), 3)
calorias = np.round(np.random.normal(350, 50, 150), 3)

ritmo_car [0] = 300
velocidad [1] = 2000
calorias [2] = 300

try:
  datos = pd.DataFrame({
    "Ritmo Cardiaco": ritmo_car,
    "Velocidad": velocidad,
    "Calorias quemadas": calorias
  })
except Exception as e:
  print("Error:", e)

datos.to_csv("dataset.csv", index = False)

print("Dataset creado correctamente")
print(datos.head())
