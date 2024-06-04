
from database.connect_dbase import connect
from models.model import create_table
from controller.control import *


cur = connect.cursor()
qt = 0
enc = "nope"

 

cur.execute(create_table)

while True:
    list_num = (1,2,3,4,5,6,7,8)
    try:
        if qt == 0:
            choix = int(input('''COMMENT PUIS-JE VOUS AIDER? : 
        1. LISTER TOUS LES CONTACTS
        2. RECHERCHER UN CONTACT
        3. RECHERCHER UN NUMÉRO
        4. AJOUTER UN NOUVEAU CONTACT
        5. SUPPRIMER UN CONTACT
        6. MODIFIER UN CONTACT
        7. SUPPRIMER TOUS
        
        SAISISSEZ VOTRE REPONSE S'IL VOUS PLAIT
        ==> '''))
        if enc == "ok":
            choix = int(input('''VOULEZ-VOUS BESOIN UNE AUTRE SERVICE ? 
        1. LISTER TOUS LES CONTACTS
        2. RECHERCHER UN CONTACT
        3. RECHERCHER UN NUMÉRO
        4. AJOUTER UN NOUVEAU CONTACT
        5. SUPPRIMER UN CONTACT
        6. MODIFIER UN CONTACT
        7. SUPPRIMER TOUS
        8. QUITTER
        
        SAISISSEZ VOTRE REPONSE S'IL VOUS PLAIT
        ==> '''))
    except:
        print("ESSAYEZ DE SUIVRE L'INDICE S'IL VOUS PALIT.")
        print()
        continue
    
    
    if choix not in list_num: 
        print("ESSAYEZ DE RENTRER LE BON NUMERO DE VOTRE CHOIX")
        print()
        continue
    
    
    #LISTEZ
    if choix == 1:
        print()
        affiche = lists(connect)
        print("LES LISTES DES CONTACTS EXISTENT : \n")
        for liste in affiche : 
            print(f"ID : {liste[0]} \tNOM : {liste[1]}  \t\tNUMÉRO : {liste[2]} \t\tEMAIL : {liste[3]}")
        print()
        enc = "ok"
        qt = 1
        continue
    
    
    #RECHERCHEZ
    if choix == 2:
        print()
        name_search = input("ENTREZ ICI LE NOM QUE VOUS VOULEZ RECHERCHER :  ")
        search = search_one(connect, name_search.title())
        
        if len(search) == 0 :
            print(f"\n'LE NOM '{name_search}' N'EXISTE PAS DANS LE REPERTOIRE.\n")
            pose = input('''VOUS-VOULEZ :
            ANNULER la recherche
              ou 
            CONTINUER la recherche
        VOTRE REPONSE (annuler ou continuer)=> ''')
            if pose.lower() == "continuer":
                qt = ' a refaire '
                enc = 0
                continue
            if pose.lower() == "annuler" :
                qt = 1
                enc = "ok"
                print("\nVOTRE RECHERCHE EST ANNULÉ.\n")
                continue
            qt = 1
            enc = "ok"
            print("\nVOTRE RECHERCHE SERA ANNULÉ.\n")
            continue
        
        for affiche_cont in search:
            print(f"\nNOM : {affiche_cont[1]} \t\tNUMÉRO : {affiche_cont[2]} \t\tCOMPTE EMAIL : {affiche_cont[3]}")
        print()
        qt = 1
        enc = "ok" 
    
    #RECHERCHER UN NUM
    if choix == 3 : 
        print()
        qt = 1
        enc = "ok"
        try:
            num_search = int(input("VEUILLEZ ENTRER ICI LE NUMÉRO : "))
        except:
            print("\nVEUILLEZ ENTRER LE NUMÉRO EN NOMBRE S'IL VOUS PLAIT.\n")
            qt = 1
            enc = 0
            continue
        
        cherch_num = search_num(connect, num_search)
        if len(cherch_num) == 0 :
            print(f"\nLE NUMÉRO {num_search} N'EXISTE PAS DANS LE REPERTOIRE.\n")
            continue
        for p in cherch_num :
            print(f"\nNOM : {p[1]} \t\tNUMÉRO : {p[2]} \t\tCOMPTE EMAIL : {p[3]}\n")
        continue        
            
    
    #AJOUTEZ 
    if choix == 4:
        qt = 1
        enc = "ok"  
        print() 
        nom = input("-AJOUTEZ LE NOM : ")
        mail = input("-AJOUTEZ LE COMPTE EMAIL : ")
        numero_str = input("-AJOUTEZ LE NUMERO : ")
        print()
        try:
            numero = int(numero_str)
        except:
            print("IL FAUT METTRE EN NOMBRE LE NUMERO.\n")
            numero = ""
        
        if nom == "" or mail == "" or numero == "":
            print("\n REMPLISSEZ BIEN TOUS LES FORMULAIRES.\n")
            qt = 'a refaire'
            enc = 0
            continue
        
        demd = input('''VOULEZ-VOUS ENREGISTRER CE NOUVEAU CONTACT ?
            <Oui> ACCEPTER
               ou
            <Non> REFUSER
        VOTRE REPONSE => ''')
        
        if demd.lower() == "accepter" or demd.lower() == "oui" or demd.lower() == "o" : 
            ajouter(connect, nom.title(), numero, mail)
            print("\nLE NOUVEAU CONTACT EST ENREGISTRÉ.\n")
            continue
        
        if demd.lower() == "refuser" or demd.lower() == "non" :
            print("\nLE NOUVEAU CONTACT N'EST PAS ENREGISTRÉ.\n")
            print()
            continue
        print("\nL'ACTION SERA ANNULÉE\n")
        continue
      
      
    
    #SUPPRIMEZ
    if choix == 5:
        print()
        name_sup = input("ENTREZ ICI LE NOM QUE VOUS VOULEZ SUPPRIMER :  ")
        search = search_one(connect, name_sup.title())
        if len(search) == 0 :
            print(f"\nLE NOM '{name_sup.title()}' N'EXISTE PAS DANS LE REPERTOIRE.\n")
            que = input('''VOULEZ-VOUS :
            ANNULER
              ou 
            CONTINUER
        VOTRE REPONSE => ''')
            if que.lower() == "continuer":
                qt = ' a refaire '
                enc = 0
                continue
            if que.lower() == "annuler" :
                qt = 1
                enc = "ok"
                print("\nL'ACTION DE SUPPRIMER UN CONTACT EST ANNULÉE.\n")
                continue
            print()
            qt ="mdr"
            enc = "ok"
            continue
        
        for contact_aff in search :   
            print(f"\n NOM : {contact_aff[1]} \t\tNUMÉRO : {contact_aff[2]} \t\tCOMPTE EMAIL : {contact_aff[2]}\n")
        delette = input('''VOULEZ-VOUS VRAIMENT EFFACER CE CONTACT :
            <O> OUI 
                ou
            <N> NON 
        VOTRE REPONSE => ''')
        
        if delette.lower() == "o" or delette.lower() == "oui": 
            delete_contact(connect, name_sup.title())
            print("\nLE CONTACT EST EFFACÉ.\n")
            qt = 1
            enc = "ok"
            continue
        
        if delette.lower() == "n" or delette.lower() == "non":
            print("\nLE CONTACT N' EST PAS EFFACÉ.\n")
            qt = 1
            enc = "ok"
            continue
        
        print("SOYEZ INTELLIGENT(e) S'IL VOUS PLAIT.\n")
        qt = 'a refaire'
        enc = "ok"
        continue
    
    
    #MODIFIEZ
    if choix == 6 :
        print()
        contact_up = input("ENTREZ LE NOM À MODIFIER : ")
        contact_sear = search_one(connect, contact_up.title())
        if len(contact_sear) == 0 :
            print(f"\nLE NOM '{contact_up.title()}' N'EXISTE PAS DANS LE REPERTOIRE. \n") 
            qt = 1
            enc = "ok"
            continue
        for contact_aff in contact_sear:
            print(f"\nNOM : {contact_aff[1]} \t\tNUMÉRO : {contact_aff[2]} \t\t COMPTE EMAIL : {contact_aff[3]}\n")
        dmd = input('''VOULEZ-VOUS VRAIMENT MODIFIER CE CONTACT ?
        <O> OUI
           ou
        <N> NON
        VOTRE REPONSE => ''')
        print()
        if dmd.lower() == 'oui' or dmd.lower() == 'o' :
            NOM = input("- ENTREZ LE NOUVEAU NOM : ")
            EMAIL = input("- ENTREZ LE NOUVEAU COMPTE EMAIL : ")
            try:
                NUMERO = int(input("- ENTREZ LE NOUVEAU NUMERO : "))
            except:
                print("LE NUMERO DOIT EN NOMBRE.\n")
                NUMERO = ""
                
            if NOM == "" or EMAIL == "" or NUMERO == "" :
                print("VEUILLEZ REMPLIR LES FORMULAIRES.\n")
                qt = 'a refaire'
                enc = 0
                continue

            conf = input('''VOULEZ-VOUS :
        <C> CONFIRMER
              ou
        <A> ANNULER
        VOTRE REPONSE : ''')
            if conf.lower() == "c" or conf.lower() == "confirmer" : 
                update_contact(connect, NOM.title(), NUMERO, EMAIL, contact_up)
                print("\nLA MODIFICATION EST RÉUSSIE.\n")
                qt = 1
                enc = "ok"
                continue
            print("\nLA MODIFICAITON EST ANNULÉE.\n")
            qt = 1
            enc = "ok"
            continue
        print("\nLA MODIFICATION SERA ANNULÉE.\n")
        qt = 1
        enc = "ok"
        
        
    #SUPPRIMER TOUS:
    if choix == 7:
        print()
        conf = input('''VOULEZ-VOUS VRAIMENT EFFACER TOUS LES CONTACTS  :
        <O> OUI
            ou
        <N> NON
        VOTRE REPONSE => ''')
        
        if conf.lower() == "o" or conf.lower() == "oui" :
            cur.execute("DROP TABLE IF EXISTS repertoire") 
            connect.commit()
            print("\nLES CONTACTS SONT TOUS EFFACÉS.\n")   
            cur.execute(create_table)
            qt = 1
            enc = "ok"
            continue
        print("\nLA SUPPRESSION EST ANNULÉ.\n")
        qt = 1
        enc = "ok"
        
           
        
    #QUITTEZ
    if choix == 8:
        print()
        quitt = input('''VOULEZ-VOUS VRAIMENT QUITTER ?
            <O> OUI 
                ou
            <N> NON
        VOTRE REPONSE => ''')
        if quitt.upper() == 'O' or quitt.upper() == 'OUI' :
            print("\nAU REVOIR ET À BIENTOT !!! ")
            break
        
        if quitt.upper() == 'N' or quitt.upper() == 'NON' :
            print()
            print()
            qt = 1
            enc = "ok"
            continue
        
        print("SOYEZ INTELLIGENT(e) S'IL VOUS PLAIT. ")
        print()
        qt = 'revenir au question quitt'   



if connect is not None:
    connect.close()

