def main():

    state = "Practica els problemes de list comprehensions per a ser més Pythonic!"
    resultat = [i for i in state.split() if len(i) < 6]
    print(resultat)


if __name__ == '__main__':
    main()
