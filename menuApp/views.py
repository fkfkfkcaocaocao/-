from django.shortcuts import render


# def user(request):
#     return render(request, 'user.html')

# from .models import Merchant, Product, Cart, Order

# def menu(request):
#     merchants = Merchant.objects.all()
#     return render(request, 'takeaway/menu.html', {'merchants': merchants})
#
# def add_to_cart(request, product_id):
#     # 将菜品添加到购物车的逻辑
#     pass
#
# def view_cart(request):
#     cart_items = Cart.objects.filter(user=request.user)
#     return render(request, 'takeaway/cart.html', {'cart_items': cart_items})
#
# def submit_order(request):
#     # 提交订单的逻辑
#     pass
#
# def view_order(request, order_id):
#     order = Order.objects.get(id=order_id)
#     return render(request, 'takeaway/order.html', {'order': order})
#
# def mark_as_completed(request, order_id):
#     # 商家版点击订单完成后更新订单状态的逻辑
#     pass

# Create your views here.
