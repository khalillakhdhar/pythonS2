a=-1
b=-1
cnt="o"
def controle(x):
    x=int(input("donner un entier"))
    while(x<1):
        x=int(input("veuillez redonnez un entier positif!"))
    return x


def pgcd(a,b):
    while(a!=b):
        if(a>b):
            a=a-b
        else:
            b=b-a
    print("le PGCD est de  : %s"%a)


while(cnt!="n"):
    a = controle(a)
    b = controle(b)
    pgcd(a, b)
    cnt=input("Continuer? OUI (o)/Non (n)")
