# coding: utf-8

import copy
import problema_espacio_estados as probee
import búsqueda_espacio_estados as busqueda
import time

#Primero vamos a realizar los métodos de cada pieza, en total son 63, con sus restricciones y la aplicabilidad de cada una.

#PONER I-------------------------------------------------------------------------
class ponerI(probee.Acción):
    def __init__(self, i, j):  #Constructor de la clase
        nombre = "Colocamos la I en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    # En este método (hay_ hueco_ )comprobamos que la casilla en la que se va a colocar la pieza está vacía, para ello
    #cogemos una casilla de referencia de la pieza , y a partir de ella vamos colocando las casillas restantes
    #sumándole y restándole columnas y filas a esa casilla. Por ejemplo si la pieza ocupase 3 casillas horizontales (- - -) y cogiésemos
    #de referencia la primera casilla empezando por la izquierda sería: estado[self.fila][self.columna] estado[self.fila][self.columna+1] estado[self.fila][self.columna+2]
    #le sumaríamos una columna primero para tener - - y después otra más a la casilla inicial para tener la pieza resultante (- - -), de la misma forma haríamos con las filas.

    #Explicaremos el primer método hay_hueco y este será igual para todas las piezas cambiando el número de pieza y la forma de cada una.
    def hay_hueco_I(self, estado):
        res = []
        i = 1
        if i - estado[self.fila][self.columna] == i: #para comprobar que la casilla está vacía hemos optado por la opción de asignarle un número a cada pieza de manera que si
            res.append(True)                         #la casilla está vacía, es decir, su valor es 0 la resta del número de la casilla menos 0 debe ser igual a dicho número,
        else:                                        #en este caso el 1, en cualquier otro caso la resta no devolverá el número de la pieza por lo tanto la casilla no estará
            res.append(False)                        #vacía

        if i - estado[self.fila][self.columna - 1] == i:  #Si es verdad que la casilla está vacía se añadirá un True a una lista que hemos creado al principio del método,
            res.append(True)                              #en caso contrario se añadirá un False a dicha lista.
        else:
            res.append(False)

        if i - estado[self.fila][self.columna - 2] == i:
            res.append(True)
        else:
            res.append(False)

        if i - estado[self.fila][self.columna - 3] == i:
            res.append(True)
        else:
            res.append(False)

        if i - estado[self.fila][self.columna - 4] == i:
            res.append(True)
        else:
            res.append(False)

        if res.count(False)>0:                          #Aquí comprobamos que la lista no tiene ningún False, por lo que la ficha cabe pues todas las casillas que
            return False                                #ocupa están vacías
        else:
            return True


#El método es_aplicable comprueba que el método hay_hueco ha dado true, que la ficha no  se sale de los límites del tablero y  a partir de qué posición
#se puede colocar la casilla de refencia utilizada, por ejemplo si queremos colocar una L formada por dos casillas verticales y una horizontal se haría de la siguiente
#manera:
#  Si cogiésemos como referencia la casilla horizontal, para colocar esta casilla tenemos la restricción de que la tenemos que colocar a partir de la columna 1
#(teniendo en cuenta que la primera columna en python es la número 0), ya que si la colocásemos en la 0 tendríamos un problema, las dos casillas verticales se saldrían
#del tablero. También tendríamos otra restricción y es que se tendría que colocar a partir de la fila 1 (teniendo en cuenta también que la primera fila en python es
# la número 0), si la colocásemos en la fila 0 tendríamos el mismo problema que antes. Por último tendríamos que comprobar que la fila de la casilla de referencia
#no fuese mayor que el número de filas del tablero self.fila < len(estado), no podemos colocar la casilla x en la fila 4 cuando nuestro tablero solo tiene 3 filas y
# lo mismo con las columnas self.columna < len(estado[0]).
#  A continuación vamos a explicar de una manera más gráfica la condición de los límites del tablero, en este caso vamos a colocar una L como la de antes pero invertida,
#es decir, _| esta se compone de dos fichas verticales y una horizontal situada a la izquierda. Tendríamos que hacer las comprobaciones pertinentes para las columnas
#y las filas como en el caso anterior y las de los límites del tablero pero en este caso no solo valdría con poner self.fila < len(estado) y self.columna < len(estado[0])
# tendríamos que poner self.columna < len(estado[0])-1 ya que la casilla horizontal (la cual hemos tomado como referencia) tiene dos casillas situadas en una columna más
# a la derecha que ella por lo que si tuviésemos un tablero 4x4 y colocásemos dicha casilla en la posición columna 3, las otras dos casillas que forman el palo de la L
#invertida se saldrían del tablero, para las filas la restricción sería la misma que la anterior self.fila < len(estado) ya que no hay ninguna casilla por debajo de la
#casilla de referencia

    def es_aplicable(self, estado):
        if self.columna >= 4 and self.columna < len(estado[0]) and self.fila >= 0 and self.fila < len(estado):
            if (self.hay_hueco_I(estado)):
                return True
            else:
                return False

#En el método aplicar una vez que hemos comprobado con los métodos anteriores las restricciones para poder introducir la ficha sustituímos en la casilla pertinente
#el cero que nos indica que está vacía por el número que le corresponde a la casilla, en este caso de la I es el 1.


    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 1
        nuevo_estado[self.fila][self.columna -1] = 1
        nuevo_estado[self.fila][self.columna -2] = 1
        nuevo_estado[self.fila][self.columna - 3] = 1
        nuevo_estado[self.fila][self.columna - 4] = 1
        return nuevo_estado




