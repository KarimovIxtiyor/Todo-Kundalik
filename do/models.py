from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.CharField(max_length=500)
    datetime=models.DateTimeField(auto_now_add=True)       # modulimiz yaratilgan vaqtni o`zi kititadi sistemada olib
    done=models.BooleanField(default=False)                # bajatilgan yoki bajarilmaganini tekshirish

    def __str__(self):
        return f'Todo of {self.user.username}'