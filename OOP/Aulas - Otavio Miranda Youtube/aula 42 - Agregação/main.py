from classes import *

carrinho = CarrinhoDeCompras()

p1 = Produto('camiseta', 50)
p2 = Produto('Iphone', 8800)
p3 = Produto('Caneca', 15)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)

carrinho.listar_produtos()
print(carrinho.somar_total())
