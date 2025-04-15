from exceptions import ingrese_numero, NumeroDebeSerPositivo

def ingrese_numero():
        num = int(input("Ingrese un número: "))
        
        if num < 0:
            raise NumeroDebeSerPositivo("El número tiene que ser positivo")  
        return num

def main():
    """
    Solicita números al usuario y muestra los resultados.
    """
    while True:
        try:
            resultado = ingrese_numero()
            print(f"Número aceptado: {resultado}")
        except NumeroDebeSerPositivo as e:
            print(f"Error: {e}")
            break
if __name__ == "__main__":
    main()