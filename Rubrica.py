import os

lista = [] #lista per il nome (cognome incluso)
lista2 = [] #lista per il numero


def menu():

    rub = input('''
RUBRICA

[1] Aggiungi un contatto
[2] Ricerca per nome
[3] Stampa la rubrica
[4] Elimina contatto
[E] Esci dal programma

 ''')

    if rub == '1':
        print('Stai inserendo un contatto.')
        inserisci()

    elif rub == '2':
        print('Stai effettuando una ricerca per nome.')
        ricerca()

    elif rub == '3':
        print('Stai stampando la rubrica aggiornata.')
        stampa()
    
    elif rub == '4':
        print('Stai eliminando l\'intera rubrica.')
        elimina()

    elif rub == 'E' or rub == 'e':

        uscita = input('Sei sicuro di voler uscire? S/n ')
        esci = False #variabile booleana a falso 

        if uscita == 'S' or uscita == 's':
            print('PROGRAMMA TERMINATO...')
            esci = True #variabile booleana vera, esce da programma 

        elif uscita == 'N' or uscita == 'n':
            menu()

def inserisci():
    global lista
    global lista2    

    i = 1
    while True:
        
        nome = input('Inserisci il ' + str(i) + '° contatto desiderato: ')
        numero = int(input('Inserisci il numero: '))
        lista.append(nome)
        lista2.append(numero)
        
        i = i + 1

        if i == 100: #in estremo la rubrica può contenere massimo 100 contatti
            print('I tuoi contatti sono stati salvati.')
            print(nome)
            menu()
            break

        controllo = input('Vuoi inserire un altro contatto? S/n ')

        if controllo == 'S' or controllo == 's':
            continue

        elif controllo == 'N' or controllo == 'n':
            print('I tuoi contatti sono stati salvati.')
            menu()
            break

def ricerca():
    global lista
    global lista2

    if len(lista) == 0:
        print('Non ci sono contatti.')
        menu()

    elif len(lista) == 1:
        print('C\'è solo un contatto nella tua rubrica.')
        i = 0
        print('Nome: ', lista[i])
        print('Numero: ', lista2[i])
        menu()

    else:
        ricercato = input('Inserisci il contatto da ricercare: ')
        trovato = False #variabile boolena a sentinella impostata a spenta
        i = 0

        while i < len(lista) and not trovato:
            if lista[i] == ricercato:
                print('Contatto trovato.')
                print('Nome: ', lista[i])
                print('Numero: ', lista2[i])
                trovato = True #si attiva la sentinella se viene trovata una corrispondenza 

            i = i + 1 #incrementa il indice contatore 
                   
    menu()

def stampa():
    global lista
    global lista2
    i = 0 #indice collegato alla lista
    j = 1 #indice per definire la posizione del contatto
    while True:
        print('Contatto ' + str(j) + '->', 'Nome:', lista[i], 'Numero:', lista2[i])
        i = i + 1 #incremento l'indice della lista per nome e numero
        j = j + 1 #incremento la posizione del contatto 
                            
        if i == len(lista): #if i == len(lista2)
            break           #se la lunghezza della prima lista (o della seconda) termina   
                            # interrompi (break)
    menu()

def elimina():
    global lista
    global lista2

    ricercato = input('Inserisci il contatto da ricercare: ')
    trovato = False #variabile boolena a sentinella impostata a spenta
    i = 0

    while i < len(lista) and not trovato:
        if lista[i] == ricercato:
            trovato = True #si attiva la sentinella se viene trovata una corrispondenza 
            elimina = input("Vuoi eliminare il contatto? S/n ")
            if elimina == "S" or elimina == "s":
                lista.remove(ricercato)
                print("Contatto eliminato.")
                menu()
            elif elimina == "N" or elimina == "n":
                print("Contatto non eliminato.")
                menu()
        i = i + 1 #incrementa il indice contatore 
        

if __name__ == "__main__":
    menu()
    os.system('pause')