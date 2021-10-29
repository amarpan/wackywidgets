from django.urls import path
from . import views

# 3 total URLS total only
urlpatterns = [
    path('', views.widgets_index, name='index'),
    # path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
    # path('widgets', views.WidgetCreate.as_view(), name='widgets_create')
    path('create/', views.add_widget, name='add_widget'),
    path('delete/<int:widget_id>/', views.delete_widget, name='delete_widget'),
]

