import re,copy,pdb
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
    litere="ABCDEFGHIJKLMNOPQRSTUVWXYZ⊤⊥"
    cifre = "0123456789"
    conectori = "¬∧∨⇒⇔|∇⊤⊥"
    all=litere+conectori+"()"
    global nr_im
    for i in n:
        if i[0] in cifre or i[0] not in all:
            print(color.WARNING + "-------EROARE------" + color.ENDC)
            print(f"Element necunoscut: {i}")
            exit(0)
        if i in "(":
            p_deschisa(arbore, poz)
        elif i[0] in litere:
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
def parcurg(arbore,k):
    if len(arbore)==1:
        return 0
    if len(arbore)==3:
        l_r(arbore,k)
        if len(arbore)==3:
            parcurg(arbore[1],k)
            parcurg(arbore[2],k)

    if len(arbore)==2:
        l_r(arbore,k)
        if len(arbore)==2:
            parcurg(arbore[1],k)
        if len(arbore)==3:
            parcurg(arbore[1],k)
            parcurg(arbore[2],k)
def change(arbore,p):
    if len(arbore[p]) == 1:
        arbore[0] = arbore[p][0]
        arbore.pop(1)
        arbore.pop(1)
    elif len(arbore[p]) == 2:
        arbore[0] = arbore[p][0]
        arbore[1] = arbore[p][1]
        arbore.pop(2)
    elif len(arbore[p]) == 3:
        arb=copy.deepcopy(arbore[p])
        arbore[0] = arb[0]
        arbore[1] = arb[1]
        arbore[2] = arb[2]
def change1(arbore,a,b):
    if len(arbore[a][b]) == 1:
        arbore[0] = arbore[a][b][0]
        arbore.pop(1)
        arbore.pop(1)
    elif len(arbore[a][b]) == 2:
        arbore[0] = arbore[a][b][0]
        arbore[1] = arbore[a][b][1]
        arbore.pop(2)
    elif len(arbore[a][b]) == 3:
        arb=copy.deepcopy(arbore[a][b])
        arbore[0] = arb[0]
        arbore[1] = arb[1]
        arbore[2] = arb[2]
def neg(arbore,a,b,c):
    if arbore[a][b] in arbore[c][1] and arbore[c][0]=="¬":
        return True
    if arbore[a][b] in arbore[c][2] and arbore[c][0]=="¬":
        return True
    return False
