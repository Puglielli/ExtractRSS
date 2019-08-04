import csv
import feedparser


link = input("Informe o Link: ")
if not link.__contains__("http"):
    link = "http://" + link
print("Link: " + link)

link = feedparser.parse(link)

#Metodo para transformar texto do mes em numero

def mes(arg):
	x =  arg.upper()
	if x == "JAN":
  	  return "01"
	elif x == "FEV" or x == "FEB":
	    return "02"
	elif x == "MAR":
		return "03"
	elif x == "ABR" or x == "APR":
		return "04"
	elif x == "MAI" or x == "MAY":
		return "05"
	elif x == "JUN":
		return "06"
	elif x == "JUL":
		return "07"
	elif x == "AGO" or x == "AUG":
		return "08"
	elif x == "SET" or x == "SEP":
		return "09"
	elif x == "OUT" or x == "OCT":
		return "10"
	elif x == "NOV":
		return "11"
	elif x == "DEZ" or x == "DEC":
		return "12"
	else:
 	  return "00"

#Metodo para separar a data da hora

def splitDate(date):
    first = date.split(',')
    second = first[1].split(" ")
    date = second[1] + "/" + mes(second[2])+ "/" + second[3] + " - " + second[4]
    return date


def salvarCSV():
	try:
		type = input("\nDigite 'w' para Substituir ou 'a' para Acrescentar\n ")
		with open('Rss.csv', type, newline='') as csvfile:
			file = csv.writer(csvfile, delimiter=";")
			header = ['titulo', 'data_noticia', 'LINK']
			file.writerow(header)
			string = []
			for page in link.entries:
				date = splitDate(page.published)
				string.append([page.title, date, page.link])
				string.append({"___________________________________________________________________________________"})
			else:
				file.writerows(string)
	except ValueError:
		opcErro(0)
	except PermissionError:
		 opcErro(1)


def opcErro(erro):
	if erro == 1:
		print ("Oops!  Não foi possível salvar, pois o arquivo está aberto.  Tente novamente...\n")
	elif erro == 2:
		print("Error de caracter")
	else:
		print("Erro invalido")

	opc = input("\nDigite 1 para tentar novamente ou 0 para sair\n")
	if opc == "1":
	   salvarCSV()
	elif opc == "0":
	   print("Os dados não foram salvos")
	else:
	   print("Digito inválido")

#Chamar Metodo SalvaCSV
salvarCSV()
