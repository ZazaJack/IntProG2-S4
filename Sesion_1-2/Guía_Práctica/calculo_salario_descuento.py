
nombre_trabajador: str = "Zahid"  
horas_trabajadas: int = 45  
precio_por_hora: float = 45.00  
sueldo_bruto: float = horas_trabajadas * precio_por_hora  
descuento_renta: float = sueldo_bruto * 0.10  
salario_a_pagar: float = sueldo_bruto - descuento_renta  
print("Nombre del trabajador:", nombre_trabajador)
print("Sueldo bruto:", sueldo_bruto)
print("Descuento de renta:", descuento_renta)
print("Salario a pagar:", salario_a_pagar)  