def l_r(arbore,k):
    if k=="∧":
        a="∧"; b="∨"; c="⊤";d="⊥"
    if k=="∨":
        a="∨"; b="∧"; c="⊥";d="⊤"
    litere = "ABCDEFGHIJKLMNOPQRSTUVWXYZ⊤⊥"
    global ok
    if arbore[0]=="⇔":
        arbore[0]="∧"
        a=copy.deepcopy(arbore[1])
        b=copy.deepcopy(arbore[2])
        arbore[1]=["∨",["¬",a],b]
        arbore[2]=["∨",a,["¬",b]]
        ok=1
        return 0
    if arbore[0]=="⇒":
        if arbore[1]==arbore[2]:
            arbore[0] = "⊤"
            arbore.pop(1)
            arbore.pop(1)
            ok = 1
            return 0
        else:
            arbore[0]="∨"
            arbore[1]=["¬",arbore[1]]
            ok=1
            return 0
    if arbore[0]=="¬" :
        if len(arbore[1])==3:
            if arbore[1][0]=="∧":
                arbore[0]="∨"
                arb1=copy.deepcopy(arbore[1])
                arbore[1]=["¬",arb1[1]]
                arbore.append(["¬",arb1[2]])
                ok=1
                return 0
            if arbore[1][0]=="∨":
                arbore[0]="∧"
                arb2=copy.deepcopy(arbore[1])
                arbore[1]=["¬",arb2[1]]
                arbore.append(["¬",arb2[2]])
                ok=1
                return 0
        if len(arbore[1]) == 2:
            if arbore[1][1][0] != "¬":
                if len(arbore[1][1]) == 1:
                    arbore[0] = arbore[1][1][0]
                    arbore.pop(1)
                    ok = 1
                    return 0
                if len(arbore[1][1]) == 3:
                    arbore[0] = arbore[1][1][0]
                    arbore.append(arbore[1][1][2])
                    arbore[1] = arbore[1][1][1]
                    ok = 1
                    return 0
        if len(arbore[1])==1:
            if arbore[1][0]=="⊤":
                arbore[0]="⊥"
                arbore.pop(1)
                ok=1
                return 0
            if arbore[1][0]=="⊥":
                arbore[0]="⊤"
                arbore.pop(1)
                ok=1
                return 0

    if (arbore[0]== a and arbore[1][0] == b) or (arbore[0]== b and arbore[1][0] == a):
        if arbore[2] in arbore[1]:
            change(arbore, 2)
            ok = 1
            return 0

        if arbore[2][0]==arbore[1][0]:
            if arbore[1][1] in arbore[2] and ((arbore[1][2] in arbore[2][1] and arbore[2][1][0]=="¬")
                                              or (arbore[1][2] in arbore[2][2] and arbore[2][2][0]=="¬" )):
                change1(arbore,1,1)
                ok=1
                return 0
            if arbore[1][2] in arbore[2] and ((arbore[1][1] in arbore[2][1] and arbore[2][1][0]=="¬")
                                              or (arbore[1][1] in arbore[2][2] and arbore[2][2][0]=="¬" )):
                change1(arbore,1,2)
                ok=1
                return 0
        if arbore[2] in arbore[1][1] :
            arbore[1]=arbore[1][2]
            ok=1
            return 0
        if arbore[2] in arbore[1][2]:
            arbore[1]=arbore[1][1]
            ok=1
            return 0
    if (arbore[0]== a and arbore[2][0] == b) or (arbore[0]== b and arbore[2][0] == a):
        if arbore[1] in arbore[2]:
            change(arbore, 1)
            ok = 1
            return 0
        if arbore[2][0]==arbore[1][0]:
            if arbore[2][1] in arbore[1] and ((arbore[2][2] in arbore[1][1] and arbore[1][1][0]=="¬")
                                              or (arbore[2][2] in arbore[1][2] and arbore[1][2][0]=="¬" )):
                change1(arbore,2,1)
                ok=1
                return 0
            if arbore[2][2] in arbore[1] and ((arbore[2][1] in arbore[1][1] and arbore[1][1][0]=="¬")
                                              or (arbore[2][1] in arbore[1][2] and arbore[1][2][0]=="¬" )):
                change1(arbore,2,2)
                ok=1
                return 0
        if arbore[1] in arbore[2][1] :
            arbore[2]=arbore[2][2]
            ok=1
            return 0
        if arbore[1] in arbore[2][2]:
            arbore[2]=arbore[2][1]
            ok=1
            return 0

    if arbore[0]==a :
        if arbore[1] == arbore[2]:
            change(arbore,2)
            ok = 1
            return 0
        if arbore[1][0]==d or arbore[2][0]==d:
            arbore[0]=d
            arbore.pop(1)
            arbore.pop(1)
            ok=1
            return 0
        if arbore[1][0] == c:
            change(arbore,2)
            ok=1
            return 0
        if arbore[2][0] == c:
            change(arbore,1)
            ok = 1
            return 0
        if (len(arbore[1])==2 and arbore[1][0]=="¬" and arbore[1][1]==arbore[2]) or  \
                (len(arbore[2]) == 2 and arbore[2][0]=="¬" and arbore[2][1]==arbore[1]):
                arbore[0]=d
                arbore.pop(1)
                arbore.pop(1)
                ok=1
                return 0
        if arbore[2][0]==a and arbore[1][0]==b:
            if arbore[2][2] in arbore[1]:
                arbore[0]=a
                arbore[1]=[a,arbore[1],arbore[2][2]]
                change(arbore[2],1)
            if arbore[2][1] in arbore[1]:
                arbore[0]=a
                arbore[1]=[a,arbore[1],arbore[2][1]]
                change(arbore[2],2)
        if arbore[1][0]==a and arbore[2][0]==b:
            if arbore[1][2] in arbore[2]:
                arbore[0]=a
                arbore[2]=[a,arbore[2],arbore[1][2]]
                change(arbore[1],1)
            if arbore[1][1] in arbore[2]:
                arbore[0]=a
                arbore[2]=[a,arbore[2],arbore[1][1]]
                change(arbore[1],2)
        if arbore[1][0]==a:
            if arbore[2] in arbore[1]:
                change(arbore,1)
                ok=1
                return 0
        if arbore[2][0]==a:
            if arbore[1] in arbore[2]:
                change(arbore,2)
                ok=1
                return 0

    if arbore[0]==b :
        if len(arbore[1])==1 and len(arbore[2])==3:
            if arbore[2][0]==b and len(arbore[2][1])==2:
                if arbore[1][0]==arbore[2][1][1][0]:
                    arbore[0]=c
                    arbore.pop(1)
                    arbore.pop(1)
                    ok=1
                    return 0
            if arbore[2][0] == b and len(arbore[2][2]) == 2:
                if arbore[1][0]==arbore[2][2][1][0]:
                    arbore[0]=c
                    arbore.pop(1)
                    arbore.pop(1)
                    ok=1
                    return 0
        if len(arbore[2])==1 and len(arbore[1])==3:
            if arbore[1][0]==b and len(arbore[1][1])==2:
                if arbore[2][0]==arbore[1][1][1][0]:
                    arbore[0]=c
                    arbore.pop(1)
                    arbore.pop(1)
                    ok=1
                    return 0
            if arbore[1][0] == b and len(arbore[1][1]) == 2:
                if arbore[2][0]==arbore[1][1][1][0]:
                    arbore[0]=c
                    arbore.pop(1)
                    arbore.pop(1)
                    ok=1
                    return 0
        if len(arbore[1])==3 and len(arbore[2])==3:
            if arbore[1][0]==arbore[2][0] and arbore[1][0]==b:
                if len(arbore[2][1])==2:
                    if arbore[2][1][1]==arbore[1][1] or arbore[2][1][1]==arbore[1][2]:
                        arbore[0] = c
                        arbore.pop(1)
                        arbore.pop(1)
                        ok = 1
                        return 0
                if len(arbore[2][2])==2:
                    if arbore[2][2][1]==arbore[1][1] or arbore[2][2][1]==arbore[1][2]:
                        arbore[0] = c
                        arbore.pop(1)
                        arbore.pop(1)
                        ok = 1
                        return 0
                if len(arbore[1][1])==2:
                    if arbore[1][1][1]==arbore[2][1] or arbore[1][1][1]==arbore[2][2]:
                        arbore[0] = c
                        arbore.pop(1)
                        arbore.pop(1)
                        ok = 1
                        return 0
                if len(arbore[1][2])==2:
                    if arbore[1][2][1]==arbore[2][1] or arbore[1][2][1]==arbore[2][2]:
                        arbore[0] = c
                        arbore.pop(1)
                        arbore.pop(1)
                        ok = 1
                        return 0
        if len(arbore[1])==2 and len (arbore[2])==3 and arbore[2][0]==b:
            if arbore[1][1]==arbore[2][1] or arbore[1][1]==arbore[2][2]:
                arbore[0] = c
                arbore.pop(1)
                arbore.pop(1)
                ok = 1
                return 0
        if len(arbore[2]) == 2 and len(arbore[1]) == 3 and arbore[1][0]==b:
            if arbore[2][1] == arbore[1][1] or arbore[2][1] == arbore[1][2]:
                arbore[0] = c
                arbore.pop(1)
                arbore.pop(1)
                ok = 1
                return 0

        if arbore[1][0] == a:
            arbore[0] = a
            arb6 = copy.deepcopy(arbore[1])
            arbore[1] = [b, arbore[2], arb6[1]]
            arbore[2] = [b, arbore[2], arb6[2]]
            ok = 1
            return 0
        if  arbore[2][0] == a:
            arbore[0] = a
            arb7 = copy.deepcopy(arbore[1])
            arbore[1] = [b, arb7, arbore[2][1]]
            arbore[2] = [b, arb7, arbore[2][2]]
            ok = 1
            return 0
        if arbore[1]==arbore[2] :
            change(arbore,2)
            ok = 1
            return 0
        if arbore[1][0] == c or arbore[2][0] == c:
            arbore[0] = c
            arbore.pop(1)
            arbore.pop(1)
            ok=1
            return 0
        if arbore[1][0] == d:
            change(arbore,2)
            ok = 1
            return 0
        if arbore[2][0] == d:
            change(arbore,1)
            ok = 1
            return 0
        if (len(arbore[1])==2 and arbore[1][0]=="¬" and arbore[1][1]==arbore[2]) or \
                (len(arbore[2]) == 2 and arbore[2][0]=="¬" and arbore[2][1]==arbore[1]) :
                arbore[0]=c
                arbore.pop(1)
                arbore.pop(1)
                ok=1
                return 0
        if arbore[1][0]==b and arbore[2][0]==b:
            if arbore[1][1] in arbore[2]:
                arbore[1][1]=d
                ok=1
                return 0
            if arbore[1][2] in arbore[2]:
                arbore[1][2]=d
                ok=1
                return 0
        if arbore[1][0]==b:
            if arbore[2] in arbore[1]:
                change(arbore,1)
                ok=1
                return 0
        if arbore[2][0]==b:
            if arbore[1] in arbore[2]:
                change(arbore,2)
                ok=1
                return 0
