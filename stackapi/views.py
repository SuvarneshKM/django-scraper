from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Price, Pricesilver
from .serializer import PriceSerializer, PricesilverSerializer
from bs4 import BeautifulSoup
import urllib.request 
from pprint import pprint 
from html_table_parser import HTMLTableParser 
from time import sleep

# Create your views here.


def index(request):
	return HttpResponse("Success")


class PriceAPI(viewsets.ModelViewSet):
	queryset = Price.objects.all()
	serializer_class = PriceSerializer

class PricesilverAPI(viewsets.ModelViewSet):
	queryset = Pricesilver.objects.all()
	serializer_class = PricesilverSerializer


def latest(request):
	try:
		def create_currency():
			print('Creating forex data ..')
			def url_get_contents(url): 
				req = urllib.request.Request(url=url) 
				f = urllib.request.urlopen(req) 
				return f.read() 

			xhtml = url_get_contents('https://www.goodreturns.in/gold-rates/').decode('utf-8') 

			p = HTMLTableParser() 
			p.feed(xhtml) 
			gram = p.tables[0][1][0]
			today = p.tables[0][1][1]
			yesterday = p.tables[0][1][2]
			change = p.tables[0][1][3]

			Price.objects.create(
					gram=gram,
					today=today,
					yesterday=yesterday,
					change=change
				)

			xhtml1 = url_get_contents('https://www.goodreturns.in/silver-rates/').decode('utf-8') 

			p1 = HTMLTableParser() 
			p1.feed(xhtml1) 
			sgram = p1.tables[0][1][0]
			stoday = p1.tables[0][1][1]
			syesterday = p1.tables[0][1][2]
			schange = p1.tables[0][1][3]

			Pricesilver.objects.create(
					sgram=sgram,
					stoday=stoday,
					syesterday=syesterday,
					schange=schange
				)

		def update_currency():
			print('Updating data ..')
			print('Updating forex data ..')
			def url_get_contents(url): 
				req = urllib.request.Request(url=url) 
				f = urllib.request.urlopen(req) 
				return f.read() 

			xhtml = url_get_contents('https://www.goodreturns.in/gold-rates/').decode('utf-8') 

			p = HTMLTableParser() 
			p.feed(xhtml) 
			gram = p.tables[0][1][0]
			today = p.tables[0][1][1]
			yesterday = p.tables[0][1][2]
			change = p.tables[0][1][3]

			print({'gram':gram, 'today':today, 'yesterday':yesterday, 'change':change})
			data = {'gram': gram, 'today':today, 'yesterday':yesterday, 'change':change}
			Price.objects.filter(gram=gram).update(**data)
				
			
			xhtml1 = url_get_contents('https://www.goodreturns.in/silver-rates/').decode('utf-8') 

			p1 = HTMLTableParser() 
			p1.feed(xhtml1) 
			sgram = p1.tables[0][1][0]
			stoday = p1.tables[0][1][1]
			syesterday = p1.tables[0][1][2]
			schange = p1.tables[0][1][3]

			print({'sgram':sgram, 'stoday':stoday, 'syesterday':syesterday, 'schange':schange})
			datas = {'sgram':sgram, 'stoday':stoday, 'syesterday':syesterday, 'schange':schange}
			Pricesilver.objects.filter(sgram=sgram).update(**datas)
			   
			sleep(3)   

		     
		create_currency()

		while True:
			sleep(15)
			update_currency()
		return HttpResponse("Latest Data Fetched from Stack Overflow")
	except:
		return HttpResponse("Failed")