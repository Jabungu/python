x = 5

def countdown(x): 
# function accepts number as input, and returns a new list of that numbers countdown from x to 0
    
    for x in range (x, -1, -1):
    
        print(x)
        y= []
        y.append(x)
        print(y)
        return y
    
countdown(5)

#Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel

def iterateDictionary(someList):
    for s in somelist: 
        print (dictionary)
        for key, value in dictionary.items():
            print(f"{key} - {value}")


#Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
#Michael
#John
#Mark
#KB
#And iterateDictionary2('last_name', students) should output:
#Jordan
#Rosales
#Guillen
#Tonel


       


