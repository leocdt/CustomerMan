import os
green = '\033[92m'
white = '\033[0m'
red = '\033[91m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_mainMenu():
    clear()
    choice : str
    print(green +"                                    ████████████████████████████████████████████████████████████")
    print("                                    ██                       CustomerMan                      ██")       
    print("                                    ██════════════════════════════════════════════════════════██")
    print("                                    ██                                                        ██")
    print("                                    ██                 [1] - Get current clients              ██")
    print("                                    ██                 [2] - add a client                     ██")
    print("                                    ██                 [3] - update a client                  ██")
    print("                                    ██                 [4] - get a clientid                   ██")
    print("                                    ██                 [5] - delete a client                  ██")
    print("                                    ██                 [6] - get client informations          ██")
    print("                                    ██                 [7] - quit                             ██")
    print("                                    ██                                                        ██")
    print("                                    ████████████████████████████████████████████████████████████" + white)
    choice = ""
    while choice not in ['1','2','3','4','5','6','7']:
        choice = input("Enter your choice : ")
    return choice