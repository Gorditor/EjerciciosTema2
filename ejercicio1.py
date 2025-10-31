import pandas as pd

datos = {
"Nombre": ["Anna", "Joan", "Maria", "Pere", None],
"Edad": [20, 21, None, 22, 21],
"Notas": [8.5, 7.0, 6.5, None, 9.0]
}

df = pd.DataFrame(datos)

dfSinVacios = df.dropna()
print(dfSinVacios)

#df["Edad"].fillna(df["Edad"].mean(), inplace=True)

dfSinDuplicados = df.drop_duplicates()
print(dfSinDuplicados)

#df["Edad"] = df["Edad"].astype(int)

df["Precios"] = df["Precios"] = ["12.5","8.0","5.0","34.6","20.0"]

df["Precios"] = pd.to_numeric(df["Precios"])

mediaPrecios = df["Precios"].mean()

print(df)
print(f"\nMedia de precios: {mediaPrecios:.2f}")



