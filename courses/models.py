from django.db import models

class Publisherstatus(models.TextChoices):
    PUBLISHED = 'PUB', 'Published'
    Comming_soon = 'Commong soon', 'soon'
    Draft = "draft", "Draft"
class AceessRequrement(models.TextChoices):
    Anyone = 'any', 'Anyone'
    Email_required = 'email_required', 'Email requred immediately'
    Draft = "draft", "Draft"
    
    
# Create your models here.
class  Course(models.Model):
    pass
    # title 
    # description
    # publishdate
    # image 
    # access
    # status
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    
    access = models.CharField(
                max_length=10,choices=AceessRequrement.choices,
                default=AceessRequrement.Draft)
    status = models.CharField(
                max_length=10,choices=Publisherstatus.choices,
                default=Publisherstatus.Draft)
    @property
    def  is_published(self):
        return self.status == Publisherstatus.PUBLISHED
        