import pandas as pd

df = pd.read_csv('CO2_emissions.csv')

df_limpio = df.dropna(subset=['Año', 'Emisiones_CO2'])

df_limpio['Año'] = pd.to_numeric(df_limpio['Año'], errors='coerce', downcast='integer')
df_limpio['Emisiones_CO2'] = pd.to_numeric(df_limpio['Emisiones_CO2'], errors='coerce')

df_limpio['Nivel_Emisión'] = df_limpio['Emisiones_CO2'].apply(
    lambda x: 'Alta' if x > 250 else 'Media' if x > 200 else 'Baja'
)

df_limpio.to_csv('CO2_emissions_limpio.csv', index=False)

print("Proceso completado. Archivo exportado como CO2_emissions_limpio.csv")
