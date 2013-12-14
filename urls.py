from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	(r'^index','zapocty.views.index'),
    (r'^admin/', include(admin.site.urls)),
	(r'^studenti/$','zapocty.views.studenti'),  
	(r'^studenti/(?P<student_id>\d+)','zapocty.views.studentEdit'),
	(r'^predmety/$','zapocty.views.predmety'),  
	(r'^predmety/(?P<predmet_id>\d+)','zapocty.views.predmetEdit'),
	(r'^zapocty/$','zapocty.views.zapocty'),  
	(r'^zapocty/(?P<zapocet_id>\d+)','zapocty.views.zapocetEdit'),
	(r'^studenti/add','zapocty.views.studentAdd'),
	(r'^zapocty/add','zapocty.views.zapocetAdd'),  
)
