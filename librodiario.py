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
        try:
            tipo = tipo.strip().lower()
            if tipo not in ("ingreso", "egreso"):
                raise ValueError(f"Tipo inválido: {tipo}")
            try:
                datetime.strptime(fecha, "%Y-%m-%d")
            except ValueError:
                raise ValueError(f"Formato de fecha inválido: {fecha}.")
            
            monto = float(monto)
            if monto <= 0:
                raise Montoerror(f"Monto inválido: {monto}.")

            transaccion = {
                "fecha": fecha,
                "descripcion": descripcion,
                "monto": monto,
                "tipo": tipo
            }
            self.transacciones.append(transaccion)
            logging.info(f"Transacción exitosamente: {transaccion}")
            print("Transacción correctamente.")

        except ValueError as ve:
            logging.exception(f"ValueError: {ve}")
            print(f"Error de valor: {ve}")

        except Montoerror as me:
            logging.exception(f"MontoError: {me}")
            print(f"Error de monto: {me}")

        except Exception as e:
            logging.exception(f"Error inesperado: {e}")
            print(f"Error inesperado: {e}")

    def calcular_resumen(self) -> Dict[str, float]:
        """Devuelve el resumen total de ingresos y egresos."""
        resumen = {"ingresos": 0.0, "egresos": 0.0}
        for transaccion in self.transacciones:
            if transaccion["tipo"] == "ingreso":
                resumen["ingresos"] += transaccion["monto"]
            else:
                resumen["egresos"] += transaccion["monto"]
        return resumen
