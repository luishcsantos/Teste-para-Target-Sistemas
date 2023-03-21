# Definindo a string a ser invertida
string = input("Escreva uma string para ser invertida: ")
# Convertendo a string em uma lista de caracteres
lista_caracteres = list(string)

# Definindo os índices de início e fim da lista
inicio = 0
fim = len(lista_caracteres) - 1

# Invertendo os caracteres da lista
while inicio < fim:
    lista_caracteres[inicio], lista_caracteres[fim] = lista_caracteres[fim], lista_caracteres[inicio]
    inicio += 1
    fim -= 1

# Convertendo a lista de caracteres de volta para uma string
string_invertida = ''.join(lista_caracteres)

# Imprimindo a string invertida
print(string_invertida)