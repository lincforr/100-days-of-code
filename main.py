from replit import clear
pick = input("type 1 if you would like to do hangman type 2 if you would like to do calculator press 3 if you would like to do an auction type 4 if you want to encode some text in saesar cipher, or if you want to play black jack type 5: ")

if pick == "1":
    print("loading ...")
    from hangman import hang_man
    clear()
    hang_man()
elif pick == "2":
    print("loading ...")
    from calculator import calculator
    clear()
    calculator()
elif pick == "3":
    print("loading ...")
    from blind_auction import auction
    clear()
    auction()
elif pick == "4":
    print("loading ...")
    from cipher import cipher
    clear()
    cipher()
elif pick == "5":
    print("loading ...")
    from black_jack import black_jack
    clear()
    black_jack()