def transf_back(arbore,prop):
    if len(arbore)==1:
        return arbore[0]
    if len(arbore)==2:
        return f"¬{arbore[1][0]}"
    if arbore[0] in "∧∨⇒⇔":
        prop.append("(")
        prop.append(transf_back(arbore[1],prop))
        prop.append(arbore[0])
        prop.append(transf_back(arbore[2],prop))
        prop.append(")")
    if arbore[0] in "¬":
        prop.append("(")
        prop.append("¬")
        prop.append(transf_back(arbore[1],prop))
        prop.append(")")
def transf_in_formula(arbore,prop,k):
    if len(arbore) == 1:
        prop.append(arbore[0])
    if len(arbore) == 2:
        prop.append(arbore[0])
        prop.append(arbore[1])
    prop = str(prop)
    prop = re.sub("None|,|'|\[|]| ", "", prop)
    prop1 = "";last = 0
    for i in range(len(prop)):
        if prop[i] == k:
            p = re.sub("\(|\)", "", prop[last:i])
            if last == 0:
                prop1 = prop1 + "(" + p + ")"
            else:
                prop1 = prop1 + k + "(" + p + ")"
            last = i + 1
    if last != 0:
        p = re.sub("\(|\)", "", prop[last:len(prop)])
        prop1 = prop1 + k + "(" + p + ")"
    if prop1 == "":
        p = re.sub("\(|\)", "", prop[0:len(prop)])
        prop1 = prop1 + p
    return prop1

