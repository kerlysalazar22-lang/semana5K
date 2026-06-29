# Punto de inicio del programa.

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


# Se crea el objeto principal del restaurante.
restaurante_principal = Restaurante(
    "Sabor Casero",
    "Alfaro, Pichincha"
)

# Se crean dos objetos de la clase Producto.
producto_almuerzo = Producto(
    1,
    "Almuerzo ejecutivo",
    3.50,
    True
)

producto_batido = Producto(
    2,
    "Batido de mora",
    2.00,
    True
)

# Se crean dos objetos de la clase Cliente.
cliente_kerly = Cliente(
    "1234567890",
    "Kerly Salazar",
    18,
    True
)

cliente_michelle = Cliente(
    "0987654321",
    "Michelle Lopez",
    19,
    False
)

# Se agregan los productos a la lista del restaurante.
restaurante_principal.agregar_producto(producto_almuerzo)
restaurante_principal.agregar_producto(producto_batido)

# Se agregan los clientes a la lista del restaurante.
restaurante_principal.agregar_cliente(cliente_kerly)
restaurante_principal.agregar_cliente(cliente_michelle)

# Se muestra la información organizada en consola.
print("=== SISTEMA BÁSICO DE GESTIÓN DE RESTAURANTE ===")

restaurante_principal.mostrar_informacion_restaurante()
restaurante_principal.mostrar_productos()
restaurante_principal.mostrar_clientes()