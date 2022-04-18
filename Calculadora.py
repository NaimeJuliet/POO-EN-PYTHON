class Calculadora:
    #todo contructor recibe los atributos
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2


    #los metodos de una clase pueden acceder a un atributo de esta (la clase)

    def sumar(self):
        return(self.num1+self.num2)
    def restar(self):
        return(self.num1-self.num2)
    def mutiplicar(self):
        return(self.num1*self.num2)
    def dividir(self):
        return(self.num1/self.num2)