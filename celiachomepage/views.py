from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'celiachomepage/index.html')

def main(request):
    return render(request, 'celiachomepage/main.html')