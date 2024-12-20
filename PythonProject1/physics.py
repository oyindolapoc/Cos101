print("Welcome To COS 101")
print("Name: ADEONIGBAGBE OYINDOLAPO CHARLES")
print("Matric Number: BHU/24/04/09/0003")

def a():
    v = float(input("Enter Velocity: "))
    t = float(input("Enter Time: "))
    output = str(v * t)
    print("Acceleration: " +output+"m/s^2")

def b():
    d = float(input("Enter Distance: "))
    t = float(input("Enter Time: "))
    output = str(d * t)
    print("Speed: " +output+"m/s")

def c():
    f = float(input("Enter Force: "))
    d = float(input("Enter Distance: "))
    output = str(f * d)
    print("Work: " +output+"J")

def d():
    c = float(input("Enter Charge: "))
    t = float(input("Enter Time: "))
    output = str(c * t)
    print("Current: " +output+"A")

def e():
    w = float(input("Enter Work: "))
    t = float(input("Enter Time: "))
    output = str(w * t)
    print("Energy: " +output+"J")

def main():
        user_choice = input("Enter Operation")

        if user_choice == 'a':
            a()
        elif user_choice == 'b':
            b()
        elif user_choice == 'c':
            c()
        elif user_choice == 'd':
            d()
        elif user_choice == 'e':
            e()

if __name__ == '__main__':
    main()