from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    #return HttpResponse("Список новых вопросов. Главная страница!")
    context = {
        'question': 'question',
        'answers': 'answers',
        'form': 'form',
    }
    template = loader.get_template('base.html')
    return HttpResponse(template.render(context))

def hotQuestions(request):
    return HttpResponse("список hot вопросов")

def questionDetail(request, question_id):
    context = {
        'question_num': question_id,

    }
    template = loader.get_template('question.html')
    return HttpResponse(template.render(context))

def tag(request, tag_name):
    context = {
        'tag': tag_name,

    }
    template = loader.get_template('questionbytag.html')
    return HttpResponse(template.render(context))

def formLogin(request):
    context = {
        'question': 'question',
        'answers': 'answers',
        'form': 'form',
    }
    template = loader.get_template('Login.html')
    return HttpResponse(template.render(context))

def formSignUp(request):
    context = {
        'question': 'question',
        'answers': 'answers',
        'form': 'form',
    }
    template = loader.get_template('signup.html')
    return HttpResponse(template.render(context))

def formAsk(request):
    context = {
        'question': 'question',
        'answers': 'answers',
        'form': 'form',
    }
    template = loader.get_template('ask.html')
    return HttpResponse(template.render(context))

