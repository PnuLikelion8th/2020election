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


class Candidate(models.Model):
    candi_id = models.CharField('후보자ID',max_length=200)
    sggname = models.CharField('선거구명',max_length=200)
    sdname = models.CharField('시도명',max_length=200)
    wiwname = models.CharField('구시군명',max_length=200)
    jdname = models.CharField('정당이름',max_length=200)
    name = models.CharField('이름',max_length=200)
    gender = models.CharField('성별',max_length=10)
    birth = models.CharField('생년월일',max_length=100)
    age = models.IntegerField('연령',)
    addr = models.CharField('주소',max_length= 200)
    job = models.CharField('직업',max_length=200)
    edu = models.CharField('학력',max_length=255)
    career1 = models.CharField('경력1',max_length=255)
    career2 = models.CharField('경력2',max_length=255)
    status = models.CharField('등록상태',max_length=200)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.name)
