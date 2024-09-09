import secrets

# Gerar uma chave secreta aleatória com 32 bytes
secret_key = secrets.token_hex(32)
print(secret_key)  # Isso imprimirá uma chave secreta segura, como 'a3b6c7e8f9...'