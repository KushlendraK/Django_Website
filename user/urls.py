"""user_admin_panel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
 
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('login', views.login),
    path('login_user', views.login_user),
    path('user_dash', views.user_dash),
    path('admin_dash', views.admin_dash),
    path('emp_dash', views.emp_dash),
    path('signup', views.signup),
    path('new_user', views.new_user),
    path('user_logout',views.user_logout),
    path('emp_logout',views.emp_logout),
    path('admin_logout',views.admin_logout),

    # 
    path('add_item',views.add_item),
    path('admin_items',views.admin_items),
    path('show_all_items',views.show_all_items),
    path('admin_search',views.admin_search),
    path('search_by_category',views.search_by_category),
    path('delete_item',views.delete_item),
    
    path('cart',views.cart),
    path('buy',views.buy),
    path('add_to_cart',views.add_to_cart),
    path('user_shopping',views.user_shopping),
    path('user_cart_page',views.user_cart_page),
    path('admin_delete_item',views.admin_delete_item),
    path('admin_edit_item',views.admin_edit_item),
    path('admin_edit_item_set',views.admin_edit_item_set),
    path('show_all_user',views.show_all_user),
    path('admin_delete_user',views.admin_delete_user),
    path('show_cart_detail',views.show_cart_detail),
    path('sales_history',views.sales_history),
    path('invoice',views.invoice),
    

    

]
