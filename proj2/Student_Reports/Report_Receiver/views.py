from django.http import response
from django.shortcuts import render

from django.core.files.storage import FileSystemStorage 

from django.core.mail import send_mail

import back
import os
import glob


from django.shortcuts import render, redirect
#from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages


def index (request) :

    if request.method == 'POST':

        remove_files = glob.glob(os.path.join('output','*'))
        for f in remove_files :
            os.remove(f)

        remove_files = glob.glob(os.path.join('transcriptsIITP','*'))
        for f in remove_files :
            os.remove(f)
            
        if 'upload' in request.POST:
            remove_files = glob.glob(os.path.join('uploaded_sign','*'))
            for f in remove_files :
                os.remove(f)
            signature = request.FILES['sig']
            fs = FileSystemStorage()
            fs.save('signature.png', signature)

            seal = request.FILES['seal']
            fr = FileSystemStorage()
            fr.save('seal.jpg', seal)

        import back
        import back1
        import pdf3
        if 'submit1' in request.POST:
            sr = request.POST.get('sr')
            er = request.POST.get('er')
            back.generate_marksheet_range(request.POST.get('sr'),request.POST.get('er'))
            files = glob.glob(os.path.join('output','*'))
            invalid_roll = []
            srx = int(str(sr[6]+sr[7]))
            erx = int(str(er[6]+er[7]))
            prefix = sr[0] + sr[1] + sr[2] + sr[3] + sr[4] + sr[5]
            for i in range (srx,erx+1):
                file_name = os.path.join("output", prefix + str(i).zfill(2) + ".xlsx")
                if file_name not in files:
                    invalid_roll.append(file_name[7:15])
            pdf3.generate()
            msg = "Invalid roll numbers are : "
            ind = 0
            cnt = len(invalid_roll)
            cntt = 1
            for item in invalid_roll:
                ind = 1
                msg += str(item)
                if cntt != cnt :
                    msg += " , "
                cntt += 1
            if ind == 1:
                messages.info(request, msg)
                
        if 'submit2' in request.POST:
            back1.generate_marksheet()
            pdf3.generate()
            
    return render(request,'Report_Receiver/index.html')


