# Create your views here.
from mysite.zapocty.models import Student,Predmet,Zapocet
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from zapocty.form import StudentForm,PredmetForm,ZapocetForm
from django.core.urlresolvers import reverse

# INDEX
def index(request):
    return render_to_response('index.html')
def studenti(request):
	studenti = Student.objects.all()
	return render_to_response('studenti.html',{'studenti':studenti})

def studentEdit(request,student_id):
	student = get_object_or_404(Student,pk = student_id)
	if request.method == "POST":
		form = StudentForm(request.POST,instance = student)
		if form.is_valid():
			form.save()
	else:
		form = StudentForm(instance = student)
	return render_to_response('studentedit.html',{'form':form})

def studentAdd(request):
	form = StudentForm()
	if request.method =="POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/studenti/')
	return render_to_response('studentadd.html',{'form':form})

def predmety(request):
	predmety = Predmet.objects.all()
	return render_to_response('predmety.html',{'predmety':predmety})

def predmetEdit(request,predmet_id):
	predmet = get_object_or_404(Predmet,pk = predmet_id)
	if request.method == "POST":
		form = PredmetForm(request.POST,instance = predmet)
		if form.is_valid():
			form.save()
	else:
		form = PredmetForm(instance = predmet)
	return render_to_response('predmetedit.html',{'form':form})

def zapocty(request):
	zapocty = Zapocet.objects.all()
	return render_to_response('zapocty.html',{'zapocty':zapocty})

def zapocetEdit(request,zapocet_id):
	zapocet = get_object_or_404(Zapocet,pk = zapocet_id)
	if request.method == "POST":
		form = ZapocetForm(request.POST,instance = zapocet)
		if form.is_valid():
			form.save()
	else:
		form = ZapocetForm(instance = zapocet)
	return render_to_response('zapocetedit.html',{'form':form})
def zapocetAdd(request):
	form = ZapocetForm()
	if request.method =="POST":
		form = ZapocetForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/zapocty/')
	return render_to_response('zapocetadd.html',{'form':form})
