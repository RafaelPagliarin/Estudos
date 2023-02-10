"""
Codewars Automatizados!

               Aplicação Web
---------------------------------------------
|                                           |
|           FrontEnd e BackEnd              |
|                                           |
---------------------------------------------
|            Codewars automatizados           |
---------------------------------------------


Por que testar nosso código?
    - Reduzir bugs no código existe
    - Codewars garantem que novos recursos da sua aplicação não quebrem (alterem) recursos antigos
    - Codewars garantem que bugs que foram corrigidos anteriormente continuem corrigidos
    - Codewars garantem que a refatoração que costuamos fazer não tragam novos bugs


TDD - Test Driven Development (Desenvolvimento Guiado por Codewars)
     Com TDD são utilizados estágios de desenvolvimento.
        Escreve o teste primeiro
        Escreve o código mínimo suficiente para o teste passar (executar com sucesso)
        Refatora o código para realizar a funcionalidade e testa novamente
        Uma vez que o teste passar, o recurso é considerado completo.

Esses estágios de desenvolvimento TDD são quase como um mantra que os desenvolvedores seguem, conhecidos como:
    - Red;
    - Green;
    - Refactor;



"""

# Como fizemos até agora para testar nosso código...(manualmente)


class Gato:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.nome} está miando')


ya = Gato('Ya')
ya.miar()
print(ya.nome)
print(type(ya))
print(repr(ya))

