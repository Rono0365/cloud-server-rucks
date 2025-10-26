from django.urls import path
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from cloud2 import views
from django.conf.urls.static import static
from django.conf import settings
from .views import upload_resume
from cloud import consumers

from django.urls import re_path
#from transit import *
#from elearn import *


urlpatterns = [
    path('upload_resume/',upload_resume, name = "files" ),
    path('students/', views.StudentList.as_view()),
    path('grades/', views.gradesList.as_view()),
    path('matukio/<int:pk>/', views.matukioDetail.as_view()),#for app user events
    path('matukios/', views.matukioList.as_view()),#for app user events
    
    path('cattendance/', views.cattendanceList.as_view()),
    path('sessions/', views.sessionList.as_view()),
    path('session/<int:pk>/', views.sessionDetail.as_view()),
    path('student/<int:pk>/', views.StudentDetail.as_view()),#mpatientDetail
    path('patient/<int:pk>/', views.mpatientDetail.as_view()),#mpatientDetail
    path('patients/', views.mpatientList.as_view()),#mpatientDetail
    path('me/<int:pk>/', views.userDetail.as_view()),
    path('try/<int:qu_id>', views.show_image),
    path('stages/', views.StageList.as_view()),
    path('buschedule/', views.scheduleList.as_view()),
    path('schools/', views.SchoolList.as_view()),
    path('schedulehistory/', views.historyList.as_view()),
    path('pics/', views.picList.as_view()),
    path('profpic/', views.profpicList.as_view()),
    path('online/', views.onlineList.as_view()),
    path('seen/', views.seenList.as_view()),
    path('verified/', views.verifiedList.as_view()),
    path('verified2/', views.verified2List.as_view()),
    path('subject/<int:pk>/', views.SubjectDetail.as_view()),
    path('HW/', views.hmm2List.as_view()),
    path('homework/<int:pk>/', views.homeworkDetail.as_view()),
    path('busloc/<int:pk>/',views.UpdatelocationView.as_view()),
    path('teachers/', views.TeacherList.as_view()),
    path('information/', views.infoList.as_view()),
    path('rollcall/', views.checkoffList.as_view()),#checkoffList
    path('notef/', views.notefList.as_view()),
    path('notefx/<int:pk>/', views.notefx.as_view()),
    path('Schools/', views.SchoolList.as_view()),
    path('transolution/', views.tranzoList.as_view()),
    path('Sbuss/', views.sbsDetail.as_view()),
    path('Subjects/', views.SubjectList.as_view()),
    path('classes/', views.ClassList.as_view()),
    path('homeworks/', views.homeworkList.as_view()),
    path('api-token-auth/', views.CustomAuthToken.as_view()),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    
    path('teachers/<int:pk>/', views.TeacherDetail.as_view()),
    #BUswise
    path('schid/', views.schidList.as_view()),
    
    #Freshfit urls start here
    
    path('registerff/', views.RegisterffView.as_view()),
    path('restaurant/', views.restaurantList.as_view()),
    path('restaurant/<int:pk>/', views.restaurantDetail.as_view()),
    
    path('api-token-auth_forfF/', views.CustomAuthTokenff.as_view()),
    path('meff/<int:pk>/', views.userffDetail.as_view()),
    re_path('api/chat/messages/<str:room_name>/', consumers.ChatConsumer.retrieve_room_messages),
    path('watus/', views.musers.as_view()),
    #path('table/<int:year>/<slug:slug>/', tableDetail.as_view()),
    path('table/<str:room>/', views.tableDetail.as_view()),
    path('meeting/<int:pk>/', views.meetingDetail.as_view()),
    path('meetings/', views.meetingList.as_view()),
    #name='article_detail'),
    path('orderx/', views.UpdateOrderView.as_view()),
    path('cart/', views.cartList.as_view()),
    path('chatff/', views.messageDetail.as_view()),
    path('orderconf/', views.orderconfDetail.as_view()),
    
    path('foodff/', views.foodList.as_view()),
    path('foods/', views.foodDetail.as_view()),
    path('orderff/', views.orderDetail.as_view()),
    path('orderf/<int:pk>/', views.UpdateOrderView.as_view()),
    #Verflip
    path('unfo/', views.unfoDetail.as_view()),
    path('work/<str:title2>/', views.workDetail2.as_view()),
    
    path('work/', views.workDetail.as_view()),
    path('event/', views.eventDetail.as_view()),
    path('bemjs/', views.bemjsDetail.as_view()),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#print("heelo"+str(settings.MEDIA_URL)+str(settings.MEDIA_ROOT))
