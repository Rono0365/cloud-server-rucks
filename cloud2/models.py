from django.db import models
from django.contrib.auth.models import User

class School1(models.Model):
    name = models.CharField(max_length=10,default='he')
    
class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default='he')
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE,default='')
class homework(models.Model):
    name = models.CharField(max_length=100,default = 'no homework')
    Class = models.ManyToManyField('Class', blank=True)
    #subject = models.ForeignKey('Subject',on_delete=models.CASCADE)
    deadline = models.CharField(max_length=100,default = '')
    #students = models.ManyToManyField('Student')
#create transit routes     

class category(models.Model):#day
    day = models.CharField(max_length=100,default = 'c')
    food =  models.ManyToManyField('Subject')       
class Menu(models.Model):#timetable
    menu = models.ManyToManyField('category')
class Class(models.Model):
    name = models.CharField(max_length=100,default = '')  
    owner = models.CharField(max_length=100, blank=True, default='')
    menu = models.CharField(max_length=100,default='menu')
    session = models.CharField(max_length=100,default = 'yes')
    school = models.CharField(max_length=100,default='school')
    #subjects = models.ManyToManyField('Subject')
class Classx(models.Model):
    name = models.CharField(max_length=100,default = '')  
    owner = models.CharField(max_length=100, blank=True, default='')
    menu = models.CharField(max_length=100,default='menu')
    
    school = models.CharField(max_length=100,default='school')
    #subjects = models.ManyToManyField('Subject')    
class hmss(models.Model):
    name = models.CharField(max_length=100,default = 'headline') #headline
    topic = models.CharField(max_length=100,default='samdhing real')
    mclass = models.CharField(max_length=100,default='samdhing real')
class session(models.Model):#using this to mark done events 
    name = models.CharField(max_length=100,default = 'no') #headline
    school = models.CharField(max_length=100,default = 'not done') #date
    
class grades(models.Model):
    name = models.CharField(max_length=100,default = 'no') #headline
    school = models.CharField(max_length=100,default = 'no') #date
    klass = models.CharField(max_length=100,default = 'no')
    session = models.CharField(max_length=100,default = 'yes')
    adm_no = models.CharField(max_length=100,default = 'no')
    subject = models.CharField(max_length=10000,default = 'no') #hell yeadh
class cattendance(models.Model):
    name = models.CharField(max_length=100,default = 'no') #headline
    school = models.CharField(max_length=100,default = 'no') #date
    klass = models.CharField(max_length=100,default = 'no')
    day = models.CharField(max_length=100,default = 'yes')
    adm_no = models.CharField(max_length=100,default = 'no')
    state = models.CharField(max_length=100,default = 'no')
       
class hmss2(models.Model):
    name = models.CharField(max_length=100,default = 'no') #headline
    date = models.CharField(max_length=100,default = 'no') #date
    lass = models.CharField(max_length=100,default = 'no')
    school = models.CharField(max_length=100,default = 'no')
    subject = models.CharField(max_length=100,default = 'no') #date
class pics(models.Model):
    id = models.AutoField(primary_key=True)
    image =models.CharField(max_length=10000, null=True, default='')#
class Profpic(models.Model):
    id = models.AutoField(primary_key=True)
    username1 = models.CharField(max_length=1000,default = 'none')#name of user  
    image =models.CharField(max_length=10000, null=True, default='')#
class Online(models.Model):
    id = models.AutoField(primary_key=True)
    username1 = models.CharField(max_length=1000,default = 'none')#name of user
    
    image =models.CharField(max_length=10000, null=True, default='')#
class Seen(models.Model):
    id = models.AutoField(primary_key=True)
    username1 = models.CharField(max_length=1000,default = 'none')#name of user
    
    image =models.CharField(max_length=1000, null=True, default='')#    
class Verified(models.Model):
    id = models.AutoField(primary_key=True)
    username1 = models.CharField(max_length=1000,default = 'none')#name of user
    
    image =models.CharField(max_length=10000, null=True, default='')#    
class Verified2(models.Model):#link for user and student
    id = models.AutoField(primary_key=True)
    username1 = models.CharField(max_length=1000,default = 'none')#name of user
    
    image =models.CharField(max_length=10000, null=True, default='')#        
