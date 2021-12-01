
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.core.mail import EmailMessage

import csv
from openpyxl import load_workbook
from openpyxl import Workbook
import xlsxwriter
import pandas as pd

def gen_email () :
    
    ff = pd.read_csv('sample_input/responses.csv')
    last_col = len(ff.columns)

    email_id = ''
    roll_no = ''

    with open('sample_input/responses.csv','r') as f:                                                                                              # iterating through all rows of names_roll to create our required dictionary
            response = csv.reader(f)
            correct_ans = {}
            cnt = 0
            for row in response :
                
                if cnt == 0 :
                    cnt += 1
                    continue
                
                email_id = row[4]
                roll_no = row[6] + '.xlsx'

                cnt += 1
                email = EmailMessage(
                    'Subject...',
                    'Main_body...',
                    'shreyacb48.saurabhee53@gmail.com',
                    [email_id]
                )
                path  = './marksheet/' + roll_no
                email.attach_file(path)
                email.send(fail_silently = False)
