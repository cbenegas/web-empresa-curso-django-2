from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            # Suponemos que todo salio bien, redireccionamos
            #return redirect('/contact/?ok')

            # Enviamos el correo y redireccionamos
            """
            EmailMessaje(
                asunto,
                cuerpo,
                email_origen,
                email_destino,
                repty_to=[email]
            )
            """
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["benegascristian@gmail.com"],
                reply_to=[email]
            )

            try:
                email.send()
                # Todo ha salido bien, redireccionamos a OK
                return redirect(reverse('contact')+"?ok")
            except:
                #Algo no ha ido bien, redirecicinamos a FAIL
                return redirect(reverse('contact')+"?fail")

    return render(request, 'contact/contact.html', {'form':contact_form})