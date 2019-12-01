#!//usr/bin/python3

y = "2,3,4,6,7"
print (y.split())


wartosci = input()
lista = wartosci.split()
print(lista, type(lista))


for i in range(len(lista)):
    lista[i] = int(lista[i])

    #robie liste w liscie, to ponizej jest tozsame dla tego co jest nizej
lista = [int(i) for in in lista]

    print(lista, type(lista))


wynik= list(map(int(), wartosci))


liczby = list()
for i in range(2000, 3001):
    if((i%7==0) and (i%5!=0)):
        liczby.append(i)
print(liczby)
