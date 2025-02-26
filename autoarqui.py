arquivo = open('arqtext.txt', 'w')

arquivo.write('curso python \n')
arquivo.write('aula pratica')
arquivo.close()

# leitura do arquivo

leitura = open('arqtext.txt', 'r')
print(leitura.read())
leitura.close()
