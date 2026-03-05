import json
from abc import ABC

class AbstracCrud(ABC):

    def detalhar(self):
        return self.__dict__ 
    
    def inserir(self):

        lista = self.consultar()
        lista.append(self.detalhar())
        self.__gravarArquivo(lista)

        with open(self.arquivo, 'w') as file:
            json.dump(lista, file, indent=4)
       

    def alterar(self, item):

        lista = self.consultar()
        lista[item] = self.detalhar()
        self.__gravarArquivo(lista)

    def __gravarArquivo(self, lista):
        with open(self.arquivo, 'w') as file:
            json.dump(lista, file, indent=4)
        
        print('Operação realizada com sucesso!')

    @classmethod
    def excluir(cls, item):

        lista = cls.consultar()
        del lista[item]
        cls.__gravarArquivo(lista)

        with open(cls.arquivo, 'w') as file:
            json.dump(lista, file, indent=4)

        print('Operação realizada com sucesso!')
       

    @classmethod
    def listarTodos(cls):
         
        lista = cls.consultar()
        
        for i, p  in enumerate(lista):
            print(f"{i} - {p}")
        
    @classmethod
    def consultar(cls, item=None):
        try:
            with open(cls.arquivo) as file:
                lista =  json.load(file)

            return lista if isinstance(item, int) else lista

        except Exception:
            return []