#from pathlib import Path
from pathlib import *


dir = input("Digite o diretório a ser listado: ")

p = Path(dir)
print(p)

lista = [x for x in p.iterdir() if x.is_dir()]
print(lista)

d = PurePath(dir)
print(d.parts[1])
