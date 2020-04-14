
from django.shortcuts import render, get_object_or_404, redirect
from .models import JualProduk
from django.urls import reverse
from django.db.models import Q


# Create your views here.
# def index(request):
#     # return HttpResponse("Hello, wolrd. You're at polls in ")
#     return render(request, 'index.html')

def index(request):
    jualproduk = JualProduk.objects.all()
    return render(request, 'index.html', {
        'jualproduk':jualproduk,
    })
    
# def produk(request):
#     return render(request, 'produk.html')

def produk(request, id):
    produk = get_object_or_404(JualProduk, pk=id)
    prodtype = JualProduk.name
    shofa = JualProduk.objects.filter(product_type=name)
    
    return render(request, 'produk.html', {
        'jualproduk':JualProduk,
        'produk':produk
    })
    

# def SearchResultView(request):
#     model_produk = JualProduk
#     template_name = 'search_result.html'
#     query = request.GET.get('q')
#     object_list = JualProduk.objects.filter(name__icontains=query)
        
#     return render(request, 'search_result.html',{
#         'object_list':object_list,
#         'query' : query,
        
#     })
    