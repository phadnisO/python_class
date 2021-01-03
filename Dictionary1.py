keys = ["SRK", "Salman""Amir"]
Names={
  "SRK" : 20,
  "Salman" : 40,
  "Amir": 50,
}
print (Names)
for key_label in Names.keys():
  print(key_label)
for key_label in Names.values():
  print(key_label)
Names["Akshay"] = 60
print (Names)
for key_label,key_val in Names.items():
  print(key_label+" " + str (key_val))
Names["Salman"]=80
print(Names)
 
total= Names["Salman"]- Names["Amir"]
print(total)


#output
#{'SRK': 20, 'Salman': 40, 'Amir': 50}
#SRK
#Salman
#Amir
#20
#40
#50
#{'SRK': 20, 'Salman': 40, 'Amir': 50, 'Akshay': 60}
#SRK 20
#Salman 40
#Amir 50
#Akshay 60
#{'SRK': 20, 'Salman': 80, 'Amir': 50, 'Akshay': 60}
#30
