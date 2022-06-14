from django.shortcuts import render, get_object_or_404
from .models import Entry

# Create your views here.
def entryList(request):
    displayList = Entry.objects.all().order_by("-date_created")
    template = 'entries/index.html'
    context = {
        'displayList': displayList,
    }
    return render(request, template, context)

def entryDetailView(request, entry_id):
    displayView = get_object_or_404(Entry, pk=entry_id)
    template = 'entries/detail_view.html'
    context = {
        'displayView':  displayView,
       
    }
    return render(request, template, context)
