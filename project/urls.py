
from django.contrib import admin
from django.urls import path,include
from tickets import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('guests', views.viewsets_guest)
router.register('movies', views.movies)
router.register('resevation', views.resevation)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1
    path('django/jsonresponcenomodel/',views.no),
    
    # 2 
    path('django/jsonresponcenomodel1/',views.no1),
    
    # 3.1
    path('rest/fbvlist/',views.FBV_List),
    
    # 3.2
    path('rest/fbv/pk/<int:pk>',views.FBV_pk),
    
    # 4.1
    path('rest/cbv/',views.CBV_list.as_view()),
    
    # 4.2
    path('rest/cbv/pk/<int:pk>',views.CBV_pk.as_view()),
    
    # 5.1
    path('rest/mixins/',views.Mixins_list.as_view()),
    
    # 5.2
    path('rest/mixins/pk/<int:pk>',views.Mixins_pk.as_view()),
    
    # 6.1
    path('rest/generics/',views.generics_list.as_view()),
    
    # 6.2
    path('rest/generics/pk/<int:pk>',views.generics_pk.as_view()),
    
    # 7
    path('rest/viewsets/',include(router.urls)),
    
    # 8
    path('fbv/find/',views.find_movie),
]
