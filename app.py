from librodiario import LibroDiario
libro = LibroDiario()
libro.agregar_transaccion('18/06/2025', 'Compra de laptop', 780, 'egreso')
libro.agregar_transaccion('18/06/2025', 'Venta de sensor TK-110', 780, 'Ingreso')
libro.agregar_transaccion('18/06/2025', 'Compra de insumos de oficina', -85.60, 'egreso')
print(libro.calcular_resumen())