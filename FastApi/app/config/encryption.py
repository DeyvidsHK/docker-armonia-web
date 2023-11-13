import bcrypt

def hash_password(password: str) -> bytes:
    # Genera una sal aleatoria
    salt = bcrypt.gensalt()
    
    # Hashea la contraseña con la sal
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    return hashed_password

def verify_password(password: str, hashed_password: bytes) -> dict:
    # Verifica la contraseña proporcionada con el hash almacenado
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return {"success": True, "message": "Contraseña verificada correctamente."}
    else:
        return {"success": False, "message": "La contraseña proporcionada no es válida."}