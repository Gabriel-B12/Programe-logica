import re
class color:
    TEXT = '\033[33m'
    WARNING = '\033[91m'
    ENDC = '\033[0m'
def copy(arbore,poz,l):                     # functia copy copiaza in arbore pe pozitia poz pe l
    arbt = arbore                           # l poate reprezenta o prop atomica dar si un subarbore
    if poz == []:
        eroare(arbore,poz)
    if acces(arbore,poz)==["prop"]:
        for i in range(len(poz)-1):
            arbt = arbt[poz[i]]
        arbt[poz[-1]]=l
    else:
        for i in range(len(poz)-1):
            arbt = arbt[poz[i]]
        arbt[0] = l
def eroare(arbore,poz):                     #aceasta functie este apelata in caz de o eroare
    print(color.WARNING + "-------EROARE------"+color.ENDC)
    print(color.TEXT)
    print(arbore)
    print()
    print(f"Pozitia_curenta=Arbore{poz}")
    exit(0)
def acces(arbore, poz):                        # functia acces acceseza un element din interiorul arborelui
    arbt=arbore                                # - poz este o lista cu valori
    for i in poz:
        arbt = arbt[i]
    return arbt
def p_deschisa(arbore,poz):                     # functia este apelata atunci cand intalnim o paranteza deschisa
    if arbore == []:
        arbore.append("con")
        arbore.append(["prop"])
        arbore.append(["prop"])
    elif acces(arbore,poz)== "con" or len(arbore) == 1:
        eroare(arbore,poz)
    else:
        l=["con",["prop"],["prop"]]
        copy(arbore,poz,l)
    poz.append(1)
def v(arbore,poz,var):                      # functia este apelata atunci cand intalnim o variabila
    l=[]
    l.append(var)
    if acces(arbore,poz) == ["prop"]:
        copy(arbore,poz,l)
    elif arbore == []:
        arbore.append(var)
        return 0
    else:
        eroare(arbore,poz)
    poz[-1] = 0
def con(arbore,poz,c):                      # functia este apelata atunci cand intalnim un conector
    if poz == [] or poz[-1] == 2 :
        eroare(arbore,poz)
    if c == "¬" :
        arbt = arbore
        for i in range(len(poz) - 1):
            arbt = arbt[poz[i]]
        arbt.pop(2)
        poz[-1]=0
    if acces(arbore,poz) == "con":
        copy(arbore,poz,c)
    else:
        eroare(arbore,poz)

    if c == "¬":
        poz[-1] = 1
    else:
        poz[-1] = 2
def p_inchisa(arbore,poz):                      # functia este apelata atunci cand intalnim o paranteza inchisa
    if len(poz) >0:
        if  acces(arbore,poz) == ["prop"] or acces(arbore,poz) == "con" :
            eroare(arbore,poz)
        else:
            poz.pop(len(poz) - 1)
            if len(poz)>0:
                poz[-1]=0
            else:
                pass
    else:
        print(color.WARNING + "Prea MULTE paranteze inchise"+color.ENDC)
        eroare(arbore,poz)
def parcurgere(n):                     # aceasta functie este folosita pentru a parcurge formula
    litere="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cifre = "0123456789"
    conectori = "¬∧∨⇒⇔|∇⊤⊥"
    all=litere+cifre+conectori+"()"
    for i in n:
        print(color.WARNING + i + color.ENDC)
        if i[0] in cifre or i[0] not in all:
            print(color.WARNING + "-------EROARE------" + color.ENDC)
            print(f"Element necunoscut: {i}")
            exit(0)
        if i in "(":
            p_deschisa(arbore, poz)
            print(arbore)
            print(f"Pozitia_curenta=Arbore{poz}")
        elif i[0] in litere:
            v(arbore, poz, i)
            print(arbore)
            print(f"Pozitia_curenta=Arbore{poz}")
        elif i in ")":
            p_inchisa(arbore, poz)
            print(arbore)
            print(f"Pozitia_curenta=Arbore{poz}")
        elif i in conectori:
            con(arbore, poz, i)
            print(arbore)
            print(f"Pozitia_curenta=Arbore{poz}")
def transf(m):                      # functia transf este folosita in cazul in care avem prop atomice scrise astfel:
    cifre = "1234567890"            # - Vx unde V este o litera iar x un numar
    if m=="":
        return m
    n=0
    prop=[]
    litere = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    st = 0
    dr = 0
    if len(m)==1:
        prop.append(m[0])
        return prop
    while n<len(m):
        if m[n] not in litere:
            prop.append(m[n])
        else :
            st=n
            dr=n
            for i in range(st+1,len(m)):
                if m[i] in cifre:
                    dr+=1
                    n+=1
                    if i==len(m)-1:
                        prop.append(m[st:dr + 1])
                else:
                    prop.append(m[st:dr+1])
                    break
            if n==len(m)-1 and m[n] in litere:
                prop.append(m[n])
        n+=1
    return prop
