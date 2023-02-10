"""
OOP - Métodos Mágicos

são todos os métodos que utilizam dunder.

# dunder init -> def __init__(self): -> método gerador

# dunder repr -> def __repr__(self): -> representação do objeto
# dunder str -> def __str__(self): -> representação do objeto também, preferencia à ele.
ps: se tiver repr e str, o codigo vai dar preferencia ao str

# dunder len -> __len__(self) -> define o metodo len para a classe

# dunder del -> __del__(self) -> define o metodo del para a classe

# dunder add -> __add__(self, outro) -> define o metodo de adição a classe (concatenação ou adição)

# dunder mul -> __mul__(self, outro) -> define o metodo de multiplicaçào a classe
"""
########################################################################################################################


class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'

    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.paginas

    def __del__(self):
        return 'Um objeto do tipo Livro foi deletado da memória.'

    def __add__(self, outro):
        return f'{self} - {outro}'

    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'

livro1 = Livro('Python Rocks', 'Rafael', 400)
livro2 = Livro('Inteligencia Artificial', 'Joãozinho Nerdão', 543)

#print(livro1)
#print(livro2)

print(livro1 * 5)