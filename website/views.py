from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
	context = {}
	return render(request, 'index.html', context)

def contact(request):
	context = {}
	if request.method == "POST":
		message_name = request.POST["message-name"]
		message_email = request.POST["message-email"]
		message = request.POST["message"]
		msg_subject = "Name is : " + message_name
		msg_body = "Email " + message_email + "\n" + "May be wants to book an appouintment.\n" + "Message : " + message + "\n" + "There is a channel listening"

		# Send Mail
		send_mail(
			msg_subject,
			msg_body,
			message_email,
			['sanojvaidyan93@gmail.com'],
			fail_silently=False,
			)
		context["message_name"] = message_name
		return render(request, 'contact.html', context)
	else:
		return render(request, 'contact.html', context)