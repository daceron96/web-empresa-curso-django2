from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

def contact(request):
    contact_form = ContactForm
    
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid:
            name = request.POST.get('name',"")
            email = request.POST.get('email',"")
            content = request.POST.get('content',"")
            #enviamos el correo y redireccionamos
            mail = EmailMessage(
                "La Caffetiera: Nuevo mensaje de contacto",
                "De:{} <{}>\n\nEscribio:\n\n{}".format(name,email,content),
                "no-contestar@inbox.mailtrap.io",
                ['datutalcha3@misena.edu.co'],
                reply_to=[email]
            )
            try:
                mail.send()
                return redirect(reverse('contact')+"?ok")
            except:
                #algo no ha ido bien redireccionamos a fail
                return redirect(reverse('contact')+"?fail")

            
    return render(request,'contact/contact.html',{'form':contact_form})
