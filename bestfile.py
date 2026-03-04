while True:
    wa = input("what's your favourite number?")
    try:
        wa = int(wa)
    except ValueError:
        print("be better")
    if wa == 25:
        print("correct")
    else:
        print("wrong")
