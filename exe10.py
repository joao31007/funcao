def login(usuario, senha):
    if usuario == "admin" and senha == "1234":
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha incorretos.")

login("admin", "1234")