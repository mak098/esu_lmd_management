from django.db import models
from django.conf import settings
from authentication.models import School

class Order(models.Model):
    school = models.ForeignKey(School,null=True, blank=True,on_delete=models.PROTECT,related_name='shool_order' ,verbose_name='school order' )
    order_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,on_delete=models.PROTECT,related_name='order_created_by' ,verbose_name='order by' )
    reference_payment= models.CharField(max_length=350, blank=False, verbose_name='Reference payment')
    payment_mode= models.CharField(max_length=350, blank=False, verbose_name='Payment Mode')
    date_payment = models.DateField(blank=False, verbose_name='Date Payment')
    amount = models.FloatField(default=0.00, blank=False, verbose_name='amount')
    quantity = models.IntegerField(blank=False, verbose_name='quantity')
    proof_of_payment = models.FileField(upload_to ='order/proof_of_payment/', verbose_name="proof of payment")
    bedrock_file = models.FileField(upload_to ='order/bedrock_file/', verbose_name="bedrock file")
    diploma_file = models.FileField(upload_to ='order/diploma_file/', verbose_name="diploma file")
    status = models.CharField(max_length=20, blank=True,  default='waiting',
		choices=(
			('waiting', 'waiting'),
			('approved', 'approved'),
			('rejected', 'rejected')			
		),
        verbose_name='Status',
    )
    approve_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,on_delete=models.PROTECT,related_name='order_approve_by' ,verbose_name='approve by' )
    reject_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,on_delete=models.PROTECT,related_name='order_reject_by' ,verbose_name='reject by' )
    approved_at = models.DateTimeField(blank=True,null=True,verbose_name='approved at')
    rejected_at = models.DateTimeField(blank=True,null=True,verbose_name='Rejected at')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.id}"
    class Meta:
        verbose_name_plural = "Orders"
        db_table = "orders"


class Diploma(models.Model):
    order = models.ForeignKey(Order,null=True, blank=True,on_delete=models.PROTECT,related_name='diploma_order' ,verbose_name='diploma order')    
    approve_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,on_delete=models.PROTECT,related_name='diploma_approve_by' ,verbose_name='approved by' )
    number = models.CharField(max_length=15,default='-',null=True, blank=True, verbose_name='Number')
    student_name = models.CharField(max_length=50,default='-',null=True, blank=True, verbose_name='Student name')
    place_of_birth = models.CharField(max_length=50,default='-',null=True, blank=True, verbose_name='place of birth')
    date_of_birth = models.CharField(max_length=50,default='-',null=True, blank=True, verbose_name='date of birth')
    gender = models.CharField(max_length=20, blank=True,  default='male',
		choices=(
			('male', 'male'),
			('female', 'female')			
		),
        verbose_name='Gender',
    )
    level = models.CharField(max_length=20, blank=True,  default='LICENCE',
		choices=(
			('LICENCE', 'LICENCE'),
			('MAITRISE', 'MAITRISE'),			
			('DOCTORAT', 'DOCTORAT'),			
			('BREVET', 'BREVET'),			
		),
        verbose_name='level',
    )
    faculty = models.CharField(max_length=256,default='-',null=True, blank=True, verbose_name='faculty')
    option = models.CharField(max_length=256,default='-',null=True, blank=True, verbose_name='option')
    mention = models.CharField(max_length=256,default='-',null=True, blank=True, verbose_name='mention')
    academic_year = models.CharField(max_length=10,default='-',null=True, blank=True, verbose_name='academic year')
    # homologation
    approval_number = models.CharField(max_length=256,default='-',null=True, blank=True, verbose_name='approval number')
    folio_number = models.CharField(max_length=256,default='-',null=True, blank=True, verbose_name='folio number')
    literal_number = models.CharField(max_length=256,default='-',null=True, blank=True, verbose_name='literal number')
    approval_date = models.DateTimeField(blank=True,null=True,verbose_name='counterpart at')
    
    sign_at = models.DateTimeField(blank=True,null=True,verbose_name='sign at')
    
    status = models.CharField(max_length=20, blank=True,  default='waiting',
		choices=(
			('waiting', 'waiting'),
			('approved', 'approved'),
			('printed', 'printed'),
			('rejected', 'rejected')			
		),
        verbose_name='Status',
    )
    approve_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,on_delete=models.PROTECT,related_name='diploma_approve_by' ,verbose_name='approve by' )
    printed_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,on_delete=models.PROTECT,related_name='diploma_printed_by' ,verbose_name='printed by' )
    reject_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,on_delete=models.PROTECT,related_name='diploma_reject_by' ,verbose_name='reject by' )
    approved_at = models.DateTimeField(blank=True,null=True,verbose_name='approved at')
    printed_by = models.DateTimeField(blank=True,null=True,verbose_name='printed at')
    rejected_at = models.DateTimeField(blank=True,null=True,verbose_name='Rejected at')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.number}"
    class Meta:
        verbose_name_plural = "Diplomas"
        db_table = "diplomas"

class OrderHistory(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT,related_name='order_history' ,verbose_name='Order')
    comment = models.CharField(max_length=256,null=True, blank=True, verbose_name='comment')
    status = models.CharField(max_length=100, null=True, blank=True, verbose_name='status')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,on_delete=models.PROTECT,related_name='order_history_owner' ,verbose_name='owner' )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.order.id} {self.status}"

    class Meta:
        verbose_name_plural = "Order histories"
        db_table = "order_histories"
        
class DiplomaHistory(models.Model):
    diploma = models.ForeignKey(Diploma,on_delete=models.PROTECT,related_name='diploma_history' ,verbose_name='Diploma')
    comment = models.CharField(max_length=256,null=True, blank=True, verbose_name='comment')
    status = models.CharField(max_length=100, null=True, blank=True, verbose_name='status')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,on_delete=models.PROTECT,related_name='diploma_history_owner' ,verbose_name='owner' )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.order.id} {self.status}"

    class Meta:
        verbose_name_plural = "Diploma histories"
        db_table = "diploma_histories"