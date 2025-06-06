# -*- coding: utf-8 -*-
"""Biblioteca.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FjBdeG9qHrItyfeoKE-7jqX1c3rHoQ1G
"""

class Livro:
    def __init__(self, titulo, autor, ano, copias):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.copias = copias
        self.emprestados = 0

    def emprestar(self):
        if self.copias > 0:
            self.copias -= 1
            self.emprestados += 1
            return True
        return False

    def devolver(self):
        if self.emprestados > 0:
            self.copias += 1
            self.emprestados -= 1
            return True
        return False

class Usuario:
    def __init__(self, nome, id, contato):
        self.nome = nome
        self.id = id
        self.contato = contato

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def cadastrar_livro(self, livro):
        self.livros.append(livro)

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_livro(self, chave, valor):
        resultados = [livro for livro in self.livros if getattr(livro, chave).lower() == valor.lower()]
        return resultados

    def listar_livros(self):
        for livro in self.livros:
            print(f"{livro.titulo} - {livro.autor} ({livro.ano}) | Disponíveis: {livro.copias}")

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(f"{usuario.nome} | ID: {usuario.id} | Contato: {usuario.contato}")

class SistemaBiblioteca:
    def __init__(self):
        self.biblioteca = Biblioteca()

    def menu(self):
        while True:
            print("\n--- Menu Biblioteca ---")
            print("1. Cadastrar Livro")
            print("2. Cadastrar Usuário")
            print("3. Emprestar Livro")
            print("4. Devolver Livro")
            print("5. Consultar Livro")
            print("6. Relatórios")
            print("7. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.cadastrar_livro()
            elif opcao == '2':
                self.cadastrar_usuario()
            elif opcao == '3':
                self.emprestar_livro()
            elif opcao == '4':
                self.devolver_livro()
            elif opcao == '5':
                self.consultar_livro()
            elif opcao == '6':
                self.gerar_relatorios()
            elif opcao == '7':
                print("Saindo...")
                break
            else:
                print("Opção inválida.")

    def cadastrar_livro(self):
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = input("Ano: ")
        copias = int(input("Número de cópias: "))
        livro = Livro(titulo, autor, ano, copias)
        self.biblioteca.cadastrar_livro(livro)
        print("Livro cadastrado com sucesso!")

    def cadastrar_usuario(self):
        nome = input("Nome: ")
        id = input("ID: ")
        contato = input("Contato: ")
        usuario = Usuario(nome, id, contato)
        self.biblioteca.cadastrar_usuario(usuario)
        print("Usuário cadastrado com sucesso!")

    def emprestar_livro(self):
        titulo = input("Título do livro: ")
        livros = self.biblioteca.buscar_livro('titulo', titulo)
        if livros:
            if livros[0].emprestar():
                print("Livro emprestado com sucesso!")
            else:
                print("Livro indisponível para empréstimo.")
        else:
            print("Livro não encontrado.")

    def devolver_livro(self):
        titulo = input("Título do livro: ")
        livros = self.biblioteca.buscar_livro('titulo', titulo)
        if livros:
            if livros[0].devolver():
                print("Livro devolvido com sucesso!")
            else:
                print("Nenhuma cópia emprestada para devolver.")
        else:
            print("Livro não encontrado.")

    def consultar_livro(self):
        chave = input("Buscar por (titulo/autor/ano): ")
        valor = input(f"{chave.capitalize()}: ")
        resultados = self.biblioteca.buscar_livro(chave, valor)
        if resultados:
            for livro in resultados:
                print(f"{livro.titulo} - {livro.autor} ({livro.ano}) | Disponíveis: {livro.copias}")
        else:
            print("Nenhum livro encontrado.")

    def gerar_relatorios(self):
        print("\n--- Relatório de Livros ---")
        self.biblioteca.listar_livros()
        print("\n--- Relatório de Usuários ---")
        self.biblioteca.listar_usuarios()

# Execução do sistema
if __name__ == "__main__":
    sistema = SistemaBiblioteca()
    sistema.menu()