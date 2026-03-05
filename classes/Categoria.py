from classes.AbstracCrud import AbstracCrud

class Categoria(AbstracCrud):

    arquivo = 'db/categorias.json'

    def __init__(self, nome):
        self.nome = nome
