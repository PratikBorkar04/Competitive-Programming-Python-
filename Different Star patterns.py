#program to print different star patterns
while True:
    # Input number of rows
    num=int(input("Enter number of rows\t"))
    print("Different Star patterns:-")
    print("1:-Square")
    print("2:-Right angle Triangle ")
    print("3:-An Equilateral Triangle")
    print("4:-Water Reflection of An Equilateral Triangle")
    print("5:-Real image [+] Water Reflection of An Equilateral Triangle")
    print("6:---EXIT---")
    # Enter your choice
    choice=int(input("Enter your choice\t"))
    if choice == 1:
        for i in range(1,num+1):
            print(" * "*num)
    elif choice == 2:
        for i in range(1,num+1):
            print(" * "*i)
    elif choice == 3:
        for i in range(1,num+1):
            print(" "*(num-i)+("* ")*i)
    elif choice == 4:
        for i in range(num,0,-1):
            print(" "*(num-i)+("* ")*i)
    elif choice == 5:
        for i in range(1,num+1):
            print(" "*(num-i)+"* "*i)
        for i in range(num,0,-1):
            print(" "*(num-i)+"* "*i)
    #break statement use to exit from the loop
    elif choice == 6:
        break
    else:
        print("** Invalid Input **")
        print("\n")


