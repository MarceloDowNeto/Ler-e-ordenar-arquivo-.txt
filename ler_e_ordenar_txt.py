def ordenar_insertion(lista):
  for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
      if lista[i] > lista[j]:
        lista[i], lista[j] = lista[j], lista[i]
  return lista

def ordena_arquivo(nome_arquivo):
  numeros = []
  with open(nome_arquivo, 'r') as arquivo:
    for linha in arquivo:
      linha_limpa = linha.strip()
      if linha_limpa:
        if ' ' in linha_limpa:
          for numero_str in linha_limpa.split():
            try:
              numero = int(numero_str)
              numeros.append(numero)
            except ValueError:
              print(f"O valor '{numero_str}' não é um número válido.")
        else:
          try:
            numero = int(linha_limpa)
            numeros.append(numero)
          except ValueError:
            print(f"A linha '{linha}' não é um número válido.")

  return ordenar_insertion(numeros)

arquivo = 'extra.txt'

print(ordena_arquivo(arquivo))