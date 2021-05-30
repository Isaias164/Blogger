def verification(f):
    def numbers(*args):
        for i in args:
            try:
                int(i)
            except:
                return False #"Ingreso uno o varios valores que no son numericos"
        return  True #f(*args)
    return numbers
        
def calculadora(option=None):
    def operations(f):
        if option == "+":
            def suma(*args):
                if(f(*args)):
                    return sum([int(i) for i in args])
                return "Ingreso uno o varios valores que no son numericos"
            return suma

        elif option == "-":
            def resta(*args):
                if(f(*args)):
                    i2 = 0
                    for i in args:
                        i2 = int(i) - i2
                    return i2
                return "Ingreso uno o varios valores que no son numericos"
            return resta

        elif option == "*":
            def multiplicacion(*args):
                if(f(*args)):
                    num1 = 1
                    for i in args:
                        num1 = num1*int(i)
                    return num1
                return "Ingreso uno o varios valores que no son numericos"
            return multiplicacion
        else:
            def divicion(*args):
                if(f(*args)):
                    num1 = 1
                    for i in args:
                        num1 = num1/int(i)
                    return num1
                return "Ingreso uno o varios valores que no son numericos"
            return divicion
    return operations

@calculadora(option="+")
@verification
def operation1(*args):
    pass

@calculadora(option="-")
@verification
def operation2(*args):
    pass

@calculadora(option="*")
@verification
def operation3(*args):
    pass

@calculadora(option="/")
@verification
def operation4(*args):
    pass

print("\nEl resultado de la suma es: ",operation1(4,55,67,67,"33"))
print("El resultado de la resta es: ",operation2(4,55,67,67,"32"))
print("El resultado de la multiplicación es: ",operation3(4,55,"90",67,67))
print("El resultado de la divición es: ",operation4(4,55,67,67,45,"90",3))
print("El resultado de una operación con un valor invalido es: ",operation4(45,"f",3))
