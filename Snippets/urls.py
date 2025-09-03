from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('', views.index_page),
    path('snippets/add', views.add_snippet_page, name="add_snippet"),
    path('snippets/list', views.snippets_page, name="snippet_list"),
    path('snippets/<int:snippet_id>', views.page_snippet, name="page_snippet"),
    path('snippets/<int:snippet_id>/delete', views.snippet_delete, name="snippet-delete"),
    path('snippets/<int:snippet_id>/edit', views.snippet_edit, name="snippet-edit"),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('mysnippets', views.my_snippets, name='my-snippets'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
