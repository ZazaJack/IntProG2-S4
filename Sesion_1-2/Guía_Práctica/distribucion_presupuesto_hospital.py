
presupuesto_total: float = 245000.00
urgencias: float = 0.70  
pediatria: float = 0.20  
traumatologia: float = 0.35  
presupuesto_urgencias: float = presupuesto_total * urgencias  
presupuesto_pediatria: float = presupuesto_total * pediatria  
presupuesto_traumatologia: float = presupuesto_total * traumatologia  
print("Presupuesto Urgencias:", presupuesto_urgencias)
print("Presupuesto Pediatría:", presupuesto_pediatria)
print("Presupuesto Traumatología:", presupuesto_traumatologia)  