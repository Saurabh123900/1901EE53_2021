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

        

        import back
        import back1
        import pdf3
        if 'submit1' in request.POST:
            print(request.POST.get('sr'),request.POST.get('er'))
            back.generate_marksheet_range(request.POST.get('sr'),request.POST.get('er'))
            pdf3.generate()
        if 'submit2' in request.POST:
            back1.generate_marksheet()
            pdf3.generate()
            
    return render(request,'Report_Receiver/index.html')

