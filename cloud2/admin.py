# Register your models here.
from django.contrib import admin
from cloud2.models import *
# Register your models here.
class PicAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(matukio)
admin.site.register(Meeting)
admin.site.register(grades)
admin.site.register(cattendance)
admin.site.register(session)
admin.site.register(Class)
admin.site.register(School)
admin.site.register(Seen)
admin.site.register(School1)
admin.site.register(Subject)
admin.site.register(homework)
admin.site.register(sbus)
admin.site.register(Online)
admin.site.register(Verified)
admin.site.register(Verified2)
admin.site.register(stagemine)
admin.site.register(info ,PicAdmin)
admin.site.register(tranzoia)
admin.site.register(hmss)
admin.site.register(hmss2)
admin.site.register(notef)
admin.site.register(checkoff)
#Profpic
admin.site.register(Profpic) 
admin.site.register(pics)
admin.site.register(category)
admin.site.register(Menu)
admin.site.register(Schedule)
admin.site.register(History)
#BUswise
admin.site.register(Schid)
#Freshfit starts here

admin.site.register(food)
admin.site.register(ategoryx)
admin.site.register(Menux)
admin.site.register(table)
admin.site.register(restaurant)
admin.site.register(order)
#order2
admin.site.register(order2)
admin.site.register(orderconf)
admin.site.register(Vcart)
admin.site.register(messageswick)
#Verflip
admin.site.register(unfo)
admin.site.register(event1)
admin.site.register(work1)
admin.site.register(bemjs)
#someapp
admin.site.register(mpatient)

