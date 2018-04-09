from django.contrib.auth.decorators import login_required
from django.http import request

from book.models import Book
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import BookForm
from django.core.files.storage import FileSystemStorage


class BookCreateView(CreateView):
    form_class = BookForm
    template_name = 'bookcreat.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(BookCreateView, self).form_valid(form)


def model_form_upload(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'bookcreat.html', {'form': form})


@login_required
def book_all_list_view(request):
    q = request.POST.get('q1')

    query1 = Book.objects.search(q)
    query2 = Book.objects.all()#filter(user=request.user)

    context = {
        'search': query1,
        'object': query2
    }

    return render(request, 'book/book_all_list.html', context)



@login_required
def book_list_view(request):
    q = request.POST.get('q1')

    query1 = Book.objects.search(q)
    query2 = Book.objects.filter(user=request.user)

    context = {
        'search': query1,
        'object': query2
    }

    return render(request, 'book/book_list.html', context)


class BookUpdateView(LoginRequiredMixin, UpdateView):
    form_class = BookForm
    success_url = reverse_lazy('book-list')

    def get_context_data(self, **kwargs):
        context = super(BookUpdateView, self).get_context_data(**kwargs)
        name = self.get_object().book_name
        context['title'] = f'Update Book: {name}'
        return context

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('book-list')
