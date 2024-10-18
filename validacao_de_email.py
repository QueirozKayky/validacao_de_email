"""
Como verificar se um e-mail é válido?
Se a solicitação chegar ao endereço de e-mail dos destinatários e receber uma resposta, 
o e-mail é considerado ativo e você pode enviar e-mails reais com segurança para ele. 
Isso também é conhecido como autenticação SMTP.
"""
import re

def validar_email(email):
    padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(padrao_email,email):
        return True
    else:
        return False
    
emails = [
    'valido@gmail.com.br',
    "invalido.com",
    "suporte.ti@gmail"
]


for email in emails:
    print(validar_email(email))
