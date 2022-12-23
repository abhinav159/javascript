from django.urls import path
from . import views

urlpatterns = [
    path('baabtrahome',views.baabtrahome),
    path('home',views.home),
    path('newpage',views.newpage),
    path('new',views.new),
    path('js',views.js),
    path('largest',views.largest),
    path('SON',views.Sum_number),
    path('reverse',views.reverse),
    path('pattern',views.pattern),
    path('holosquare',views.holosquare),
    path('inverted_right_triangle',views.inverted_right_triangle),
    path('inverted_pyramid',views.inverted_pyramid),
    path('mirror_triangle',views.mirror_triangle),
    path('javascript',views.javascript),
    path('calculator',views.calculator),
    path('customer',views.customer),
    path('addproduct',views.addproduct),
    path('viewprice',views.viewprice),
    path('jquery',views.jquery),
    path('coloring',views.coloring),
    path('validation',views.validation),
    path('todo',views.todo),
]