conectori = "¬∧∨⇒⇔|∇⊤⊥"
arbore=[];arbore1=[];arbore2=[]; poz=[]; prop=[];prop1=[];ok = 1
print("¬ ∧ ∨ ⇒ ⇔ | ∇ ⊤ ⊥")
n=input("Propozitie:")
n=re.sub(" +","",n)
n=n.upper()
n=transf(n)
n=s_stricta(n)
parcurgere(n)
print("Arbore:", arbore)

k="∧"
arbore1=copy.deepcopy(arbore)
print(color.TEXT)
if poz==[] and arbore1 != []:
    while ok!=0:
        ok=0
        l_r(arbore1,k)
        parcurg(arbore1,k)
    print("Arbore (formula in FNC): ", arbore1)
else:
    print(color.WARNING + "-------EROARE------" );print(color.TEXT + "------Nu------")
    print(arbore);print(f"Pozitia_curenta=Arbore{poz}")

transf_back(arbore1,prop)
rez=transf_in_formula(arbore1,prop,k)
print("Formula in FNC: ", rez,"\n")
ok=1
arbore1=copy.deepcopy(arbore)
k="∨"
if poz==[] and arbore != []:
    while ok!=0:
        ok=0
        l_r(arbore,k)
        parcurg(arbore,k)
    print("Arbore (formula in FND): ", arbore)
else:
    print(color.WARNING + "-------EROARE------" );print(color.TEXT + "------Nu------")
    print(arbore);print(f"Pozitia_curenta=Arbore{poz}")

transf_back(arbore,prop1)
rez1=transf_in_formula(arbore,prop1,k)
print("Formula in FND: ", rez1)


