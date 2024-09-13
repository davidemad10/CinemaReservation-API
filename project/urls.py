from django.contrib import admin
from django.urls import path
from tickets import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #1
    path('django/jsonresponsenomodel/', views.no_rest_no_model),

    #2
    path('django/jsonresponsefrommodel/', views.no_rest_with_model),

    #3.1
    path('rest/fbv/', views.FBV_List),

    #3.2
    path('rest/fbv/<int:pk>', views.FBV_PK),

    #4.1 GET POST from rest framework class based view APIView
    path('rest/cbv/',views.CBV_List.as_view()),

    #4.2 GET PuT delete from rest framework class based view APIView
    path('rest/cbv/<int:pk>',views.CBV_pk.as_view()),
    
    #5.1 GET POST from rest framework class based view mixins
    path('rest/mixins/',views.mixins_list.as_view()),

    #5.2 GET PuT delete from rest framework class based view mixins
    path('rest/mixins/<int:pk>',views.mixins_pk.as_view()),

    #6.1  GET POST from rest framework class based view generics
    path('rest/generic/',views.generics_list.as_view()),

    #6.2  GET PuT delete from rest framework class based view generics
    path('rest/generic/<int:pk>',views.generics_pk.as_view()),
]
