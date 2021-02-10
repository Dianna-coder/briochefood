from django.urls import path

from customers import views

urlpatterns = [
    path(
        'customers',
        views.CustomerView.as_view(),
        name="get_and_create_customer"
    ),
]
