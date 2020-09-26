from django.forms.models import modelformset_factory

from .models import Company, AdditionalOffice, Cabinet, Collaborator


CompanyFormSet = modelformset_factory(Company, fields=('name', 'adress'), can_delete=True)
AdditionalOfficeFormSet = modelformset_factory(AdditionalOffice, fields=('company', 'name', 'adress'),
                                               can_delete=True)
CabinetFormSet = modelformset_factory(Cabinet, fields=('additional_office', 'floor', 'number'),
                                      can_delete=True)
CollaboratorFormSet = modelformset_factory(Collaborator, fields=('user', 'cabinet', 'full_name',
                                                                 'position'), can_delete=True)
