#turns a list into a string with commas between items and 'and' before the final item
#works with lists that have mixed data types
def listToString (list):
    newString = ''

    #for loop that iterates through full length of 'list'
    for i in range(len(list)):

        #check to see if i is on last element in list and applies 'and' formatting
        if i == len(list) - 1:
            newString += 'and ' + str(list[i])
            
        #applies comma formatting to all other items
        else:
            newString += str(list[i]) + ', '
        
    return newString 
    


#testing
spam = [1, 2, 'butts', 'glue', 6, 7, 8.0]
print(listToString(spam))
