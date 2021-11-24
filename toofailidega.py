def loe_failist(file:str)->str:
    """Loeme tekst failist
    """
    f=open(file,'r')
    stroka=f.read() #str
    #stroka=f.readlines() #list
    f.close()
    return stroka
stroka=loe_failist("TextFile.txt")
print(stroka)

def loe_failist_listisse(file:str)->list:
    """Loeme tekst failist ja salvesta järjendisse
    """
    f=open(file,'r')
    list_=[]
    for stroka in f:
        list_.append(stroka.strip())
    f.close()
    return list_
spisok=loe_failist_listisse("TextFile.txt")
print(spisok)

def salvesta_failisse(file:str):
    f=open(file,'a')
    text=input("Sisesta tekst:")
    f.write(text+'\n')
    f.close()

for i in range(10):
    salvesta_failisse("Loetelu.txt")

def aa(file:str):
    """Changing text in file
    """
    text=input("Sisesta uus tekst:")
    with open(file,'w') as f: #Не надо делать .close
        f.write(text+'\n')

aa(input("Faili nimetus")+".txt")
  