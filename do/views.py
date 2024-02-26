from django.shortcuts import render,redirect
from django.views import  View
from .models import Todo
from django.contrib.auth.mixins import LoginRequiredMixin                    # agar login qilib tizimga kirgan bo`lsagina shu viewga kiradi

class IndexView(LoginRequiredMixin,View):
    def get(self,request):                                                   # saytga keliyapkan get request larni shu funksiya qabul qiladi
        todos=Todo.objects.filter(user=request.user).order_by('-datetime')   # user ga aloqador bo`lgan barcha todolarni chiqazib berish
        return render(request,"index.html",{'todos':todos})

    def post(self,request):                                                  # yangi post (todo)
        body=request.POST.get('body')
        if body:
            Todo.objects.create(user=request.user,body=body)                 # todo yaratish

        return redirect('index')                                             # index view ga yuboramiz url orqali


class TodoActionView(LoginRequiredMixin,View):                               # bajarildi , o`chirish amallariini qo`shish
    def post(self,request,todo_id,action):
        todo=Todo.objects.filter(id=todo_id,user=request.user).first()
        if todo:                                                             # agar todo mavjud bolsa bajariladi
            if action=='done':
                todo.done=True                                               # done qismini true deb ketamiz va save qilamiz
                todo.save()
            elif action=='delete':
                todo.delete()
        return redirect('index')


def about_views(request):                                                    # sayt haqidagi  sahifa
    return render(request,'about.html')