from django.urls import path
from .views import *

urlpatterns=[
    path('reg',RegView.as_view(),name="reg"),
    path('logout',LogoutView.as_view(),name="logout"),
    path('home',HomeView.as_view(),name='home'),
    path('accomodation',AccomodationView.as_view(),name='accomodation'),
    path('bicycle',bicycleView.as_view(),name='bicycle'),
    path('bicycle1',BicycleDetails.as_view(),name='bicycle1'),
    path('bydel/<int:bid>',BookedBicycleDeleteView.as_view(),name='bydel'),
    path('det/<str:cat>',DetailsView.as_view(),name='det'),
    path('dest',DestinationView.as_view(),name='dest'),
    path('pay',HbookView.as_view(),name="pay"),
    path('order1/<int:pid>',Order1View.as_view(),name='order1'),
    path('select/<int:pid>',addtoselection,name='addselection'),
    path('blist',BookedListView.as_view(),name='blist'),
    path('bdel/<int:sid>',BookedItemDeleteView.as_view(),name='bdel'),
    path('arev/<int:pid>',addreview,name='arev'),
    path('book/<int:sid>',bookView.as_view(),name='book'),
    path('mview',BookedflistView.as_view(),name='mview'),
    path('corder',cancelView,name='corder'),



    

]