from django.shortcuts import render, redirect, get_object_or_404
from .models import Roles
from .form import RoleCreate

from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
from xhtml2pdf import pisa

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
            role.etats = 'ENCOURS' 
            # role.created_by = request.user
           
            role.save()
            
            return redirect('home')
    else:
        form = RoleCreate()

    return render(request, 'roles/create.html', {'form': form})


def roleUpdate(request, role_id):
    role = Roles.objects.get(id=role_id)

    if request.method == 'POST':
        form = RoleCreate(request.POST, request.FILES, instance=role)
        if form.is_valid():
            # role.modified_by = request.user  # Enregistrer l'utilisateur actuel comme modificateur
            form.save()
            return redirect('home')
    else:
        form = RoleCreate(instance=role)
    
    return render(request, 'roles/update.html', {'form': form, 'role': role})

def delete(request, role_id):
    role = get_object_or_404(Roles, id=role_id)
    if request.method == 'POST':
        
        role.delete()
        return redirect('confirm_delete')
    return render(request, 'roles/delete.html', {'role': role})


def confirm_delete(request):
    return render(request, 'roles/confirm_delete.html')




def role_detail(request, role_id):
    role = get_object_or_404(Roles, id=role_id)
    context = {'role': role}
    return render(request, 'roles/detail.html', context)


def print_document(request, role_id):
    # Récupérer les données pour le document à partir de la base de données ou d'autres sources
    data_print = Roles.objects.get(id=role_id)

    # Charger le modèle HTML pour le document
    template = 'report.html'

    # Créer le contexte avec les données à passer au modèle
    context = {
        'data_print': data_print
    }

    # Rendre le modèle HTML avec le contexte
    html = render_to_string(template, context)

    # Créer un document PDF à partir du modèle HTML
    pdf_file = BytesIO()
    pisa.CreatePDF(html, dest=pdf_file)
    

    # Retourner le document PDF comme une réponse HTTP
    response = HttpResponse(pdf_file.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="document.pdf"'
    return response


