def get_memory_score():
    
    memmory = []                                        #memmory of the game
    
    freq = []                                           #represents occurance of elements in memmory
    
    for x in range (11):
        freq.append(0)                                  #initially memmory is empty so all of them would be 0
    
    score = 0                                           #score of the game
    
    for x in input_nums:
        if freq[x]>0:                                   #if element is present
            score += 1                                  #increment of score acc to the rules
        else :
            if len(memmory)==5 :                        #if memmory size is full
                freq[memmory[0]] -= 1                   #we remove the first element because it is the oldest
                memmory.pop(0)
                memmory.append(x)                       #we append current element at the end of list
                freq[x] += 1                            #increment the freq of x
            else :                                      #if memmory not filled
                memmory.append(x)                       #we append current element at the end of list
                freq[x] += 1                            #increment the freq of x
    
    print ("Score:", score)                             #end of game and we print score
    
    return

input_nums =   [3, 4, 1, 6, 3, 3, 9, 0, 0, 0]          #input 

flag = 1                                                #represents whether the list is valid or not 
invalid = []                                            #list of invalid inputs

for x in input_nums :                                   #checking the validity of list
    if isinstance(x,int) == True :                      #checks whether the number is integer or not
        if x > 10 :                                     #checks whether the number is less than 10 or not
            flag=0
            invalid.append(x)
    else :
        flag=0
        invalid.append(x)
        
if flag == 1 :                                          #if the list is valid we play the game
    get_memory_score()
else :                                                  #else we print the invalid elements
    print("Please enter a valid input list . Invalid inputs detected:",invalid)