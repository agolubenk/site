from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import Post
from django.http import Http404


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'

def post_list(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')[:3]
    return render(request, 'home.html', {'posts': posts, 'title': 'Хочу в IT · Рекрутинговое агентство', 'meta_1': 'Хочу в IT. Рекрутинговое агентство по подбору IT-специалистов', 'meta_2': 'Рекрутинговое агентство по профессиональному подбору IT-специалистов любого грейда и любой сложности. Мы соберем Вашу команду мечты! Работаем с применением различных техник в части поиска и подбора персонала, используем как классические инструменты, так и современные методики для оценки и поиска сотрудников.', 'meta_3': 'кадровое агентство, резюме, HR, вакансии, IT, работа, подбор персонала, оффер, рекрутер, рекрутинг, дешевый поиск персонала, разработчики, аутстафф, айти, быстрый поиск персонала, rflhjdjt futyncndj, htp.vt, HR, dfrfycbb, IT, hf,jnf, gjl,jh gthcjyfkf, jaath, htrhenth, htrhenbyu, ltitdsq gjbcr gthcjyfkf, hfphf,jnxbrb, fencnfaa, fqnb, ,scnhsq gjbcr gthcjyfkf, recruitment agency, resume, HR, vacancies, IT, job, recruitment, offer, recruiter, recruiting, cheap staff search, developers, outstaff, IT, quick staff search, кускгшеьуте фпутсн, куыгьу, РК, мфсфтсшуы, ШЕ, ощи, кускгшеьуте, щааук, кускгшеук, кускгшештп, сруфз ыефаа ыуфкср, вумудщзукы, щгеыефаа, ШЕ, йгшсл ыефаа ыуфкср'})



def about(request):
    posts = Post.objects.order_by('-created_on')[:3]
    return render(request, 'about.html', {'posts': posts, 'title': 'Хочу в IT · Рекрутинговое агентство', 'meta_1': 'Хочу в IT. Рекрутинговое агентство по подбору IT-специалистов', 'meta_2': 'Рекрутинговое агентство по профессиональному подбору IT-специалистов любого грейда и любой сложности. Мы соберем Вашу команду мечты! Работаем с применением различных техник в части поиска и подбора персонала, используем как классические инструменты, так и современные методики для оценки и поиска сотрудников.', 'meta_3': 'кадровое агентство, резюме, HR, вакансии, IT, работа, подбор персонала, оффер, рекрутер, рекрутинг, дешевый поиск персонала, разработчики, аутстафф, айти, быстрый поиск персонала, rflhjdjt futyncndj, htp.vt, HR, dfrfycbb, IT, hf,jnf, gjl,jh gthcjyfkf, jaath, htrhenth, htrhenbyu, ltitdsq gjbcr gthcjyfkf, hfphf,jnxbrb, fencnfaa, fqnb, ,scnhsq gjbcr gthcjyfkf, recruitment agency, resume, HR, vacancies, IT, job, recruitment, offer, recruiter, recruiting, cheap staff search, developers, outstaff, IT, quick staff search, кускгшеьуте фпутсн, куыгьу, РК, мфсфтсшуы, ШЕ, ощи, кускгшеьуте, щааук, кускгшеук, кускгшештп, сруфз ыефаа ыуфкср, вумудщзукы, щгеыефаа, ШЕ, йгшсл ыефаа ыуфкср'})

def vacancy(request):
    posts = Post.objects.order_by('-created_on')[:3]
    return render(request, 'vacancy.html', {'posts': posts, 'title': 'Хочу в IT · Рекрутинговое агентство', 'meta_1': 'Хочу в IT. Рекрутинговое агентство по подбору IT-специалистов', 'meta_2': 'Рекрутинговое агентство по профессиональному подбору IT-специалистов любого грейда и любой сложности. Мы соберем Вашу команду мечты! Работаем с применением различных техник в части поиска и подбора персонала, используем как классические инструменты, так и современные методики для оценки и поиска сотрудников.', 'meta_3': 'кадровое агентство, резюме, HR, вакансии, IT, работа, подбор персонала, оффер, рекрутер, рекрутинг, дешевый поиск персонала, разработчики, аутстафф, айти, быстрый поиск персонала, rflhjdjt futyncndj, htp.vt, HR, dfrfycbb, IT, hf,jnf, gjl,jh gthcjyfkf, jaath, htrhenth, htrhenbyu, ltitdsq gjbcr gthcjyfkf, hfphf,jnxbrb, fencnfaa, fqnb, ,scnhsq gjbcr gthcjyfkf, recruitment agency, resume, HR, vacancies, IT, job, recruitment, offer, recruiter, recruiting, cheap staff search, developers, outstaff, IT, quick staff search, кускгшеьуте фпутсн, куыгьу, РК, мфсфтсшуы, ШЕ, ощи, кускгшеьуте, щааук, кускгшеук, кускгшештп, сруфз ыефаа ыуфкср, вумудщзукы, щгеыефаа, ШЕ, йгшсл ыефаа ыуфкср'})

def price(request):
    posts = Post.objects.order_by('-created_on')[:3]
    return render(request, 'price.html', {'posts': posts, 'title': 'Хочу в IT · Рекрутинговое агентство', 'meta_1': 'Хочу в IT. Рекрутинговое агентство по подбору IT-специалистов', 'meta_2': 'Рекрутинговое агентство по профессиональному подбору IT-специалистов любого грейда и любой сложности. Мы соберем Вашу команду мечты! Работаем с применением различных техник в части поиска и подбора персонала, используем как классические инструменты, так и современные методики для оценки и поиска сотрудников.', 'meta_3': 'кадровое агентство, резюме, HR, вакансии, IT, работа, подбор персонала, оффер, рекрутер, рекрутинг, дешевый поиск персонала, разработчики, аутстафф, айти, быстрый поиск персонала, rflhjdjt futyncndj, htp.vt, HR, dfrfycbb, IT, hf,jnf, gjl,jh gthcjyfkf, jaath, htrhenth, htrhenbyu, ltitdsq gjbcr gthcjyfkf, hfphf,jnxbrb, fencnfaa, fqnb, ,scnhsq gjbcr gthcjyfkf, recruitment agency, resume, HR, vacancies, IT, job, recruitment, offer, recruiter, recruiting, cheap staff search, developers, outstaff, IT, quick staff search, кускгшеьуте фпутсн, куыгьу, РК, мфсфтсшуы, ШЕ, ощи, кускгшеьуте, щааук, кускгшеук, кускгшештп, сруфз ыефаа ыуфкср, вумудщзукы, щгеыефаа, ШЕ, йгшсл ыефаа ыуфкср'})

def docs(request):
    posts = Post.objects.order_by('-created_on')[:3]
    return render(request, 'docs.html', {'posts': posts, 'title': 'Хочу в IT · Рекрутинговое агентство', 'meta_1': 'Хочу в IT. Рекрутинговое агентство по подбору IT-специалистов', 'meta_2': 'Рекрутинговое агентство по профессиональному подбору IT-специалистов любого грейда и любой сложности. Мы соберем Вашу команду мечты! Работаем с применением различных техник в части поиска и подбора персонала, используем как классические инструменты, так и современные методики для оценки и поиска сотрудников.', 'meta_3': 'кадровое агентство, резюме, HR, вакансии, IT, работа, подбор персонала, оффер, рекрутер, рекрутинг, дешевый поиск персонала, разработчики, аутстафф, айти, быстрый поиск персонала, rflhjdjt futyncndj, htp.vt, HR, dfrfycbb, IT, hf,jnf, gjl,jh gthcjyfkf, jaath, htrhenth, htrhenbyu, ltitdsq gjbcr gthcjyfkf, hfphf,jnxbrb, fencnfaa, fqnb, ,scnhsq gjbcr gthcjyfkf, recruitment agency, resume, HR, vacancies, IT, job, recruitment, offer, recruiter, recruiting, cheap staff search, developers, outstaff, IT, quick staff search, кускгшеьуте фпутсн, куыгьу, РК, мфсфтсшуы, ШЕ, ощи, кускгшеьуте, щааук, кускгшеук, кускгшештп, сруфз ыефаа ыуфкср, вумудщзукы, щгеыефаа, ШЕ, йгшсл ыефаа ыуфкср'})


