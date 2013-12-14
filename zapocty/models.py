from django.db import models
import datetime

# Create your models here.

class Student(models.Model):
	login = models.CharField(max_length=7)
	jmeno = models.CharField(max_length=20)
	prijmeni = models.CharField(max_length=20)
	
	def JmenoPrijmeni(self):
		return (self.jmeno + "" + self.prijmeni)
	def __unicode__(self):
		return self.JmenoPrijmeni()

class Predmet(models.Model):
	zkratka = models.CharField(max_length=10)
	nazev = models.CharField(max_length= 40)
	
	def __unicode__(self):
		return self.nazev

class Zapocet(models.Model):
	student = models.ForeignKey('Student')
	predmet = models.ForeignKey('Predmet')
	body = models.IntegerField()
	vykonan = models.BooleanField('Zapocet')

	def splnen(self):
		if(self.vykonan==True):
			return 'Splnen'
		else:
			return 'Nesplnen'
	def __unicode__(self):
		return str(self.body)
