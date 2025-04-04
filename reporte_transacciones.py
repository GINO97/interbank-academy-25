import csv

def transaccion(archivo_csv):
    # Inicializar variables
    total_credito = 0.0
    total_debito = 0.0
    max_monto = 0.0
    id_max_monto = None
    cont_credito = 0
    cont_debito = 0

    # Lectura del archivo CSV
    with open(archivo_csv, mode='r',  encoding='utf-8') as file:
        reader = csv.DictReader(file)  
        #con el for se va a mapear todo el archivo dentro de la lista row
        for row in reader:
            monto = float(row['monto'])  # variable monto va almacenar los datos de la columna [monto]
          #  se hara la distincion de la transaccion por columna [tipo] = Debito or Credito
            if row['tipo'] == 'Crédito': 
                total_credito += monto 
                cont_credito += 1
          #Acumulador del monto de c/tipo sera almacenado por total_credito/debito
          # El contador de c/tipo, en la variable cont_debito/credito
            elif row['tipo'] == 'Débito':
                total_debito += monto
                cont_debito += 1
            
            # Verificación de transacción con mayor monto
            if monto > max_monto:
                max_monto = monto
                id_max_monto = row['id'] # captura el id de la columna con el max. monto

    # Calculo de balance final
    balance_final = total_credito - total_debito

    # Generación de reporte
    print("\nReporte de Transacciones")
    print("---------------------------------------------")
    print(f"Balance Final: {balance_final:.2f}")
    print(f"Transacción de Mayor Monto: ID {id_max_monto} - {max_monto:.2f}") #monto con 2 decimales
    print(f"Conteo de Transacciones: Crédito: {cont_credito} Débito: {cont_debito}\n")

""" ------------------------------------------------------------------------"""
#Colab
#archivo = '/content/retotecnico-cobol/archivo.csv'
# VSC 
archivo = 'data.csv'

try:
  transaccion(archivo)
except FileNotFoundError:
  print(f"Error: El archivo '{archivo}' no fue encontrado.")
except Exception as e:
  print(f"Ocurrió un error: {e}")