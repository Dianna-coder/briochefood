from django.urls import path

from bakeries import views

urlpatterns = [
    path(
        'bakeries',
        views.BakeryView.as_view(),
        name="get_and_create_bakery"
    ),
    path(
        'bakeries/<bakery_cnpj>/recipient',
        views.RecipientAndBankCreateView.as_view(),
        name="create_recipient_and_bank"
    ),
    path(
        'bakeries/products',
        views.ProductView.as_view(),
        name="get_and_create_product"
    ),
    path(
        'bakeries/<bakery_cnpj>/sales',
        views.SaleCreateView.as_view(),
        name="create_sale"
    )
]
