class Member:
    height = None
    imc = None
    name = None 

    def __init__(self, name):
        self.name = name

    def register(self):
        print('Usuario registrado')

    def welcome(self):
        print(f'Hola, bienvenido {self.name}')




rafa = Member('Rafa')
 
rafa.height = 172 
rafa.imc = 15
#rafa.name = 'Rafael'
print(type(rafa))
    
print(rafa.height)
print(rafa.imc)
rafa.register()
rafa.welcome()
    
billy = Member('Billy')
    #Billy.name = 'Billy'
billy.welcome()
    #HERENCIA

class Person():
    first_name = None
    last_name = None
    birthdate = None

    def be_in_gym(self):
        print('Estoy en el gimnacio')

class Trainer(Person):
    salary = None

    def be_in_gym(self):
        print('Estoy trabajando')

class Member(Person):
    imc = None 

    def be_in_gym(self):
        print('Estoy ejercitandome')

alumno = Member()
alumno.be_in_gym()


persona = Person
print(type(persona))

from abc import ABC, abstractmethod

class Vehicule(ABC):
    doors = None  
    wheels = None

    @abstractmethod
    def avanzar(self):
        pass

class Car(Vehicule):
    doors = 5
    wheels = 4

    def avanzar(self):
        return 'Avanzo en 4 ruedas'

class Bike(Vehicule):
    doors = 0 
    wheels = 2

    def avanzar(self):
        print(f'Avanzo en {self.wheels} ruedas')

    def __str__(self):
        return f'esta es una moto con {self.doors} puertas y {self.wheels} ruedas'


#vehiculo = Vehicule()
#vehiculo.avanzar()

carro = Car()
print(carro.doors)

bike = Bike()
bike.avanzar()
print(bike)

class User():
    password = 'Contraseña-encriptada'

    def __init__(self):
        self.password = self.__decrypt()

    def __decrypt(self):
        return 'Contraseña-desencriptada'

Usuario = User()
print(Usuario.password)
        