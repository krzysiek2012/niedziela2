#!/usr/bin/python3
#wczytuj wiersze wpisane przez użytkownika i wyświetl dużymi literami

while True:
    reply = input('wpisz tekst:')
    if reply == 'stop': break
    try:
        num = int(reply)
    except:
        print('niepoprawne! ' *5)
    else:
        print(int(reply)**2)
print('kuniec')
