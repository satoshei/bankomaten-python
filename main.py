user = {
    "balance": 0,
    "account": " "
}

inlogged = False
is_quit = False

print("---------------")
print("***HUVUDMENY***")
print("---------------")

print("1. Skapa konto")
print("2. Adminstrera konto")
print("3. Avsluta")
while True:
    cmd = input("Ange menyval > ")

    if cmd == "1":
        account = input("Ange kontonummer > ")
        user["account"] = account
    elif user["account"] == user[" "]:
        print("ERROR: Kontonummer finns redan, försök med nytt kontonummer")
        input("Tryck enter för att komma tillbaka till meny!")
    
    elif cmd == "2":
        account = input("Ange kontonummer > ")
        if account not in user:
            print("ERROR: Konto finns ej, försök igen")
            input("Tryck enter för att komma tillbaka till meny!")
    
    elif cmd == "3":
        print("***KONTOMENY***", "- Konto: ",user[" "])
        print("1. Ta ut pengar")
        print("2. Sätt in pengar")
        print("3. Visa saldo")
        print("4. Avsluta")

        cmd = input("Ange menyval > ")

        #w_amount = ta ut pengar variabel
        #d_amocunt = sätt in pengar variabel


        if cmd == "1":
            def withdraw_money():
                try:
                    w_amount = int(input("Hur mycket pengar vill du ta ut?"))
                    if w_amount > user["balance"]:
                        print("Medges ej!")
                    else:
                        user["balance"] = user["balance"] - w_amount
                        print(f'{w_amount} har tagits ut från ditt konto: {account}, du har totalt {user["balance"]}') 
                        print("")
                except:
                    print("Var snäll och ange ett nummer för uttag")

        elif cmd == "2":
            def deposit_money():
                try:
                    d_amount = int(input("Hur mycket pengar vill du lägga till: "))
                    user["balance"] = user["balance"] + d_amount
                    print(f'{d_amount} har suttits in i ditt konto: {account}, du har totalt {user["balance"]}')
                    print("")
                except:
                    print("Var snäll och ange ett nummer för insättning")
        
        elif cmd == "3":
            def s_balance():
                print(f'Ditt saldo är {user["balance"]}')
                print("")
        
        elif cmd == "4":
            print("Nu avslutas bankomat ärendet, du loggas ut inom 2 sekunder")
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("Tack och Hejdå")
            exit()

    else:
        print("ERROR: Ej valbart alternativ")
        input("Tryck enter för att försöka igen")   
