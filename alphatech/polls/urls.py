from django.urls import path

from . import views


app_name = 'polls'
urlpatterns = [
    path('jualproduk/<int:id>',views.produk ),
    path('', views.index, name='index'),
    # path('search/',views.SearchResultView, name='search'),
]