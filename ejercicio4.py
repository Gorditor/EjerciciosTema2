import pandas as pd

notas = pd.read_csv(r"ERD\ejercicios2\EjerciciosTema2\notas_alumnos.csv") 

media = notas['Nota'].mean()
maximo = notas['Nota'].max()
minimo = notas['Nota'].min()

print(f"Media: {media:.2f}, Maximo: {maximo}, Minimo: {minimo}")

def clasificar(nota):
    if nota >= 9:
        return "Excelente"
    elif nota >= 7:
        return "Notable"
    elif nota >= 5:
        return "Aprobado"
    else:
        return "Suspenso"

notas['Categoria'] = notas['Nota'].apply(clasificar)

print("\nNotas con categoria:")
print(notas)

ventas = pd.read_csv(r"ERD\ejercicios2\EjerciciosTema2\ventas.csv")  

ventas_limpias = ventas[(ventas['Cantidad'] >= 0) & (ventas['Fecha'].notna())].copy()

ventas_limpias.loc[:, 'Total'] = ventas_limpias['Cantidad'] * ventas_limpias['Precio']
totales = ventas_limpias.groupby('Producto')['Total'].sum().reset_index()

print("\nTotal de ventas por producto:")
print(totales)

