import random
#Teeme funktsiooni
def passautomat()->str:
	"""Parool genereeritakse masinaga
	"""	
	str0=".,:;!_*-+()/#¤%&"
	str1 = '0123456789'
	str2 = 'qwertyuiopasdfghjklzxcvbnm'
	str3 = str2.upper() # 'QWERTYUIOPASDFGHJKLZXCVBNM'
	str4 = str0+str1+str2+str3
	ls = list(str4)
	random.shuffle(ls)
	psword = ''.join([random.choice(ls) for x in range(12)])
	return psword
def paskontroll(psword: str)->bool:
	ls=list(psword)
	for e in ls:
		if e.isdigit(): d=True
		if e.isalpha(): a=True
		if e.isupper(): u=True
		if e.islower(): l=True
		if e in list(".,:;!_*-+()/#¤%&"): s=True
	if d==True and a==True and u==True and l==True and s==True:
		t=True
	else:
		t=False
	return t

def loe_failist_listisse(file:str)->list:
    """Loeme tekst failist ja salvesta järjendisse
    """
    f=open(file,'r')
    list_=[]
    for stroka in f:
        list_.append(stroka.strip())
    f.close()
    return list_

def aa(file:str,list_:list):
	"""
	"""
	with open(file,'w') as f: #Не надо делать .close
		for slovo in list_:
			f.write(slovo+'\n')