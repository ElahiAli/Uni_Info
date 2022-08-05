from django.urls import path
from . import views


app_name = 'sirs'

urlpatterns = [
    path('',views.index,name='index'),
    path('all/',views.all_info,name='all_info'),
    path('add_stt/',views.new_stt,name='new_stt'),
    path('add_cot/',views.new_cot,name='new_cot'),
    path('add_stcot/',views.new_stcot,name='new_stcot'),
    path('add_prof/',views.new_prof,name='new_prof'),
    path('add_prco/',views.new_prco,name='new_prco'),
    path('add_dept/',views.new_dept,name='new_dept'),
    path('add_prereq/',views.new_prereq,name='new_prereq'),
    path('ave/',views.average,name='average'),
    path('search/',views.search,name='search'),

]