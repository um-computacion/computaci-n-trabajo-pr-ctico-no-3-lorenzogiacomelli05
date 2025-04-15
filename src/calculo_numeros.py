from exceptions import ingrese_numero, NumeroDebeSerPositivo

def ingrese_numero():
    
    try:
        num = int(input("Ingrese un número: "))
        
        if num < 0:
            raise NumeroDebeSerPositivo("El número tiene que ser positivo")  
        return num
    
    except ValueError:
        raise ValueError("La entrada debe ser un número válido.")

def main():
    """
    Solicita números al usuario y muestra los resultados.
    """
    while True:
        try:
            resultado = ingrese_numero()
            print(f"Número aceptado: {resultado}")
        except ValueError as e:
            print(f"Error: {e}")
        except NumeroDebeSerPositivo as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("Programa terminado por el usuario.")
            break
if __name__ == "__main__":
    main()