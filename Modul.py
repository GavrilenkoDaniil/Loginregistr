from funktsioonid import *
users=loe_failist_listisse("users.txt")
passwords=loe_failist_listisse("passwords.txt")
A=""
I=""

while True:
    print("Registreerimine-1\nAutoriseerimine-2\nVälja-3")
    v=int(input())
    if v==1:
        print("Registreerimine")
        while 1:
            log=input("Login:")
            if log not in users:
                print("Tunnus soobib")
                break
            else:
                print("See nimi on olemas listis")
        v=input("Arvuti - A või ise - I loob parool")
        if v.upper()=="A":
            pas=passautomat()
            print("Sinu parool: "+pas)
        elif v.upper()=="I":
            while 1:
                pas=input("Sisesta oma parool: ")
                tulemus=paskontroll(pas)
                if tulemus==True:
                    users.append(log)
                    passwords.append(pas)
                    break
    elif v==2:
        print("Autoriseerimine")
        log=input("Login: ")
        if log not in users:
            print("Sina ei ole registreeritud")
        else:
            pas=input("Password: ")
            if pas not in passwords:
                print("Vale parool")
            else:
                if users.index(log)==passwords.index(pas):
                    print("Tere tulemast!")
                else:
                    print("Vale parool või login")
    elif v==3:
        print("Välja")
        aa("users.txt",users)
        aa("passwords.txt",passwords)
        break
    else:
        print("On vaja valida 1,2 või 3")