class stagemine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000,default = '')#name of stage  
    place =models.CharField(max_length=1000, blank=True, default='')#
    coordinates = models.CharField(max_length=1000,default = '')  
    school = models.CharField(max_length=100,default='samdhing real')
    
    usernamemi =  models.CharField(max_length=1000,default = 'nouser')
    curbus = models.CharField(max_length=1000,default = 'xon')
    #subject = models.ManyToManyField(Student) 
class info(models.Model):
    id = models.AutoField(primary_key=True)
    whoiswho =  models.CharField(max_length=1000,default = 'whoiswho')
    to = models.CharField(max_length=1000,default = 'noo')#name of stage 
    tag = models.CharField(max_length=1000,default = 'nooo')#name of stage 
    location = models.CharField(max_length=1000,default = '')#name of stage 
    writer =models.CharField(max_length=1000, blank=True, default='anonymous')#
    mation = models.CharField(max_length=10000,default = '')  
    title =  models.CharField(max_length=1000,default = 'notitle')
    image1 = models.TextField(default='notitle')
    image2 = models.TextField(default='notitle')
    image3 = models.TextField(default='notitle')
    image = models.TextField(default='notitle')#ImageField(upload_to= 'files/',null = True)
    delete = models.CharField(max_length=10,default = 'no')
    date = models.CharField(max_length=1000,default = 'no date')    #
    class Meta:
        
        ordering =['id']    
    def __str__(self):
        return f'{self.whoiswho} to {self.to} by {self.writer}'    
class sbus(models.Model):
    id = models.AutoField(primary_key=True)
    nameq =models.CharField(unique=True,max_length=100, blank=True, default='')
    place =models.CharField(max_length=100, blank=True, default='')
    owner = models.CharField(max_length=100, blank=True, default='')
    
    school = models.CharField(max_length=100,default='samdhing real')
    commute = models.CharField(max_length=100,default='off')
    cordinates = models.CharField(max_length=100, blank=True, default='')    
class Student(models.Model):
    id = models.AutoField(primary_key=True)
   
    #created = models.DateTimeField(auto_now_add=True)
    School = models.TextField(default='School')
    Class = models.CharField(max_length=100,default = '')
    owner = models.CharField(max_length=100, blank=True, default='')
    profpic = models.CharField(max_length=10000, null=True ,default='jello')
    adm_no = models.CharField(max_length=100, blank=True, default='',unique=True)
    
    class Meta:
        ordering = ['adm_no']
class tranzoia(models.Model):
    id = models.AutoField(primary_key=True)
    sc = models.CharField(max_length=100,blank=True, default='')   
    bi = models.CharField(max_length=100,blank=True, default='') 
    school = models.CharField(max_length=100,default='samdhing real')
    
    userN = models.CharField(max_length=100,blank=True, default='')
class notef(models.Model):
    id = models.AutoField(primary_key=True)
    titles = models.CharField(max_length=100,blank=True, default='titles')
    state = models.CharField(max_length=100,blank=True, default='offline')
    numbx = models.CharField(max_length=100,blank=True, default='old')
    useryou = models.CharField(max_length=100,blank=True, default='none')  
class checkoff(models.Model):
    id = models.AutoField(primary_key=True)
    checkIn = models.CharField(max_length=100,blank=True, default='notyet')
    checkout = models.CharField(max_length=100,blank=True, default='notyet')
    driver = models.CharField(max_length=100,blank=True, default='dere')
    useryou = models.CharField(max_length=100,blank=True, default='child')
    datetime = models.CharField(max_length=100,blank=True, default='time')          
class Teacher(models.Model):
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')
    #owner = models.ForeignKey('auth.User', on_delete=models.CASCADE,unique=True,default='')
    
    #created = models.DateTimeField(auto_now_add=True)
    School = models.CharField(max_length=100, blank=True, default='')
    #Subjectz = models.ForeignKey('Subject',default = '',on_delete=models.CASCADE)
    adm_no = models.CharField(max_length=100, blank=True, default='')
    #Subjects =  models.ForeignKey(SubjectsV,default = '',on_delete=models.CASCADE)
    class Meta:
        ordering = ['first_name']
