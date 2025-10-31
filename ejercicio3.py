import pandas as pd

df = pd.read_csv(r"ERD\ejercicios2\EjerciciosTema2\alumnos.csv")

print(df.head())

alumnos_limpio = df.dropna()

alumnos_limpio.to_csv(r'ERD\ejercicios2\EjerciciosTema2\limpio.csv', index=False)

df_alumnos = pd.read_csv(r"ERD\ejercicios2\EjerciciosTema2\alumnos.csv") 
df_notas = pd.read_csv(r"ERD\ejercicios2\EjerciciosTema2\notas.csv")     

df_completo = pd.merge(df_alumnos, df_notas, on='Nombre', how='inner')

print(df_completo)


