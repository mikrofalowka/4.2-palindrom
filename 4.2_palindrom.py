
def czy_to_palindrom(slowo):
    '''sprawdza czy dane slowo jest palindromem, 
    przyjmuje jeden argument typu string,
    zwaraca True kiedy slowo jest palindromem i False kiedy nie jest'''
    licznik = 0
    for i in range(len(slowo)):
        if slowo[i] == slowo[-i-1]:
            licznik +=1
    if licznik == len(slowo):
        return True
    else:
        return False

print(czy_to_palindrom("kajak"))
