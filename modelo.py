class Producto:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

# Base de datos temporal (en memoria)
productos = []

def guardar_producto(producto):
    productos.append(producto)
    return True

def obtener_productos():
    return productos

def borrar_productos():
    productos.clear()
