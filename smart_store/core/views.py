from django.shortcuts import render
from .product_similarity import get_similar_products
# Create your views here.

def home(request):
    results = []

    if request.method == "POST":
        product = request.POST.get("product")

        results = get_similar_products(product)
        print("RESULTS:", results)

    return render(request, "index.html", {
        "results": results
    })