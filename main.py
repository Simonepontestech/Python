print("Você procura por um carro 0KM, com o maior numero de parcelas sem comprometer muito sua renda?"
      "Informe seus dados e vamos procurar a melhor oportunidade")


nome = str(input("Qual é o seu nome?: "))
renda = int(input("Insira sua renda: "))
entrada = int(input("Insira o valor de entrada: "))

print("Para não comprometer sua renda {}, o valor das parcelas do automovel terá que ser menor ou igual a 30%"
      " da sua renda de: {}".format(nome,renda))

ofertaA = (60000 - entrada)/48
ofertaB = (80000 - entrada)/60
ofertaC = (50000 - entrada)/48
ofertaD = (75000 - entrada)/60
ofertaE = (36000 - entrada)/36
ofertaF = (48000 - entrada)/40
ofertaG = (77000 - entrada)/60
ofertaH = (150000 - entrada)/60

ofertas = []

lista = [ofertaA, ofertaB, ofertaC,
          ofertaD, ofertaE, ofertaF,
          ofertaG, ofertaH]

lista.sort()
ofertas.append(lista)

while True:
  if ofertas[0][0] == ofertaA:
        print(" Caoa Chery é sua melhor oportunidade!")
        break
  elif ofertas[0][0] == ofertaB:
        print("Capital Fiat é sua melhor oportunidade!")
        break
  elif ofertas[0][0] == ofertaC:
        print("Mais é sua melhor oportunidade!")
        break
  elif ofertas[0][0] == ofertaD:
        print("Monte Carlo Peugeot é sua melhor oportunidade!")
        break
  elif ofertas[0][0] == ofertaE:
        print("Fiori é sua melhor oportunidade!")
        break    
  elif ofertas[0][0] == ofertaF:
        print("Tambaí é sua melhor oportunidade!")
        break
  elif ofertas[0][0] == ofertaG:
        print("Cavalcante Primo é sua melhor opotunidade!")
        break
  elif ofertas[0][0] == ofertaH:
        print("Promac é sua melhor oportunidade!")
        break
  else:
        print("Não há oportunidade para você.")
        break