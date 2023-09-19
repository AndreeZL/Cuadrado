class Cuadrado:
    def dibujar_cuadrado(tamano):
        for i in range(tamano):
            for j in range(tamano):
                if i == 0 or i == tamano - 1 or j == 0 or j == tamano - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

    if __name__ == "__main__":
        dibujar_cuadrado()