import pandas as pd

# Exemple: dades d’alumnes
dades = {
"Nom": ["Anna", "Joan", "Maria", "Pere", None],
"Edat": [20, 21, None, 22, 21],
"Nota": [8.5, 7.0, 6.5, None, 9.0]
}
df = pd.DataFrame(dades)
#print("Dades originals:\n", df)

df_sense_buits = df.dropna()
#print(df_sense_buits)

#df["Edat"].fillna(df["Edat"].mean(), inplace=True) # substituir per la mitjana
#df["Nota"].fillna(0, inplace=True) # substituir per 0

df["Aprovat"] = df["Nota"] >= 5

print("Dades:\n", df)   