class Meeting(models.Model):
    title = models.CharField(max_length=255)
    day = models.CharField(max_length=255,default="todaay")
    start_time = models.CharField(max_length=255,default="timezone.now")
    end_time = models.CharField(max_length=255,default="timezone.now")
    color = models.CharField(max_length=255, default="#FF5722")  # Store color as hex code
    is_all_day = models.CharField(max_length=255,default="False")
    room = models.CharField(max_length=255,default="notspecified")
    username = models.CharField(max_length=150)  # Assuming username is a string
    prioritylevel= models.CharField(max_length=150,default="normal")
    #rioritylevel= models.CharField(max_length=150,default="normal")
    def __str__(self):
        return self.title        
class Subject(models.Model):
    headline = models.CharField(max_length=100)
    #n_students = models.ManyToManyField(Student,default='')
    school = models.CharField(max_length=100,default='samdhing real')
    Class =  models.CharField(max_length=100,default='samng real')
    
    code =models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    
    
    class Meta:
        ordering = ['headline']
        
class Schedule(models.Model):
    Location = models.CharField(max_length=100,default='pronto')
    #n_students = models.ManyToManyField(Student,default='')
    day = models.CharField(max_length=100,default='prontoday')#self arrange in the timetable
    trip = models.CharField(max_length=100,default='prontotrip')#self arrange in the timetable
    occurence = models.CharField(max_length=100,default='prontoccurence')#self arrange in the timetable
    driver = models.CharField(max_length=100, default='dere')#self arrange in the timetable
    session = models.CharField(max_length=100, default='sess')#self arrange in the timetable
class History(models.Model):
    daydate = models.CharField(max_length=100,default='prontoday')#self arrange in the timetable
    time = models.CharField(max_length=100,default='prontotrip')#self arrange in the timetable
    dist = models.CharField(max_length=100,default='prontoccurence')#self arrange in the timetable
    student_number = models.CharField(max_length=100, default='dere')#self arrange in the timetable
    est_fuel = models.CharField(max_length=100, default='sess')#self arrange in the timetable    
#Buswise school id model

class Schid(models.Model):
    id = models.AutoField(primary_key=True)
    schoolID = models.CharField(max_length=1000,default='schid')
    school = models.CharField(max_length=1000,default='Sch')
    childname = models.CharField(max_length=1000,default='childname')
    
 
#Freshfit models start here

class food(models.Model):#Subject
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default='game1')
    price = models.CharField(max_length=100,default='game1')
    points = models.CharField(max_length=100,default='1')
    save1 = models.CharField(max_length=100,default='1')
    
    count = models.CharField(max_length=100,default='1')
    image_url = models.TextField(default='notitle')
    def __str__(self):
        return f'{self.name}'
class ategoryx(models.Model):#day
    name = models.CharField(max_length=10000,default='x')
    image =  models.CharField(max_length=10000,default='1')
    caption = models.CharField(max_length=10000,default='x')
    food =  models.ManyToManyField(food)
class Menux(models.Model):#timetable
    menu = models.ManyToManyField(ategoryx, blank=True)
class table(models.Model):
    #menu = models.ManyToManyField(food)
    name = models.CharField(max_length=10000,default='x')
    #order =  models.ManyToManyField(food)
    #restaurant =  models.ForeignKey('restaurant',on_delete=models.CASCADE)
    menu = models.ManyToManyField(Menux, blank=True)
    slug = models.SlugField(null=True , unique=True) # new
        
    '''
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})
    '''
class restaurant(models.Model):
    
    #menu = models.ManyToManyField(food)
    id = models.AutoField(primary_key=True)
    username =  models.ForeignKey(User, on_delete=models.CASCADE, default='game1')
    location = models.CharField(max_length=100,default='game1')
    city = models.CharField(max_length=100,default='game1')
    image_of_restaurant = models.TextField(default='notitle')
    orders = models.ManyToManyField('order2', blank=True)
    menu = models.ManyToManyField(Menux, blank=True)
    #ownert = models.ForeignKey('auth.User', on_delete=models.CASCADE, default='game1')
    
class order(models.Model):
    #name = models.CharField(max_length=100,default='game1')
    #table = models.ForeignKey(table,on_delete=models.CASCADE)
    food =  models.CharField(max_length=100,default='game1')
class messageswick(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default='game1')
    
    sender = models.TextField(default='notitle')
    message_me =  models.TextField(default='notitle')
    receiver  =  models.CharField(max_length=100,default='game1')
    time = models.CharField(max_length=100,default='game1')
    
