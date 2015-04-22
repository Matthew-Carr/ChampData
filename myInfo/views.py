from django.shortcuts import render

def about(request):
	return render(request, 'myInfo/about.html')
