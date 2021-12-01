from django.http import response
from django.shortcuts import render

from django.core.files.storage import FileSystemStorage 

from django.core.mail import send_mail

#import back
#import back2
import os
import glob

def index (request) :
    if request.method == 'POST':

        remove_files = glob.glob(os.path.join('sample_input','*'))
        for f in remove_files :
            os.remove(f)

        master_roll = request.FILES['myfile']
        fs = FileSystemStorage()
        fs.save('master_roll.csv', master_roll)

        responses = request.FILES['response']
        fr = FileSystemStorage()
        fr.save('responses.csv', responses)

        import back
        import back2
        import back3

        if 'submit1' in request.POST:
            back.gen_master_roll(int(request.POST.get('cm')),int(request.POST.get('nm')))
        elif 'submit2' in request.POST:
            back2.gen_concisee_marksheet(int(request.POST.get('cm')),int(request.POST.get('nm')))
        elif 'submit3' in request.POST:
            back3.gen_email()

    return render(request,'Report_Receiver/index.html')

