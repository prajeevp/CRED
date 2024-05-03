from django.urls import path
from .views import signupPage,loginPage,homePage,logoutPage,details_view

urlpatterns = [
    path('', signupPage, name='signupPage'),
    path('login/', loginPage, name='loginPage'),
    path('home/', homePage, name='homePage'),
    path('logout/', logoutPage, name='logout'),
    path('all-details/', details_view, name='allDetails'),

]
