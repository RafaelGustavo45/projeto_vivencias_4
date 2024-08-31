#escolhido: liderança
#link: https://www.youtube.com/watch?v=MYdWsF83uL4
soma=0
print("1- voce confia nas pessoas?")
print("A) depende da situação que tenhamos que lidar")
print("B) não muito, mas confio nos mais proximos")
print("C) eu tento deixar que elas se provem confiaveis")
res = str(input())
res = res.lower()
if res=="a":
    soma+=10
elif res =="b":
  soma += 30
elif res=="c":
    soma +=20

print("2- quem toma as decisões no seu grupo de amigos?")
print("A) eu, euzinho")
print("B) nós nos revezamos")
print("C) qualquer um menos eu, não gosto da pressão")
res = str(input())
res = res.lower()
if res=="a":
    soma+=10
elif res =="b":
  soma += 30
elif res=="c":
    soma +=20


print("3- quem voce busca fazer feliz?")
print("A) eu mesmo")
print("B) nós")
print("C) eles")
res = str(input())
res = res.lower()
if res=="a":
    soma+=30
elif res =="b":
  soma += 10
elif res=="c":
    soma +=20

print("4- em uma mensagem em grupo todo mundo tenta planejar algo, voce: ")
print("A) tomo a frente e vejo algo que funcionaria para todos")
print("B) digo quando posso e deixo que eles marquem")
print("C) deixo que planejem e apareço no dia combinado")
res = str(input())
res = res.lower()
if res=="a":
    soma+=10
elif res =="b":
  soma += 20
elif res=="c":
    soma +=30

print("5- com qual frequencia voce pede ajuda?: ")
print("A) eventualmente quando realmente preciso")
print("B) nunca, faço tudo sozinho")
print("C) literalmente sempre")
res = str(input())
res = res.lower()
if res=="a":
    soma+=10
elif res =="b":
  soma += 30
elif res=="c":
    soma +=20

print("6- que filho voce é?")
print("A) caçula")
print("B) do meio/filho unico")
print("C) mais velho")
res = str(input())
res = res.lower()
if res=="a":
    soma+=20
elif res =="b":
  soma += 30
elif res=="c":
    soma +=10

print("7- o quanto suas emoções influenciam suas decisões?")
print("A) minhas escolhas sao 100% emocionais")
print("B) 0%, estou alem das emoções pelo bem de todos")
print("C) um pouquinho, mas consigo resistir")
res = str(input())
res = res.lower()
if res=="a":
    soma+=30
elif res =="b":
  soma += 10
elif res=="c":
    soma +=20

print("8- voce acaba de ganhar um premio, com quem voce agradece?")
print("A) ninguem!, a conquista é minha")
print("B) a todos que me apoiaram")
print("C) todos que me ajudaram a chegar lá!")
res = str(input())
res = res.lower()
if res=="a":
    soma+=30
elif res =="b":
  soma += 20
elif res=="c":
    soma +=10

print("9- qual palavra voce relaciona mais com liderança?")
print("A) carisma")
print("B) autoridade")
print("C) liberdade")
res = str(input())
res = res.lower()
if res=="a":
    soma+=10
elif res =="b":
  soma += 20
elif res=="c":
    soma +=30

print("10- escolha uma citação")
print("A) liderança é uma serie de comportamentos")
print("B) um lider lidera pelo exemplo, não pela força")
print("C) liderança é ação, não posição")
res = str(input())
res = res.lower()
if res=="a":
    soma+=30
elif res =="b":
  soma += 20
elif res=="c":
    soma +=10


print("resultados")

if soma >= 100 and soma <= 160:
    print("lider natural \n")
    print(
      "um lider natural não necessariamente precisa liderar, as outras pessoas simplesmente se sentem atraidas a te seguir. Um lider é independente mas inclusivo, tambem é um sonhador e alguem que faz acontecer, as pessoas te seguem mais por respeito do que por medo"
    )
elif soma > 160 and soma <= 240:
    print("lider quando for preciso \n")
    print(
      "voce está feliz seguindo, mas pode assumir as redeas se sugir a necessidade. Voce é o braço direito em qualquer grupo. Voce é um lider capaz, apesar de saber quando alguem é melhor candidato a liderar doque voce. Voce não tem problemas para seguir ordens, desde que sejam pelo bem de todos"
    )
elif soma > 240 and soma <= 300:
    print("seguir solitario \n")
    print(
      "um solitario é a pessoa que evita ou não busca ativamente interação humana, existem varias razoes para a solidão, seja intencional ou não. Razões intencionais incluem ser introvertido ,ter considerações religiosas, espirituais ou misticas, ou filosofias pessoais "
    )