class order2(models.Model):
    id = models.AutoField(primary_key=True)
    #name = models.CharField(max_length=100,default='game1')
    table = models.CharField(max_length=100,default='game1')
    owner = models.TextField(default='notitle')
    food =  models.TextField(default='notitle')
    restaurantx  =  models.CharField(max_length=100,default='game1')
    time = models.CharField(max_length=100,default='game1')
    totalprice = models.CharField(max_length=100,default='game1')
    ordertype = models.CharField(max_length=100,default='game1')
    orderlocation = models.CharField(max_length=100,default='game1')
    ordertrak = models.CharField(max_length=100,default='game1')
    ordertime = models.CharField(max_length=100,default='game1')
    def __str__(self):
        return f'{self.owner} at {self.time}'

class orderconf(models.Model):
    id = models.AutoField(primary_key=True)
    #name = models.CharField(max_length=100,default='game1')
    Mpesacode = models.CharField(max_length=100,default='game1')
    owner = models.TextField(default='notitle')
    location =  models.CharField(max_length=100,default='game1')
    time = models.CharField(max_length=100,default='game1')
    totalprice = models.CharField(max_length=100,default='game1')
    
    def __str__(self):
        return f'{self.owner} at {self.time} mpesacode is {self.Mpesacode}'        

class Vcart(models.Model):
    #name = models.CharField(max_length=100,default='game1')
    count = models.CharField(max_length=100,default='1')
    food =  models.CharField(max_length=10000,default='1')
#Verflip
class unfo(models.Model):
    id = models.AutoField(primary_key=True)
    #name = models.CharField(max_length=100,default='game1')
    username = models.CharField(max_length=100,default='game1')
    likes = models.TextField(default='notitle')
    skills = models.TextField(default='notitle')
    location =  models.CharField(max_length=100,default='game1')
    
    def __str__(self):
        return f'{self.username} from {self.location}' 
class work1(models.Model):
    id = models.AutoField(primary_key=True)
    title2 = models.CharField(max_length=100,default='event title')
    username = models.CharField(max_length=100,default='game1')
    salary = models.TextField(default='notitle')
    skills = models.TextField(default='notitle')
    title =  models.CharField(max_length=100,default='game1')
    location =  models.CharField(max_length=100,default='game1')
    time =  models.CharField(max_length=100,default='time')
    
    def __str__(self):
        return f'{self.title} from {self.location}'
class event1(models.Model):
    id = models.AutoField(primary_key=True)
    #name = models.CharField(max_length=100,default='game1')
    username = models.CharField(max_length=100,default='game1')
    #salary = models.TextField(default='notitle')
    date = models.TextField(default='notitle')
    skills = models.TextField(default='notitle')
    title =  models.TextField(default='notitle')
    location =  models.CharField(max_length=100,default='game1')
    
    def __str__(self):
        return f'{self.title} from {self.location}'        
class bemjs(models.Model):
    id = models.AutoField(primary_key=True)
    #name = models.CharField(max_length=100,default='game1')
    username = models.CharField(max_length=100,default='game1')
    quantity = models.TextField(default='notitle')
    emojiname = models.TextField(default='notitle')
    
    def __str__(self):
        return f'{self.username} bought {self.quantity} {self.emojiname}'

#some medical app

class mpatient(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100,default='game1')
    username = models.CharField(max_length=100,default='game1')
    fl = models.TextField(default='notitle')
    dob = models.TextField(default='notitle')
    gender = models.TextField(default='notitle')
    location = models.TextField(default='notitle')
    county = models.TextField(default='notitle')
    country = models.TextField(default='notitle')
    postalcode = models.TextField(default='notitle')
    phonenumber = models.TextField(default='notitle')
    emcontact = models.TextField(default='notitle')
    emcontact2 = models.TextField(default='notitle')
    bloodtype = models.TextField(default='notitle')
    allergies = models.TextField(default='notitle')
    medhistory = models.TextField(default='notitle')
#to be continued    
class matukio(models.Model):
    id = models.AutoField(primary_key=True)
    #name = models.CharField(max_length=100,default='game1')
    username = models.CharField(max_length=100,default='game1')
    usertype = models.TextField(default='notitle')
    datetime = models.TextField(default='notitle')
    sessiontime = models.TextField(default='notitle')
    event = models.TextField(default='notitle')
    device =  models.TextField(default='notitle')
    geolocation =  models.CharField(max_length=100,default='game1')
    
    
  