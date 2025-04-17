class User:
    def __init__(self, user_id, username):
        # Inicializa os atributos do usuário
        self.id = user_id  # ID único do usuário
        self.username = username  # Nome de usuário
        self.followers = 0  # Número de seguidores, começa com 0
        self.following = 0  # Número de pessoas que o usuário segue, começa com 0
    
    def follow(self, user):
        # Permite que o usuário atual siga outro usuário
        user.followers += 1  # Incrementa o número de seguidores do usuário seguido
        self.following += 1  # Incrementa o número de pessoas que o usuário atual está seguindo

# Criação de dois usuários
user_1 = User("001", "Arnaldo")  # Usuário com ID "001" e nome "Arnaldo"
user_2 = User("002", "Mari")  # Usuário com ID "002" e nome "Mari"

# user_1 segue user_2
user_1.follow(user_2)

# Exibe o número de seguidores e seguidos de user_1
print(user_1.followers)  # Saída: 0 (user_1 não tem seguidores)
print(user_1.following)  # Saída: 1 (user_1 está seguindo 1 pessoa)

# Exibe o número de seguidores e seguidos de user_2
print(user_2.followers)  # Saída: 1 (user_2 tem 1 seguidor)
print(user_2.following)  # Saída: 0 (user_2 não está seguindo ninguém)