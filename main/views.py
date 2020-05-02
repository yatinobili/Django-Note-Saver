from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm

def all(response):
    return render(response, 'main/all.html')
    #return HttpResponse("<t>higggg<t1>")


def published(response):
    entries = Entry.objects.order_by('-date_posted')
    context = {'entries' : entries}

    return render(response, 'main/published.html', context)


def drafts(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('drafts')

    else :
        form = EntryForm()

    form = EntryForm()
    context = {'form' : form}

    return render(request, 'main/drafts.html', context)



def deleted(response):
    return render(response, 'main/deleted.html')