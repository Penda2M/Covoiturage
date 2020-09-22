from django.urls import path

from main import views

urlpatterns = [
    path('', views.index, name='index'),

    path('index/', views.index, name='index'),

    #pour la partie trajet
    path('trajets/', views.trajets, name='trajets'),
    path('trajets/<int:id>', views.trajet_detail, name='trajet_detail'),

    #pour les conducteurs
    path('conducteurs/', views.conducteurs, name='conducteurs'),
    path('conducteurs/<int:id>', views.un_conducteur, name='un_conducteur'),

    #pour les passagers
    path('passagers/', views.passagers, name='passagers'),
    path('passagers/<int:id>', views.un_passager, name='un_passager'),

    #pour ajouter un trajet
    path('nouveau_trajet_conducteur/', views.nouveau_trajet_conducteur, name='nouveau_trajet_conducteur'),


    #pour modifier un trajet
    path('update_trajet/<int:id>', views.update_trajet, name='update_trajet'),

     #pour supprimer un trajet
    path('delete_trajet/<int:id>', views.delete_trajet, name='delete_trajet')

]