#Cuaterniones 
import copy
import math
from typing import Union

class Cuaternion:
	def __init__(self, u,i,j,k ):
	   try:
	        assert(isinstance(u,float) or isinstance(u,int) or isinstance(u,complex)) #Se verifica que los valores introducidos sean numeros
	        assert(isinstance(i,float) or isinstance(i,int) or isinstance(i,complex))
	        assert(isinstance(j,float) or isinstance(j,int) or isinstance(j,complex))
	        assert(isinstance(k,float) or isinstance(k,int) or isinstance(k,complex))
	   except AssertionError:
	        print("Las entradas de Cuaternion deben ser numeros.")
	   self.cuaternion = [u,i,j,k]
	def __str__(self):
		return str(self.cuaternion)
	def __radd__(self, other):  #Sobrecarga de la suma a izquierda
		if isinstance(other, Cuaternion): #Se utiliza esta funcion para que se puedan realizar sumas tanto a derecha como izquierda
			salida = Cuaternion(0,0,0,0)
			salida.cuaternion = list(map(lambda x, y: x + y, self.cuaternion, other.cuaternion))
			return salida
		else:
			nuevo = copy.copy(self.cuaternion) #Se reailza una copia del cuaternion para evitar que se modifique el actual 
			nuevo[0] += other                  #al realizar la operacion
			salida = Cuaternion(0,0,0,0)
			salida.cuaternion = nuevo
			return salida
	def __add__(self,other): #Sobrecarga de la suma a derecha
		return self.__radd__(other)
	def __neg__(self): #Sobrecarga del - unario
		res = list(map(lambda x: -x, self.cuaternion))
		res[0] = self.cuaternion[0]
		salida = Cuaternion(0,0,0,0)
		salida.cuaternion = res
		return salida
	def __invert__(self): #Sobrecarga de la ~
		return self.__neg__()
	def __rmul__(self, other): #Sobrecarga de la multiplicacion de derecha
		if isinstance(other, Cuaternion):
		    U = self.cuaternion[0]*other.cuaternion[0]-self.cuaternion[1]*other.cuaternion[1]-self.cuaternion[2]*other.cuaternion[2]-self.cuaternion[3]*other.cuaternion[3]
		    I = self.cuaternion[0]*other.cuaternion[1]+self.cuaternion[1]*other.cuaternion[0]+self.cuaternion[2]*other.cuaternion[3]-self.cuaternion[3]*other.cuaternion[2]
		    J = self.cuaternion[0]*other.cuaternion[2]-self.cuaternion[1]*other.cuaternion[3]+self.cuaternion[2]*other.cuaternion[0]+self.cuaternion[3]*other.cuaternion[1]
		    K = self.cuaternion[0]*other.cuaternion[3]+self.cuaternion[1]*other.cuaternion[2]-self.cuaternion[2]*other.cuaternion[1]+self.cuaternion[3]*other.cuaternion[0]
		    salida = Cuaternion(U,I,J,K)
		    return salida
		else:
			nuevo = copy.copy(self.cuaternion)
			nuevo[0] *= other
			salida = Cuaternion(0,0,0,0)
			salida.cuaternion = nuevo
			return salida
	def __mul__(self,other): #Sobrecarga de la multiplicacion a izquierda
		return self.__rmul__(other)
	def __pos__(self): #Sobrecarga de la suma unaria
		return math.sqrt(sum(list(map(lambda x : x**2, self.cuaternion))))
	def __eq__(self,other): #Sobrecarga de la igualdad para poder comparar cuaterniones en los unit test
		if self.cuaternion[0] == other.cuaternion[0] and self.cuaternion[1]==other.cuaternion[1] and self.cuaternion[2] == other.cuaternion[2] and self.cuaternion[3]==other.cuaternion[3]:
			return True
		else:
			return False
