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
    entry = Entry.objects.get(id=entry_id)

    template = 'entries/detail_view.html'
    
    form = EntryForm()
    displayView.save()

    context = {
        'entry' : entry,
        'form': form,
        'displayView': displayView,
       
    }
    return render(request, template, context)

def editDetailView(request, entry_id ):
    editView = get_object_or_404(Entry, pk=entry_id)

    if request.method == "POST":
        form = EntryForm(request.POST, instance=editView)
        if form.is_valid():
            form.save()
            return redirect(reverse('detail_view', args=[editView.id]))
    else:
        form = EntryForm(instance=editView)

    template = 'entries/detail_view.html'
    context = {
        'editView': editView,
        'form' : form, 
    }
    return render(request, template, context)