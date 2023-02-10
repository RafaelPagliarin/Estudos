# alguns aprendizados não vistos antes com a vídeo aula de 6 horas no canal "Programming with Mosh"
########################################################################################################################

# 1. unpacking

# tuples or lists.

'''coordinates = (1, 2, 3)

x = coordinates[0]
y = coordinates[1]
z = coordinates[2]'''

# ou...
import openpyxl as openpyxl

'''x, y, z = coordinates''' # isso é unpacking. o python distribui automaticamente os valores de uma tuple ou list para
                      # as variáveis. ao invés de atribuir variável por variável como no exemplo acima


########################################################################################################################

# 2. Classes

# importante em programação, não é algo só de python
# usamos para definir novos "tipos"
# tipos básicos em python: numbers, strings, booleans
# tipos complexos em python: lists, dictionaries

# agora imagine um novo "tipo" não oferecido no python, como de um "ponto", onde possamos medir a distancia entre 2
# pontos, move-lo, desenha-lo.

'''class Point:  # a convenção para nomear classes é diferente, escrevemos tudo sem separação nenhuma e colocamos a 1 letra
              # de cada palavra em maiusculo exemplo: EmailClient
    def move(self):
        print('move')

    def draw(self):
        print('draw')

# então basicamente nós definimos a classe e dentro dela colocamos metodes que compoem tal classe


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)'''

########################################################################################################################

# 3. Constructors

# imagine agora que para um ponto existir, ele precisa de coordenadas
# como fazemos para passar os parametros de x e y para a classe ponto?


'''class Point:
    def __init__(self, x, y): # o self é uma referencia ao proprio objeto
        self.x = x
        self.y = y


point = Point(10, 20)
print(point.x)

####

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f'Hi, I am {self.name}')


john = Person('John Smith')
john.talk()
bob = Person('Bob Marley')
bob.talk()'''
# cada objeto é uma "different instance of a person class"

########################################################################################################################
# 4. Inheritance

# DRY = don't repeat yourself
# conceito de não colocar trechos de códigos iguais ao longo do código, igual as funções.
# motivo: imagina q vc colocou uma função manualmente 100x no código (identica) e descobre que ela tem um erro
# vc precisará arrumar 100 trechos de código. Se essa função for uma Função (de fato), vc só precisará arrumar a função
# é o mesmo conceito aqui, porem com classes

'''class Dog:
    def walk(self):
        print('walk')


class Cat:
    def walk(self):
        print('walk')'''

# aqui podemos ver a redundancia no código. ambos as classes possuem o mesmo method chamado walk, para corrigir fazemos:


'''class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    def bark(self):
        print('bark')


class Cat(Mammal):
    def be_annoying(self):
        print('annoying')


dog1 = Dog()
dog1.bark()
cat1 = Cat()
cat1.be_annoying()'''


########################################################################################################################

# 5. pathlib

'''from pathlib import Path

# Absolute path
# c:\Program Files\Microsoft
# Relative path
#

path = Path() #vazio = pasta do projeto
print(path.exists()) #return boolean
path2 = Path('emails')
path2.mkdir() #create (make) a directory
path2.rmdir() #remove a directory


for file in path.glob('*'): # name.type - > *.py ; *.xms
    print(file)'''

# 6. Pypi and Pip - site com várias bibliotecas

'''pip install openpyxl''' #pacote para mexer com excel