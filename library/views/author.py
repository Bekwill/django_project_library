from django.http import HttpResponse
from library.models import Author
from django.shortcuts import render, get_object_or_404, redirect
from library.forms import AuthorForm


def create(request):
    form = AuthorForm()
    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('author-detail', form.instance.pk)

    return render(request, 'author/create.html', {'form': form})


def list_all(request):
    authors = Author.objects.all()

    return render(request, 'author/list.html', {'authors': authors})


def detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'author/detail.html', {'author': author})


def update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    form = AuthorForm(instance=author)
    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author-detail', author.pk)
    return render(request, 'author/update.html', {'form': form})


def delete(request, pk):
    if request.method == "POST":
        author = get_object_or_404(Author, pk=pk)
        author.delete()
        return redirect('author-list')
