from django.shortcuts import render
from .forms import ContactForm
from .models import contactDetails


def showform(request):
    print("hiiiii")
    print(request)
    if request.method == 'GET':
        try:
            request.GET['name']
            print('ada1')
            print(request.GET['name'])
            form = contactDetails()
            form.firstname = request.GET['name']
            form.email = request.GET['email']
            form.subject = request.GET['subject']
            form.comment = request.GET['comment']
            form.save()

            return render(request, 'contact.html')
        except:
            return render(request, 'contact.html')

    else:
        print('ada2')
        return render(request,'contact.html')
# def contact(request):
#    return render(request,'contact.html')
