from django.urls import path
from . import views
from info.views import NoticeListView, NoticeDetailView,AssignmentListView, AssignmentDetailView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('admission/', views.admission, name='admission'),
    path('faculty/', views.faculty, name='faculty'),
    path('gallary/', views.gallary, name='gallary'),
    path('campus/', views.campus, name='campus'),
    #path('notice/', views.notice, name='notice'),
    path('notice/' , NoticeListView.as_view() , name = "notice-list"),
    path('notice/<int:pk>/', NoticeDetailView.as_view() , name = 'notice-detail' ),
    #path('assignment/', views.assignment, name='assignment'),
    path('assignment/' , AssignmentListView.as_view() , name = "assignment-list"),
    path('assignment/<int:pk>/', AssignmentDetailView.as_view() , name = 'assignment-detail' ),
    path('s/', views.noticesearch, name="noticesearch"),
    path('a/', views.assignmentsearch, name="assignmentsearch"),
#    path('feed/', views.feed, name='feed')
]
