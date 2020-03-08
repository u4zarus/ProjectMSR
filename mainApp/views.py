from django.shortcuts import render

def index(request):
	return render(request, 'mainApp/homePage.html')

def contact(request):
	return render(request, 'mainApp/basic.html', {'values': ['If you have any questions, feel free to write us an e-mail', 's3x@who.com', '(068) 068-68-68']})
