import csv
from openpyxl import load_workbook
from openpyxl import Workbook
import xlsxwriter
import pandas as pd

def gen_concisee_marksheet(cm = 0, nm = 0) :
    ff = pd.read_csv('sample_input/responses.csv')
    last_col = len(ff.columns)

    file_name = 'marksheet/' + 'concise_marksheet' + '.xlsx'
    wb = xlsxwriter.Workbook(file_name)
    worksheet = wb.add_worksheet()


    with open('sample_input/responses.csv','r') as f:                                                                                              # iterating through all rows of names_roll to create our required dictionary
            response = csv.reader(f)
            correct_ans = {}
            cnt = 0
            for row in response :

                if cnt == 0:
                    for i in range (0,6) :
                        worksheet.write(cnt, i, row[i])
                
                    worksheet.write(cnt, 6, 'Score_After_Negative')
                    worksheet.write(cnt, 2, 'Google_Score')
                    worksheet.write(cnt, 7, 'Roll_Number')


                    for i in range (7,last_col) :
                        s1 = 'Unnamed: ' + str(i)
                        worksheet.write(cnt, i+1, s1)
                    worksheet.write(cnt, last_col+1, 'statusAns')
                    cnt += 1
                    continue
                
                if cnt == 1:
                    for i in range(7,last_col):
                        correct_ans[i] = row[i]

                cell_format = wb.add_format()
                cell_format.set_font_size(30)
                cell_format.set_underline()

                marks_c = 0
                marks_n = 0
                x = 0
                na = 0

                for i in range(7,last_col) :
                    if row[i] == "" :
                        na += 1
                        continue
                    if correct_ans[i] == row[i] :
                        marks_c += cm
                    else :
                        marks_n += nm

                for i in range (0,6) :
                    worksheet.write(cnt, i, row[i])
                
                tot_marks = (na + (marks_c // cm) + (marks_n // nm) ) * cm
                s2 = str(marks_c + marks_n) + '/' + str(tot_marks)
                worksheet.write(cnt, 6, s2)
                
                for i in range (6,last_col) :
                    worksheet.write(cnt, i+1, row[i])
                
                s3 = '[' + str(marks_c//cm) + ',' + str(marks_n//nm) + ',' + str(na) + ']'
                worksheet.write(cnt, last_col+1, s3)

                cnt += 1

            wb.close() 
                
gen_concisee_marksheet(5,-1)
