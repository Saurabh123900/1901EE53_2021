def output_by_subject():
    subject_set = {"uninitiated"}                                                #set for maintaining distinct subjects
    f_in = open("regtable_old.csv","r")                                          #File Reading
    column_headers = ["uninitiated","uninitiated","uninitiated","uninitiated"]   #Represents headers of each column.
    cnt = 0                                                                      #Represents current row in file
    for row in f_in :                                                            #loop for each row in given file
        elements = row.split(",")                                                #represents elements of a perticular row
        cur_subject = elements[3]
        if cnt == 0 :
            column_headers[0] = elements[0]                                      #giving values to column headers
            column_headers[1] = elements[1]
            column_headers[2] = elements[3]
            column_headers[3] = elements[8]
            cnt += 1
            continue

        path = "output_by_subject/" + cur_subject + ".csv"                       #assigning path for writing
        f_out = open(path,"a")                                                   #opening the file of the given path

        if (cur_subject in subject_set) == False :                               #if the subject appears 1st time
            cnt2 = 0                                                             #Represents index of column_header
            for headers in column_headers :
                f_out.write(headers)                                             #we write column headers at the begining of a file.
                cnt2 += 1
                if cnt2 != 4 :
                    f_out.write(",")
            subject_set.add(cur_subject)

        cur = 0                                                                  #represents index of elements of row
        for element in elements :
            if cur == 0 :
                f_out.write(elements[0])                                         #writting the reuired imformation
                f_out.write(",")
            if cur == 1 :
                f_out.write(elements[1])                                         #writting the reuired imformation
                f_out.write(",")
            if cur == 3 :
                f_out.write(elements[3])                                         #writting the reuired imformation
                f_out.write(",")
            if cur == 8 :
                f_out.write(elements[8])                                         #writting the reuired imformation
            cur += 1
        cnt += 1

    return

def output_individual_roll():
    rollno_set = {"uninitiated"}                                                #set for maintaining distinct Roll no
    f_in = open("regtable_old.csv","r")                                         #File Reading
    column_headers = ["uninitiated","uninitiated","uninitiated","uninitiated"]  #Represents headers of each column.
    cnt = 0                                                                     #Represents current row in file
    for row in f_in :                                                           #loop for each row in given file
        elements = row.split(",")                                               #represents elements of a perticular row
        cur_roll = elements[0]

        if cnt == 0 :
            column_headers[0] = elements[0]                                     #giving values to column headers
            column_headers[1] = elements[1]                                     #Represents index of column_header
            column_headers[2] = elements[3]
            column_headers[3] = elements[8]
            cnt += 1
            continue 

        path = "output_individual_roll/" + cur_roll + ".csv"                    #assigning path for writing
        f_out = open(path,"a")                                                  #opening the file of the given path

        if (cur_roll in rollno_set) == False :                                  #if the Roll No appears 1st time
            cnt2 = 0
            for headers in column_headers :                                     #we write column headers at the begining of a file.
                f_out.write(headers)
                cnt2 += 1
                if cnt2 != 4 :
                    f_out.write(",")
            rollno_set.add(cur_roll)

        cur = 0                                                                #represents index of elements of row
        for element in elements :
            if cur == 0 :
                f_out.write(elements[0])                                        #writting the reuired imformation
                f_out.write(",")
            if cur == 1 :
                f_out.write(elements[1])                                        #writting the reuired imformation
                f_out.write(",")
            if cur == 3 :
                f_out.write(elements[3])                                        #writting the reuired imformation
                f_out.write(",")
            if cur == 8 :
                f_out.write(elements[8])                                        #writting the reuired imformation
            cur += 1
    return
    
output_by_subject()                                                             #Function Call
output_individual_roll()                                                        #Function Call