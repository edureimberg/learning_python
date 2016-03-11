from string import ascii_lowercase

lettermap = dict((c, k) for k, c in enumerate(ascii_lowercase, 1))

print(lettermap)
print(len(lettermap))

#Versão com comprehension

lettermap2 = {c: k for k, c in enumerate(ascii_lowercase, 1)}
print(lettermap2)
