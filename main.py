
pick = input("type 1 if you would like to do hangman type 2 if you would like to do calculator press 3 if you would like to do an auction type 4 if you want to  encode some text in saesar cipher: ")

if pick == "1":
    from hangman import hang_man
    hang_man()
elif pick == "2":
    from calculator import calculator
    calculator()
elif pick == "3":
    from blind_auction import auction
    auction()
elif pick == "4":
    from cipher import cipher
    cipher()
