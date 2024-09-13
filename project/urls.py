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
]
