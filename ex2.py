print("Programa usando laços para desenhar um retangulo na tela utilizando #")

print("Informe quantas linhas quer no retangulo")
linha = int(input())

print("Informe quantas colunas quer no retangulo")
coluna = int(input())

for i in range(0, coluna):
    print ("#" *linha)