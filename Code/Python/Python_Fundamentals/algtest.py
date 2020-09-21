word = "Democratic Republic Of Congo"
def abbrev(input):
    temp = ""
    temp = input[0]
    

    for i in range (0, len(input), 1):
        
        if input[i] == " ":
            temp += input[i+1]
            temp = input.upper()    
    return temp


print(abbrev(word))
    


