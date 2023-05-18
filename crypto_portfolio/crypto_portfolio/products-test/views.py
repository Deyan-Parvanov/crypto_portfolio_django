# from django.shortcuts import render
# from django.views import View
#
# from crypto_portfolio.products.model_category import Category
# from crypto_portfolio.products-test.model_orders import Order
# from crypto_portfolio.products-test.model_product import Products
#
#
# class HomeView(View):
#
#     def post(self, request):
#         product = request.POST.get('product')
#         remove = request.POST.get('remove')
#         cart = request.session.get('cart')
#
#         if cart:
#             quantity = cart.get(product)
#             if quantity:
#                 if remove:
#                     if quantity <= 1:
#                         cart.pop(product)
#                     else:
#                         cart[product] = quantity - 1
#                 else:
#                     cart[product] = quantity + 1
#             else:
#                 cart = {}
#                 cart[product] = 1
#
#         request.session['cart'] = cart
#         # print('cart', request.session['cart'])
#         return render(request, 'core/home-page.html')
#         # return redirect('index')
#
#     def get(self, request):
#         pass
#
#
# def store(request):
#     # cart = request.session.get('cart')
#     # if not cart:
#     #     request.session['cart'] = {}
#
#     # products-test = None
#     categories = Category.get_categories()
#     category_id = request.GET.get('category')
#
#     if category_id:
#         products-test = Products.get_products_by_category_id(category_id)
#     else:
#         products-test = Products.get_products()
#
#     context = {
#         'products-test': products-test,
#         'categories': categories,
#     }
#
#     return render(request, 'core/home-page.html', context)
#
#
# class OrderView(View):
#
#     def get(self, request):
#         user = request.session.get('user')
#         orders = Order.get_orders_by_customer(user)
#         # print(orders)
#         return render(request, '', {'orders': orders})
