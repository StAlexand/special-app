while True:
    c = input("Vvedite operaciu (+ - *):")
    n = int(input("Skolko bydet operandov?"))
    rez = 0
    ymnojenie = 1
    if c == "+":
        for i in range(1, n + 1):
            print("Vvedite operand {0}:".format(i), end='')
            a = int(input())
            rez += a
        print("Rezyltat:", rez)
    elif c == "-":
        for i in range(1, n + 1):
            print("Vvedite operand {0}:".format(i), end='')
            a = int(input())
            if i == 0:
                rez -= a
            else:
                rez -= a
        print("Rezyltat:", rez)
    elif c == "*":
        for i in range(1, n + 1):
            print("Vvedite operand {0}:".format(i), end='')
            a = int(input())
            ymnojenie *= a
        print("Rezyltat:", ymnojenie)
    else:
        print("Neverno vibrana operaciya, povtorite vvod")
