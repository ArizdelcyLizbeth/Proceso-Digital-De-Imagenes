from Filtro_Imagenes import Filtros  

def main():
    image_path = "Imagen.jpg" 
    filters = Filtros(image_path)
    
    while True:
        print("Seleccione el filtro que desea aplicar:")
        print("1. Alto Contraste")
        print("2. Filtro Rojo")
        print("3. Filtro Verde")
        print("4. Filtro Azul")
        print("5. Filtro Morado")
        print("6. Inverso")
        print("7. Filtro Color a Gris")
        print("8. Filtro Mosaico")
        print("9. Brillo")
        print("0. Salir")
        choice = input("Ingrese el número del filtro que desea aplicar: ")

        if choice == '1':
            filters.alto_contraste()
        elif choice == '2':
            filters.filtro_rojo()
        elif choice == '3':
            filters.filtro_verde()
        elif choice == '4':
            filters.filtro_azul()
        elif choice == '5':
            filters.filtro_morado()
        elif choice == '6':
            filters.inverso()
        elif choice == '7':
            print("Seleccione el método para el filtro de color a gris:")
            print("a. A+G+B div 3")
            print("b. 0.28*R + 0.56*G + 0.11*B")
            print("c. Usar R, G, o B")
            metodo = input("Ingrese el método (a, b, o c): ")
            filters.filtro_color_a_gris(metodo)
        elif choice == '8':
            filters.filtro_mosaico()
        elif choice == 9:
            cte = int(input("Ingrese el valor de la constante de brillo (positivo para aumentar, negativo para disminuir): "))
            filters.filtro_brillo(cte)
        elif choice == '0':
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()