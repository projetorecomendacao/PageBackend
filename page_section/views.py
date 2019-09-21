from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

def testar(request):
    pageForm = PageForm()
    depressionForm = DepressionForm()
    depressionForm2 = DepressionForm2()
    cognitionDeficitForms = CognitionDeficitForms ()
    cognitionDeficitForms2 = CognitionDeficitForms2 ()
    negativeAttitudesAgingForms = NegativeAttitudesAgingForms ()
    negativeAttitudesAgingForms2 = NegativeAttitudesAgingForms2 ()
    psychologicalAspectsForm = PsychologicalAspectsForm()

    return render(request, 'teste.html', {'page': pageForm,'cognition1':cognitionDeficitForms,'cognition2':cognitionDeficitForms2,'depression1': depressionForm, 'depression2': depressionForm2, \
                                          'negative1': negativeAttitudesAgingForms, 'negative2': negativeAttitudesAgingForms2,'psychological': psychologicalAspectsForm})
