from django.db import models

# Create your models here.


class Party(models.Model):
    name = models.CharField('정당이름',max_length=100,)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
    
class PartyPolicy(models.Model):
    name = models.ForeignKey(Party,on_delete=models.CASCADE)
    number = models.IntegerField('순번')
    title = models.CharField('제목',max_length=255)
    category = models.CharField('분야', max_length=255)
    desc = models.TextField('내용',)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.name)
