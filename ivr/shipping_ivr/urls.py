from django.urls import path

from . import views

urlpatterns = [
    path('welcome', views.welcome, name='welcome'),
    path('menu', views.menu, name='menu'),
    path('track_shipment', views.track_shipment, name='track_shipment'),
    path('get_shipment_status', views.get_shipment_status, name='get_shipment_status'),
    path('schedule_services', views.schedule_services, name = 'schedule_services'),
    path('get_branches', views.get_branches, name = 'get_branches'),
    path('schedule_days', views.schedule_days, name = 'schedule_days'),
    path('get_cities', views.get_cities, name = 'get_cities'),
    path('confirmation', views.confirmation, name = 'confirmation'),
    path('options', views.options, name='options'),
    path('get_quotation', views.get_quotation, name='get_quotation'),
    path('get_weight', views.get_weight, name='get_weight'),
    path('invoice_input', views.invoice_input, name='invoice_input'),
    path('download_invoice', views.download_invoice, name='download_invoice'),
    path('choose_language', views.choose_language, name='choose_language'),
    path('set_language', views.set_language, name='set_language'),
]
