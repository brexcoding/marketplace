from django.shortcuts import render
from .models import Product , Order
from django.views.generic import ListView ,DetailView

def landingpage(request):
    return render( request , template_name =  'landingpage.html')
# Create your views here.
def products(request):
    products = Product.objects.all()
    return render(request, 'products_page.html' , {"products": products })

class ordering(DetailView):
    model = Product
    template_name = 'ordering.html' 

    def order_function(request):
        if request.method == "POST":
            order = Order()
            product = request.POST.get('product')
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            adress = request.POST.get('adress')
            adress1 = request.POST.get('adress1')
            amount = request.POST.get('amount')
    
            order.product = product
            order.name = name
            order.phone = phone
            order.adress = adress
            order.adress1 = adress1
            order.amount = amount
            
            order.save()
        
            return render(request, 'contact_msg.html')
        else : return render(request, 'landingpage.html')
class ordering(DetailView):
    model = Product
    template_name = 'ordering.html'

    def post(self, request, *args, **kwargs):
        product = self.get_object()  # Retrieve the product instance

        order = Order()
        order.product = product
        order.name = request.POST.get('name')
        order.phone = request.POST.get('phone')
        order.adress = request.POST.get('adress')
        order.adress1 = request.POST.get('adress1')
        order.amount = request.POST.get('amount')
        order.save()

        return render(request, 'order_msg.html')