def s_stricta(n):                        # functia modifica formula in cazul in care este in sintaxa relaxata
    def not1(n):
        i=len(n)-1
        while i>=0:
            if n[i] == "¬":
                j=i
                if n[j+1]!="(" and j-1>=0 and j+2<len(n):
                    if n[j-1] != "(" or n[j+2]!=")":
                        n.insert(j+2,")")
                        n.insert(j,"(")
                else:
                    if n[j+1]!="(":
                        n.insert(j + 2, ")")
                        n.insert(j, "(")
                if n[j+1]=="(":
                    nr3=0
                    j1=j
                    while True:
                        j1 = j1 + 1
                        if n[j1] == "(":
                            nr3 += 1
                        if n[j1] == ")":
                            nr3 -= 1
                        if nr3 == 0 and n[j1] == ")":
                            break
                        if j1==len(n)-1:
                            print("Eroare")
                            exit(0)

                if n[j+1]=="(" and j-1>=0 and j1+1<len(n):
                    if n[j-1]!="(" or n[j1+1]!=")":
                        n.insert(j,"(")
                        n.insert(j1+2,")")
                else:
                    if n[j + 1] == "(":
                        n.insert(j, "(")
                        n.insert(j1 + 2, ")")


            i-=1
        return n

    def con1(n,c):
        i = len(n) - 1
        while i >= 0:
            if n[i] == c:
                j = i
                if n[j + 1] != "(" and n[j-1]!=")"   and j+2<len(n) and j-2>=0:
                    if n[j +2] != ")" or n[j -2] != "(":
                        n.insert(j + 2, ")")
                        n.insert(j - 1, "(")
                        i+=1
                        j+=1
                else:
                    if n[j + 1] != "(" and n[j - 1] != ")":
                        n.insert(j+2,")")
                        n.insert(j-1,"(")
                        j+=1
                        i+=1
                if n[j+1]=="(":
                    nr3=0
                    j1=j
                    while True:
                        j1 = j1 + 1
                        if n[j1] == "(":
                            nr3 += 1
                        if n[j1] == ")":
                            nr3 -= 1
                        if nr3 == 0 and n[j1] == ")":
                            break
                        if j1==len(n)-1:
                            print("Eroare")
                            exit(0)
                if n[j-1]==")":
                    nr4=0
                    j2=j
                    while True:
                        j2 = j2 - 1
                        if n[j2] == "(":
                            nr4 -= 1
                        if n[j2] == ")":
                            nr4 += 1
                        if nr4 == 0 and n[j2] == "(":
                            break
                        if j2==0:
                            print("Eroare")
                            exit(0)

                if n[j + 1] == "("  and j1 + 1 < len(n)  and n[j-1]!=")"   and j-2>=0:
                    if  n[j1 + 1] != ")" or n[j -2] != "(" :
                        n.insert(j1 +1, ")")
                        n.insert(j - 1, "(")
                        j+=1
                        i+=1
                else:
                    if n[j + 1] == "(" and n[j-1]!=")":
                        n.insert(j1 + 1, ")")
                        n.insert(j - 1, "(")
                        j += 1
                        i += 1

                if n[j + 1] == "("  and j1 + 1 < len(n)  and n[j-1]==")"   and j2-1>=0:
                    if  n[j1 + 1] != ")" or n[j2 -1] != "(" :
                        n.insert(j1 + 1, ")")
                        n.insert(j2 , "(")
                        j+=1
                        i+=1
                else:
                    if n[j + 1] == "(" and n[j-1]==")":
                        n.insert(j1 + 1, ")")
                        n.insert(j2 , "(")
                        j += 1
                        i += 1

                if n[j + 1] != "("  and j + 2 < len(n)  and n[j-1]==")"   and j2-1>=0:
                    if  n[j + 2] != ")" or n[j2 -1] != "(" :
                        n.insert(j + 2, ")")
                        n.insert(j2 , "(")
                        j+=1
                        i+=1
                else:
                    if n[j + 1] != "(" and n[j-1]==")":
                        n.insert(j + 2, ")")
                        n.insert(j2 , "(")
                        j += 1
                        i += 1

            i -= 1
        return n
    n=not1(n)
    n=con1(n,"∧")
    n = con1(n, "∨")
    n = con1(n, "⇒")
    n = con1(n, "⇔")
    return n

conectori = "¬∧∨⇒⇔|∇⊤⊥"
arbore=[]
poz=[]
print(" Negatie:    ","¬"," "*10,"Conjunctie:","∧","\n","Disjunctie: ","∨"," "*10,"Implicatie:","⇒",)
print(" Echivalenta:","⇔"," "*10,"Nand:  ","|","\n","Nor:  ","∇"," "*16,"Tautologie:","⊤","\n","Contradictie:","⊥")
n=input(color.TEXT+"Propozitie:"+color.ENDC)
n=re.sub(" +","",n)
n=n.upper()

n=transf(n)
n=s_stricta(n)
print(n)
parcurgere(n)

print(color.TEXT)
if poz==[] and arbore != []:
    print("------DA, este formula propozitionala.-------")
    print(arbore)
else:
    print(color.WARNING + "-------EROARE------" )
    print(color.TEXT + "------Nu------")
    print(arbore)
    print(f"Pozitia_curenta=Arbore{poz}")
