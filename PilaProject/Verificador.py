# -*- coding: utf-8 -*-
from PilaClass import Pila
class Verificador:
    
    def __init__(self):
        self._pila = Pila()
        
    def verificar_balanceo(self,expresion):
        print("Expresion a validar:  ",expresion)
        self._pila.vaciar()
        
        for caracter_actual in expresion:
            print("Caracter actual: ",caracter_actual)                     
            if(caracter_actual=='(' 
               or caracter_actual=='[' 
               or caracter_actual=='{'):
                
                print("Metiendo a la pila ", caracter_actual)
                self._pila.push(caracter_actual)
                self._pila.imprimir()
    
            elif caracter_actual==')':     
    
                if(self._pila.esta_vacia()):
                    return False
                tope = self._pila.pop();
                self._pila.imprimir()
                if(('(' !=tope)):
                    return False
                      
            elif caracter_actual==']':   

                 if(self._pila.esta_vacia()):
                    return False     
                
                 tope = self._pila.pop();
                 
                 if(('[' !=tope)):
                    return False
                
            elif caracter_actual=='}':         
                if(self._pila.esta_vacia()):
                    return False     
                tope = self._pila.pop();
                if(('{' !=tope)):
                    return False
                
            print(self._pila.imprimir())
                
        if self._pila.esta_vacia():
            return True
        else:
            self._pila.imprimir()
            return False
            
verificador = Verificador()

print("Verifica (a+b}: " ,verificador.verificar_balanceo("(a+b}"))
print("Verifica {[(a+b-c]+a}: " ,verificador.verificar_balanceo("{[(a+b-c]+a}"))
print("Verifica: (a+b+[{d+b}])" ,verificador.verificar_balanceo("(a+b+[{d+b}])"))
      
    