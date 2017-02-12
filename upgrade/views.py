# -*- encoding=utf-8 -*-

from django import forms
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render


class ContactFrom(forms.Form):
    version_choices = (('1', 'U2000',), ('2', 'M2000',))
    subject_choices = (('1', 'install'),)
    version = forms.ChoiceField(label=u'版本', choices=version_choices)
    subject = forms.ChoiceField(label=u'类型', choices=subject_choices)
    IP = forms.GenericIPAddressField(label=u'服务器ip',
                                     error_messages={'required': 'IP地址不能为空', 'invalid': 'IP地址格式错误,请填写IPV4地址'})
    pwd = forms.CharField(label=u'密码', widget=forms.PasswordInput, error_messages={'required': '密码不能为空'})

    # def clean(self):
    #     message = self.cleaned_data['IP']
    #     pwd = self.cleaned_data['pwd']


class SeachFrom(forms.Form):
    TXT = forms.CharField(widget=forms.TextInput, show_hidden_initial=forms.HiddenInput)
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
            # result = add.delay(1, 2)
            # time.sleep(22)
            return send_email(request)
            return HttpResponse(str(result.result) + 'yyy')
    else:
        form = ContactFrom()
    return render(request, 'index.html', {'form': form, 'visitor': name})


def index(request):
    name = request.META['USERNAME']
    form = None
    if request.method == 'POST':
        form = SeachFrom(request.POST)
        # print form
        if form.is_valid():
            TXT = form.cleaned_data['TXT']
            # print TXT,'test'
            return SeachResult(request, TXT)

    forms = SeachFrom()
    return render(request, 'result.html', {'form': forms, 'visitor': name})


def SeachResult(request, keys):
    return render(request, 'result.html', {"title": keys})


def send_email(request):
    subject = u'这是邮件标题'
    message = u'<h1>这是邮件内容</h1>'
    text_content = 'This is an important message.'

    html_content = '<p>This is an <strong>important</strong> message.</p>'
    from_email = u'1173372284@qq.com'  # 邮件接受者
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['1173372284@qq.com'], fail_silently=False)
            msg = EmailMultiAlternatives(subject, text_content,from_email,['1173372284@qq.com'])
            msg.attach_alternative(html_content,'text/html')
            msg.attach_file(U'D:\迅雷下载\celery-master.zip')
            msg.send()
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponse(U'<h3>发送成功</3>')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
