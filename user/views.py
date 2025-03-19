from django.shortcuts import render, redirect
from user import models
from django.contrib import messages


# Create your views here.
def login(request):
    if request.method == "POST":
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        role = request.POST.get('role', 'owner')
        user = models.user.objects.filter(phone=phone, password=password, role=role).first()
        if phone == '' or password == '' or role == '':
            context = {
                'error': '请输入完整信息'
            }
            return render(request, 'user/login.html', context)
        if user:
            request.session['user_info'] = {
                'id': user.id,
                'username': user.username,
                'phone': user.phone,
                'role': user.role
            }

            request.session.set_expiry(60 * 60 * 3)
            return redirect("/")
        else:
            context = {
                'error': '用户名或密码错误！(是否选择了身份)'
            }
            return render(request, 'user/login.html', context)
    else:
        return render(request, 'user/login.html')


def register(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        role = request.POST.get('role', 'owner')
        counts = len(password1)
        if models.user.objects.filter(phone=phone).exists():
            context = {
                'error': '该手机号已被注册'
            }
        elif username == "" or phone == "" or password1 == "" or password2 == "" or role == "":
            context = {
                'error': '请填写完整信息'
            }

        elif counts < 8:
            context = {
                'error': '密码长度不能小于8位'
            }
        elif password1 != password2:
            context = {
                'error': '两次密码不一致'
            }
        else:
            models.user.objects.create(username=username, phone=phone, password=password1, role=role)
            messages.error(request, "完成注册，可以登录了")
            return redirect("/user/login")

    return render(request, 'user/register.html', context)


def logout(request):
    request.session.clear()
    return redirect("/")
