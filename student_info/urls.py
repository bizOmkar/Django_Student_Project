from django.urls import path
from . import views


urlpatterns = [
    path('',views.StudentsListView.as_view(),name='index'),
    path('detail_info/<int:pk>', views.StudentDetailView.as_view(),name='detail_info'),
    path('new_student/', views.StudentCreateView.as_view(), name="new_student"),
    path('edit/<int:pk>', views.StudentUpdateView.as_view(), name='edit_student'),
    path('delete/<int:pk>', views.StudentDeleteView.as_view(), name='delete_student'),
    path('edit_mark/', views.MarkUpdateView.as_view(), name='edit_mark'),
    
    
]