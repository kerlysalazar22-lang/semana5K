# Clase que representa a un cliente registrado en el restaurante.

class Cliente:
    #  doble guion bajo para el constructor
    def __init__(
        self,
        cedula: str,
        nombre: str,
        edad: int,
        cliente_frecuente: bool
    ):
        self.cedula = cedula
        self.nombre = nombre
        self.edad = edad
        self.cliente_frecuente = cliente_frecuente

    def mostrar_informacion(self) -> str:
        tipo_cliente = (
            "Cliente frecuente"
            if self.cliente_frecuente
            else "Cliente regular"
        )

        return (
            f"Cédula: {self.cedula} | "
            f"Nombre: {self.nombre} | "
            f"Edad: {self.edad} años | "
            f"Tipo: {tipo_cliente}"
        )

    # doble guion bajo para el método str
    def __str__(self) -> str:
        return self.mostrar_informacion()