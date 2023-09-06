class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class arbolBinario_:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if not self.raiz:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual, valor):
        if int(valor.dpi) < int(nodo_actual.valor.dpi):
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierda, valor)
        elif int(valor.dpi) > int(nodo_actual.valor.dpi):
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecha, valor)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo_actual, valor):
        if nodo_actual is None:
            return False
        if int(nodo_actual.valor.dpi) == int(valor.dpi):
            return valor
        elif int(valor.dpi) < int(nodo_actual.valor.dpi):
            return self._buscar_recursivo(nodo_actual.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo_actual.derecha, valor)

    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo_actual, valor):
        if nodo_actual is None:
            return nodo_actual
        
        if int(valor.dpi) < int(nodo_actual.valor.dpi):
            nodo_actual.izquierda = self._eliminar_recursivo(nodo_actual.izquierda, valor)
        elif int(valor.dpi) > int(nodo_actual.valor.dpi):
            nodo_actual.derecha = self._eliminar_recursivo(nodo_actual.derecha, valor)
        else:
            if nodo_actual.izquierda is None:
                return nodo_actual.derecha
            elif nodo_actual.derecha is None:
                return nodo_actual.izquierda

            nodo_actual.valor = self.min_value_node(nodo_actual.derecha).valor
            nodo_actual.derecha = self._eliminar_recursivo(nodo_actual.derecha, nodo_actual.valor)

        return nodo_actual

    def busquedaNombreRango(self, nombre):
        listaNombre = []
        self._busquedaNombreRango(self.raiz, nombre, listaNombre)
        return listaNombre

    def _busquedaNombreRango(self, nodo_actual, nombre, listaNombre):
        if nodo_actual:
            self._busquedaNombreRango(nodo_actual.izquierda, nombre, listaNombre)
            
            if nodo_actual.valor.nombre == nombre:
                listaNombre.append(nodo_actual.valor)
            
            self._busquedaNombreRango(nodo_actual.derecha, nombre, listaNombre)

    def busquedaDpi(self, dpi):
        listanombre = []
        self._busquedaDpi(self.raiz, dpi, listanombre)
        return listanombre

    def _busquedaDpi(self, nodo_actual, dpi, listanombre):
        if nodo_actual:
            self._busquedaDpi(nodo_actual.izquierda, dpi, listanombre)
            
            if nodo_actual.valor.dpi == dpi:
                listanombre.append(nodo_actual.valor)
            
            self._busquedaDpi(nodo_actual.derecha, dpi, listanombre)

    def min_value_node(self, nodo):
        current = nodo
        while(current.izquierda is not None):
            current = current.izquierda
        return current