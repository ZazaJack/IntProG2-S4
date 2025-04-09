

precio1: float = 20.00  
precio2: float = 30.00  
precio3: float = 50.00  
subtotal: float = precio1 + precio2 + precio3 
iva: float = subtotal * 0.15  
total: float = subtotal + iva  
print("Subtotal:", subtotal)
print("IVA:", iva)
print("Total a pagar:", total) 