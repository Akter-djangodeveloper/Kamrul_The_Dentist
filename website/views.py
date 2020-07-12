from django.shortcuts import render
from dentist import settings
from django.core.mail import send_mail

def home(request):
	if request.method == "POST":
		news_subject = 'Thanks For Subscribing!'
		message_email = request.POST['nl-email']
		to_email = "jwel.ayan@gmail.com"

		# send an email
		msg = "From:" + " " + message_email 

		send_mail('New Subscriber', msg, settings.EMAIL_HOST_USER, [to_email], fail_silently = False,)
			    		
		return render(request, 'home.html', {'news_subject': news_subject})
	else:
		return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		subject = request.POST['message-name']
		message = request.POST['message']
		message_email = request.POST['message-email']
		to_email = "jwel.ayan@gmail.com"

		# send an email
		msg = "Message: " + message + "\n" + "From:" + " " +message_email 

		send_mail(subject, msg, settings.EMAIL_HOST_USER, [to_email], fail_silently = False,)

		msg_reply = "Thanks " + subject + "\n" + "We received your email and will respond shortly..."
		send_mail('Dr. Kamrul Islam The Dentist Ever', msg_reply, settings.EMAIL_HOST_USER, [message_email], fail_silently = False,)
			    		
		return render(request, 'contact.html', {'subject': subject})
	else:
		return render(request, 'contact.html', {})


def about(request):
	return render(request, 'about.html', {})

def pricing(request):
	return render(request, 'pricing.html', {})

def service(request):
	return render(request, 'service.html', {})

def appointment(request):
	if request.method == "POST":
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_schedule = request.POST['your-schedule']
		to_email_appoint = "jwel.ayan@gmail.com"
		
		# send an email
		appointment = " Name: " + your_name + "\n" + " Phone: " + your_phone + "\n" + " Schedule: " + your_schedule

		send_mail('Appointment Request', appointment, settings.EMAIL_HOST_USER, [to_email_appoint], fail_silently = False,)

		return render(request, 'appointment.html', {
			'your_name': your_name,
			'your_phone': your_phone,
			'your_schedule': your_schedule,
			})

	else:
		return render(request, 'home.html', {})