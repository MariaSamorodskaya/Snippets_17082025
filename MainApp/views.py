from django.http import Http404, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from MainApp.forms import SnippetForm
from MainApp.models import Snippet


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    form = SnippetForm()
    context = {
        'pagename': 'Добавление нового сниппета',
        'form': form
         }
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    list_snippet = Snippet.objects.all()
    context = {'pagename': 'Просмотр сниппетов', 
               'list_snippet': list_snippet,
               'len_snippet': list_snippet.count()}
    return render(request, 'pages/view_snippets.html', context)

def page_snippet(request, snippet_id: int):
    try:
        snippet = Snippet.objects.get(id = snippet_id)
    except Snippet.DoesNotExist:
        return render(request, 'pages/errors.html', context = {"error": f"Сниппет с id={snippet_id} не найден"})
    else:
        context = {'snippet': snippet}
        return render(request, 'pages/page_snippet.html', context)    
    
def create_snippet(request):
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("snippet_list")
        return render(request, 'pages/page_snippet.html', context={"form": form}) 
    
    return HttpResponseNotAllowed(["POST"],"You must make POST request to add snippet.")
