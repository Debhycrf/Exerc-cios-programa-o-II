class Livro:
    def _init_(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano de Publicação: {self.ano_publicacao}")

# Exemplo de uso:
livro1 = Livro("O Alquimista", "Paulo Coelho", 1988)
livro1.exibir_detalhes()