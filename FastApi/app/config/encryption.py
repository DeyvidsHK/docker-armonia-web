import bcrypt

def hash_password(password: str) -> bytes:
    # Genera una sal aleatoria
    salt = bcrypt.gensalt()
    
    # Hashea la contraseña con la sal
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    return hashed_password

def verify_password(password: str, hashed_password: bytes) -> bool:
    # Verifica la contraseña proporcionada con el hash almacenado
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

# Ejemplo de uso
# password_to_store = "123"
# hashed_password = hash_password(password_to_store)

# # Almacena `hashed_password` en tu base de datos

# # Verificación de contraseña
# user_input_password = "123"
# if verify_password(user_input_password, hashed_password):
#     print("Contraseña válida.")
# else:
#     print("Contraseña incorrecta.")
