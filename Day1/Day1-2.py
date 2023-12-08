with open("input1.txt") as input:
    
  words = {'one': 1,
             'two': 2,
             'three': 3,
             'four': 4,
             'five': 5,
             'six': 6,
             'seven': 7,
             'eight': 8,
             'nine': 9}

    lines = input.readlines()
    sum = 0
    for line in lines:
        chars = list(line)
        first = 0
        last = 0
        buffer = ""
        for char in chars:
            buffer = buffer + char

            for word in words:
                if(word in buffer):
                    if(first == 0):
                        first = words[word]
                    else:
                        last = words[word]
                
                    buffer = buffer[-1] # ex. eightwo
                    break

            if(char.isnumeric()):
                if(first == 0):
                    first = char
                else:
                    last = char
                
        if(last == 0):
            last=first

        print (line + "first :  " + str(first) + " last = ",last)
        sum += int(str(first) + str(last))

    print(sum)
                
        

