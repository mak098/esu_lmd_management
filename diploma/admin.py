from django.contrib import admin
from .models import Order,Diploma,OrderHistory,DiplomaHistory

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display =['id','school','reference_payment','amount','quantity']
    

@admin.register(Diploma)
class DiplomaAdmin(admin.ModelAdmin):
    pass
@admin.register(OrderHistory)
class OrderHistoryAdmin(admin.ModelAdmin):
    pass
@admin.register(DiplomaHistory)
class DiplomaHistoryAdmin(admin.ModelAdmin):
    pass