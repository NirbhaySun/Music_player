from django.shortcuts import render
from .models import Song
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    paginator=Paginator(Song.objects.all(),1)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"index.html",context)



# def index(request):
#     # Fetch all songs
#     queryset = Song.objects.all()  # Corrected 'Song.object' to 'Song.objects'
    
#     # Initialize paginator with the queryset and items per page
#     paginator = Paginator(queryset, 2)  # Adjust '2' as per your desired pagination size
    
#     # Get the page number from the request
#     page_number = request.GET.get('page')
    
#     # Get the relevant page of items
#     page_obj = paginator.get_page(page_number)
    
#     # Context to pass to the template
#     context = {"page_obj": page_obj}
    
#     return render(request, "index.html", context)