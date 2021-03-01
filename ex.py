# Saisie
def saisie():
    x=0
    while x==0:
        x=input("Nombre de villes:")
        try:
            if 4<=int(x)<=10:
                break
            else:
                print("valeur incorrect")
                x=0
        except:
            print("ce n'est pas un nombre")
            x=0
    return int(x)
#saisie_population
def saisie_population():
    x=0
    while x==0:
        x=input()
        try:
            if int(x)>=5000:
                break
            else:
                print("population invalide")
                x=0
        except:
            print("valeur incorrect")
            x=0
    return int(x)
            
# Lecture
def lecture():
    ch=""
    while ch=="":
        ch=input()
        L=ch.split()
        i=0
        for m in L:
            if m.isalpha():
                i=i+1
        if i==len(L):
            break
        else:
            ch=""
    return ch
            
# Remplir
def remplir(N):
    L=[]
    for i in range(N):
        print("Ville n°",i+1,"(Nom-Population-Gouvernorat):")
        v={"nom":lecture(),"population":saisie_population(),"nomg":lecture()}
        L.append(v)
    return L
# Afficher:
def afficher(T,N,nom_gov):
    for i in range(len(T)):
        d=T[i] # un dictionnaire
        if d["nomg"]==nom_gov:
            print(d["nom"],end="  ")

#Calculer
def calculer(T,N,nom_gov):
    t=0
    for i in range(len(T)):
        d=T[i]
        if d["nomg"]==nom_gov:
            t=t+d["population"]
    return t

# Programme Principal
N=saisie()
T=remplir(N)
print(T)
print("Entrer le nom du gouvernorat à chercher:")
nom_gov=lecture()
print("Les villes de",nom_gov,"sont:")
afficher(T,N,nom_gov)
tot=calculer(T,N,nom_gov)
print("\nTotal population=",tot)