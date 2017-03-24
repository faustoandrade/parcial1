import matriz
import threading

matrizA = matriz.Matriz()
matrizB = matriz.Matriz()

def crearmatrizA():
        matrizA.crearMatrizA()
        a = matrizA.llenarmatrizA()
        matrizA.imprimirmatriz()
        columnasA = matrizA.getColumnas()
        filasA = matrizA.getFilas()

def crearmatrizB():
        matrizB.crearMatrizA()
        b = matrizB.llenarmatrizA()
        matrizB.imprimirmatrizC()
        columnasB = matrizB.getColumnas()
        filasB = matrizB.getFilas()

def identica():
    print "IDENTIDAD"
    matrizA = matriz.Matriz()
    matrizA.matrizidentica()

def sumam(matrizA, matrizB):
    print "SUMA"
    matrizA = matriz.Matriz()
    matrizA.crearMatrizA()
    a = matrizA.llenarmatrizA()
    matrizA.imprimirmatriz()
    columnasA = matrizA.getColumnas()
    filasA = matrizA.getFilas()

    matrizB = matriz.Matriz()
    matrizB.crearMatrizA()
    b = matrizB.llenarmatrizA()
    matrizB.imprimirmatrizC()
    columnasB = matrizB.getColumnas()
    filasB = matrizB.getFilas()
    matrizA.sumamatriz(filasA, columnasB, filasB, columnasA, a, b)


def determinante():
    matrizA = matriz.Matriz()
    matrizA.crearMatrizA()
    a = matrizA.llenarmatrizA()
    matrizA.imprimirmatriz()
    matrizA.matriz_det(a)


hilo1 = threading.Thread(target=crearmatrizA, args=())
hilo1.start()
hilo1.join()
hilo2 = threading.Thread(target=crearmatrizB, args=())
hilo2.start()
hilo2.join()
hilo3 = threading.Thread(target=identica, args=())
hilo3.start()
hilo3.join()
hilo4 = threading.Thread(target=sumam, args=(matrizA,matrizB))
hilo4.start()
hilo4.join()
hilo5 = threading.Thread(target=determinante, args=())
hilo5.start()


#crearmatrizA()
#crearmatrizB()