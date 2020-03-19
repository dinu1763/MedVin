

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
		date = request.POST['date-picker']
		text = message + address  + schedule + package + date
		send_mail(
			message_name,
			text,
			message_email,
			['dinu1763@gmail.com'],
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
			['dinu1763@gmail.com'],
			fail_silently=False,
			)
		return render(request, 'contact.html', {'message_name': message_name})
	else:
	
		return render(request, 'contact.html', {})