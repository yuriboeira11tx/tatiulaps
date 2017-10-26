from django.shortcuts import render

def index(request):
	dudu_mini_crack = "Alo"
	return render(request, 'home/index.html')
