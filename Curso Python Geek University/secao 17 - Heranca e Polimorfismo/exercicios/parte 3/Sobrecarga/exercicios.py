""" 1. Crie um novo pacote chamado sobrecarga.

    2. Crie uma classe Pessoa.

    3. Na Classe Pessoa crie 3 variáveis de instância: código, nome e idade.

    4. Crie um método exibe(), que exiba o conteúdo de todas as variáveis declaradas na classe em questão.

    5. Crie uma sobrecarga do método exibe() que receba como parametro um número inteiro e decida por meio do valor
    desse parametro se a idade será exibida ou não. Para isso use o seguinte critério: se o valor do parametro for
    igual a 1, imprima a idade, se não, não imprima a idade, mas apenas as outras variáveis de instância.

    6. Crie um construtor padrão explítito para a classe Pessoa, esse construtor deverá exibir uma mensagem:
    "Construtor padrão".

    7. Crie uma classe chamada TestePessoa que instancie um objeto da classe Pessoa usando o construtor padrão.

    8. Ainda na classe TestePessoa, inicialize as variáveis de instância: código, nome e idade com valores à sua escolha
    e acione o método exibe(), sem nenhum parâmetro.

    9. Repita a operação da questão anterior, acionando o método exibe(), passando a ele um parametro inteiro de valor 1

    10. Repita o que foi feito na questão anterior, só que dessa vez, passando um argumento diferente de 1.

    11. Crie um construtor sobrecarregado que permita instanciar objetos com os 3 valores sendo inicializados por
    valores passados como parâmetros.

    12. Na classe TestaPessoa instancie um objeto usando o segundo construtor(com os 3 parâmetros).

    13. Exiba os dados do objeto que foi instanciado na questão anterior por meio do método exibe() sem argumentos."""


class Pessoa:
    def __init__(self, codigo, nome, idade):
        self.__codigo = codigo
        self.__nome = nome
        self.__idade = idade
        print('Construtor Padrão')

    def exibir(self, criterio=0):
        print(f'Pessoa: {self.__nome}\nCódigo: {self.__codigo}')
        if criterio == 1:
            print(f'Idade: {self.__idade}')


class TestePessoa:
    teste = Pessoa(123, 'Rafael', 30)
    teste.exibir()
    teste.exibir(1)
    teste.exibir(2)

    def __init__(self, codigo=None, nome=None, idade=None):
        self.__codigo = codigo
        self.__nome = nome
        self.__idade = idade

    def exibir(self, criterio=0):
        print(f'Pessoa: {self.__nome}\nCódigo: {self.__codigo}')
        if criterio == 1:
            print(f'Idade: {self.__idade}')





# Codewars
#rafael = Pessoa('1', 'Rafael', '32')
#rafael.exibir(1)

luis = TestePessoa(111, 'luis', 39)
luis.exibir()