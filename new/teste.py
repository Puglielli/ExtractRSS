
test = "Sun, 19 May 2019 08:00:53 -0000"

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


def date(date):
    first = date.split(',')
    second = first[1].split(" ")
    date = second[1] + "/" + mes(second[2])+ "/" + second[3] + " - " + second[4]
    return date

date = date(test)
print(date)
