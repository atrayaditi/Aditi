from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from Base.models import Contact

# Home Page
def home(request):
    return render(request, 'home.html')

# About Page
def about(request):
    return render(request, 'about.html')

# Projects Page
def projects(request):
    return render(request, 'projects.html')

# Skills Page
def skills(request):
    return render(request, 'skills.html')



# Contact Page with form handling
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        number = request.POST.get('number', '').strip()
        content = request.POST.get('content', '').strip()

        # Validations
        if not name or len(name) < 2 or len(name) > 30:
            messages.error(request, 'Name must be between 2 and 30 characters.')
            return render(request, 'contact.html')

        if not email or len(email) < 5 or len(email) > 50:
            messages.error(request, 'Please enter a valid email.')
            return render(request, 'contact.html')

        if not number or not number.isdigit() or len(number) < 10 or len(number) > 12:
            messages.error(request, 'Please enter a valid phone number (10–12 digits).')
            return render(request, 'contact.html')

        if not content or len(content) < 5:
            messages.error(request, 'Message must be at least 5 characters long.')
            return render(request, 'contact.html')

        # Save to database
        Contact.objects.create(name=name, email=email, number=number, content=content)
        messages.success(request, 'Thank you for contacting me! Your message has been saved.')
        return redirect('contact')

    return render(request, 'contact.html')

