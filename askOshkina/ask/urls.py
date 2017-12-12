from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^hot/$', views.hotQuestions, name='new-questions'), #список hot вопросов
    url(r'^login/$', views.formLogin, name='login'), # форма логина
    url(r'^signup/$', views.formSignUp, name='signup'), #форма регистрации
    url(r'^ask/$', views.formAsk, name='ask-question'), #форма создания вопроса
    url(r'^question/(?P<question_id>[0-9]+)/$', views.questionDetail, name='question'),#один вопрос со списком ответов
    url(r'^tag/(?P<tag_name>[a-zA-Z]+)/$', views.tag, name='tag-question'),#вопрос по тегу
    url(r'^$', views.index, name='main-page'), # список новых вопросов (главная страница)
]