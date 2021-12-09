def main():
    state = "Practica els problemes de list comprehensions per a ser més Pythonic!"
    resultat = [i for i in state if i in 'aeiouyAEIOUYé']
    print("N'hi ha", len(resultat), "espais.")


if __name__ == '__main__':
    main()
