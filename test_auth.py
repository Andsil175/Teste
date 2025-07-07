from auth import validar_login
def test_login_sucesso():
    assert validar_login("admin", "admin123") == "Login bem-sucedido."
def test_senha_invalida():
    assert validar_login("admin", "senhaerrada") == "Credenciais invalidas."
def test_usuario_invalido():
    assert validar_login("user", "admin123") == "Credenciais invalidas."
def test_usuario_vazio():
    assert validar_login("", "admin123") == "Usuario ou senha nao podem ser vazios."
def test_senha_vazia():
    assert validar_login("admin", "") == "Usuario ou senha nao podem ser vazios."
def test_ambos_vazios():
    assert validar_login("", "") == "Usuario ou senha nao podem ser vazios."
