#-*- encoding=utf-8 -*-

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response
from django import forms
from models import ErrorRe,Comment,FileList
from tasks import add



class ContactFrom(forms.Form):
    version_choices =(('1','U2000',),('2','M2000',))
    subject_choices =(('1','install'),)
    version = forms.ChoiceField(label=u'版本',choices=version_choices)
    subject = forms.ChoiceField(label=u'类型',choices=subject_choices)
    IP = forms.GenericIPAddressField(label=u'服务器ip',error_messages={'required': 'IP地址不能为空', 'invalid': 'IP地址格式错误,请填写IPV4地址'})
    pwd = forms.CharField(label=u'密码',widget=forms.PasswordInput,error_messages={'required': '密码不能为空'})

    # def clean(self):
    #     message = self.cleaned_data['IP']
    #     pwd = self.cleaned_data['pwd']
class SeachFrom(forms.Form):
    TXT = forms.CharField(widget=forms.TextInput,show_hidden_initial=forms.HiddenInput)
    # TXT.widget.attrs['style'] = 'width:500px;height:40px;font-size:26'
    TXT.widget.attrs['class'] = 'form-control input-lg'
    TXT.widget.attrs['type'] = 'text'

def LogAnalyze(request):
    name = request.META['USERNAME']
    form = None
    if request.method == 'POST':
        form = ContactFrom(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            version = form.cleaned_data['version']
            IP = form.cleaned_data['IP']
            pwd = form.cleaned_data['pwd']
            result = add.delay(1,2)
            import time
            # time.sleep(22)
            return HttpResponse(str(result.result)+'yyy')
    else:
        form = ContactFrom()
    return render(request,'index.html',{'form':form,'visitor':name})


def index(request):
    name = request.META['USERNAME']
    form = None
    if request.method == 'POST':
        form = SeachFrom(request.POST)
        # print form
        if form.is_valid():
            TXT = form.cleaned_data['TXT']
            # print TXT,'test'
            return SeachResult(request,TXT)

    forms = SeachFrom()
    return render(request,'result.html',{'form':forms,'visitor':name})

def SeachResult(request,keys):
    return render(request,'result.html',{"title":keys})


