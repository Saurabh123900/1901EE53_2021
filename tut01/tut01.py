cnt1 = 0                                         #Total meraki numbers
cnt2 = 0                                         #Total non meraci numbers

"""This will detect meraki numner"""
def meraki_helper(n):
    x = n
    global cnt1 , cnt2
    if n < 10 :                                     #if the number is less than 10 its a miraki numbers by defination
        cnt1 += 1                                   #incrementing meraki count
        print ("Yes -", n , "is a Meraki number")   
        return

    prev = x%10                                     #prev and cur represents adjacent digits 
    x //= 10
    flag = 1                                        #if flag is 1 it represents miraki number

    while x > 0 :                                   #for checking all adjacent pair of digits
        cur =  x%10
        x //= 10
        if abs(cur-prev) != 1 :                     #if defination of miraki violated
            flag = 0                                
            break
        else :
            prev = cur

    if flag == 1 :                                  # if its a miraki number
        print ("Yes-", n , "is a Meraki number")
        cnt1 += 1                                   #incrementing meraki count
    else :
        print ("No -", n , "is not a Meraki number") # if its not a miraki number
        cnt2 += 1                                    # incrementing non meraki count

input = [12, 14, 56, 1]                             #Can change the list for different inputs

for x in input :
    meraki_helper(x)                                #checking whether its a miraki number or not

#Printing the Total miraki and non miraki numbers
print ("The input list contains" , cnt1 , "meraki and" , cnt2 , "non meraki numbers.") 
