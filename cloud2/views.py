from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from django.conf import settings
from .models import Teacher
from django.http import Http404
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework import viewsets

class ChatViewSet(viewsets.ModelViewSet):
    queryset = notef.objects.all()
    serializer_class = notefSerializer

def upload_resume(request):
    if request.method == 'POST':
        form = infoSerializer(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/") 
    else:
        form = infoSerializer
    return render(request, 'files/resume.html', {'form':form})

# Create your views here. /home/afleetco/3
def show_image(request,qu_id):
    queryset = info.objects.get(pk=qu_id)
    if queryset is not None:
        print(queryset)
        return render(request,'pic.html',{'queryset': queryset})    
    else:
        raise Http404("Does not exist")
class CustomAuthToken(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            #'email': user.email
        })
class userDetail(generics.RetrieveUpdateDestroyAPIView):
    #lookup_field = 'pk'
    queryset = User.objects.all()
    serializer_class = userSerializer
class matukioList(generics.ListCreateAPIView):
    #lookup_field = 'pk'
    
    permission_classes = (AllowAny,)
    queryset = matukio.objects.all()
    serializer_class = matukioSerializer    
    def perform_create(self, serializer):
        serializer.save()    
class matukioDetail(generics.RetrieveUpdateDestroyAPIView):
    #lookup_field = 'pk'
    #permission_classes = (AllowAny,)
    queryset = matukio.objects.all()
    serializer_class = matukioSerializer    
class mpatientDetail(generics.RetrieveUpdateDestroyAPIView):
    #lookup_field = 'pk'
    queryset = mpatient.objects.all()
    serializer_class = mpatientSerializer   
class mpatientList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = mpatient.objects.all()
    serializer_class = mpatientSerializer

    def perform_create(self, serializer):
        serializer.save()    
