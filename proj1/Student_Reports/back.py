import csv
from openpyxl import load_workbook
from openpyxl import Workbook
import xlsxwriter
import pandas as pd

def gen_master_roll (cm = 0, nm = 0) :
    ff = pd.read_csv('sample_input/responses.csv')
    last_col = len(ff.columns)

    with open('sample_input/responses.csv','r') as f:                                                                                              # iterating through all rows of names_roll to create our required dictionary
            response = csv.reader(f)
            correct_ans = {}
            cnt = 0
            for row in response :

                if cnt == 0:
                    cnt += 1
                    continue
                
                if cnt == 1:
                    for i in range(7,last_col):
                        correct_ans[i] = row[i]
                
                file_name = 'marksheet/' + row[6] + '.xlsx'
                wb = xlsxwriter.Workbook(file_name)

                red = wb.add_format({'font_color': 'red'})
                green = wb.add_format({'font_color': 'green'})
                blue = wb.add_format({'font_color': 'blue'})

                bcenter = wb.add_format({'font_color' : 'blue'})
                bcenter.set_align('center')

                rcenter = wb.add_format({'font_color' : 'red'})
                rcenter.set_align('center')

                gcenter = wb.add_format({'font_color' : 'green'})
                gcenter.set_align('center')

                center = wb.add_format()
                center.set_align('center')

                centerb = wb.add_format()
                centerb.set_bold()
                centerb.set_align('center')

                right = wb.add_format()
                right.set_align('right')

                rightb = wb.add_format()
                rightb.set_bold()
                rightb.set_align('right')

                left = wb.add_format()
                left.set_align('left')

                leftb = wb.add_format()
                leftb.set_bold()
                leftb.set_align('left')

                underline = wb.add_format()
                underline.set_underline()

                underlineb = wb.add_format()
                underlineb.set_bold()
                underlineb.set_align('center')
                underlineb.set_underline()

                bold = wb.add_format({'bold': True})
                worksheet = wb.add_worksheet()

                cell_format = wb.add_format()
                cell_format.set_font_size(30)
                cell_format.set_underline()

                worksheet.write('A5', 'Marksheet', underlineb)
                worksheet.insert_image('A1', 'IITP_logo.jpg')

                worksheet.write('A6', 'Name:', right)
                worksheet.write('A7', 'Roll Number:', right)
                worksheet.write('D6', 'Exam:', right)
                worksheet.write('E6', 'quiz',leftb)

                worksheet.write('A10', 'No.', centerb)
                worksheet.write('A11', 'Marking', centerb)
                worksheet.write('A12', 'Total',  centerb)
                worksheet.write('B9', 'Right', centerb)
                worksheet.write('C9', 'Wrong', centerb)
                worksheet.write('D9', 'Not Attempt',  centerb)
                worksheet.write('E9', 'Max', centerb)
                worksheet.write('A15', 'Student Ans', centerb)
                worksheet.write('B15', 'Correct Ans', centerb)
                
                worksheet.write('B6', row[3], leftb)
                worksheet.write('B7', row[6], leftb)

                marks_c = 0
                marks_n = 0
                x = 0
                na = 0
                
                #print (last_col)

                for i in range(7,last_col) :
                    y = i + 8
                    worksheet.write(y,1,correct_ans[i],bcenter)
                    if row[i] == "" :
                        na += 1
                        continue
                    if correct_ans[i] == row[i] :
                        worksheet.write(y,0,row[i],gcenter)
                        marks_c += cm
                    else :
                        worksheet.write(y,0,row[i],rcenter)
                        marks_n += nm


                # print (marks_c)
                # print (marks_n)

                worksheet.write('B10' , int(marks_c//cm) , gcenter )
                worksheet.write('C10', int(marks_n//nm) , rcenter)
                worksheet.write('D10', na, center)
                worksheet.write('D11', 0, center)
                worksheet.write('B11', cm , gcenter)
                worksheet.write('C11', nm , rcenter)
                worksheet.write('B12', marks_c , gcenter)
                worksheet.write('C12', marks_n , rcenter)
                worksheet.write('E10', last_col - 7, center )
                worksheet.write('E12', str(marks_c + marks_n) + "/" + str((last_col - 7)*cm) , bcenter)

                wb.close() 
                cnt += 1


