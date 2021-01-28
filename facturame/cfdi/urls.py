from django.urls import path
from django.conf.urls import url
from . import views as views

urlpatterns_cfdi = ([

    path('cfdilist/',
         views.CfdiView.as_view(),
         name='cfdi_list'),
])