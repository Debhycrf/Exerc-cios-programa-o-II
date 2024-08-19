'''Desenvolva um sistema de estoque que possui a Classe produtos com as
seguintes características:
○ Atributos: nome, preco, quantidade e codigo.
○ Métodos: calcular_total, atualizar_preco e verificar_disponibilidade.
'''

class Produtos:
    def _init_(self, nome, preco, quantidade, codigo):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.codigo = codigo

    def calcular_total(self):
        total = self.preco * self.quantidade
        print(f"Total em estoque do produto '{self.nome}': R${total:.2f}")
        return total

    def atualizar_preco(self, novo_preco):
        self.preco = novo_preco
        print(f"Preço do produto '{self.nome}' atualizado para: R${self.preco:.2f}")

    def verificar_disponibilidade(self):
        if self.quantidade > 0:
            print(f"Produto '{self.nome}' está disponível em estoque.")
        else:
            print(f"Produto '{self.nome}' está esgotado.")

produto1 = Produtos("Caneta", 1.50, 100, "001")
produto2 = Produtos("Caderno", 15.00, 50, "002")


produto1.calcular_total()  
produto2.calcular_total() 


produto1.atualizar_preco(2.00) 


produto1.verificar_disponibilidade() 
produto2.verificar_disponibilidade()  

produto2.quantidade = 0
produto2.verificar_disponibilidade()  