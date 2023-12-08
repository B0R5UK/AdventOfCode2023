with open("input1.txt") as input:
    lines = input.readlines()
    sum = 0
    for line in lines:
        chars = list(line)
        first = 0
        last = 0
        
        for char in chars:

            if(char.isnumeric()):
                if(first == 0):
                    first = char
                else:
                    last = char
                
            if(last == 0):
                last=first


        print ("first :  " + first + " x = ",last)
        sum += int(first + last)

    print(sum)
                
        

