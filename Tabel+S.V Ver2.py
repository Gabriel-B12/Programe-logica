import re, copy
class color:
    TEXT = '\033[33m'
    WARNING = '\033[91m'
    ENDC = '\033[0m'
def copy1(arbore,poz,l):
    arbt = arbore
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
def eroare(arbore,poz):
    print(color.WARNING + "-------EROARE------"+color.ENDC)
    print(color.TEXT)
    print(arbore)
    print()
    print(f"Pozitia_curenta=Arbore{poz}")
    exit(0)
def acces(arbore, poz):
    arbt=arbore
    for i in poz:
        arbt = arbt[i]
    return arbt
def p_deschisa(arbore,poz):
    if arbore == []:
        arbore.append("con")
        arbore.append(["prop"])
        arbore.append(["prop"])
    elif acces(arbore,poz)== "con" or len(arbore) == 1:
        eroare(arbore,poz)
    else:
        l=["con",["prop"],["prop"]]
        copy1(arbore, poz, l)
    poz.append(1)
def v(arbore,poz,var):
    l=[]
    l.append(var)
    if acces(arbore,poz) == ["prop"]:
        copy1(arbore, poz, l)
    elif arbore == []:
        arbore.append(var)
        return 0
    else:
        eroare(arbore,poz)
    poz[-1] = 0
def con(arbore,poz,c):
    if poz == [] or poz[-1] == 2 :
        eroare(arbore,poz)
    if c == "¬" :
        arbt = arbore
        for i in range(len(poz) - 1):
            arbt = arbt[poz[i]]
        arbt.pop(2)
        poz[-1]=0
    if acces(arbore,poz) == "con":
        copy1(arbore, poz, c)
    else:
        eroare(arbore,poz)

    if c == "¬":
        poz[-1] = 1
    else:
        poz[-1] = 2
def p_inchisa(arbore,poz):
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
def parcurgere(n):
    global s
    litere="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cifre = "0123456789"
    conectori = "¬∧∨⇒⇔|∇⊤⊥"
    all = litere  + conectori +"()"
    for i in n:
        if i[0] in cifre or i[0] not in all:
            print(color.WARNING + "-------EROARE------" + color.ENDC)
            print(f"Element necunoscut: {i}")
            exit(0)
        if i in "(":
            p_deschisa(arbore, poz)
        elif i[0] in litere:
            s.add(i)
            v(arbore, poz, i)
        elif i in ")":
            p_inchisa(arbore, poz)
        elif i in conectori:
            con(arbore, poz, i)
def transf(m):
    cifre = "1234567890"
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
def functie(con,a,b):
    if con == "¬":
        return (a+1)%2
    elif con == "∧":
        return a and b
    elif con == "∨":
        return a or b
    elif con=="⇒":
        if a==1 and b==0: return 0
        else: return 1
    elif con=="⇔":
        return (a+b+1)%2
    elif con=="∇":
        return ((a or b)+1)%2
    elif con =="|":
        return ((a and b)+1)%2
def val(a,d):
    if a==0 or a==1:
        return a
    return d[a]
def v_interpretare(arbore):
    global d1

    if len(arbore) == 3:
        if len(arbore[1])==1 and len(arbore[2])==1:
            con=arbore[0]
            arbore[0]=functie(con,val(arbore[1][0],d1),val(arbore[2][0],d1))
            arbore.pop(1)
            arbore.pop(1)
            return arbore
        if len(arbore)>1:

            if len(arbore[1])>1:
                return v_interpretare(arbore[1])
            if len(arbore[2])>1:
                return v_interpretare(arbore[2])
    else :
        if len(arbore[1]) == 1:
            arbore[0]=functie("¬",val(arbore[1][0],d1),0)
            arbore.pop(1)
            return arbore
        else:
            return v_interpretare(arbore[1])
def tabel(arbore,poz):
    f=open("tabel.txt","w",encoding="utf-8")
    global nr_i, s, d1, d, n1, nr1
    arbore1 = copy.deepcopy(arbore)
    if poz != []:
        eroare(arbore, poz)
    for j in range(len(s)):
        f.write(str(s[j])+" ")
    f.write("\n")
    for i in range(nr_i):
        for j in range(len(s) - 1):
            d1[s[j]] = (i//(2**(len(s)-2-j)))%2
            f.write(str(d1[s[j]])+" "*len(s[j]))
        if len(arbore) == 1:
            arbore[0] = val(arbore[0], d1)
            f.write(str(arbore[0]))
        else:
            while len(arbore) > 1:
                v_interpretare(arbore)
        d1[n1]=arbore[0]
        if d1[n1]==1:
            nr1+=1
        f.write(" "*(len(n1)//2))
        f.write(str(d1[n1]))
        f.write("\n")
        arbore = copy.deepcopy(arbore1)
    f.close()
def s_stricta(n):
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


litere="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
conectori="¬∧∨⇒⇔|∇⊤⊥"
paranteze="()"
cifre="0123456789"
arbore=[]
arbore1=[]
poz=[]
s=set()
d1={}

print("¬ ∧ ∨ ⇒ ⇔ | ∇ ⊤ ⊥")
n=input(color.TEXT+"Propozitie:")
n=re.sub(" +","",n)
n=n.upper()
n1=n
nr1=0
n=transf(n)
n=s_stricta(n)
parcurgere(n)
arbore1=copy.deepcopy(arbore)
m=len(s)
nr_i=2**m
s=list(s)
s.sort()
s.append(n1)

if len(s)==2:
    f = open("tabel.txt", "w", encoding="utf-8")
    f.write(str(s[0]) + "\n")
    f.write("0" + "\n")
    f.write("1" + "\n")
    f.close()
    nr1=1
else:
    tabel(arbore,poz)
print("Tabelul de adevar se afla in tabel.txt")
print("Arbore: ", arbore1)
if nr1==nr_i: print("Formula este valida.")
else: print("Formula este nevalida.")
if nr1==0: print("Si nesatisfiabila")
else: print("Si satisfiabila")
