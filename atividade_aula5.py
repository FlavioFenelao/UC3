# Classe para representar um Livro
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

# Classe para representar um Usuário
class Usuario:
    def __init__(self, nome):
        self.nome = nome

# Classe para representar um Empréstimo
class Emprestimo:
    def __init__(self, livro, usuario):
        self.livro = livro
        self.usuario = usuario

# Listas para armazenar os livros, usuários e empréstimos
livros = []
usuarios = []
emprestimos = []

# Função para cadastrar um livro
def cadastrar_livro(titulo, autor):
    livro = Livro(titulo, autor)
    livros.append(livro)
    print(f'Livro "{titulo}" cadastrado com sucesso!')

# Função para cadastrar um usuário
def cadastrar_usuario(nome):
    usuario = Usuario(nome)
    usuarios.append(usuario)
    print(f'Usuário "{nome}" cadastrado com sucesso!')

# Função para consultar livros
def consultar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
    else:
        print("Livros cadastrados:")
        for idx, livro in enumerate(livros, start=1):
            print(f"{idx}. {livro.titulo} por {livro.autor}")

# Função para consultar usuários
def consultar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        print("Usuários cadastrados:")
        for idx, usuario in enumerate(usuarios, start=1):
            print(f"{idx}. {usuario.nome}")

# Exemplo de uso
cadastrar_livro("A Redoma de Vidro", "Sylvia Plath")
cadastrar_usuario("Flávio Fenelão")
consultar_livros()
consultar_usuarios()
