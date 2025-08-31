print("="*100)

print("\nwelcome \ (^ __^) / !! This program creates a triangular pattern using stars with the help of input from the user.")
print("="*100)

print("1. left angled triangle")
print("2. right angled triangle")
print("3. pyramid")
print("4. Inverse pyramid")
print("5. Quit")
print("="*100)

    
choice= int(input("What type of pattern would you like to create: "))
if choice==1:
          lines= int(input("Enter how many lines long you want your left triangle to be: "))
          for i in range(1,lines+1):
             print("*"*i)

elif choice==2:
          lines= int(input("Enter how many lines long you want your right triangle to be: "))
          for i in range(1,lines+1):
             print("  " * (lines-i) + "* " * i)

elif choice==3:
          lines= int(input("Enter how many lines long you want your pyramid to be: "))
          for i in range(1, lines+1):
                    print("  " * (lines-i) + "* " * (2*i-1))

elif choice==4:
            lines= int(input("Enter how many lines long you want your reverse pyramid to be: "))
            for i in range(lines, 0, -1):
                    print("  " * (lines-i) + "* " * (2*i-1))

elif choice==5:
            print("Goodbye! thank you for playing this game")


           

    






    

    

      
