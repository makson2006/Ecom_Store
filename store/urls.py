from django.urls import path
from . import views
urlpatterns = [
   path('', views.home, name='home'),
   path('about/', views.about, name='about'),
   path('login/', views.login_user, name='login'),
   path('logout/', views.logout_user, name='logout'),
   path('register', views.register_user, name='register'),
   path('product/<int:pk>', views.product, name='product'),
   path('category/<str:foo>', views.category, name='category'),
   path('all_products/', views.all_products, name='all-products'),
   path('books/', views.books, name='books'),
   path('book/<int:pk>', views.book, name='book'),
   path('download/<int:book_id>/', views.download_book, name='download_book'),

]