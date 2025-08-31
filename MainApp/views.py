from django.http import Http404, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404
from MainApp.forms import SnippetForm
from MainApp.models import Snippet
from django.contrib import auth


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == "GET":    
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'but_name': 'Создать сниппет',
            'form': form
            }
        return render(request, 'pages/add_snippet.html', context)
    
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("snippet_list")
        return render(request, 'pages/add_snippet.html', context={"form": form}) 
    
    return HttpResponseNotAllowed(["POST"],"You must make POST request to add snippet.")

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

def snippet_delete(request, snippet_id: int):
    if request.method == "GET" or request.method == "POST":
        snippet = get_object_or_404(Snippet, id = snippet_id)
        snippet.delete()
    return redirect("snippet_list")

def snippet_edit(request, snippet_id: int):
    snippet = get_object_or_404(Snippet, id = snippet_id)
    if request.method == "GET":    
        dictfields = {"name": snippet.name, "lang": snippet.lang, "code": snippet.code}
        form = SnippetForm(initial = dictfields)
        context = {
            'pagename': 'Редактирование сниппета',
            'but_name': 'Сохранить изменения',
            'form': form
            }
        return render(request, 'pages/add_snippet.html', context)
    
    if request.method == "POST":
        name_post = request.POST.get("name")
        lang_post = request.POST.get("lang")
        code_post = request.POST.get("code")
        Snippet.objects.filter(id=snippet_id).update(name=name_post, lang=lang_post,code=code_post)
        return redirect("snippet_list")
    
def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print("username =", username)
        # print("password =", password)
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
        # Return error message
            pass
    return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')


