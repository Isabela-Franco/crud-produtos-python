from classes.AbstracCrud import AbstracCrud

class Produto(AbstracCrud):

    arquivo = 'db/produtos.json'

    def __init__(self, codigo, nome, quantidade=0, valor=0.0):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor

    def inserir(self):
        lista = self.consultar()
        produtoDuplicado = list(filter(lambda p: p['codigo'] == self.codigo, lista))

        if len(list(produtoDuplicado)):
            print()
            print('Já existe um produto com esse código. Tente novamente!')
        else:
            super().inserir()
    

    

   