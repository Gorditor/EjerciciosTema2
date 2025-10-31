import pandas as pd

datos = {
"Nombre": ["Anna", "Joan", "Maria", "Pere", None],
"Notas": [8.5, 4.0, 6.5, None, 3.0]
}

df = pd.DataFrame(datos)

df["Resultado"] = df["Notas"] >= 5 
print(df)

ventas = pd.DataFrame({
    'Producto': ['Libro', 'Boligrafo', 'Cuaderno', 'Goma'],
    'Cantidad': [5, 12, 8, 15],
    'Precio': [10.0, 1.5, 3.0, 0.5]
})

ventasCantidad = ventas[ventas["Cantidad"] > 10]
print(ventasCantidad)

alumnosOrdenados = df.sort_values(by="Notas", ascending=False)
print(alumnosOrdenados)

