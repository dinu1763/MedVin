

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import get_template


def home(request):
	if request.method == 'POST':
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']
		address = request.POST['your-address']
		schedule = request.POST['your-scheldule']
		package = request.POST['your-test']
		phone = request.POST['message-phone']
		date = request.POST['message-date']
		text = " Name :" + message_name + " \n " + "Date :" +date + " \n " + "Email Address :" + message_email+ " \n " + \
							"Mobile Number :" + phone + " \n " + "Address :" + address + " \n "  + \
							"Scheduled On :" +schedule + " \n " + "Package Name :" +package + " \n " + "Message :" + message
		send_mail(
			message_name,
			text,
			message_email,
			['selvan1763@gmail.com'],
			fail_silently=False,
			)
		return render(request, 'home.html', {'message_name': message_name})
	else:
	
		return render(request, 'home.html', {})


def contact(request):
	if request.method == 'POST':
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']
		
		send_mail(
			message_name,
			message,
			message_email,
			['selvan1763@gmail.com'],
			fail_silently=False,
			)
		return render(request, 'contact.html', {'message_name': message_name})
	else:
	
		return render(request, 'contact.html', {})
		
def service(request):
	return render(request, 'service.html', {})
	
	
def about(request):
	return render(request, 'about.html', {})
	
def pricing(request):
	return render(request, 'pricing.html', {})