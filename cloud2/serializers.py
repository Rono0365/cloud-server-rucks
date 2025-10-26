from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
class sessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = session
        fields = ['name','school']
        
class gradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = grades
        fields = ['name','klass','school','adm_no','subject','session']

class cattendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = cattendance
        fields = ['name','klass','school','adm_no','day','state']        
        
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['first_name','last_name','School','adm_no','Subjectz']
class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields =['daydate','time','dist','student_number','est_fuel'] 
class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['Location' ,'day' ,'trip' ,'occurence' ,'driver','session']        
class sbsSerializer(serializers.ModelSerializer):
    #permission_classes = (AllowAny,)
    owner = serializers.ReadOnlyField(source='owner.username')
   
    class Meta:
        model = sbus
        fields = ['id','nameq','school','owner','commute','place','cordinates']   
class stageSerializer(serializers.ModelSerializer):
    #permission_classes = (AllowAny,)
    class Meta:
        model = stagemine
        fields = ['id','name','place','coordinates','usernamemi','curbus']     
#BUswise
class schidSerializer(serializers.ModelSerializer):
    #permission_classes = (AllowAny,)
    class Meta:
        model = Schid
        fields = ['id','schoolID',' school','childname']     
#someapp
class mpatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = mpatient
        fields = ['id','email','username','fl','dob','gender','location','county','country','postalcode','phonenumber','emcontact','emcontact2','bloodtype','allergies','medhistory']
        
'''
class matukio(models.Model):
    id = models.AutoField(primary_key=True)
    #name = models.CharField(max_length=100,default='game1')
    username = models.CharField(max_length=100,default='game1')
    #salary = models.TextField(default='notitle')
    datetime = models.TextField(default='notitle')
    sessiontime = models.TextField(default='notitle')
    event = models.TextField(default='notitle')
    device =  models.TextField(default='notitle')
    geolocation =  models.CharField(max_length=100,default='game1')
    
    def __str__(self):
'''
class matukioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = matukio
        fields = ['id','username','usertype','datetime','sessiontime','event','device','geolocation']
         
#info
class profpicSerializer(serializers.ModelSerializer):
    #permission_classes = (AllowAny,)
    #image=serializers.ImageField(max_length=200,use_url=True)
    class Meta:
        model = Profpic
        fields = ['id','username1','image']
class onlineSerializer(serializers.ModelSerializer):
    #permission_classes = (AllowAny,)
    #image=serializers.ImageField(max_length=200,use_url=True)
    class Meta:
        model = Online
        fields = ['id','username1','image'] 
class seenSerializer(serializers.ModelSerializer):
    #permission_classes = (AllowAny,)
    #image=serializers.ImageField(max_length=200,use_url=True)
    class Meta:
        model = Seen
        fields = ['id','username1','image']         
class verifiedSerializer(serializers.ModelSerializer):
    #permission_classes = (AllowAny,)
    #image=serializers.ImageField(max_length=200,use_url=True)
    class Meta:
        model = Verified
        fields = ['id','username1','image']   
class verified2Serializer(serializers.ModelSerializer):
    #permission_classes = (AllowAny,)
    #image=serializers.ImageField(max_length=200,use_url=True)
    class Meta:
        model = Verified2
        fields = ['id','username1','image']           
class picsSerializer(serializers.ModelSerializer):
    #permission_classes = (AllowAny,)
    #image=serializers.ImageField(max_length=200,use_url=True)
    class Meta:
        model = pics
        fields = ['id','image']        
class infoSerializer(serializers.ModelSerializer):
    #permission_classes = (AllowAny,)
    #image=serializers.ImageField(max_length=200,use_url=True)
    class Meta:
        model = info
        fields = ['id','to','whoiswho','writer','to','location','tag','mation','image','image1','image2','image3','title','date']       
class checkoffSerializer(serializers.ModelSerializer):
    #permission_classes = (AllowAny,)
    """
    checkIn = models.CharField(max_length=100,blank=True, default='notyet')
    checkout = models.CharField(max_length=100,blank=True, default='notyet')
    useryou = models.CharField(max_length=100,blank=True, default='child')
    datetime = models.CharField(max_length=100,blank=True, default='time') 
    """
    class Meta:
        model = checkoff
        fields = ['id','checkIn','checkout','useryou','datetime','driver']               

#tranzoia
#hmss2 

class tranzSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = tranzoia
        fields = ['id','sc','bi','userN']
class notefSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = notef
        fields = ['id','state','titles','useryou','numbx']
class SchoolSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = School
        fields = ['name','owner']
class SubjectSerializer(serializers.ModelSerializer):
    #homework = serializers.ReadOnlyField(source='homework.name')    
    class Meta:
        #unique_together = (('headline','day_taught','time_duration','time_taught','code','teacher','place_taught'),)
        model = Subject
        
        
        fields = ['headline','Class','school','code','teacher']
class categorySerializer(serializers.ModelSerializer):
    food = SubjectSerializer(many=True)
    class Meta:
        model =  category
        fields = ['day','food']        
class menuSerializer(serializers.ModelSerializer):
    menu = categorySerializer(many=True)
    class Meta:
        model =  Menu
        fields = ['menu']        
