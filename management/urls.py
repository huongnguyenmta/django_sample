from django.urls import path

from management import views

urlpatterns = [
    path("", views.user_login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.user_logout, name="logout"),
    path("books/", views.list_books, name="list_books"),
    path("books/create-book", views.create_book, name="create_book"),
    path("books/edit-book/<int:pk>", views.update_book, name="edit_book"),
    path("books/delete-book/<int:pk>", views.delete_book, name="delete_book"),
    path("books/show-book/<int:pk>", views.show_book, name="show_book"),
    path(
        "books/create-multi-genere-book",
        views.create_multi_genere_book,
        name="create_multi_genere_book",
    ),
]
