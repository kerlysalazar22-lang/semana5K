# Clase que administra los productos y clientes del restaurante.

from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    #  doble guion bajo para el constructor
    def __init__(self, nombre: str, direccion: str):
        self.nombre = nombre
        self.direccion = direccion
        self.productos: list[Producto] = []
        self.clientes: list[Cliente] = []

    def agregar_producto(self, producto: Producto) -> None:
        self.productos.append(producto)

    def agregar_cliente(self, cliente: Cliente) -> None:
        self.clientes.append(cliente)

    def mostrar_productos(self) -> None:
        print("\n--- PRODUCTOS REGISTRADOS ---")
        for producto in self.productos:
            print(producto)

    def mostrar_clientes(self) -> None:
        print("\n--- CLIENTES REGISTRADOS ---")
        for cliente in self.clientes:
            print(cliente)

    def mostrar_informacion_restaurante(self) -> None:
        print(f"Restaurante: {self.nombre}")
        print(f"Dirección: {self.direccion}")
        print(f"Total de productos: {len(self.productos)}")
        print(f"Total de clientes: {len(self.clientes)}")