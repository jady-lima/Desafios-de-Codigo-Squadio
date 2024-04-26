import re

def verificar_forca_senha(senha):

  comprimento_minimo = 8
  tem_letra_maiuscula = False
  tem_letra_minuscula = False
  tem_numero = False
  tem_caractere_especial = False

  # Verificando o comprimento da senha
  if len(senha) < comprimento_minimo:
    return f"Sua senha e muito curta. Recomenda-se no minimo {comprimento_minimo} caracteres."

  # Verificando se a senha contém letras maiúsculas
  if (re.search(r'[A-Z]', senha)):
    tem_letra_maiuscula = True
  
  # Verificando se a senha contém letras minúsculas
  if (re.search(r'[a-z]', senha)):
    tem_letra_minuscula =  True

  # Verificando se a senha contém números
  if (re.search(r'[0-9]', senha)):
    tem_numero = True
  
  # Verificando se a senha contém caracteres especiais
  if (re.search(r'[@*/!#$%+-_¨&()`^~:;.,|{}=?[]', senha)):
    tem_caractere_especial = True

  # Verificando se a senha contém sequências comuns
  sequencias_comuns = ["123456", "abcdef"]
  for sequencia in sequencias_comuns:
    if sequencia in senha:
      return "Sua senha contem uma sequencia comum. Tente uma senha mais complexa."

  # Verificando se a senha contém palavras comuns
  palavras_comuns = ["password", "123456", "qwerty"]
  if senha in palavras_comuns:
    return "Sua senha e muito comum. Tente uma senha mais complexa."

  for i in range(len(senha) - 2):
    if ord(senha[i]) == (ord(senha[i+1]) - 1) == (ord(senha[i+2]) - 2):
      return "Sua senha nao atende aos requisitos de seguranca."

  # TODO: Verificar o comprimento mínimo e critérios de validação
  if (tem_letra_maiuscula == True and tem_letra_minuscula == True and tem_numero == True and tem_caractere_especial == True):
    return "Sua senha atende aos requisitos de seguranca. Parabens!"
  else: 
    return "Sua senha nao atende aos requisitos de seguranca."

# Obtendo a senha do usuário
senha = input().strip()

# Verificando a força da senha
resultado = verificar_forca_senha(senha)

# Imprimindo o resultado
print(resultado)