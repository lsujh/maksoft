from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .formset import  CompanyFormSet, AdditionalOfficeFormSet, CabinetFormSet, CollaboratorFormSet


@login_required
def company_view(request):
    if request.method == 'POST':
        formset = CompanyFormSet(request.POST)
        if formset.is_valid():
            formset.save()
    else:
        formset = CompanyFormSet
    return render(request, 'company.html', {'formset': formset})

@login_required
def additional_office_view(request):
    if request.method == 'POST':
        formset = AdditionalOfficeFormSet(request.POST)
        print(formset.errors)
        if formset.is_valid():
            formset.save()
    else:
        formset = AdditionalOfficeFormSet()
    return render(request, 'additional_office.html', {'formset': formset})

@login_required
def cabinet_view(request):
    if request.method == 'POST':
        formset = CabinetFormSet(request.POST)
        if formset.is_valid():
            formset.save()
    else:
        formset = CabinetFormSet
    return render(request, 'cabinet.html', {'formset': formset})

@login_required
def collaborator_view(request):
    if request.method == 'POST':
        formset = CollaboratorFormSet(request.POST)
        if formset.is_valid():
            formset.save()
    else:
        formset = CollaboratorFormSet()
    return render(request, 'collaborator.html', {'formset': formset})

@login_required
def menu(request):
    return render(request, 'menu.html')



