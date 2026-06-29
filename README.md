# Sistema de Registro - Restaurante "Sabor Casero" (Semana 5)

Este proyecto consiste en una aplicación modular desarrollada en Python para la gestión interna de un restaurante. El objetivo principal es aplicar los pilares de la **Programación Orientada a Objetos (POO)** mediante la separación del código en paquetes, módulos y clases independientes, garantizando un diseño estructurado, limpio y fácil de mantener.

## 🚀 Funcionalidades Principales
* **Módulo de Modelos:** * `Producto`: Permite registrar platos y bebidas con su respectivo código, precio y estado de disponibilidad en el menú.
  * `Cliente`: Gestiona los datos de los usuarios incluyendo cédula, edad y si califica como cliente frecuente.
* **Módulo de Servicios:** * `Restaurante`: Actúa como el controlador central que administra las listas dinámicas de productos y clientes en memoria, permitiendo el ingreso masivo y la impresión de reportes en la consola.

## 📁 Estructura de Archivos del Proyecto
La distribución del código sigue las buenas prácticas de empaquetado modular:

```text
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── cliente.py
│   └── producto.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
├── main.py
└── README.md