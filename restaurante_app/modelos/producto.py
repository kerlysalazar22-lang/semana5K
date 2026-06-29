# Clase que representa un producto disponible en el restaurante.

class Producto:
    # doble guion bajo para el constructor
    def __init__(
        self,
        codigo: int,
        nombre: str,
        precio: float,
        disponible: bool
    ):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.disponible = disponible

    def mostrar_informacion(self) -> str:
        estado = "Disponible" if self.disponible else "No disponible"

        return (
            f"Código: {self.codigo} | "
            f"Producto: {self.nombre} | "
            f"Precio: ${self.precio:.2f} | "
            f"Estado: {estado}"
        )

    # doble guion bajo para el método str
    def __str__(self) -> str:
        return self.mostrar_informacion()