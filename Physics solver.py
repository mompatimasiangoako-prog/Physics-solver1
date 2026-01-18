
option = str(input("Enter which solver would you like: Force, Kinetic Energy"));

option = option.strip().lower();

if option == "force":
    mass = int(input("Enter a mass"));
    acc = int(input("Enter the acceleration"))
    Force = mass * acc;
    print("The force is", Force);
    
if option == "kinetic energy":
    mass1 = int(input("Enter a mass"));
    velocity = int(input("enter the velocity"));
    KE = (mass1 * velocity) / 2;
    print("The kinetic energy is:", KE);
    
