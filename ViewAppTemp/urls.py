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

    path('branches/', views.all_branches, name="all-branches"),
    path('branches/<str:city>/', views.branch_detail, name="branch-detail"),

    path('history/', views.all_history, name="all-history"),
    path('history/<str:god>/', views.history_detail, name="history-detail"),

]