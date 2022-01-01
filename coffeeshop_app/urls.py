from django.urls import path
from .import views
app_name='coffeeshop'
urlpatterns=[
    path('',views.coffeeshop,name='coffeeshop'),
    path('shop/<int:book_id>',views.detail,name='detail'),
    path('add/',views.add_product,name='add_product'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>', views.delete, name='delete')

]