class infodet(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = info.objects.all()
    serializer_class = infoSerializer
    def perform_create(self, serializer):
        return render(self, 'cloud/pic.html',{'queryset': queryset})    
        
class StageList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = stagemine.objects.all()
    serializer_class = stageSerializer

    def perform_create(self, serializer):
        serializer.save()
class gradesList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = grades.objects.all()
    serializer_class = gradeSerializer

    def perform_create(self, serializer):
        serializer.save() 
class cattendanceList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = cattendance.objects.all()
    serializer_class = cattendanceSerializer

    def perform_create(self, serializer):
        serializer.save()         
class sessionList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = session.objects.all()
    serializer_class = sessionSerializer

    def perform_create(self, serializer):
        serializer.save()       
class sessionDetail(generics.RetrieveUpdateDestroyAPIView):
    #lookup_field = 'pk'
    #permission_classes = (AllowAny,)
    queryset = session.objects.all()
    serializer_class = sessionSerializer            
class picList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = pics.objects.all()
    serializer_class = picsSerializer

    def perform_create(self, serializer):
        serializer.save() 
class schidList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Schid.objects.all()
    serializer_class = schidSerializer
    def perform_create(self, serializer):
        serializer.save()
class scheduleList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def perform_create(self, serializer):
        serializer.save()
class historyList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = History.objects.all()
    serializer_class = HistorySerializer

    def perform_create(self, serializer):
        serializer.save()        
class profpicList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Profpic.objects.all()
    serializer_class = profpicSerializer

    def perform_create(self, serializer):
        serializer.save()   
class verifiedList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Verified.objects.all()
    serializer_class = verifiedSerializer

    def perform_create(self, serializer):
        serializer.save()       
class verified2List(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Verified2.objects.all()
    serializer_class = verified2Serializer

    def perform_create(self, serializer):
        serializer.save()               
class onlineList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Online.objects.all()
    serializer_class = onlineSerializer

    def perform_create(self, serializer):
        serializer.save()       
class seenList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Seen.objects.all()
    serializer_class = seenSerializer

    def perform_create(self, serializer):
        serializer.save()               
class checkoffList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = checkoff.objects.all()
    serializer_class = checkoffSerializer

    def perform_create(self, serializer):
        serializer.save()        
class infoList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = info.objects.all()
    serializer_class = infoSerializer
    def perform_create(self, serializer):
        serializer.save()      
        return render(self, 'pic.html',{'movie': queryset})    
        
class StudentList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Student.objects.all()
    serializer_class = studentSerializer

    def perform_create(self, serializer):
        serializer.save()
class SchoolList(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def perform_create(self, serializer):
        serializer.save()
class tranzoList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = tranzoia.objects.all()
    serializer_class = tranzSerializer

    def perform_create(self, serializer):
        serializer.save()
class notefx(generics.RetrieveUpdateDestroyAPIView,generics.UpdateAPIView):
    permission_classes = (AllowAny,)
    queryset = notef.objects.all()
    serializer_class = notefSerializer
    def update(self, request, *args, **kwargs):
        instance = self.get_object()#model
        serializer = self.get_serializer(instance, data=request.data)
        #print(serializer)
        

        if serializer.is_valid():
            #serializer1 = order2.objects.filter(pk=instance.pk).update(ordertrak='ready')
            #print(instance.ordertrak)
            #Survey.objects.filter(pk=survey.pk).update(active=True)
            #print(record)
            instance.save()
            serializer.save()
            
            return Response(serializer.data)
        
        else:
            print('not valid serilizer')
            return Response(serializer.data)

class notefList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = notef.objects.all()
    serializer_class = notefSerializer

    def perform_create(self, serializer):
        serializer.save()        
class hmm2List(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = hmss2.objects.all()
    serializer_class = hmss2Serializer

    def perform_create(self, serializer):
        serializer.save()        
class SubjectList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Subject.objects.all()
    #permission_classes = (AllowAny,)
    serializer_class = SubjectSerializer

    def perform_create(self, serializer):
        serializer.save()
class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
class UpdatelocationView(generics.RetrieveUpdateDestroyAPIView,generics.UpdateAPIView):
    queryset = sbus.objects.all()
    serializer_class = sbsSerializer
    lookup_field = 'pk'
    permission_classes = (AllowAny,)   
    def update(self, request, *args, **kwargs):
        instance = self.get_object()#model
        serializer = self.get_serializer(instance, data=request.data)
        #print(serializer)
        

        if serializer.is_valid():
            #serializer1 = order2.objects.filter(pk=instance.pk).update(ordertrak='ready')
            #print(instance.ordertrak)
            #Survey.objects.filter(pk=survey.pk).update(active=True)
            #print(record)
            instance.save()
            serializer.save()
            
            return Response(serializer.data)
        
        else:
            print('not valid serilizer')
            return Response(serializer.data)    
class ClassList(generics.ListCreateAPIView):
    queryset = Class.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ClassSerializer

    def perform_create(self, serializer):
        serializer.save()
        #sbsSerializer
class sbsDetail(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = sbus.objects.all()
    serializer_class = sbsSerializer
    def perform_create(self, serializer):
        serializer.save()
         
class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def perform_create(self, serializer):
        serializer.save()
class homeworkList(generics.ListCreateAPIView):
    queryset = homework.objects.all()
    serializer_class = HomeworkSerializer

    def perform_create(self, serializer):
        serializer.save()
class homeworkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = homework.objects.all()
    serializer_class = HomeworkSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Student.objects.all()
    serializer_class = studentSerializer
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer          

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

#Freshfit begins here
class CustomAuthTokenff(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
class foodList(generics.ListCreateAPIView):
    queryset = food.objects.all()
    serializer_class = foodxSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save()
class foodDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = food.objects.all()
    serializer_class = foodxSerializer        
class cartList(generics.ListCreateAPIView):
    queryset = Vcart.objects.all()
    serializer_class = cartSerializer

    def perform_create(self, serializer):
        serializer.save()

class tableList(generics.ListCreateAPIView):
    queryset = table.objects.all()
    serializer_class = tableSerializer

    def perform_create(self, serializer):
        serializer.save()
class tableDetail(generics.RetrieveUpdateDestroyAPIView):
    #lookup_field = 'pk'
    queryset = table.objects.all()
    serializer_class = tableSerializer
class userffDetail(generics.RetrieveUpdateDestroyAPIView):
    #lookup_field = 'pk'
    queryset = User.objects.all()
    serializer_class = userfSerializer
    permission_classes = (AllowAny,)
    #filter_fields = ('name')
    # inside OrganisationDetail
    #ueryset = table.objects.all()
    '''
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        # make sure to catch 404's below
        obj = queryset.get(pk=self.request.user.table_id)
        self.check_object_permissions(self.request, obj)
        return obj
        # delete view for details
def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "delete_view.html", context)

    '''
       
class orderxDetail(generics.ListCreateAPIView):
    #lookup_field = 'pk'
    queryset = order.objects.all()
    #permission_classes = (AllowAny,)
   
    serializer_class = orderxSerializer
    def perform_create(self, serializer):
        serializer.save() 
    def update(self,request, serializer,*args,**kwargs):
        instance = self.get_object()
        instance.sender = self.get_user()
        serializer = self.get_serializer(instance,data = request.data)
        self.perform_update(serializer)
        return Response(serializer.data)    
class meetingDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Meeting.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = meetingSerializer

    # def perform_create(self, serializer):
    #     serializer.save()

    def get_user(self):
        if hasattr(self.request, 'user') and self.request.user.is_authenticated:
            return self.request.user
        return None # Replace with your actual logic

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        sender_user = self.get_user()
        if sender_user:
             serializer.save(sender=sender_user)
        else:
             serializer.save()
class meetingList(generics.ListCreateAPIView):
    lookup_field = 'pk'
    
    queryset = Meeting.objects.all()
    serializer_class = meetingSerializer
    permission_classes = (AllowAny,)

       
class RegisterffView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer          
class RestregisterView(generics.CreateAPIView):
    queryset = restaurant.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = restaurantSerializer      
class restaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    #lookup_field = 'pk'
    queryset = restaurant.objects.all()
    serializer_class = restaurantSerializer
class restaurantList(generics.ListCreateAPIView):
    queryset = restaurant.objects.all()
    serializer_class = restaurantSerializer

    def perform_create(self, serializer):
        serializer.save()
class musers(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = muserserializer

           
class UpdateOrderView(generics.RetrieveUpdateDestroyAPIView,generics.UpdateAPIView):
    queryset = order2.objects.all()
    serializer_class = orderSerializer
    lookup_field = 'pk'
    permission_classes = (AllowAny,)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()#model
        serializer = self.get_serializer(instance, data=request.data)
        #print(serializer)
        

        if serializer.is_valid():
            #serializer1 = order2.objects.filter(pk=instance.pk).update(ordertrak='ready')
            #print(instance.ordertrak)
            #Survey.objects.filter(pk=survey.pk).update(active=True)
            #print(record)
            instance.save()
            serializer.save()
            
            return Response(serializer.data)
        
        else:
            print('not valid serilizer')
            return Response(serializer.data)
class orderDetail(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView,generics.UpdateAPIView):
    #lookup_field = 'pk'
    queryset = order2.objects.all()
    permission_classes = (AllowAny,)
    
    #print(queryset)
    serializer_class = orderSerializer
    
    def perform_create(self, serializer):
        #self.id   
        serializer.save() 
    def update(self, request, *args, **kwargs):
        instance = self.get_object()#model
        serializer = self.get_serializer(instance, data=request.data)
        #print(serializer)
        

        if serializer.is_valid():
            #serializer1 = order2.objects.filter(pk=instance.pk).update(ordertrak='ready')
            #print(instance.ordertrak)
            #Survey.objects.filter(pk=survey.pk).update(active=True)
            #print(record)
            instance.save()
            serializer.save()
            
            return Response(serializer.data)
        
        else:
            print('not valid serilizer')
            return Response(serializer.data)
class orderconfDetail(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView,generics.UpdateAPIView):
    #lookup_field = 'pk'
    queryset = orderconf.objects.all()
    permission_classes = (AllowAny,)
    
    #print(queryset)
    serializer_class = orderconfSerializer
    
    def perform_create(self, serializer):
        #self.id   
        serializer.save() 
    def update(self, request, *args, **kwargs):
        instance = self.get_object()#model
        serializer = self.get_serializer(instance, data=request.data)
        #print(serializer)
        

        if serializer.is_valid():
            #serializer1 = order2.objects.filter(pk=instance.pk).update(ordertrak='ready')
            #print(instance.ordertrak)
            #Survey.objects.filter(pk=survey.pk).update(active=True)
            #print(record)
            instance.save()
            serializer.save()
            
            return Response(serializer.data)
        
        else:
            print('not valid serilizer')
            return Response(serializer.data)
#Verflip            
class unfoDetail(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView,generics.UpdateAPIView):
    #lookup_field = 'pk'
    queryset = unfo.objects.all()
    permission_classes = (AllowAny,)
    
    #print(queryset)
    serializer_class = unfoSerializer
    
    def perform_create(self, serializer):
        #self.id   
        serializer.save() 
    def update(self, request, *args, **kwargs):
        instance = self.get_object()#model
        serializer = self.get_serializer(instance, data=request.data)
        #print(serializer)
        

        if serializer.is_valid():
            #serializer1 = order2.objects.filter(pk=instance.pk).update(ordertrak='ready')
            #print(instance.ordertrak)
            #Survey.objects.filter(pk=survey.pk).update(active=True)
            #print(record)
            instance.save()
            serializer.save()
            
            return Response(serializer.data)
        
        else:
            print('not valid serilizer')
            return Response(serializer.data)
class eventDetail(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView,generics.UpdateAPIView):
    #lookup_field = 'pk'
    queryset = event1.objects.all()
    permission_classes = (AllowAny,)
    
    #print(queryset)
    serializer_class = eventSerializer
    
    def perform_create(self, serializer):
        #self.id   
        serializer.save() 
    def update(self, request, *args, **kwargs):
        instance = self.get_object()#model
        serializer = self.get_serializer(instance, data=request.data)
        #print(serializer)
        

        if serializer.is_valid():
            #serializer1 = order2.objects.filter(pk=instance.pk).update(ordertrak='ready')
            #print(instance.ordertrak)
            #Survey.objects.filter(pk=survey.pk).update(active=True)
            #print(record)
            instance.save()
            serializer.save()
            
            return Response(serializer.data)
        
        else:
            print('not valid serilizer')
            return Response(serializer.data)
class bemjsDetail(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView,generics.UpdateAPIView):
    #lookup_field = 'pk'
    queryset = bemjs.objects.all()
    permission_classes = (AllowAny,)
    
    #print(queryset)
    serializer_class = bemjsSerializer
    
    def perform_create(self, serializer):
        #self.id   
        serializer.save() 
    def update(self, request, *args, **kwargs):
        instance = self.get_object()#model
        serializer = self.get_serializer(instance, data=request.data)
        #print(serializer)
        

        if serializer.is_valid():
            #serializer1 = order2.objects.filter(pk=instance.pk).update(ordertrak='ready')
            #print(instance.ordertrak)
            #Survey.objects.filter(pk=survey.pk).update(active=True)
            #print(record)
            instance.save()
            serializer.save()
            
            return Response(serializer.data)
        
        else:
            print('not valid serilizer')
            return Response(serializer.data)            


class workDetail2(generics.RetrieveUpdateDestroyAPIView,generics.UpdateAPIView):
    lookup_field = 'title2'
    queryset = work1.objects.all()
    permission_classes = (AllowAny,)
    
    #print(queryset)
    serializer_class = workSerializer
    

class workDetail(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView,generics.UpdateAPIView):
    #lookup_field = 'pk'
    queryset = work1.objects.all()
    permission_classes = (AllowAny,)
    
    #print(queryset)
    serializer_class = workSerializer
    
    def perform_create(self, serializer):
        #self.id   
        serializer.save() 
    def update(self, request, *args, **kwargs):
        instance = self.get_object()#model
        serializer = self.get_serializer(instance, data=request.data)
        #print(serializer)
        

        if serializer.is_valid():
            #serializer1 = order2.objects.filter(pk=instance.pk).update(ordertrak='ready')
            #print(instance.ordertrak)
            #Survey.objects.filter(pk=survey.pk).update(active=True)
            #print(record)
            instance.save()
            serializer.save()
            
            return Response(serializer.data)
        
        else:
            print('not valid serilizer')
            return Response(serializer.data)            

class messageDetail(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView,generics.UpdateAPIView):
    #lookup_field = 'pk'
    queryset = messageswick.objects.all()
    permission_classes = (AllowAny,)
    
    #print(queryset)
    serializer_class = messageSerializer
    
    def perform_create(self, serializer):
        #self.id   
        serializer.save() 
    def update(self, request, *args, **kwargs):
        instance = self.get_object()#model
        serializer = self.get_serializer(instance, data=request.data)
        #print(serializer)
        

        if serializer.is_valid():
            #serializer1 = order2.objects.filter(pk=instance.pk).update(ordertrak='ready')
            #print(instance.ordertrak)
            #Survey.objects.filter(pk=survey.pk).update(active=True)
            #print(record)
            instance.save()
            serializer.save()
            
            return Response(serializer.data)
        
        else:
            print('not valid serilizer')
            return Response(serializer.data)        
        """'table': i['table'],
                                                        'food': i[
                                                            'food'], //list for food
                                                        'restaurantx':
                                                            i['restaurantx'],
                                                        'time': i['time'],
                                                        'owner': i['owner'],
                                                        //$sum
                                                        'totalprice':
                                                            i['totalprice'],
                                                        'ordertype':
                                                            i['ordertype'],
                                                        'ordername':
                                                            i['ordername'],
                                                        'ordertrak': 'ready',
                                                        'ordertime':
                                                            i['ordertime'],"""