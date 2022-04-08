from django.http import HttpResponse #ES LO QUE DEVUELVE AL SERVIDOR
import datetime #SABER LA HORA Y FECHA ACTUALES
from django.template.loader import get_template #LEER UN TEMPLATE
from django.shortcuts import render

class Persona(object):
	def __init__(self, name, lastName):
		self.name = name 
		self.lastName = lastName

def Hello(req):

	p1 = Persona("Juan","Diaz")

	temasD = ["Plantillas","Modelos","Formularios","Vistas","App"]
	date = datetime.datetime.now()

	ctx = {"name": p1.name, "lastName": p1.lastName, "date":date, "temas": temasD}
	return render(req, 'index.html', ctx)

def Time(req):
	date = datetime.datetime.now()
	document = """<html>
	<body>
	<h2>Fecha y hora actuales %S</h2>
	</body>
	</html>
	""" % date

	return HttpResponse(document)

def Age(req, age, year):
	period = year-2022
	ageF = age+period
	document = "<html><body><h2>In the year %s u will be %s years </h2></body></html>" %(year,ageF)

	return HttpResponse(document)

def CursoC(req):
	date = datetime.datetime.now()
	return render(req, 'extend.html', {"date":date})