class hmss2Serializer(serializers.ModelSerializer):
    
    #subject = SubjectSerializer(many=True)
    class Meta:
        model = hmss2
        fields = ['name','date','lass','school','subject']

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
class studentSerializer(serializers.ModelSerializer):
    #homework = serializers.ReadOnlyField(source='homework.name')
    #Subjects = serializers.SerializerMethodField('Subject.headline')
    #username = serializers.ReadOnlyField(source='owner.username')
    #Subjects = SubjectSerializer(many=True)
    #Class = serializers.ReadOnlyField(source='Class.name')
    #School = serializers.ReadOnlyField(source='School.name')
    
    
    class Meta:
         ordering =['id']
         model = Student
         fields = ['id','School','adm_no','owner','Class','profpic']#,'stateNF','userNM','newmssg']

class ClassSerializer(serializers.ModelSerializer):
    #subjects = SubjectSerializer(many=True)
    
    class Meta:
        model = Class
        fields = ['name','school','owner','menu','session']
class HomeworkSerializer(serializers.ModelSerializer):
    # = serializers.ReadOnlyField(source='Class.name')
    #name = serializers.ReadOnlyField(source='Subject.headline')#headline
    Class = serializers.ReadOnlyField(source='Class.name')
    #homework = serializers.ReadOnlyField(source='homework.name')    
    class Meta:
        model = homework
        fields = ['name','deadline','Class']        
class RegisterSerializer(serializers.ModelSerializer,):
    permission_classes = []
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user   

#freshfit begins here        

class userfSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','id','email']

class foodxSerializer(serializers.ModelSerializer):
    class Meta:
        model = food
        fields = ['id','name','price','count','points','save1','image_url']
class meetingSerializer(serializers.ModelSerializer):
    ''''
    title = models.CharField(max_length=255)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    color = models.CharField(max_length=7, default="#FF5722")  # Store color as hex code
    is_all_day = models.BooleanField(default=False)
    username = models.CharField(max_length=150)  # Assuming username is a string

    '''
    class Meta:
        model = Meeting
        fields = ['id','title','start_time','end_time','color','is_all_day','username','day','prioritylevel','room']        
class cartSerializer(serializers.ModelSerializer):
    food = foodxSerializer(many=True)
    class Meta:
        model = Vcart
        fields = ['count','food']
class muserserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','id','email']
       
class ategoryxSerializer(serializers.ModelSerializer):
    food = foodxSerializer(many=True)
    class Meta:
        model =  ategoryx
        fields = ['name','caption','food','image']        
class menuxSerializer(serializers.ModelSerializer):
    menu = ategoryxSerializer(many=True)
    class Meta:
        model =  Menux
        fields = ['menu']

class tableSerializer(serializers.ModelSerializer):
    #restaurant = serializers.ReadOnlyField(source='restaurant.name')
    menu = menuxSerializer(many=True)
    #order = foodSerializer(many=True)
    class Meta:
         model = table
         fields = ['name','menu']


class messageSerializer(serializers.ModelSerializer):
    #food = foodSerializer(many=True)
    #table = serializers.ReadOnlyField(source='order2.id')
    #add table nameUnsupported Media Type: /order2/
    #username = serializers.ReadOnlyField(source='owner.username')#owner.username
    #lastname = serializers.ReadOnlyField(source='owner.last_name')
    #orderxx = serializers.PrimaryKeyRelatedField(queryset=order2.objects.all())
    
    class Meta:
        model = messageswick
        fields = ['id','name','sender','message_me','receiver','time']#,'customer' 

class orderSerializer(serializers.ModelSerializer):
    #food = foodSerializer(many=True)
    #table = serializers.ReadOnlyField(source='order2.id')
    #add table nameUnsupported Media Type: /order2/
    #username = serializers.ReadOnlyField(source='owner.username')#owner.username
    #lastname = serializers.ReadOnlyField(source='owner.last_name')
    #orderxx = serializers.PrimaryKeyRelatedField(queryset=order2.objects.all())
    
    class Meta:
        model = order2
        fields = ['id','table','food','owner','restaurantx','time','totalprice','ordertype','orderlocation','ordertrak','ordertime']#,'customer' 
class orderconfSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = orderconf
        fields = ['id','Mpesacode','owner','location','time','totalprice']#,'customer'         
class restaurantSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='username.username')
    
    menu = menuxSerializer(many=True)
    orders = orderSerializer(many=True)
    #'namer'
    class Meta:
        model =  restaurant
        fields = ['id','location','city','orders','menu','username','image_of_restaurant']                

class orderxSerializer(serializers.ModelSerializer):
    #food = foodSerializer(many=True)
    #table = serializers.ReadOnlyField(source='table.name')
    #add table nameUnsupported Media Type: /order2/
    
    class Meta:
        model = order
        fields = ['food']#,'customer' 

class RegisterSerializer(serializers.ModelSerializer,):
    permission_classes = []
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user   
#Verflip//wave//onestack
class unfoSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = unfo
        fields = ['id','username','likes','location','skills']
class workSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = work1
        fields = ['id','username','skills','location','time','title','title2','salary']
class bemjsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = bemjs
        fields = ['id','username','quantity','emojiname']        
class eventSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = event1
        fields = ['id','username','skills','date','title','location']        
