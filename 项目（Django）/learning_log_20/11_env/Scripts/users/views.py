from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
 
def my_login(request):
    #username = request.POST['username']
    #password = request.POST['password']
    username = '11_admin'
    password = 'qdreamer'
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
        else:
            # 返回一个无效帐户的错误
            raise Http404
    else:
        # 返回登录失败页面。
        raise Http404

def logout_view(request):
    '''注销用户'''
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
    
def register(request):
    '''注册新用户'''
    if request.method != 'POST':
        '''显示空的注册表'''
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form':form}
    return render(request, 'users/register.html', context)