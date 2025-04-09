

salario_actual: float = 3500.00  
incremento: float = 0.10  
descuento: float = 0.030  
nuevo_salario: float = salario_actual * (1 + incremento) * (1 - descuento)  
print("El nuevo salario es:", nuevo_salario) 
