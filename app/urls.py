from django.urls import path
# from .views import ItemFilterView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView
from django.conf.urls import url
from . import views


app_name = 'app'
urlpatterns = [
    #path('',  ItemFilterView.as_view(), name='index'),
    #path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    # path('create/', ItemCreateView.as_view(), name='create'),
    # path('update/<int:pk>/', ItemUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete'),
    url(r'^form/', views.form, name = 'form'),
    url(r'^complete/', views.complete, name = 'complete'),
    path('', views.Top.as_view(), name='top'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('user_create/', views.UserCreate.as_view(), name='user_create'),
    path('user_create/done/', views.UserCreateDone.as_view(), name='user_create_done'),
    path('user_create/complete/<token>/', views.UserCreateComplete.as_view(), name='user_create_complete'),
    path('user_detail/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('user_update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
    path('password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDone.as_view(), name='password_change_done'),
    path('password_reset/', views.PasswordReset.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),

]
