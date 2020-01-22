''' This program outputs the list of dir options for a function / model into a 
user friendly screen output'''
# FDDI-CentOS@

def printDir(command):
    command = str(command).lower()
    try:
        if command in list(dir(command)):
            bic = list(dir(command))
            for item in bic:
                print(item)
        else:
            var = input(f"{command.title()} command not found. Would you like to see a list of valid Built In Modules? (Y/N)")
            if var.lower() == 'y':
                bif = list(dir(__builtins__))
                for item in bif:
                    print(item)
            else:
                print("Have a great day!")
    except:
        var = input(f"{command.title()} command not found. Would you like to see a list of valid Built In Modules? (Y/N)")
        if var.lower() == 'y':
                bif = list(dir(__builtins__))
                for item in bif:
                    print(item)
        
if __name__ == '__main__':
    var = input("Enter a Python command: ")
    printDir(var)

    while True:
        flag = input("Would you like to check another command? (Y/N)")

        if flag.lower() == 'y':
            var = input("Enter a Python command: ")
            printDir(var)
        else:
            print("Have a great day!")
            break

