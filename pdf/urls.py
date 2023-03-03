from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index' ),
    path('chapter1/',views.chapter1, name='chapter1' ),
    path('chapter2/',views.chapter2, name='chapter2' ),
    path('chapter3/',views.chapter3, name='chapter3' ),
    path('chapter4/',views.chapter4, name='chapter4' ),
    path('chapter5/',views.chapter5, name='chapter5' ),
    path('chapter6/',views.chapter6, name='chapter6' ),
    path('chapter7/',views.chapter7, name='chapter7' ),
    path('chapter8/',views.chapter8, name='chapter8' ),
    path('chapter9/',views.chapter9, name='chapter9' ),
    path('chapter10/',views.chapter10, name='chapter10' )
]