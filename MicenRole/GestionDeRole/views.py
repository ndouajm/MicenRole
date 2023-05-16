from django.shortcuts import render, redirect, get_object_or_404
from .models import Roles
from .form import RoleCreate

from django.http import HttpResponse
from django.template.loader import get_template
from reportlab.pdfgen import canvas
from io import BytesIO


def index(request):
    
    
    roles = Roles.objects.all()
    
    context = {'roles': roles}
    
    return render(request, 'index.html', context)


def roleCreate(request):
    newRole = Roles.objects.create(**request.POST.dict())
    return render(request, 'roles/create.html')


def roleCreate(request):
    if request.method == 'POST':
        form = RoleCreate(request.POST, request.FILES)
        if form.is_valid():
            role = form.save(commit=False)
            role.save()
            
            return redirect('home')
    else:
        form = RoleCreate()
        
    return render(request, 'roles/create.html', {'form': form})

# def role_detail(request, role_id):
#     roles = get_object_or_404(Roles, id=role_id)
    

#     return render(request, 'roles/detail.html', {'role': Roles})

def role_detail(request, role_id):
    role = get_object_or_404(Roles, id=role_id)
    context = {'role': role}
    return render(request, 'roles/detail.html', context)






def print_document(request):
    # Récupérer les données pour le document à partir de la base de données ou d'autres sources
    
    context = {
        'name': 'John Doe',
        'address': '123 Main Street',
        'city': 'Anytown',
        'state': 'CA',
        'zip': '12345',
    }
    # Charger le modèle HTML pour le document
    template = get_template('report.html')
    html = template.render(context)

    # Créer un document PDF à partir du modèle HTML
    pdf_file = BytesIO()
    p = canvas.Canvas(pdf_file)
    p.drawString(100, 750, "Hello world.")
    p.drawString(100, 700, "Name: %s" % context['name'])
    p.drawString(100, 650, "Address: %s" % context['address'])
    p.drawString(100, 600, "City: %s" % context['city'])
    p.drawString(100, 550, "State: %s" % context['state'])
    p.drawString(100, 500, "Zip: %s" % context['zip'])
    p.showPage()
    p.save()

    # Retourner le document PDF comme une réponse HTTP
    response = HttpResponse(pdf_file.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="document.pdf"'
    return response



# def roleCreate(request):
#     nom = request.POST.get('nom_document'),
#     date_conseil= request.POST.get('date_conseil'),
#     objet=request.POST.get('objet'),
#     economie=request.POST.get('economie'),
#     recommandation=request.POST.get('recommandation'),
#     observation_ct=request.POST.get('observation_ct'),
#     order_jour=request.POST.get('order_jour')
    
#     newRole = Documents.objects.create(
#         nom = nom,
#         date_conseil = date_conseil,
#         objet = objet,
#         economie = economie,
#         recommandation = recommandation,
#         observation_ct = observation_ct,
#         order_jour = order_jour
#     )
#     newRole.save()
#     return render(request, 'roles/create.html')