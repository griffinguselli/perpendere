import sys
dictfile = {}

def dictionary(val):
    with open("dict.csv") as file:
        for line in file:
            dictkey, dictvalue = line.rstrip().split(",")
            dictfile[dictkey] = dictvalue
    try:
        return dictfile[val]
    except KeyError:
        print(f"'{val}' is not in the dictionary.")    
while True:
    try:
        index = int(sys.argv[1])
    except IndexError:
        print("Please input an argument for Index.")
        sys.exit ()
    else:
        if index == 0:
            try:
                value = sys.argv[2]
                break
            except IndexError:
                print("Input an argument for 'Value'")
                sys.exit()
        elif index == 1:
            try:
                value = sys.argv[2]
                meaning = sys.argv[3]
                break
            except IndexError:
                print("Input an argument for 'Value' or argument 'Meaning'")
                sys.exit()
        else:
            print("Index is not 0 or 1. 0 is 'search' and 1 is 'import'")
            sys.exit()
if index == 0:
    while True:
        try:
            print(dictionary(value))
                
            break
        except FileNotFoundError:
            open("dict.csv","x")
else:
    with open("dict.csv", "a") as file:
        file.write(f"{value},{meaning}\n")
