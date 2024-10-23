from django.shortcuts import render

# Create your views here.
def index(request):
    """Main page for coding blog"""
    return render(request, 'coding_Blogs/index.html')