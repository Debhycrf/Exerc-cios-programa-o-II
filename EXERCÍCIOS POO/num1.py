'''Suponha que você está desenvolvendo um sistema de biblioteca. Crie a
classe Livro com as seguintes características:
○ Atributos: titulo, autor, ano_publicacao.
○ Métodos: exibir_detalhes.
'''

class Livro:
    def _init_(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano de Publicação: {self.ano_publicacao}")
livro1 = Livro("O Alquimista", "Paulo Coelho", 1988)
livro1.exibir_detalhes()