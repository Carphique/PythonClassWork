from django.urls import path
# Імпортуємо всі класи з файлу views.py
from .views import HomeView, NewsView, ManagementView, AboutView, ContactsView, ProductView
from . import views

urlpatterns = [
    # path('products/', ProductView.as_view(), name='products'),

    #path('', HomeView.as_view(), name='home'),
    #path('news/', NewsView.as_view(), name='news'),
    #path('management/', ManagementView.as_view(), name='management'),
    #path('about/', AboutView.as_view(), name='about'),
    #path('contacts/', ContactsView.as_view(), name='contacts'),

    path('', views.index, name="start-page"),
    path('json/', views.json_response, name="json-example"),
    path('products/', views.get_all_products, name="products"),
    path('product/<int:id>', views.get_product_by_id, name="product"),
    path('except/', views.exept_view, name="exception"),

    path('history/', views.history_view, name='history_main'),
    path('history/<int:year>/', views.history_view, name='history_year'),

    # 2. Маршруты для городов
    path('cities/', views.cities_view, name='cities_main'),
    path('cities/<str:city>/<int:year>/', views.cities_view, name='cities_details'),

]