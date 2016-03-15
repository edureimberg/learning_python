import os, sys

path = input("Digite o caminho do diretório: ")

print("O conteúdo do diretório", path, "é: ", os.listdir(path))
