#!/usr/bin/python3
from os import system
while True:
    system("clear")
    print("Hey John what do you want to do?")
    print("1) install one or more python3 library.")
    print("2) use python interpreter on terminal.")
    print("3) nothing, exit choice.\n\n")
    print("=======================")
    print("===  BONUS OPTIONS  ===")
    print("=======================\n")
    print("4) you want PING an ip or domain name(like an server or website).")
    print("5) DDOS (type of DDOS: SYN requests flooding) with hping3.")
    print("6) navigate secretly on internet from the position \n\tof this service with elinks in TUI mode.")
    choice = str(input("choice ?: "))
    if choice == "1":
        libs_ = input("library name(s), space separated: ")
        system("python3 -m pip install {l}".format(
            l = libs_
            ))
    elif choice == "2":
        system("python3")
    elif choice == "3":
        break
    elif choice == "4":
        ping_ = input("domain name or ip: ")
        system("ping {p}".format(
            p = ping_
            ))
    elif choice == 5:
        pass
    elif choice == 6:
        pass

exit(0)
