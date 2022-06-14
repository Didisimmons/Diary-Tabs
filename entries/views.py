from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Entry
from .forms import EntryForm

# Create your views here.
def entryList(request):
    entry = None
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save()
            entry.save()
            return redirect(reverse('home'))
    else:
        form = EntryForm()

    form = EntryForm()

    displayList = Entry.objects.all().order_by("-date_created")
    template = 'entries/index.html'
    context = {
        'entry': entry,
        'form': form,
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
