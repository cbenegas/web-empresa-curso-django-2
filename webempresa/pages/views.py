from django.shortcuts import render, get_object_or_404
from .models import Pages
# Create your views here.

def page(request, page_id):
    page = get_object_or_404(Pages, id=page_id)
    return render(request, 'pages/sample.html', {'page':page})
