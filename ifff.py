#!/usr/bin/python3
#wczytuj wiersze wpisane przez użytkownika i wyświetl dużymi literami

while True:
    reply = input('wpisz tekst:')
    if reply == 'stop' :
        break
    elif not reply.isdigit():
        print('niepoprawne! ' *5)
    else:
        num = int(reply)
    if num < 20:
            print('mało')
    else:
        print(num**2)
print('kuniec')
