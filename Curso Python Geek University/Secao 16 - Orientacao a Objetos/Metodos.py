"""

O metodo dunder innit (__init__) é um metodo especial chamado método construtor e sua função é construir o objeto
a partir da classe

todo elemento em python que inicia e finaliza com duplo underline é chamado de dunder (double underline)
Os métodos/funções dunder em python são chamados de métodos mágicos.

Não é aconselhável criar nossas funçòes como dunder, mesmo que seja possível.

"""

# Metodo de Instancia.


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade


class ContaCorrente:
    contador = 4999

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """ Retorna o valor do produto com o desconto """
        return self.__valor * (100 - porcentagem) / 100


from passlib.hash import pbkdf2_sha256 as cryp


"""
class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

nome = input('nome: ')
sobrenome = input('sobrenome: ')
email = input('email:')
senha = input('senha: ')
senha_confirma = input('confirme a senha: ')

if senha == senha_confirma:
    user = Usuario(nome, sobrenome, email, senha)

else:
    print('Senha não confere...')
    exit(1)

print('usuário criado com sucesso!')

senha = input('Informe a senha de acesso: ')

if user.checa_senha(senha):
    print('Acesso Permitido')
else:
    print('Acesso Negado')

print(f'Senha User Criptografada: {user._Usuario__senha}') # Acesso 'errado'

"""


class Usuario:
    contador = 0
    # Metodo de Classe
    # utilizamos metodos de instancia quando esse metodo precisa fazer acesso a atributos de instancia
    # utilizamos metodos de classe quando não utilizamos atributos de instancia
    # metodo de classe são conhecidos como métodos estáticos em outras linguagens

    # para usar método de classe usamos o decorator @classmethod, e ao invés de usar self, usamos cls
    # tendo em vista que o método não utiliza o objeto da classe

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuário(s) no sistema')

    # Metodo Estático
    # o decorator é diferente e não recebe parametro (o cls, no caso)

    @staticmethod
    def definicao():
        return 'XERTGG54'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    # Metodo Privados
    # Assim como os atributos, os metodos podem ser tanto privados quanto publicos, e são publicos por default.
    # a convenção é a mesma, utilizamos double underline no começo para mostrar que é privado

    def __gera_usuario(self):
        return self.__email.split('@')[0]


user = Usuario('Rafael', 'Pagliarin', 'pagliarinrafael@gmail.com', '111111')

Usuario.conta_usuarios() # Forma correta - via nome de classe
user.conta_usuarios() # possível, mas incorreto - via instancia da classe

# ===========================================================================================





