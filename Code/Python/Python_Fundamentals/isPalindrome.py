def isPalindrone(isString):
        newString=''
        for i in range (len(isString)-1, -1, -1):
            newString+= isString[i]
        if isString == newString:
            print(true)
            return true
            
        else:
            print(false)
            return false




testList=[37, 2, 1, 9]

def reverseList(list):
    list= list[::-1]
    print(list)
    return list

print (reverseList(testList))







            



isPalindrone(isString)