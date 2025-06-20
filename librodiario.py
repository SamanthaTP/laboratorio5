import logging
logging.basicConfig(filename='log_contable.log', level=logging.ERROR)
from datetime import datetime
from typing import List, Dict

class Montoerror(Exception):
    pass

class LibroDiario:
    """Gestión contable básica de ingresos y egresos."""

    def __init__(self):
        self.transacciones: List[Dict] = []

    def agregar_transaccion(self, fecha: str, descripcion: str, monto: float, tipo: str) -> None:
        """Agrega una transacción al libro diario."""
        tipo = tipo.lower().strip()
        if tipo not in ("ingreso", "egreso"):
            logging.error(f"Tipo inválido: '{tipo}'. Debe ser 'ingreso' o 'egreso'.")
            print("Error: Tipo inválido. Por favor ingrese 'ingreso' o 'egreso'.")
            return
        try:
            datetime.strptime(fecha, "%d/%m/%Y")
        except ValueError:
            raise ValueError(f"Formato de fecha inválido: {fecha}.")
        monto = float(monto)
        if monto <= 0:
            raise Montoerror(f"Monto $ inválido: {monto}.")

        transaccion = {
            "fecha": datetime.strptime(fecha, "%d/%m/%Y"),
            "descripcion": descripcion,
            "monto": monto,
            "tipo": tipo
        }
        self.transacciones.append(transaccion)

    def calcular_resumen(self) -> Dict[str, float]:
        """Devuelve el resumen total de ingresos y egresos."""
        resumen = {"ingresos": 0.0, "egresos": 0.0}
        for transaccion in self.transacciones:
            if transaccion["tipo"] == "ingreso":
                resumen["ingresos"] += transaccion["monto"]
            else:
                resumen["egresos"] += transaccion["monto"]
        return resumen
