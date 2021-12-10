from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.forms.models import model_to_dict

# from django.db.models import Q

import datetime

from .models import Book, Author, Genere, GenegeBook
from .forms import CreateBookForm


def user_login(request, method="POST"):
    if request.method == "POST":
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        user = authenticate(email=email, password=password)

        if user is None:
            my_message = (
                "Your email address or password is incorrect. Please login again!"
            )
            messages.error(request, my_message)

            return render(request, "layouts/login.html")

        login(request, user)
        return HttpResponseRedirect("dashboard/")

    return render(request, "layouts/login.html")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")


@login_required
def dashboard(request):
    return render(request, "dashboard/index.html")


@login_required
def list_books(request, method="GET"):
    query_params = request.GET
    date_from = query_params.get("date_from", None)
    date_to = query_params.get("date_to", None)

    # Lấy danh sách tất cả book
    books = Book.objects.all()

    if date_from is not None:
        books = books.filter(created_at__gte=date_from)  # greater than equal

    if date_to is not None:
        books = books.filter(created_at__lte=date_to)

    return render(request, "books/list_books.html", {"books": books})


@login_required
def create_book(request):
    if request.method == "GET":
        authors = Author.objects.all()
        return render(request, "books/create_book.html", context={"authors": authors})
    elif request.method == "POST":
        try:
            data = request.POST
            image = request.FILES

            name = data.get("name", "")
            description = data.get("description", "")
            author = int(data.get("author", None))
            published_date = data.get("published_date", None)
            created_at = datetime.date.today()
            cover_image = image.get("cover_img", None)

            book = Book(
                name=name,
                description=description,
                author_id=author,
                published_date=published_date,
                cover_img=cover_image,
                created_at=created_at,
            )
            book.save()
            messages.success(request, "Create book successful")
        except:
            messages.error(request, "Create book failed")
            return HttpResponseRedirect(request.META["HTTP_REFERER"])

    return HttpResponseRedirect(reverse("list_books"))


# Use form
# def create_book(request):
#     if request.method == "POST":
#         form = CreateBookForm(request.POST, request.FILES)
#         if form.is_valid():
#             book = Book()

#             book.name = form.cleaned_data["name"]
#             book.description = form.cleaned_data["description"]
#             book.author = form.cleaned_data["author"]
#             book.published_date = form.cleaned_data["published_date"]
#             book.created_at = datetime.date.today()
#             book.cover_img = form.cleaned_data["cover_img"]

#             book.save()

#             messages.success(request, "Create book successful")
#             return redirect("list_books")
#     else:
#         form = CreateBookForm(initial={"published_date": datetime.date.today()})

#     context = {
#         "form": form,
#     }

#     return render(request, "books/new_book.html", context=context)


@login_required
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        form = CreateBookForm(request.POST or None)
        if form.is_valid():
            book.name = form.cleaned_data["name"]
            book.description = form.cleaned_data["description"]
            book.author = form.cleaned_data["author"]
            book.published_date = form.cleaned_data["published_date"]
            book.created_at = datetime.date.today()

            book.save()  # book.refresh_from_db() // book.update(name='', description='', ...)

            messages.success(request, "Create book successful")
            return redirect("list_books")
    else:
        form = CreateBookForm(model_to_dict(book))

    context = {"form": form, "book": book}

    return render(request, "books/edit_book_f.html", context=context)


@login_required
def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    authors = Author.objects.all()
    statuses = Book.STATUSES

    if request.method == "POST":
        data = request.POST
        img = request.FILES

        book.name = data.get("name", "")
        book.description = data.get("description", "")
        book.author_id = int(data.get("author", ""))
        book.published_date = data.get("published_date", "")
        book.status = data.get("status", 0)
        book.cover_img = img.get("cover_img", None)

        book.save()
        return redirect("list_books")

    context = {"book": model_to_dict(book), "statuses": statuses, "authors": authors}
    return render(request, "books/update_book.html", context=context)


@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()

    return redirect("list_books")


@login_required
def create_multi_genere_book(request, method="GET"):
    generes = Genere.objects.all()

    if request.method == "POST":
        data = request.POST
        list_generes = data.getlist("genere[]", [])
        list_number_books = data.getlist("book_number[]", [])

        if len(list_generes) and len(list_number_books):
            list_genere_books = []
            i = 0

            for ind in range(0, len(list_generes)):
                list_genere_books.append(
                    __new_genere_book(
                        genere_id=int(list_generes[ind]),
                        number_book=int(list_number_books[ind]),
                    )
                )
            GenegeBook.objects.bulk_create(list_genere_books)

            return redirect("list_books")

    return render(
        request, "books/_partial_book_genere.html", context={"generes": generes}
    )


@login_required
def show_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "books/show_book.html", context={"book": book})


# Private methods
def __new_genere_book(genere_id, number_book):
    genere_book = GenegeBook()
    genere_book.genere_id = genere_id
    genere_book.number_of_book = number_book

    return genere_book


def __convert_str_to_date(str):
    return datetime.datetime.strptime(str, "%Y-%m-%d").date()