#PONER F-------------------------------------------------------------------------
class ponerF(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la F en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_F(self, estado):
        res = []
        f = 2

        if f - estado[self.fila][self.columna] != f:
            res.append(False)
        else:
            res.append(True)

        if f - estado[self.fila-1][self.columna] != f:
            res.append(False)
        else:
            res.append(True)

        if f - estado[self.fila-1][self.columna - 1] != f:
            res.append(False)
        else:
            res.append(True)

        if f - estado[self.fila-2][self.columna] != f:
            res.append(False)
        else:
            res.append(True)

        if f - estado[self.fila-2][self.columna +1] != f:
            res.append(False)
        else:
            res.append(True)

        if res.count(False)>0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 1 and self.columna < len(estado[0])-1 and self.fila >= 2 and self.fila < len(estado):
            if (self.hay_hueco_F(estado)):  # == True)
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 2
        nuevo_estado[self.fila - 1][self.columna ] = 2
        nuevo_estado[self.fila- 1][self.columna - 1] = 2
        nuevo_estado[self.fila - 2][self.columna] = 2
        nuevo_estado[self.fila -2][self.columna + 1] = 2
        return nuevo_estado

#PONER L-------------------------------------------------------------------------
class ponerL(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la L en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_L(self, estado):
        res = []
        l = 3
        if l - estado[self.fila][self.columna] == l:
            res.append(True)
        else:
            res.append(False)

        if l - estado[self.fila][self.columna + 1] == l:
            res.append(True)
        else:
            res.append(False)

        if l - estado[self.fila-1][self.columna] ==l:
            res.append(True)
        else:
            res.append(False)

        if l - estado[self.fila-2][self.columna] == l:
            res.append(True)
        else:
            res.append(False)

        if l - estado[self.fila-3][self.columna] == l:
            res.append(True)
        else:
            res.append(False)

        if res.count(False)>0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 0 and self.columna < len(estado[0])-1 and self.fila >= 3 and self.fila < len(estado):
            if (self.hay_hueco_L(estado)):
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 3
        nuevo_estado[self.fila ][self.columna+1] = 3
        nuevo_estado[self.fila- 1][self.columna] = 3
        nuevo_estado[self.fila - 2][self.columna] = 3
        nuevo_estado[self.fila -3][self.columna] = 3
        return nuevo_estado

#PONER N-------------------------------------------------------------------------
class ponerN(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la N en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_N(self, estado):
        res = []

        n=4

        if estado[self.fila][self.columna] == 0:
            res.append(True)
        else:
            res.append(False)

        if estado[self.fila-1][self.columna] == 0:
            res.append(True)
        else:
            res.append(False)

        if estado[self.fila-2][self.columna] == 0:
            res.append(True)
        else:
            res.append(False)

        if estado[self.fila-2][self.columna+1] == 0:
            res.append(True)
        else:
            res.append(False)

        if estado[self.fila-3][self.columna +1] == 0:
            res.append(True)
        else:
            res.append(False)

        if res.count(False)>0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 0 and self.columna < len(estado[0])-1 and self.fila >= 3 and self.fila < len(estado):
            if (self.hay_hueco_N(estado)):  # == True)
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 4
        nuevo_estado[self.fila -1][self.columna ] = 4
        nuevo_estado[self.fila -2][self.columna] = 4
        nuevo_estado[self.fila -2][self.columna + 1] = 4
        nuevo_estado[self.fila -3][self.columna + 1] = 4
        return nuevo_estado

    # PONER P                                                  -------------------------------------------------------------------------
class ponerP(probee.Acción):
        def __init__(self, i, j):
            nombre = "Colocamos la P en {} {}".format(i, j)
            super().__init__(nombre)
            self.fila = i
            self.columna = j

        def hay_hueco_P(self, estado):
            res = []
            p = 5
            if p - estado[self.fila][self.columna] == p:
                res.append(True)
            else:
                res.append(False)

            if p - estado[self.fila - 1][self.columna ] == p:
                res.append(True)
            else:
                res.append(False)

            if p - estado[self.fila - 2][self.columna ] == p:
                res.append(True)
            else:
                res.append(False)

            if p - estado[self.fila][self.columna-1] == p:
                res.append(True)
            else:
                res.append(False)

            if p - estado[self.fila - 1][self.columna - 1] == p:
                res.append(True)
            else:
                res.append(False)

            if res.count(False) > 0:
                return False
            else:
                return True

        def es_aplicable(self, estado):
            if self.columna >= 1 and self.columna < len(estado[0]) and self.fila >= 2 and self.fila < len(estado):
                if (self.hay_hueco_P(estado)):  # == True)
                    return True
                else:
                    return False

        def aplicar(self, estado):
            nuevo_estado = copy.deepcopy(estado)
            nuevo_estado[self.fila][self.columna] = 5
            nuevo_estado[self.fila - 1][self.columna] = 5
            nuevo_estado[self.fila][self.columna - 1] = 5
            nuevo_estado[self.fila - 2][self.columna] = 5
            nuevo_estado[self.fila - 1][self.columna - 1] = 5
            return nuevo_estado


#Poner I vertical

class ponerIvert(probee.Acción):
            def __init__(self, i, j):
                nombre = "Colocamos la I en {} {}".format(i, j)
                super().__init__(nombre)
                self.fila = i
                self.columna = j

            def hay_hueco_Ivert(self, estado):
                res = []
                iVert = 7

                if iVert - estado[self.fila][self.columna] == iVert:
                    res.append(True)
                else:
                    res.append(False)

                if iVert - estado[self.fila - 1][self.columna] == iVert:
                    res.append(True)
                else:
                    res.append(False)

                if iVert - estado[self.fila - 2][self.columna] == iVert:
                    res.append(True)
                else:
                    res.append(False)

                if iVert - estado[self.fila - 3][self.columna] == iVert:
                    res.append(True)
                else:
                    res.append(False)

                if iVert - estado[self.fila - 4][self.columna] == iVert:
                    res.append(True)
                else:
                    res.append(False)

                if res.count(False) > 0:
                    return False
                else:
                    return True

            def es_aplicable(self, estado):
                if self.columna >= 0 and self.columna < len(estado[0]) and self.fila >= 4 and self.fila < len(estado):
                    if (self.hay_hueco_Ivert(estado)):  # == True)
                        return True
                    else:
                        return False

            def aplicar(self, estado):
                nuevo_estado = copy.deepcopy(estado)
                nuevo_estado[self.fila][self.columna] = 7
                nuevo_estado[self.fila - 1][self.columna] = 7
                nuevo_estado[self.fila - 2][self.columna] = 7
                nuevo_estado[self.fila - 3][self.columna] = 7
                nuevo_estado[self.fila - 4][self.columna] = 7
                return nuevo_estado


# PONER P2                                                   -------------------------------------------------------------------------

class ponerP2(probee.Acción):
            def __init__(self, i, j):
                nombre = "Colocamos la P2 en {} {}".format(i, j)
                super().__init__(nombre)
                self.fila = i
                self.columna = j

            def hay_hueco_P2(self, estado):
                res = []
                p = 31
                if p - estado[self.fila][self.columna] == p:
                    res.append(True)
                else:
                    res.append(False)

                if p - estado[self.fila][self.columna-1] == p:
                    res.append(True)
                else:
                    res.append(False)

                if p - estado[self.fila - 1][self.columna] == p:
                    res.append(True)
                else:
                    res.append(False)

                if p - estado[self.fila - 1][self.columna-1 ] == p:
                    res.append(True)
                else:
                    res.append(False)

                if p - estado[self.fila - 1][self.columna - 2] == p:
                    res.append(True)
                else:
                    res.append(False)

                if res.count(False) > 0:
                    return False
                else:
                    return True

            def es_aplicable(self, estado):
                if self.columna >= 2 and self.columna < len(estado[0]) and self.fila >= 1 and self.fila < len(estado):
                    if (self.hay_hueco_P2(estado)):  # == True)
                        return True
                    else:
                        return False

            def aplicar(self, estado):
                nuevo_estado = copy.deepcopy(estado)
                nuevo_estado[self.fila][self.columna] = 31
                nuevo_estado[self.fila - 1][self.columna] = 31
                nuevo_estado[self.fila-1][self.columna -1] = 31
                nuevo_estado[self.fila - 1][self.columna-2] = 31
                nuevo_estado[self.fila][self.columna - 1] = 31
                return nuevo_estado

#################Poner P3

class ponerP3(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la P3 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_P3(self, estado):
        res = []
        p = 32
        if p - estado[self.fila][self.columna] == p:
            res.append(True)
        else:
            res.append(False)

        if p - estado[self.fila-1][self.columna] == p:
            res.append(True)
        else:
            res.append(False)

        if p - estado[self.fila - 2][self.columna] == p:
            res.append(True)
        else:
            res.append(False)

        if p - estado[self.fila - 1][self.columna + 1] == p:
            res.append(True)
        else:
            res.append(False)

        if p - estado[self.fila - 2][self.columna +1] == p:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 0 and self.columna < len(estado[0])-1 and self.fila >= 2 and self.fila < len(estado):
            if (self.hay_hueco_P3(estado)):  # == True)
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 32
        nuevo_estado[self.fila - 1][self.columna] = 32
        nuevo_estado[self.fila - 2][self.columna] = 32
        nuevo_estado[self.fila - 1][self.columna +1] = 32
        nuevo_estado[self.fila-2][self.columna + 1] = 32
        return nuevo_estado

    #################Poner P4


class ponerP5(probee.Acción):
        def __init__(self, i, j):
            nombre = "Colocamos la P5 en {} {}".format(i, j)
            super().__init__(nombre)
            self.fila = i
            self.columna = j

        def hay_hueco_P5(self, estado):
            res = []
            p = 34
            if p - estado[self.fila][self.columna] == p:
                res.append(True)
            else:
                res.append(False)

            if p - estado[self.fila-1][self.columna] == p:
                res.append(True)
            else:
                res.append(False)

            if p - estado[self.fila-2][self.columna] == p:
                res.append(True)
            else:
                res.append(False)

            if p - estado[self.fila - 1][self.columna - 1] == p:
                res.append(True)
            else:
                res.append(False)

            if p - estado[self.fila - 2][self.columna -1] == p:
                res.append(True)
            else:
                res.append(False)

            if res.count(False) > 0:
                return False
            else:
                return True

        def es_aplicable(self, estado):
            if self.columna >= 1 and self.columna < len(estado[0]) and self.fila >= 2 and self.fila < len(estado):
                if (self.hay_hueco_P5(estado)):  # == True)
                    return True
                else:
                    return False

        def aplicar(self, estado):
            nuevo_estado = copy.deepcopy(estado)
            nuevo_estado[self.fila][self.columna] = 34
            nuevo_estado[self.fila-1][self.columna] = 34
            nuevo_estado[self.fila-2][self.columna] = 34
            nuevo_estado[self.fila - 1][self.columna - 1] = 34
            nuevo_estado[self.fila - 2][self.columna - 1] = 34
            return nuevo_estado


class ponerP6(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la P6 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_P6(self, estado):
        res = []
        p = 35
        if p - estado[self.fila][self.columna] == p:
            res.append(True)
        else:
            res.append(False)

        if p - estado[self.fila][self.columna-1] == p:
            res.append(True)
        else:
            res.append(False)

        if p - estado[self.fila][self.columna-2] == p:
            res.append(True)
        else:
            res.append(False)

        if p - estado[self.fila - 1][self.columna] == p:
            res.append(True)
        else:
            res.append(False)

        if p - estado[self.fila - 1][self.columna -1] == p:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 2 and self.columna < len(estado[0]) and self.fila >= 1 and self.fila < len(estado):
            if (self.hay_hueco_P6(estado)):  # == True)
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 35
        nuevo_estado[self.fila][self.columna-1] = 35
        nuevo_estado[self.fila][self.columna-2] = 35
        nuevo_estado[self.fila - 1][self.columna] = 35
        nuevo_estado[self.fila - 1][self.columna - 1] = 35
        return nuevo_estado






class ponerP7(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la P7 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_P7(self, estado):
        res = []
        p = 36
        if p - estado[self.fila][self.columna] == p:
            res.append(True)
        else:
            res.append(False)

        if p - estado[self.fila][self.columna-1] == p:
            res.append(True)
        else:
            res.append(False)

        if p - estado[self.fila-1][self.columna] == p:
            res.append(True)
        else:
            res.append(False)

        if p - estado[self.fila - 1][self.columna-1] == p:
            res.append(True)
        else:
            res.append(False)

        if p - estado[self.fila - 2][self.columna -1] == p:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 1 and self.columna < len(estado[0]) and self.fila >= 2 and self.fila < len(estado):
            if (self.hay_hueco_P7(estado)):  # == True)
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 36
        nuevo_estado[self.fila][self.columna-1] = 36
        nuevo_estado[self.fila-1][self.columna-1] = 36
        nuevo_estado[self.fila - 1][self.columna] = 36
        nuevo_estado[self.fila - 2][self.columna - 1] = 36
        return nuevo_estado




class ponerP8(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la P8 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_P8(self, estado):
        res = []
        p = 37
        if p - estado[self.fila][self.columna] == p:
            res.append(True)
        else:
            res.append(False)

        if p - estado[self.fila][self.columna-1] == p:
            res.append(True)
        else:
            res.append(False)

        if p - estado[self.fila][self.columna-2] == p:
            res.append(True)
        else:
            res.append(False)

        if p - estado[self.fila + 1][self.columna-1] == p:
            res.append(True)
        else:
            res.append(False)

        if p - estado[self.fila +1][self.columna -2] == p:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 2 and self.columna < len(estado[0]) and self.fila >= 0 and self.fila < len(estado)-1:
            if (self.hay_hueco_P8(estado)):
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 37
        nuevo_estado[self.fila][self.columna-1] = 37
        nuevo_estado[self.fila][self.columna-2] = 37
        nuevo_estado[self.fila +1][self.columna-1] = 37
        nuevo_estado[self.fila +1][self.columna - 2] = 37
        return nuevo_estado





class ponerP4(probee.Acción):
            def __init__(self, i, j):
                nombre = "Colocamos la P4 en {} {}".format(i, j)
                super().__init__(nombre)
                self.fila = i
                self.columna = j

            def hay_hueco_P4(self, estado):
                res = []
                p = 33
                if p - estado[self.fila][self.columna] == p:
                    res.append(True)
                else:
                    res.append(False)

                if p - estado[self.fila][self.columna - 1] == p:
                    res.append(True)
                else:
                    res.append(False)

                if p - estado[self.fila][self.columna - 2] == p:
                    res.append(True)
                else:
                    res.append(False)

                if p - estado[self.fila - 1][self.columna - 1] == p:
                    res.append(True)
                else:
                    res.append(False)

                if p - estado[self.fila - 1][self.columna - 2] == p:
                    res.append(True)
                else:
                    res.append(False)

                if res.count(False) > 0:
                    return False
                else:
                    return True

            def es_aplicable(self, estado):
                if self.columna >= 2 and self.columna < len(estado[0]) and self.fila >= 1 and self.fila < len(estado):
                    if (self.hay_hueco_P4(estado)):  # == True)
                        return True
                    else:
                        return False

            def aplicar(self, estado):
                nuevo_estado = copy.deepcopy(estado)
                nuevo_estado[self.fila][self.columna] = 33
                nuevo_estado[self.fila][self.columna - 1] = 33
                nuevo_estado[self.fila][self.columna - 2] = 33
                nuevo_estado[self.fila - 1][self.columna - 1] = 33
                nuevo_estado[self.fila - 1][self.columna - 2] = 33
                return nuevo_estado




#PONER T-------------------------------------------------------------------------
class ponerT(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la I en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_T(self, estado):
        res = []
        t = 6

        if t - estado[self.fila][self.columna] == t:
            res.append(True)
        else:
            res.append(False)

        if t - estado[self.fila-1][self.columna] == t:
            res.append(True)
        else:
            res.append(False)

        if t - estado[self.fila-2][self.columna] == t:
            res.append(True)
        else:
            res.append(False)

        if t - estado[self.fila-2][self.columna-1] == t:
            res.append(True)
        else:
            res.append(False)

        if t - estado[self.fila-2][self.columna +1] == t:
            res.append(True)
        else:
            res.append(False)

        if res.count(False)>0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 1 and self.columna < len(estado[0])-1 and self.fila >= 2 and self.fila < len(estado):
            if (self.hay_hueco_T(estado)):
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 6
        nuevo_estado[self.fila - 1][self.columna] = 6
        nuevo_estado[self.fila - 2][self.columna] = 6
        nuevo_estado[self.fila - 2][self.columna + 1] = 6
        nuevo_estado[self.fila - 2][self.columna - 1] = 6
        return nuevo_estado



################PONER T2

class ponerT2(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la t2 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_T2(self, estado):
        res = []
        t = 28

        if t - estado[self.fila][self.columna] == t:
            res.append(True)
        else:
            res.append(False)

        if t - estado[self.fila][self.columna-1] == t:
            res.append(True)
        else:
            res.append(False)
        if t - estado[self.fila][self.columna-2] == t:
            res.append(True)
        else:
            res.append(False)

        if t - estado[self.fila - 1][self.columna - 2] == t:
            res.append(True)
        else:
            res.append(False)

        if t - estado[self.fila +1][self.columna -2] == t:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 2 and self.columna < len(estado[0]) and self.fila >= 1 and self.fila < len(estado)-1:
            if (self.hay_hueco_T2(estado)):
                return True

            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 28
        nuevo_estado[self.fila][self.columna-1] = 28
        nuevo_estado[self.fila][self.columna-2] = 28
        nuevo_estado[self.fila - 1][self.columna -2] = 28
        nuevo_estado[self.fila +1][self.columna- 2] = 28
        return nuevo_estado


############ Poner T3
class ponerT3(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la t2 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_T3(self, estado):
        res = []
        t = 29

        if t - estado[self.fila][self.columna] == t:
            res.append(True)
        else:
            res.append(False)

        if t - estado[self.fila][self.columna - 1] == t:
            res.append(True)
        else:
            res.append(False)
        if t - estado[self.fila][self.columna - 2] == t:
            res.append(True)
        else:
            res.append(False)

        if t - estado[self.fila - 1][self.columna - 1] == t:
            res.append(True)
        else:
            res.append(False)

        if t - estado[self.fila - 2][self.columna - 1] == t:
            res.append(True)

        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 2 and self.columna < len(estado[0]) and self.fila >= 2 and self.fila < len(estado):
            if (self.hay_hueco_T3(estado)):
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 29
        nuevo_estado[self.fila][self.columna - 1] = 29
        nuevo_estado[self.fila][self.columna - 2] = 29
        nuevo_estado[self.fila - 1][self.columna - 1] = 29
        nuevo_estado[self.fila -2][self.columna - 1] = 29
        return nuevo_estado

############ Poner T4
class ponerT4(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la t4 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_T4(self, estado):
        res = []
        t = 30

        if t - estado[self.fila][self.columna] == t:
           res.append(True)
        else:
           res.append(False)

        if t - estado[self.fila-1][self.columna] == t:
           res.append(True)
        else:
           res.append(False)
        if t - estado[self.fila+1][self.columna] == t:
            res.append(True)
        else:
            res.append(False)

        if t - estado[self.fila][self.columna - 1] == t:
            res.append(True)
        else:
            res.append(False)

        if t - estado[self.fila][self.columna - 2] == t:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 2 and self.columna < len(estado[0]) and self.fila >= 1 and self.fila < len(estado)-1:
            if (self.hay_hueco_T4(estado)):
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 30
        nuevo_estado[self.fila][self.columna - 1] = 30
        nuevo_estado[self.fila][self.columna - 2] = 30
        nuevo_estado[self.fila - 1][self.columna] = 30
        nuevo_estado[self.fila +1][self.columna] = 30
        return nuevo_estado



#--------------------------------------------GIROS F# -----------------------------------------------------
class ponerF2(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la F2 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_f2(self, estado):
        res = []
        f2 = 8

        if f2 - estado[self.fila][self.columna] == f2:
            res.append(True)
        else:
            res.append(False)

        if f2 - estado[self.fila - 1][self.columna] == f2:
            res.append(True)
        else:
            res.append(False)

        if f2 - estado[self.fila - 1][self.columna -1] == f2:
            res.append(True)
        else:
            res.append(False)

        if f2 - estado[self.fila-1][self.columna+1] == f2:
            res.append(True)
        else:
            res.append(False)

        if f2 - estado[self.fila - 2][self.columna -1] == f2:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 1 and self.columna < len(estado[0])-1 and self.fila >= 2 and self.fila < len(estado):
            if (self.hay_hueco_f2(estado)):  # == True)
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 8
        nuevo_estado[self.fila - 1][self.columna - 1] = 8
        nuevo_estado[self.fila - 1][self.columna + 1] = 8
        nuevo_estado[self.fila -1][self.columna] = 8
        nuevo_estado[self.fila -2][self.columna - 1] = 8
        return nuevo_estado


class ponerF3(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la I en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_F3(self, estado):
        res = []
        f3 = 9

        if f3 - estado[self.fila][self.columna] == f3:
            res.append(True)
        else:
            res.append(False)

        if f3 - estado[self.fila - 1][self.columna] == f3:
            res.append(True)
        else:
            res.append(False)

        if f3 - estado[self.fila][self.columna-1] == f3:
            res.append(True)
        else:
            res.append(False)

        if f3 - estado[self.fila-1][self.columna+1] == f3:
            res.append(True)
        else:
            res.append(False)

        if f3 - estado[self.fila - 2][self.columna] == f3:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 1 and self.columna < len(estado[0])-1 and self.fila >= 2 and self.fila < len(estado):
            if (self.hay_hueco_F3(estado)):  # == True)
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 9
        nuevo_estado[self.fila - 1][self.columna] = 9
        nuevo_estado[self.fila - 1][self.columna+1] = 9
        nuevo_estado[self.fila - 2][self.columna] = 9
        nuevo_estado[self.fila][self.columna-1] = 9
        return nuevo_estado


class ponerF4(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la I en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_F4(self, estado):
        res = []
        f4 = 9

        if f4 - estado[self.fila][self.columna] == f4:
            res.append(True)
        else:
            res.append(False)

        if f4 - estado[self.fila - 1][self.columna] == f4:
            res.append(True)
        else:
            res.append(False)

        if f4 - estado[self.fila - 1][self.columna-1] == f4:
            res.append(True)
        else:
            res.append(False)

        if f4 - estado[self.fila - 1][self.columna-2] == f4:
            res.append(True)
        else:
            res.append(False)

        if f4 - estado[self.fila - 2][self.columna - 1] == f4:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 2 and self.columna < len(estado[0]) and self.fila >= 2 and self.fila < len(estado):
            if (self.hay_hueco_F4(estado)):  # == True)
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 9
        nuevo_estado[self.fila - 1][self.columna] = 9
        nuevo_estado[self.fila - 1][self.columna-1] = 9
        nuevo_estado[self.fila - 1][self.columna-2] = 9
        nuevo_estado[self.fila - 2][self.columna-1] = 9
        return nuevo_estado


class ponerF5(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la I en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_F5(self, estado):
        res = []
        F5 = 10

        if F5 - estado[self.fila][self.columna] == F5:
            res.append(True)
        else:
            res.append(False)

        if F5 - estado[self.fila - 1][self.columna] == F5:
            res.append(True)
        else:
            res.append(False)

        if F5 - estado[self.fila - 1][self.columna-1] == F5:
            res.append(True)
        else:
            res.append(False)

        if F5 - estado[self.fila - 2][self.columna] == F5:
            res.append(True)
        else:
            res.append(False)

        if F5 - estado[self.fila][self.columna +1] == F5:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 1 and self.columna < len(estado[0])-1 and self.fila >= 2 and self.fila < len(estado):
            if (self.hay_hueco_F5(estado)):  # == True)
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 10
        nuevo_estado[self.fila][self.columna+1] = 10
        nuevo_estado[self.fila - 1][self.columna] = 10
        nuevo_estado[self.fila - 1][self.columna-1] = 10
        nuevo_estado[self.fila - 2][self.columna] = 10
        return nuevo_estado


class ponerF6(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la I en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_F6(self, estado):
        res = []
        F6 = 11

        if F6 - estado[self.fila][self.columna] == F6:
            res.append(True)
        else:
            res.append(False)

        if F6 - estado[self.fila - 1][self.columna] == F6:
            res.append(True)
        else:
            res.append(False)

        if F6 - estado[self.fila - 1][self.columna+1] == F6:
            res.append(True)
        else:
            res.append(False)

        if F6 - estado[self.fila - 1][self.columna+2] == F6:
            res.append(True)
        else:
            res.append(False)

        if F6 - estado[self.fila - 2][self.columna + 1] == F6:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 0 and self.columna < len(estado[0])-2 and self.fila >= 2 and self.fila < len(estado):
            if (self.hay_hueco_F6(estado)):  # == True)
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 11
        nuevo_estado[self.fila - 1][self.columna] = 11
        nuevo_estado[self.fila - 1][self.columna+1] = 11
        nuevo_estado[self.fila - 1][self.columna+2] = 11
        nuevo_estado[self.fila - 2][self.columna+1] = 11
        return nuevo_estado


class ponerF7(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la I en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_F7(self, estado):
        res = []
        F7 = 12

        if F7 - estado[self.fila][self.columna] == F7:
            res.append(True)
        else:
            res.append(False)

        if F7 - estado[self.fila - 1][self.columna] == F7:
            res.append(True)
        else:
            res.append(False)

        if F7 - estado[self.fila - 1][self.columna+1] == F7:
            res.append(True)
        else:
            res.append(False)

        if F7 - estado[self.fila - 2][self.columna] == F7:
            res.append(True)
        else:
            res.append(False)

        if F7 - estado[self.fila - 2][self.columna - 1] == F7:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 1 and self.columna < len(estado[0])-1 and self.fila >= 2 and self.fila < len(estado):
            if (self.hay_hueco_F7(estado)):  # == True)
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 12
        nuevo_estado[self.fila - 1][self.columna] = 12
        nuevo_estado[self.fila - 1][self.columna+1] = 12
        nuevo_estado[self.fila - 2][self.columna] = 12
        nuevo_estado[self.fila - 2][self.columna-1] = 12
        return nuevo_estado


class ponerF8(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la I en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_F8(self, estado):
        res = []
        F8 = 13

        if F8 - estado[self.fila][self.columna] == F8:
            res.append(True)
        else:
            res.append(False)

        if F8 - estado[self.fila - 1][self.columna] == F8:
            res.append(True)
        else:
            res.append(False)

        if F8 - estado[self.fila - 1][self.columna-1] == F8:
            res.append(True)
        else:
            res.append(False)

        if F8 - estado[self.fila - 1][self.columna+1] == F8:
            res.append(True)
        else:
            res.append(False)

        if F8 - estado[self.fila - 2][self.columna + 1] == F8:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 1 and self.columna < len(estado[0])-1 and self.fila >= 2 and self.fila < len(estado):
            if (self.hay_hueco_F8(estado)):
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 13
        nuevo_estado[self.fila - 1][self.columna] = 13
        nuevo_estado[self.fila - 1][self.columna-1] = 13
        nuevo_estado[self.fila - 1][self.columna+1] = 13
        nuevo_estado[self.fila - 2][self.columna+1] = 13
        return nuevo_estado

#--------------------------------------------GIROS L-----------------------------------------------------
class ponerL2(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la I en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_L2(self, estado):
        res = []
        l2 = 14

        if l2 - estado[self.fila][self.columna] == l2:
            res.append(True)
        else:
            res.append(False)

        if l2 - estado[self.fila-1][self.columna] == l2:
            res.append(True)
        else:
            res.append(False)

        if l2 - estado[self.fila][self.columna -1] == l2:
            res.append(True)
        else:
            res.append(False)

        if l2 - estado[self.fila][self.columna-2] == l2:
            res.append(True)
        else:
            res.append(False)

        if l2 - estado[self.fila][self.columna -3] == l2:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 3 and self.columna < len(estado[0]) and self.fila >= 1 and self.fila < len(estado):
            if (self.hay_hueco_L2(estado)):  # == True)
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 14
        nuevo_estado[self.fila - 1][self.columna] = 14
        nuevo_estado[self.fila][self.columna-1] = 14
        nuevo_estado[self.fila][self.columna-2] = 14
        nuevo_estado[self.fila][self.columna-3] = 14
        return nuevo_estado


class ponerL3(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la I en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_L3(self, estado):
        res = []
        l3 = 15

        if l3 - estado[self.fila][self.columna] == l3:
            res.append(True)
        else:
            res.append(False)

        if l3 - estado[self.fila - 1][self.columna] == l3:
            res.append(True)
        else:
            res.append(False)

        if l3 - estado[self.fila-2][self.columna] == l3:
            res.append(True)
        else:
            res.append(False)

        if l3 - estado[self.fila-3][self.columna] == l3:
            res.append(True)
        else:
            res.append(False)

        if l3 - estado[self.fila - 3][self.columna-1] == l3:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 1 and self.columna < len(estado[0]) and self.fila >= 3 and self.fila < len(estado):
            if (self.hay_hueco_L3(estado)):  # == True)
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 15
        nuevo_estado[self.fila - 1][self.columna] = 15
        nuevo_estado[self.fila - 2][self.columna] = 15
        nuevo_estado[self.fila - 3][self.columna] = 15
        nuevo_estado[self.fila - 3][self.columna - 1] = 15
        return nuevo_estado


class ponerL4(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la L4 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_L4(self, estado):
        res = []
        l4 = 16

        if l4 - estado[self.fila][self.columna] == l4:
            res.append(True)
        else:
            res.append(False)

        if l4 - estado[self.fila +1][self.columna] == l4:
            res.append(True)
        else:
            res.append(False)

        if l4 - estado[self.fila][self.columna+1] == l4:
            res.append(True)
        else:
            res.append(False)

        if l4 - estado[self.fila][self.columna+2] == l4:
            res.append(True)
        else:
            res.append(False)

        if l4 - estado[self.fila][self.columna+3] == l4:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 0 and self.columna < len(estado[0])-3 and self.fila >= 0 and self.fila < len(estado)-1:
            if (self.hay_hueco_L4(estado)):
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 16
        nuevo_estado[self.fila+1][self.columna] = 16
        nuevo_estado[self.fila][self.columna+1] = 16
        nuevo_estado[self.fila][self.columna+2] = 16
        nuevo_estado[self.fila][self.columna+3] = 16
        return nuevo_estado


class ponerL5(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la I en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_L5(self, estado):
        res = []
        l5 = 17

        if l5 - estado[self.fila][self.columna] == l5:
            res.append(True)
        else:
            res.append(False)

        if l5 - estado[self.fila - 1][self.columna] == l5:
            res.append(True)
        else:
            res.append(False)

        if l5 - estado[self.fila - 2][self.columna] == l5:
            res.append(True)
        else:
            res.append(False)

        if l5 - estado[self.fila - 3][self.columna] == l5:
            res.append(True)
        else:
            res.append(False)

        if l5 - estado[self.fila - 3][self.columna +1] == l5:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 0 and self.columna < len(estado[0])-1 and self.fila >= 3 and self.fila < len(estado):
            if (self.hay_hueco_L5(estado)):  # == True)
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 17
        nuevo_estado[self.fila - 1][self.columna] = 17
        nuevo_estado[self.fila - 2][self.columna] = 17
        nuevo_estado[self.fila - 3][self.columna] = 17
        nuevo_estado[self.fila - 3][self.columna+1] = 17
        return nuevo_estado


class ponerL6(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la I en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_L6(self, estado):
        res = []
        l6 = 18

        if l6 - estado[self.fila][self.columna] == l6:
            res.append(True)
        else:
            res.append(False)

        if l6 - estado[self.fila - 1][self.columna] == l6:
            res.append(True)
        else:
            res.append(False)

        if l6 - estado[self.fila - 1][self.columna-1] == l6:
            res.append(True)
        else:
            res.append(False)

        if l6 - estado[self.fila - 1][self.columna-2] == l6:
            res.append(True)
        else:
            res.append(False)

        if l6 - estado[self.fila - 1][self.columna-3] == l6:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 3 and self.columna < len(estado[0]) and self.fila >= 1 and self.fila < len(estado):
            if (self.hay_hueco_L6(estado)):  # == True)
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 18
        nuevo_estado[self.fila - 1][self.columna] = 18
        nuevo_estado[self.fila - 1][self.columna-1] = 18
        nuevo_estado[self.fila - 1][self.columna-2] = 18
        nuevo_estado[self.fila - 1][self.columna-3] = 18
        return nuevo_estado


class ponerL7(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la I en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_L7(self, estado):
        res = []
        l7 = 19

        if l7 - estado[self.fila][self.columna] == l7:
            res.append(True)
        else:
            res.append(False)

        if l7 - estado[self.fila - 1][self.columna] == l7:
            res.append(True)
        else:
            res.append(False)

        if l7 - estado[self.fila - 2][self.columna] == l7:
            res.append(True)
        else:
            res.append(False)

        if l7 - estado[self.fila - 3][self.columna] == l7:
            res.append(True)
        else:
            res.append(False)

        if l7 - estado[self.fila][self.columna - 1] == l7:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 1 and self.columna < len(estado[0]) and self.fila >= 3 and self.fila < len(estado):
            if (self.hay_hueco_L7(estado)):  # == True)
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 19
        nuevo_estado[self.fila - 1][self.columna] = 19
        nuevo_estado[self.fila - 2][self.columna] = 19
        nuevo_estado[self.fila - 3][self.columna] = 19
        nuevo_estado[self.fila][self.columna-1] = 19
        return nuevo_estado


class ponerL8(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la I en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_L8(self, estado):
        res = []
        l8 = 20

        if l8 - estado[self.fila][self.columna] == l8:
            res.append(True)
        else:
            res.append(False)

        if l8 - estado[self.fila - 1][self.columna] == l8:
            res.append(True)
        else:
            res.append(False)

        if l8 - estado[self.fila][self.columna+1] == l8:
            res.append(True)
        else:
            res.append(False)

        if l8 - estado[self.fila][self.columna+2] == l8:
            res.append(True)
        else:
            res.append(False)

        if l8 - estado[self.fila][self.columna + 3] == l8:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 0 and self.columna < len(estado[0])-3 and self.fila >= 1 and self.fila < len(estado):
            if (self.hay_hueco_L8(estado)):  # == True)
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 20
        nuevo_estado[self.fila - 1][self.columna] = 20
        nuevo_estado[self.fila][self.columna+1] = 20
        nuevo_estado[self.fila][self.columna+2] = 20
        nuevo_estado[self.fila][self.columna+3] = 20
        return nuevo_estado


#----------------------------------------------------GIROS N----------------------------------------------------

class ponerN2(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la I en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_N2(self, estado):
        res = []
        n2 = 21

        if n2 - estado[self.fila][self.columna] == n2:
            res.append(True)
        else:
            res.append(False)

        if n2 - estado[self.fila-1][self.columna-3] == n2:
            res.append(True)
        else:
            res.append(False)

        if n2 - estado[self.fila-1][self.columna -2] == n2:
            res.append(True)
        else:
            res.append(False)

        if n2 - estado[self.fila][self.columna-1] == n2:
            res.append(True)
        else:
            res.append(False)

        if n2 - estado[self.fila][self.columna-2] == n2:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 3 and self.columna < len(estado[0]) and self.fila >= 1 and self.fila < len(estado):
            if (self.hay_hueco_N2(estado)):  # == True)
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 21
        nuevo_estado[self.fila - 1][self.columna-2] = 21
        nuevo_estado[self.fila - 1][self.columna-3] = 21
        nuevo_estado[self.fila][self.columna-1] = 21
        nuevo_estado[self.fila][self.columna-2] = 21
        return nuevo_estado


class ponerN3(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la I en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_N3(self, estado):
        res = []
        n3 = 22

        if n3 - estado[self.fila][self.columna] == n3:
            res.append(True)
        else:
            res.append(False)

        if n3 - estado[self.fila - 1][self.columna] == n3:
            res.append(True)
        else:
            res.append(False)

        if n3 - estado[self.fila-1][self.columna+1] == n3:
            res.append(True)
        else:
            res.append(False)

        if n3 - estado[self.fila-2][self.columna+1] == n3:
            res.append(True)
        else:
            res.append(False)

        if n3 - estado[self.fila - 3][self.columna+1] == n3:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 0 and self.columna < len(estado[0])-1 and self.fila >= 3 and self.fila < len(estado):
            if (self.hay_hueco_N3(estado)):  # == True)
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 22
        nuevo_estado[self.fila - 1][self.columna] = 22
        nuevo_estado[self.fila - 1][self.columna+1] = 22
        nuevo_estado[self.fila - 2][self.columna+1] = 22
        nuevo_estado[self.fila - 3][self.columna+1] = 22
        return nuevo_estado


class ponerN4(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la L4 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_N4(self, estado):
        res = []
        n4 = 23

        if n4 - estado[self.fila][self.columna] == n4:
            res.append(True)
        else:
            res.append(False)

        if n4 - estado[self.fila][self.columna+1] == n4:
            res.append(True)
        else:
            res.append(False)

        if n4 - estado[self.fila-1][self.columna] == n4:
            res.append(True)
        else:
            res.append(False)

        if n4 - estado[self.fila-1][self.columna-1] == n4:
            res.append(True)
        else:
            res.append(False)

        if n4 - estado[self.fila-1][self.columna-2] == n4:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 2 and self.columna < len(estado[0])-1 and self.fila >= 1 and self.fila < len(estado):
            if (self.hay_hueco_N4(estado)):
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 23
        nuevo_estado[self.fila-1][self.columna] = 23
        nuevo_estado[self.fila][self.columna+1] = 23
        nuevo_estado[self.fila-1][self.columna-1] = 23
        nuevo_estado[self.fila-1][self.columna-2] = 23
        return nuevo_estado


class ponerN5(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la I en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_N5(self, estado):
        res = []
        n5 = 24

        if n5 - estado[self.fila][self.columna] == n5:
            res.append(True)
        else:
            res.append(False)

        if n5 - estado[self.fila - 1][self.columna] == n5:
            res.append(True)
        else:
            res.append(False)

        if n5 - estado[self.fila - 1][self.columna-1] == n5:
            res.append(True)
        else:
            res.append(False)

        if n5 - estado[self.fila - 2][self.columna-1] == n5:
            res.append(True)
        else:
            res.append(False)

        if n5 - estado[self.fila - 3][self.columna -1] == n5:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 1 and self.columna < len(estado[0]) and self.fila >= 3 and self.fila < len(estado):
            if (self.hay_hueco_N5(estado)):  # == True)
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 24
        nuevo_estado[self.fila - 1][self.columna] = 24
        nuevo_estado[self.fila - 1][self.columna-1] = 24
        nuevo_estado[self.fila - 2][self.columna-1] = 24
        nuevo_estado[self.fila - 3][self.columna-1] = 24
        return nuevo_estado


class ponerN6(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la I en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_N6(self, estado):
        res = []
        n6 = 25

        if n6 - estado[self.fila][self.columna] == n6:
            res.append(True)
        else:
            res.append(False)

        if n6 - estado[self.fila - 1][self.columna] == n6:
            res.append(True)
        else:
            res.append(False)

        if n6 - estado[self.fila][self.columna-1] == n6:
            res.append(True)
        else:
            res.append(False)

        if n6 - estado[self.fila - 1][self.columna+1] == n6:
            res.append(True)
        else:
            res.append(False)

        if n6 - estado[self.fila - 1][self.columna+2] == n6:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 1 and self.columna < len(estado[0])-2 and self.fila >= 1 and self.fila < len(estado):
            if (self.hay_hueco_N6(estado)):  # == True)
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 25
        nuevo_estado[self.fila - 1][self.columna] = 25
        nuevo_estado[self.fila - 1][self.columna+1] = 25
        nuevo_estado[self.fila - 1][self.columna +2] = 25
        nuevo_estado[self.fila][self.columna-1] = 25
        return nuevo_estado


class ponerN7(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la I en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_N7(self, estado):
        res = []
        n7 = 26

        if n7 - estado[self.fila][self.columna] == n7:
            res.append(True)
        else:
            res.append(False)

        if n7 - estado[self.fila - 1][self.columna] == n7:
            res.append(True)
        else:
            res.append(False)

        if n7 - estado[self.fila - 2][self.columna] == n7:
            res.append(True)
        else:
            res.append(False)

        if n7 - estado[self.fila - 2][self.columna-1] == n7:
            res.append(True)
        else:
            res.append(False)

        if n7 - estado[self.fila-3][self.columna - 1] == n7:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 1 and self.columna < len(estado[0]) and self.fila >= 3 and self.fila < len(estado):
            if (self.hay_hueco_N7(estado)):  # == True)
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 26
        nuevo_estado[self.fila - 1][self.columna] = 26
        nuevo_estado[self.fila - 2][self.columna] = 26
        nuevo_estado[self.fila - 2][self.columna-1] = 26
        nuevo_estado[self.fila - 3][self.columna-1] = 26
        return nuevo_estado


class ponerN8(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la I en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_N8(self, estado):
        res = []
        n8 = 27

        if n8 - estado[self.fila][self.columna] == n8:
            res.append(True)
        else:
            res.append(False)

        if n8 - estado[self.fila - 1][self.columna] == n8:
            res.append(True)
        else:
            res.append(False)

        if n8 - estado[self.fila-1][self.columna+1] == n8:
            res.append(True)
        else:
            res.append(False)

        if n8 - estado[self.fila][self.columna-1] == n8:
            res.append(True)
        else:
            res.append(False)

        if n8 - estado[self.fila][self.columna-2] == n8:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):
        if self.columna >= 2 and self.columna < len(estado[0])-1 and self.fila >= 1 and self.fila < len(estado):
            if (self.hay_hueco_N8(estado)):
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 27
        nuevo_estado[self.fila - 1][self.columna] = 27
        nuevo_estado[self.fila - 1][self.columna+1] = 27
        nuevo_estado[self.fila][self.columna-1] = 27
        nuevo_estado[self.fila][self.columna-2] = 27
        return nuevo_estado

class ponerV(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la V en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_V(self, estado):

      res = []
      v=39

      if v -  estado[self.fila][self.columna] == v:
            res.append(True)
      else:
            res.append(False)
      if v - estado[self.fila][self.columna-1] == v:
            res.append(True)
      else:
            res.append(False)

      if v- estado[self.fila][self.columna-2] == v:
            res.append(True)
      else:
            res.append(False)

      if v- estado[self.fila-1][self.columna -2] ==v:
            res.append(True)
      else:
            res.append(False)

      if v - estado[self.fila-2][self.columna -2] == v:
            res.append(True)
      else:
            res.append(False)

      if res.count(False) > 0:
        return False
      else:
        return True


    def es_aplicable(self, estado):

        if self.columna >= 2 and self.columna < len(estado[0]) and self.fila >= 2 and self.fila < len(estado):

            if (self.hay_hueco_V(estado)):
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 39
        nuevo_estado[self.fila][self.columna -1] = 39
        nuevo_estado[self.fila][self.columna - 2] = 39
        nuevo_estado[self.fila-1][self.columna-2] = 39
        nuevo_estado[self.fila -2][self.columna-2] = 39
        return nuevo_estado



############Poner V2

class ponerV2(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la V2 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_V2(self, estado):
        res = []
        v=40
        if v - estado[self.fila][self.columna] == v:
            res.append(True)
        else:
            res.append(False)
        if v - estado[self.fila][self.columna+1] == v:
            res.append(True)
        else:
            res.append(False)

        if v- estado[self.fila][self.columna+2] == v:
            res.append(True)
        else:
            res.append(False)

        if v- estado[self.fila-1][self.columna+2] == v:
            res.append(True)
        else:
            res.append(False)

        if v- estado[self.fila-2][self.columna+2]== v:
            res.append(True)
        else:
            res.append(False)


        if res.count(False) > 0:
            return False
        else:
            return True


    def es_aplicable(self, estado):

        if self.columna >= 0 and self.columna < len(estado[0])-2 and self.fila >= 2 and self.fila < len(estado):
            if (self.hay_hueco_V2(estado)):
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 40
        nuevo_estado[self.fila][self.columna+1] = 40
        nuevo_estado[self.fila][self.columna+2] = 40
        nuevo_estado[self.fila-1][self.columna +2] = 40
        nuevo_estado[self.fila-2][self.columna +2] = 40
        return nuevo_estado





############Poner V3

class ponerV3(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la V3 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_V3(self, estado):

        res = []
        v3=41

        if v3- estado[self.fila][self.columna] == v3:
                    res.append(True)
        else:
                    res.append(False)

        if v3 -  estado[self.fila-1][self.columna] == v3:
                    res.append(True)
        else:
                    res.append(False)
        if  v3 - estado[self.fila-2][self.columna] == v3:
                    res.append(True)
        else:
                    res.append(False)

        if v3 -  estado[self.fila-2][self.columna -1] == v3:
                    res.append(True)
        else:
                    res.append(False)

        if  v3 - estado[self.fila-2][self.columna - 2]== v3:
                    res.append(True)
        else:
                    res.append(False)
        if res.count(False) > 0:
                return False
        else:
                return True



    def es_aplicable(self, estado):

        if self.columna >= 2 and self.columna < len(estado[0]) and self.fila >= 2 and self.fila < len(estado):
            if (self.hay_hueco_V3(estado)):
                return True
            else:
                return False


    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 41
        nuevo_estado[self.fila-1][self.columna] = 41
        nuevo_estado[self.fila-2][self.columna] = 41
        nuevo_estado[self.fila-2][self.columna-1] = 41
        nuevo_estado[self.fila-2][self.columna-2] = 41
        return nuevo_estado



############Poner V4

class ponerV4(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la V4 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_V4(self, estado):

        res = []
        v4=42

        if v4- estado[self.fila][self.columna] == v4:
                    res.append(True)
        else:
                    res.append(False)

        if v4 -  estado[self.fila][self.columna-1] == v4:
                    res.append(True)
        else:
                    res.append(False)
        if  v4 - estado[self.fila][self.columna-2] == v4:
                    res.append(True)
        else:
                    res.append(False)

        if v4 -  estado[self.fila+2][self.columna -2] == v4:
                    res.append(True)
        else:
                    res.append(False)

        if  v4 - estado[self.fila+1][self.columna -2]== v4:
                    res.append(True)
        else:
                    res.append(False)
        if res.count(False) > 0:
                return False
        else:
                return True



    def es_aplicable(self, estado):

        if self.columna >= 2 and self.columna < len(estado[0]) and self.fila >= 0 and self.fila < len(estado)-2:
            if (self.hay_hueco_V4(estado)):
                return True
            else:
                return False


    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 42
        nuevo_estado[self.fila][self.columna-1] = 42
        nuevo_estado[self.fila][self.columna-2] = 42
        nuevo_estado[self.fila+1][self.columna-2] = 42
        nuevo_estado[self.fila+2][self.columna-2] = 42
        return nuevo_estado


############Poner U

class ponerU(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la U en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_U(self, estado):

        res = []
        u=43

        if u- estado[self.fila][self.columna] == u:
                    res.append(True)
        else:
                    res.append(False)

        if u -  estado[self.fila][self.columna+1] == u:
                    res.append(True)
        else:
                    res.append(False)
        if  u - estado[self.fila][self.columna+2] == u:
                    res.append(True)
        else:
                    res.append(False)

        if u -  estado[self.fila-1][self.columna+2] == u:
                    res.append(True)
        else:
                    res.append(False)

        if  u - estado[self.fila-1][self.columna]== u:
                    res.append(True)
        else:
                    res.append(False)

        if res.count(False) > 0:
                return False
        else:
                return True



    def es_aplicable(self, estado):

        if self.columna >= 0 and self.columna <= len(estado[0])-2 and self.fila >= 1 and self.fila < len(estado):
            if (self.hay_hueco_U(estado)):
                return True
            else:
                return False


    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 43
        nuevo_estado[self.fila][self.columna+1] = 43
        nuevo_estado[self.fila][self.columna+2] = 43
        nuevo_estado[self.fila-1][self.columna+2] = 43
        nuevo_estado[self.fila-1][self.columna] = 43
        return nuevo_estado



############Poner U2

class ponerU2(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la U2 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_U2(self, estado):

        res = []
        u=44

        if u - estado[self.fila][self.columna] == u:
                    res.append(True)
        else:
                    res.append(False)

        if u -  estado[self.fila-1][self.columna] == u:
                    res.append(True)
        else:
                    res.append(False)
        if  u - estado[self.fila+1][self.columna] == u:
                    res.append(True)
        else:
                    res.append(False)

        if u -  estado[self.fila-1][self.columna-1] == u:
                    res.append(True)
        else:
                    res.append(False)

        if  u - estado[self.fila+1][self.columna -1]== u:
                    res.append(True)
        else:
                    res.append(False)

        if res.count(False) > 0:
                return False
        else:
                return True



    def es_aplicable(self, estado):

        if self.columna >= 1 and self.columna < len(estado[0]) and self.fila >= 1 and self.fila < len(estado)-1:
            if (self.hay_hueco_U2(estado)):
                return True
            else:
                return False


    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 44
        nuevo_estado[self.fila-1][self.columna] = 44
        nuevo_estado[self.fila+1][self.columna] = 44
        nuevo_estado[self.fila-1][self.columna-1] = 44
        nuevo_estado[self.fila+1][self.columna-1] = 44
        return nuevo_estado



############Poner U3

class ponerU3(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la U3 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_U3(self, estado):

        res = []
        u=45

        if u- estado[self.fila][self.columna] == u:
                    res.append(True)
        else:
                    res.append(False)

        if u -  estado[self.fila][self.columna-1] == u:
                    res.append(True)
        else:
                    res.append(False)
        if  u - estado[self.fila][self.columna+1] == u:
                    res.append(True)
        else:
                    res.append(False)

        if u -  estado[self.fila+1][self.columna-1] == u:
                    res.append(True)
        else:
                    res.append(False)

        if  u - estado[self.fila+1][self.columna +1]== u:
                    res.append(True)
        else:
                    res.append(False)

        if res.count(False) > 0:
                return False
        else:
                return True



    def es_aplicable(self, estado):

        if self.columna >= 1 and self.columna < len(estado[0])-1 and self.fila >= 0 and self.fila < len(estado)-1:
            if (self.hay_hueco_U3(estado)):
                return True
            else:
                return False


    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 45
        nuevo_estado[self.fila+1][self.columna+1] = 45
        nuevo_estado[self.fila+1][self.columna-1] = 45
        nuevo_estado[self.fila][self.columna+1] = 45
        nuevo_estado[self.fila][self.columna-1] = 45
        return nuevo_estado



############Poner U4

class ponerU4(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la U4 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_U4(self, estado):

        res = []
        u=46

        if u- estado[self.fila][self.columna] == u:

                    res.append(True)
        else:
                    res.append(False)

        if u -  estado[self.fila-1][self.columna] == u:
                    res.append(True)
        else:
                    res.append(False)
        if  u - estado[self.fila-1][self.columna+1] == u:
                    res.append(True)
        else:
                    res.append(False)

        if u -  estado[self.fila+1][self.columna] == u:
                    res.append(True)
        else:
                    res.append(False)

        if  u - estado[self.fila+1][self.columna +1]== u:
                    res.append(True)
        else:
                    res.append(False)

        if res.count(False) > 0:
                return False
        else:
                return True



    def es_aplicable(self, estado):

        if self.columna >= 0 and self.columna < len(estado[0])-1 and self.fila >=1 and self.fila < len(estado)-1:
            if (self.hay_hueco_U4(estado)):
                return True
            else:
                return False


    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 46
        nuevo_estado[self.fila-1][self.columna] = 46
        nuevo_estado[self.fila-1][self.columna+1] = 46
        nuevo_estado[self.fila+1][self.columna] = 46
        nuevo_estado[self.fila+1][self.columna+1] = 46
        return nuevo_estado


############Poner W

class ponerW(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la W en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_W(self, estado):

        res = []
        w=47

        if w- estado[self.fila][self.columna] == w:
                    res.append(True)
        else:
                    res.append(False)

        if w -  estado[self.fila][self.columna-1] == w:
                    res.append(True)
        else:
                    res.append(False)
        if  w - estado[self.fila-1][self.columna-1] == w:
                    res.append(True)
        else:
                    res.append(False)

        if w -  estado[self.fila+1][self.columna] == w:
                    res.append(True)
        else:
                    res.append(False)

        if  w - estado[self.fila+1][self.columna+1]== w:
                    res.append(True)
        else:
                    res.append(False)

        if res.count(False) > 0:
                return False
        else:
                return True

    def es_aplicable(self, estado):

        if self.columna >= 1 and self.columna < len(estado[0])-1 and self.fila >= 1 and self.fila < len(estado)-1:
            if (self.hay_hueco_W(estado)):
                return True
            else:
                return False


    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 47
        nuevo_estado[self.fila][self.columna-1] = 47
        nuevo_estado[self.fila-1][self.columna-1] = 47
        nuevo_estado[self.fila+1][self.columna] = 47
        nuevo_estado[self.fila+1][self.columna+1] = 47
        return nuevo_estado


class ponerW2(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la W2 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_W2(self, estado):

        res = []
        w=48

        if w- estado[self.fila][self.columna] == w:
                    res.append(True)
        else:
                    res.append(False)

        if w -  estado[self.fila][self.columna+1] == w:
                    res.append(True)
        else:
                    res.append(False)
        if  w - estado[self.fila-1][self.columna+1] == w:
                    res.append(True)
        else:
                    res.append(False)

        if w -  estado[self.fila+1][self.columna] == w:
                    res.append(True)
        else:
                    res.append(False)

        if  w - estado[self.fila+1][self.columna-1]== w:
                    res.append(True)
        else:
                    res.append(False)

        if res.count(False) > 0:
                return False
        else:
                return True

    def es_aplicable(self, estado):

        if self.columna >= 1 and self.columna < len(estado[0])-1 and self.fila >= 1 and self.fila < len(estado)-1:
            if (self.hay_hueco_W2(estado)):
                return True
            else:
                return False


    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 48
        nuevo_estado[self.fila][self.columna+1] = 48
        nuevo_estado[self.fila-1][self.columna+1] = 48
        nuevo_estado[self.fila+1][self.columna] = 48
        nuevo_estado[self.fila+1][self.columna-1] = 48
        return nuevo_estado

class ponerW3(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la W2 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_W3(self, estado):

        res = []
        w=49

        if w- estado[self.fila][self.columna] == w:
                    res.append(True)
        else:
                    res.append(False)

        if w -  estado[self.fila][self.columna+1] == w:
                    res.append(True)
        else:
                    res.append(False)
        if  w - estado[self.fila+1][self.columna+1] == w:
                    res.append(True)
        else:
                    res.append(False)

        if w -  estado[self.fila-1][self.columna] == w:
                    res.append(True)
        else:
                    res.append(False)

        if  w - estado[self.fila-1][self.columna-1]== w:
                    res.append(True)
        else:
                    res.append(False)

        if res.count(False) > 0:
                return False
        else:
                return True

    def es_aplicable(self, estado):

        if self.columna >= 1 and self.columna < len(estado[0])-1 and self.fila >= 1 and self.fila < len(estado)-1:
            if (self.hay_hueco_W3(estado)):
                return True
            else:
                return False


    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 49
        nuevo_estado[self.fila][self.columna+1] = 49
        nuevo_estado[self.fila+1][self.columna+1] = 49
        nuevo_estado[self.fila-1][self.columna-1] = 49
        nuevo_estado[self.fila-1][self.columna] = 49
        return nuevo_estado

class ponerW4(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la W2 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_W4(self, estado):

        res = []
        w=50

        if w- estado[self.fila][self.columna] == w:
                    res.append(True)
        else:
                    res.append(False)

        if w -  estado[self.fila-1][self.columna] == w:
                    res.append(True)
        else:
                    res.append(False)
        if  w - estado[self.fila-1][self.columna+1] == w:
                    res.append(True)
        else:
                    res.append(False)

        if w -  estado[self.fila+1][self.columna-1] == w:
                    res.append(True)
        else:
                    res.append(False)

        if  w - estado[self.fila][self.columna-1]== w:
                    res.append(True)
        else:
                    res.append(False)

        if res.count(False) > 0:
                return False
        else:
                return True

    def es_aplicable(self, estado):

        if self.columna >= 1 and self.columna < len(estado[0])-1 and self.fila >= 1 and self.fila < len(estado)-1:
            if (self.hay_hueco_W4(estado)):
                return True
            else:
                return False


    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 50
        nuevo_estado[self.fila-1][self.columna] = 50
        nuevo_estado[self.fila-1][self.columna+1] = 50
        nuevo_estado[self.fila+1][self.columna-1] = 50
        nuevo_estado[self.fila][self.columna-1] = 50
        return nuevo_estado

class ponerX(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la W2 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_X(self, estado):

        res = []
        x=51

        if x- estado[self.fila][self.columna] == x:
                    res.append(True)
        else:
                    res.append(False)

        if x -  estado[self.fila-1][self.columna] == x:
                    res.append(True)
        else:
                    res.append(False)
        if  x - estado[self.fila+1][self.columna] == x:
                    res.append(True)
        else:
                    res.append(False)

        if x -  estado[self.fila][self.columna-1] == x:
                    res.append(True)
        else:
                    res.append(False)

        if  x - estado[self.fila][self.columna+1]== x:
                    res.append(True)
        else:
                    res.append(False)

        if res.count(False) > 0:
                return False
        else:
                return True

    def es_aplicable(self, estado):

        if self.columna >= 1 and self.columna < len(estado[0])-1 and self.fila >= 1 and self.fila < len(estado)-1:
            if (self.hay_hueco_X(estado)):
                return True
            else:
                return False


    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 51
        nuevo_estado[self.fila-1][self.columna] = 51
        nuevo_estado[self.fila+1][self.columna] = 51
        nuevo_estado[self.fila][self.columna+1] = 51
        nuevo_estado[self.fila][self.columna-1] = 51
        return nuevo_estado


class ponerY(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la W2 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_Y(self, estado):

        res = []
        y=52

        if y- estado[self.fila][self.columna] == y:
                    res.append(True)
        else:
                    res.append(False)

        if y -  estado[self.fila-1][self.columna] == y:
                    res.append(True)
        else:
                    res.append(False)
        if  y - estado[self.fila-2][self.columna] == y:
                    res.append(True)
        else:
                    res.append(False)

        if y -  estado[self.fila-2][self.columna-1] == y:
                    res.append(True)
        else:
                    res.append(False)

        if  y - estado[self.fila-3][self.columna]== y:
                    res.append(True)
        else:
                    res.append(False)

        if res.count(False) > 0:
                return False
        else:
                return True

    def es_aplicable(self, estado):

        if self.columna >= 1 and self.columna < len(estado[0]) and self.fila >= 3 and self.fila < len(estado):
            if (self.hay_hueco_Y(estado)):
                return True
            else:
                return False


    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 52
        nuevo_estado[self.fila-1][self.columna] = 52
        nuevo_estado[self.fila-2][self.columna] = 52
        nuevo_estado[self.fila-2][self.columna-1] = 52
        nuevo_estado[self.fila-3][self.columna] = 52
        return nuevo_estado



class ponerY2(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la Y2 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_Y2(self, estado):

        res = []
        y=53

        if y- estado[self.fila][self.columna] == y:
                    res.append(True)
        else:
                    res.append(False)

        if y -  estado[self.fila-1][self.columna] == y:
                    res.append(True)
        else:
                    res.append(False)
        if  y - estado[self.fila-2][self.columna] == y:
                    res.append(True)
        else:
                    res.append(False)

        if y -  estado[self.fila-3][self.columna] == y:
                    res.append(True)
        else:
                    res.append(False)

        if  y - estado[self.fila-2][self.columna+1]== y:
                    res.append(True)
        else:
                    res.append(False)

        if res.count(False) > 0:
                return False
        else:
                return True

    def es_aplicable(self, estado):

        if self.columna >= 0 and self.columna < len(estado[0])-1 and self.fila >= 3 and self.fila < len(estado):
            if (self.hay_hueco_Y2(estado)):
                return True
            else:
                return False


    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 53
        nuevo_estado[self.fila-1][self.columna] = 53
        nuevo_estado[self.fila-2][self.columna] = 53
        nuevo_estado[self.fila-3][self.columna] = 53
        nuevo_estado[self.fila-2][self.columna+1] = 53
        return nuevo_estado

class ponerY3(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la Y3 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_Y3(self, estado):

        res = []
        y = 54

        if y - estado[self.fila][self.columna] == y:
            res.append(True)
        else:
            res.append(False)

        if y - estado[self.fila - 1][self.columna] == y:
            res.append(True)
        else:
            res.append(False)

        if y - estado[self.fila - 1][self.columna - 1] == y:
            res.append(True)
        else:
            res.append(False)

        if y - estado[self.fila - 2][self.columna] == y:
            res.append(True)
        else:
            res.append(False)

        if y - estado[self.fila - 3][self.columna] == y:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):

        if self.columna >= 1 and self.columna < len(estado[0]) and self.fila >= 3 and self.fila < len(estado):
            if (self.hay_hueco_Y3(estado)):
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 54
        nuevo_estado[self.fila - 1][self.columna] = 54
        nuevo_estado[self.fila - 2][self.columna] = 54
        nuevo_estado[self.fila - 3][self.columna] = 54
        nuevo_estado[self.fila - 1][self.columna - 1] = 54
        return nuevo_estado

class ponerY4(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la Y4 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_Y4(self, estado):

        res = []
        y = 55

        if y - estado[self.fila][self.columna] == y:
            res.append(True)
        else:
            res.append(False)

        if y - estado[self.fila - 1][self.columna] == y:
            res.append(True)
        else:
            res.append(False)

        if y - estado[self.fila - 1][self.columna + 1] == y:
            res.append(True)
        else:
            res.append(False)

        if y - estado[self.fila - 2][self.columna] == y:
            res.append(True)
        else:
            res.append(False)

        if y - estado[self.fila - 3][self.columna] == y:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):

        if self.columna >= 0 and self.columna < len(estado[0]) - 1 and self.fila >= 3 and self.fila < len(estado):
            if (self.hay_hueco_Y4(estado)):
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 55
        nuevo_estado[self.fila - 1][self.columna] = 55
        nuevo_estado[self.fila - 2][self.columna] = 55
        nuevo_estado[self.fila - 3][self.columna] = 55
        nuevo_estado[self.fila - 1][self.columna + 1] = 55
        return nuevo_estado

class ponerY5(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la Y5 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_Y5(self, estado):

        res = []
        y = 56

        if y - estado[self.fila][self.columna] == y:
            res.append(True)
        else:
            res.append(False)

        if y - estado[self.fila][self.columna - 1] == y:
            res.append(True)
        else:
            res.append(False)

        if y - estado[self.fila - 1][self.columna - 1] == y:
            res.append(True)
        else:
            res.append(False)

        if y - estado[self.fila][self.columna - 2] == y:
            res.append(True)
        else:
            res.append(False)

        if y - estado[self.fila][self.columna - 3] == y:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):

        if self.columna >= 3 and self.columna < len(estado[0]) and self.fila >= 1 and self.fila < len(estado):
            if (self.hay_hueco_Y5(estado)):
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 56
        nuevo_estado[self.fila][self.columna - 1] = 56
        nuevo_estado[self.fila][self.columna - 2] = 56
        nuevo_estado[self.fila][self.columna - 3] = 56
        nuevo_estado[self.fila - 1][self.columna - 1] = 56
        return nuevo_estado

class ponerY6(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la Y6 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_Y6(self, estado):

        res = []
        y = 57

        if y - estado[self.fila][self.columna] == y:
            res.append(True)
        else:
            res.append(False)

        if y - estado[self.fila][self.columna - 1] == y:
            res.append(True)
        else:
            res.append(False)
        if y - estado[self.fila + 1][self.columna - 1] == y:
            res.append(True)
        else:
            res.append(False)

        if y - estado[self.fila][self.columna - 2] == y:
            res.append(True)
        else:
            res.append(False)

        if y - estado[self.fila][self.columna - 3] == y:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):

        if self.columna >= 3 and self.columna < len(estado[0]) and self.fila >= 0 and self.fila < len(estado) - 1:
            if (self.hay_hueco_Y6(estado)):
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 57
        nuevo_estado[self.fila][self.columna - 1] = 57
        nuevo_estado[self.fila][self.columna - 2] = 57
        nuevo_estado[self.fila][self.columna - 3] = 57
        nuevo_estado[self.fila + 1][self.columna - 1] = 57
        return nuevo_estado

class ponerY7(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la Y7 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_Y7(self, estado):

        res = []
        y = 58

        if y - estado[self.fila][self.columna] == y:
            res.append(True)
        else:
            res.append(False)

        if y - estado[self.fila][self.columna + 1] == y:
            res.append(True)
        else:
            res.append(False)

        if y - estado[self.fila + 1][self.columna + 1] == y:
            res.append(True)
        else:
            res.append(False)

        if y - estado[self.fila][self.columna + 2] == y:
            res.append(True)
        else:
            res.append(False)

        if y - estado[self.fila][self.columna + 3] == y:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):

        if self.columna >= 0 and self.columna < len(estado[0])-3 and self.fila >= 0 and self.fila < len(estado) - 1:
            if (self.hay_hueco_Y7(estado)):
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 58
        nuevo_estado[self.fila][self.columna + 1] = 58
        nuevo_estado[self.fila][self.columna + 2] = 58
        nuevo_estado[self.fila][self.columna + 3] = 58
        nuevo_estado[self.fila + 1][self.columna + 1] = 58
        return nuevo_estado

class ponerY8(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la Y8 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_Y8(self, estado):

        res = []
        y = 59

        if y - estado[self.fila][self.columna] == y:
            res.append(True)
        else:
            res.append(False)

        if y - estado[self.fila][self.columna + 1] == y:
            res.append(True)
        else:
            res.append(False)

        if y - estado[self.fila - 1][self.columna + 1] == y:
            res.append(True)
        else:
            res.append(False)

        if y - estado[self.fila][self.columna + 2] == y:
            res.append(True)
        else:
            res.append(False)

        if y - estado[self.fila][self.columna + 3] == y:
            res.append(True)
        else:
            res.append(False)

        if res.count(False) > 0:
            return False
        else:
            return True

    def es_aplicable(self, estado):

        if self.columna >=0 and self.columna < len(estado[0])-3 and self.fila >= 1 and self.fila < len(estado):
            if (self.hay_hueco_Y8(estado)):
                return True
            else:
                return False

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 59
        nuevo_estado[self.fila][self.columna + 1] = 59
        nuevo_estado[self.fila][self.columna + 2] = 59
        nuevo_estado[self.fila][self.columna + 3] = 59
        nuevo_estado[self.fila - 1][self.columna + 1] = 59
        return nuevo_estado


#----------------------------------------------------pieza Z----------------------------------------------------------------------------------
class ponerZ(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la W2 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_z(self, estado):

        res = []
        z=60

        if z- estado[self.fila][self.columna] == z:
                    res.append(True)
        else:
                    res.append(False)

        if z -  estado[self.fila-1][self.columna] == z:
                    res.append(True)
        else:
                    res.append(False)
        if  z - estado[self.fila-2][self.columna] == z:
                    res.append(True)
        else:
                    res.append(False)

        if z -  estado[self.fila-2][self.columna-1] == z:
                    res.append(True)
        else:
                    res.append(False)

        if  z - estado[self.fila][self.columna+1]== z:
                    res.append(True)
        else:
                    res.append(False)

        if res.count(False) > 0:
                return False
        else:
                return True

    def es_aplicable(self, estado):

        if self.columna >= 1 and self.columna < len(estado[0])-1 and self.fila >= 1 and self.fila < len(estado):
            if (self.hay_hueco_z(estado)):
                return True
            else:
                return False


    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 60
        nuevo_estado[self.fila-1][self.columna] = 60
        nuevo_estado[self.fila-2][self.columna] = 60
        nuevo_estado[self.fila-2][self.columna-1] = 60
        nuevo_estado[self.fila][self.columna+1] = 60
        return nuevo_estado

class ponerZ2(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la W2 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_Z2(self, estado):

        res = []
        z=61

        if z- estado[self.fila][self.columna] == z:
                    res.append(True)
        else:
                    res.append(False)

        if z -  estado[self.fila-1][self.columna] == z:
                    res.append(True)
        else:
                    res.append(False)
        if  z - estado[self.fila-1][self.columna+1] == z:
                    res.append(True)
        else:
                    res.append(False)

        if z -  estado[self.fila-1][self.columna+2] == z:
                    res.append(True)
        else:
                    res.append(False)

        if  z - estado[self.fila-2][self.columna+2]== z:
                    res.append(True)
        else:
                    res.append(False)

        if res.count(False) > 0:
                return False
        else:
                return True

    def es_aplicable(self, estado):

        if self.columna >= 0 and self.columna < len(estado[0])-2 and self.fila >= 2 and self.fila < len(estado):
            if (self.hay_hueco_Z2(estado)):
                return True
            else:
                return False


    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 61
        nuevo_estado[self.fila-1][self.columna] = 61
        nuevo_estado[self.fila-1][self.columna+1] = 61
        nuevo_estado[self.fila-1][self.columna+2] = 61
        nuevo_estado[self.fila-2][self.columna+2] = 61
        return nuevo_estado

class ponerZ3(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la W2 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_Z3(self, estado):

        res = []
        z3=62

        if z3- estado[self.fila][self.columna] == z3:
                    res.append(True)
        else:
                    res.append(False)

        if z3 -  estado[self.fila-1][self.columna] == z3:
                    res.append(True)
        else:
                    res.append(False)
        if  z3 - estado[self.fila-2][self.columna] == z3:
                    res.append(True)
        else:
                    res.append(False)

        if z3 -  estado[self.fila][self.columna-1] == z3:
                    res.append(True)
        else:
                    res.append(False)

        if  z3 - estado[self.fila-2][self.columna+1]== z3:
                    res.append(True)
        else:
                    res.append(False)

        if res.count(False) > 0:
                return False
        else:
                return True

    def es_aplicable(self, estado):

        if self.columna >= 1 and self.columna < len(estado[0])-1 and self.fila >= 2 and self.fila < len(estado):
            if (self.hay_hueco_Z3(estado)):
                return True
            else:
                return False


    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 62
        nuevo_estado[self.fila-1][self.columna] = 62
        nuevo_estado[self.fila-2][self.columna] = 62
        nuevo_estado[self.fila-2][self.columna+1] = 62
        nuevo_estado[self.fila][self.columna-1] = 62
        return nuevo_estado

class ponerZ4(probee.Acción):
    def __init__(self, i, j):
        nombre = "Colocamos la W2 en {} {}".format(i, j)
        super().__init__(nombre)
        self.fila = i
        self.columna = j

    def hay_hueco_Z4(self, estado):

        res = []
        z4=63

        if z4- estado[self.fila][self.columna] == z4:
                    res.append(True)
        else:
                    res.append(False)

        if z4 -  estado[self.fila-1][self.columna] == z4:
                    res.append(True)
        else:
                    res.append(False)
        if  z4 - estado[self.fila-1][self.columna-1] == z4:
                    res.append(True)
        else:
                    res.append(False)

        if z4 -  estado[self.fila-1][self.columna-2] == z4:
                    res.append(True)
        else:
                    res.append(False)

        if  z4 - estado[self.fila-2][self.columna-2]== z4:
                    res.append(True)
        else:
                    res.append(False)

        if res.count(False) > 0:
                return False
        else:
                return True

    def es_aplicable(self, estado):

        if self.columna >= 2 and self.columna < len(estado[0]) and self.fila >= 2 and self.fila < len(estado):
            if (self.hay_hueco_Z4(estado)):
                return True
            else:
                return False


    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        nuevo_estado[self.fila][self.columna] = 63
        nuevo_estado[self.fila-1][self.columna] = 63
        nuevo_estado[self.fila-1][self.columna-1] = 63
        nuevo_estado[self.fila-1][self.columna-2] = 63
        nuevo_estado[self.fila-2][self.columna-2] = 63
        return nuevo_estado



#En la clase colocar lo que hacemos es definir las acciones que son una lista de las clases anteriores. Cada clase tiene un rango que es
#el mencionado al principio en el método es_aplicable, la fila y la columna a partir de la cual se puede colocar la casilla de referencia y la fila y la columna
#máxima en la que se puede colocar.

class Colocar(probee.ProblemaEspacioEstados):
    def __init__(self,fila,col):
        acciones = [ponerI(i, j) for i in range(0, int(fila)) for j in range(4, int(col))] + [ponerIvert(i, j) for i in range(4, int(fila)) for j in range(0, int(col))] + [ponerL(i, j) for i in range(3, int(fila)) for j in range(0, int(col) - 1)] + [ponerL2(i, j) for i in range(1, int(fila)) for j in range(3,int(col))] + [ponerL3(i, j) for i in range(3, int(fila)) for j in range(1, int(col))] + [ponerL4(i, j) for i in range(0,int(fila) - 1) for j in range(0, int(col) - 3)] + [ponerL5(i, j) for i in range(3, int(fila)) for j in range(0, int(col) - 1)] + [ponerL6(i, j) for i in range(1, int(fila)) for j in range(3, int(col))] + [ponerL7(i, j) for i in range(3, int(fila)) for j in range(1, int(col))] + [ponerL8(i, j) for i in range(1, int(fila)) for j in range(0, int(col) - 3)] + [ponerN(i, j) for i in range(3, int(fila)) for j in range(0,int(col) - 1)] + [ponerN2(i, j) for i in range(1, int(fila)) for j in range(3, int(col))] + [ponerN3(i, j) for i in range(3, int(fila)) for j in range(0, int(col) - 1)] + [ponerN4(i, j) for i in range(1, int(fila)) for j in range(2, int(col) - 1)] + [ponerN5(i, j) for i in range(3, int(fila)) for j in range(1, int(col))] + [ponerN6(i, j) for i in range(1, int(fila)) for j in range(1, int(col) - 2)] + [ponerN7(i, j) for i in range(3, int(fila)) for j in range(1, int(col))] + [ponerN8(i, j) for i in range(1, int(fila)) for j in range(2,int(col) - 1)] + [ponerP(i, j) for i in range(2, int(fila)) for j in range(1, int(col))] + [ponerP2(i, j) for i in range(1, int(fila)) for j in range(2, int(col))] + [ponerP3(i, j) for i in range(2, int(fila)) for j in range(0, int(col) - 1)] + [ponerP4(i, j) for i in range(1, int(fila)) for j in range(2, int(col))] + [ponerP5(i, j) for i in range(2, int(fila)) for j in range(1, int(col))] + [ponerP6(i, j) for i in range(1, int(fila)) for j in range(2, int(col))] + [ponerP7(i, j) for i in range(2, int(fila)) for j in range(1, int(col))] + [ponerP8(i, j) for i in range(0,int(fila) - 1)for j in range(2, int(col))] + [ponerF(i, j) for i in range(2, int(fila)) for j in range(1, int(col) - 1)] + [ponerF2(i, j) for i in range(2,int(fila)) for j in range(1, int(col) - 1)] + [ponerF3(i, j) for i in range(2, int(fila)) for j in range(1, int(col) - 1)] + [ponerF4(i, j) for i in range(2, int(fila)) for j in range(2, int(col))] + [ponerF5(i, j) for i in range(2, int(fila)) for j in range(1, int(col) - 1)] + [ponerF6(i, j) for i in range(2, int(fila)) for j in range(0, int(col) - 2)] + [ponerF7(i, j) for i in range(2, int(fila)) for j in range(1, int(col) - 1)] + [ponerF8(i, j) for i in range(2, int(fila)) for j in range(1, int(col) - 1)] + [ponerT(i, j) for i in range(2, int(fila)) for j in range(1, int(col) - 1)] + [ponerT2(i, j) for i in range(1, int(fila) - 1) for j in range(2, int(col))] + [ponerT3(i, j) for i in range(2, int(fila)) for j in range(2, int(col))] + [ponerT4(i, j) for i in range(1,int(fila) - 1) for j in range(2, int(col))] + [ponerU(i, j) for i in range(1, int(fila)) for j in range(0, int(col) - 2)] + [ponerU2(i, j)for i in range(1, int(fila) - 1) for j in range(1, int(col))] + [ponerU3(i, j) for i in range(0, int(fila) - 1) for j in range(1, int(col) - 1)] + [ponerU4(i, j) for i in range(1, int(fila) - 1) for j in range(0, int(col) - 1)] + [ponerV(i, j) for i in range(2, int(fila)) for j in range(2, int(col))] + [ponerV2(i, j) for i in range(2, int(fila)) for j in range(0, int(col) - 2)] + [ponerV3(i, j) for i in range(2, int(fila)) for j in range(2, int(col))] + [ponerV4(i, j)for i in range(0, int(fila) - 2)for j in range(2, int(col))] + [ponerX(i, j) for i in range(1, int(fila) - 1) for j in range(1, int(col) - 1)] + [ponerW(i, j)for i in range(1, int(fila) - 1) for j in range(1, int(col) - 1)] + [ponerW2(i, j) for i in range(1, int(fila) - 1) for j in range(1, int(col) - 1)] + [ponerW4(i, j) for i in range(1, int(fila) - 1) for j in range(1, int(col) - 1)] + [ponerW3(i, j) for i in range(1, int(fila) - 1) for j in range(1, int(col) - 1)] + [ponerY(i, j) for i in range(3, int(fila)) for j in range(1,int(col))] + [ponerY2(i, j) for i in range(3, int(fila)) for j in range(0, int(col) - 1)] + [ponerY3(i, j) for i in range(3, int(fila)) for j in range(1, int(col))] + [ponerY4(i, j) for i in range(3, int(fila)) for j in range(0, int(col) - 1)] + [ponerY5(i, j) for i in range(1, int(fila)) for j in range(3, int(col))] + [ponerY6(i, j) for i in range(0, int(fila) - 1) for j in range(3, int(col))] + [ponerY7(i, j) for i in range(0, int(fila) - 1) for j in range(0, int(col) - 3)] + [ponerY8(i, j) for i in range(1, int(fila)) for j in range(0,int(col) - 3)] + [ponerZ(i, j) for i in range(2, int(fila)) for j in range(1, int(col) - 1)] + [ponerZ2(i, j) for i in range(2, int(fila))for j in range(0,int(col) - 2)] + [ponerZ3(i, j) for i in range(2, int(fila)) for j in range(1, int(col) - 1)] + [ponerZ4(i, j) for i in range(2, int(fila)) for j in range(2, int(col))]
        estado_inicial = [[0 for col in range(int(col))] for row in range(int(fila))]
        super().__init__(acciones, estado_inicial)
        self.columnas = col
        self.filas = fila



#En este método comprobamos si un estado es final o no, para que el estado sea final debe haber como máximo 4 huecos en el tablero, es decir cuatro casillas vacías.
    def es_estado_final(self, estado):
        cont = 0
        for i in range(len(estado)):
            for j in range(len(estado[i])):
                if(estado[i][j] == 0):
                    cont+=1
        if(cont <= 4):
            print("Se ha llegado a un estado final")
            return True
        else:
            return False



#En este método, usado para la heurística lo que hacemos es buscar los vecinos de las casillas vacías del tablero, para ello hemos dividido el método
#dependiendo si nos encontramos en los bordes del tablero, en las esquinas o en el centro ya que el número de vecinos varía dependiendo de la posición de la casilla.
#Comprobamos que los vecinos de la casilla vacía sean 0 para poder realizar nuestra heurística, este métdo devuelve un contador que se incrementa si los vecinos están
#vacíos, el uso de este contador se explicará más abajo.

def vecinos(estado):
    vec = 0
    for i in range(len(estado)):
        for j in range(len(estado[i])):
            #Esquinas
            if i == 0 and j == 0:       #Si estamos en la esquiina superior izquierda:
                if estado[i][j] == 0: vec +=1
                if(estado[i][j+1]) == 0: vec +=1
                if estado[i + 1][j] == 0: vec +=1
                if(estado[i + 1][j + 1]) == 0: vec +=1

            if (i == 0 and j == len(estado[0])-1): #Si estamos en la esquina superior  derecha
                if(estado[i][j]) == 0: vec +=1
                if(estado[i][j-1]) == 0: vec +=1
                if(estado[i+1][j]) == 0: vec +=1
                if(estado[i+1][j-1]): vec +=1

            if (i == len(estado)-1 and j == 0): #Si estamos en la esquina inferior izquierda
                if (estado[i][j]) == 0: vec +=1
                if(estado[i-1][j]) == 0: vec +=1
                if(estado[i][j+1]) == 0: vec +=1
                if(estado[i-1][j+1]) == 0: vec +=1

            if i == len(estado)-1 and j == len(estado[0])-1: #Si estamos en la esquina inferior derecha
                if (estado[i][j]) == 0: vec +=1
                if(estado[i-1][j]) == 0: vec +=1
                if(estado[i-1][j-1]) == 0: vec +=1
                if(estado[i][j-1]) == 0: vec +=1

            #Laterales
            if (j == 0) and not((i == 0 and j == 0) and (i == len(estado)-1 and j == 0)): #Borde izquierdo (sin esquinas)
                if estado[i][j] == 0: vec +=1
                if estado[i-1][j] == 0: vec +=1
                if estado[i+1][j] == 0: vec +=1
                if estado[i][j+1] == 0: vec +=1
                if estado[i+1][j+1] == 0: vec +=1
                if estado[i-1][j+1] == 0: vec +=1

            if (i == (len(estado)-1)) and not(j == 0  and j == len(estado[0])-1): #Borde inferior (sin esquinas)
                if estado[i][j] == 0: vec +=1
                if estado[i - 1][j] == 0: vec +=1
                if estado[i][j - 1] == 0: vec +=1
                if estado[i][j+1] == 0: vec +=1
                if estado[i-1][j+1] == 0: vec +=1
                if estado[i-1][j-1] == 0: vec +=1

            if ((i == 0)) and not((i == 0 and j == 0) or (i == 0 and j == len(estado[0])-1)): #Borde superior (sin esquinas)
                if estado[i][j] == 0: vec +=1
                if estado[i + 1][j] == 0: vec +=1
                if estado[i + 1][j - 1] == 0: vec +=1
                if estado[i + 1][j + 1] == 0: vec +=1
                if estado[i][j + 1] == 0: vec +=1
                if estado[i][j - 1] == 0: vec +=1

            if (j == len(estado[0])-1) and not((i == 0 and j == len(estado[0])-1) or (i == len(estado)-1 and j == len(estado[0])-1)): #Borde derecho (sin esquinas)
                if i[j] == 0: vec +=1
                if estado[i-1][j] == 0: vec +=1
                if estado[i+1][j] == 0: vec +=1
                if estado[i][j-1] == 0: vec +=1
                if estado[i-1][j-1] == 0: vec +=1
                if estado[i+1][j-1] == 0: vec +=1

            #Centrales
            if not(i == 0 and j == 0 or (i == 0 and j == len(estado[0])-1) or (i == len(estado)-1 and j == 0) or (i == len(estado)-1 and j == len(estado[0])-1) or (j == 0) and not((i == 0 and j == 0) or (i == len(estado)-1 and j == 0)) or ((i == len(estado))-1) and not((i == len(estado)-1 and j == 0) or (i == len(estado)-1 and j == len(estado[0])-1)) or ((i == 0)) and not((i == 0 and j == 0) or (i == 0 and j == len(estado[0])-1)) or (j == len(estado[0]-1)) and not((i == 0 and j == len(estado[0])-1) or (i == len(estado)-1 and j == len(estado[0])-1))):
                if i[j] == 0: vec +=1
                else: vec +=1
                if estado[i-1][j] ==0: vec +=1
                if estado[i+1][j] ==0: vec +=1
                if estado[i][j-1] ==0: vec +=1
                if estado[i][j +1] ==0: vec +=1
                if estado[i-1][j-1] == 0: vec +=1
                if estado[i-1][j+1] == 0: vec +=1
                if [i+1][j-1] == 0: vec +=1
                if estado[i+1][j+1] == 0: vec +=1
        return vec

#En este método, que es el que nos devuelve la heurística, hacemos uso del anterior para lo siguiente:
#El objetivo de nuestra heurística es intentar que el algoritmo agrupe los huecos vacíos de 5 en 5 para poder meter el mayor número de piezas psoibles, de forma que
#la búsqueda sea lo más óptima posible. Esto lo conseguimos comprobando si el contador del que hemos hablado anteriormente es múltiplo de 5, para ello usamos el módulo,
#así nos aseguramos de que seguro cabe una pieza. Si esto no ocurre penalizamos ya que los huecos vacíos no se están agrupando como nosotros queremos.

def h(nodo):
    estado = nodo.estado
    penalizacion = 0
    cont = 0
    heur = 0
    for i in range(len(estado)):
        for j in range(len(estado[i])):
            if estado[i][j]:
                if vecinos(estado) != 0:
                    if not((vecinos(estado)%5)):
                        penalizacion = 100

            if estado[i][j] == 0:
                cont += 1
    heur = cont + penalizacion - nodo.profundidad
    return heur

#Estos son los distintos algoritmos que usamos, solo dos de ellos usan heurística
b_profundidad = busqueda.BúsquedaEnProfundidad(detallado=True)
b_anchura = busqueda.BúsquedaEnAnchura(detallado=True)
b_estrella = busqueda.BúsquedaAEstrella(h,detallado=True)
b_optima = busqueda.BúsquedaÓptima(detallado = True)
b_primero_mejor = busqueda.BúsquedaPrimeroElMejor(h,detallado=True)

#A continuación hemos implementado un menú muy simple que nos pide el número de filas y columnas y el tipo de algoritmo que queremos usar.
def menu():
    columnas = "0"
    while columnas == "0":
        print("A continuación se le pedirá que introduzca las filas y columnas que formaran su tablero.")

        filas = input("Filas: ")
        columnas = input("Columnas: ")
        if int(columnas) <= 0:
            print("Debe tener al menos una columna. Se cerrará la aplicación. La próxima vez asegurese de meter un número correcto.")
            return False
        elif int(filas) <= 0:
            print("Debe tener al menos una fila. Se cerrará la aplicación. La próxima vez asegurese de meter un número correcto.")
            return False

        print("Seleccione un algoritmo de resolución, para ello introduzca uno de los siguientes númerosque se le indican a continuación: ")
        print("Para búsqueda en profundidad: 1")
        print("Para búsqueda en anchura: 2")
        print("Para búsqueda óptima: 3")
        print("Para búsqueda Aestrella: 4")
        print("Para busqueda Primero El Mejor: 5")
        algoritmo = input("Introduzca número: ")
        if (algoritmo == "1"):
            tinp = time.time()
            return b_profundidad.buscar(Colocar(filas,columnas)),print("Tiempo de ejecución(s): ", time.time()-tinp)
        elif (algoritmo == "2"):
            tina = time.time()
            return b_anchura.buscar(Colocar(filas,columnas)),print("Tiempo de ejecución(s): ", time.time()-tina)
        elif(algoritmo == "3"):
            tino = time.time()
            return b_optima.buscar(Colocar(filas,columnas)),print("Tiempo de ejecución(s): ", time.time() - tino)
        elif(algoritmo == "4"):
            tines = time.time()
            return b_estrella.buscar(Colocar(filas,columnas)),print("Tiempo de ejecución(s): ", time.time()-tines)
        elif(algoritmo == "5"):
            tinp = time.time()
            return b_primero_mejor.buscar(Colocar(filas,columnas)),print("Tiempo de ejecución(s): ", time.time() - tinp)
        else:
            print("Número incorrecto. La aplicación se cerrará. Por favor, la próxima vez escoja un número correcto.")
menu()