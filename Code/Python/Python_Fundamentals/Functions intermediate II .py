
#2.
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

somelist= students
def iterateDictionary(somelist):

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
    for  dictionary in somelist:
        print(dictionary)
        for key, value in dictionary.items():
            print(f"{key}-{value}")
iterateDictionary(somelist)



#3.
def iterateDictionary2(key_name, some_list):

   

    for somevariable in somelist:
        print(somevariable[key_name])
        

iterateDictionary2('first_name', students)

#4 Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def itDictionary(someDictionary):
        for key, value in someDictionary.items:
            print(f'{len(value)} {key.upper()}')
            for someitem in value:
                print(someitem)

itDictionary(dojo)