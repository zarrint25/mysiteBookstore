
from book.views import BookCreateView, book_list_view, BookUpdateView, BookDeleteView, book_all_list_view
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^bookcreate/$', BookCreateView.as_view(), name='book-create'),
    url(r'^booklist/$', book_list_view, name='book-list'),
    url(r'^bookalllist/$', book_all_list_view, name='book-all-list'),
    url(r'^booklist/(?P<slug>[\w-]+)/$', BookUpdateView.as_view(), name='book-update'),
    url(r'^booklist/delete/(?P<pk>\d+)$', BookDeleteView.as_view(), name='book-delete'),
    url(r'^', include('mysite.urls')),

]

admin.site.site_header = 'My Site Admin Panel'


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)