from django.contrib import admin
from django.urls import path, include
from OPTapp import views


urlpatterns = [
    path('',views.Home,name='home'),
    path('admin/', admin.site.urls),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout,name='logout'),
    path('signup/',views.userCreate,name='signup'),
    path('school-selection/',views.school_selection,name='school_selection'),
    path('class-selection/',views.class_selection,name='class_selection'),
    path('create-excel/',views.create_excel,name='create_excel'),
    path('class/delete/<pk>/',views.delete_class,name='delete_class'),
    path('class/update/<pk>/',views.updateClass,name='update_class'),
    path('upload/',views.upload,name='upload'),
    path('upload/mark-table/', views.mark_table, name='mark_table'),
    path('table/',views.table,name='table'),
    path('table/delete/<pk>/',views.delete_table,name='delete_table'),
    path('table/delete_all/',views.delete_all,name='delete_all'),
    path('table/delete_uploaded/',views.delete_uploaded,name='delete_uploaded'),
    path('table/delete_manuals/',views.delete_manuals,name='delete_manuals'),
    path('classDeleteAll/',views.classDeleteAll,name='classDeleteAll'),
    path('finalize/',views.finalize,name='finalize'),
    path('guide/',views.guide,name='guide'),
]
