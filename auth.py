def validar_login(usuario, senha):
    """
    valida as credenciais de um usuario.
    Regras de negocio:
    - O usuario e a senha nao podem ser vazios.
    - O usuario 'admin' com a senha 'admin123' é valido.
    - Qualquer outro usuario/senha é invalido.
    """
    if not usuario or not senha:
        return "Usuario ou senha nao podem ser vazios."
    if usuario == "admin" and senha == "admin123":
        return "Login bem-sucedido."
    else:
        return "Credenciais invalidas."
