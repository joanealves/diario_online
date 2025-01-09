from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa, Diario

def home(request):
    textos = Diario.objects.order_by('create_at')[:3]
    return render(request, 'home.html', {'textos': textos})

    
def escrever(request):
    if request.method == "GET":
        pessoas = Pessoa.objects.all()
        textos = Diario.objects.order_by('create_at')   
        return render(request, 'escrever.html', {'pessoas': pessoas, 'textos': textos})
    else:
        titulo = request.POST.get("titulo")
        tags = request.POST.getlist("tags")
        pessoas = request.POST.getlist("pessoas")
        texto = request.POST.get("texto")

        if len(titulo.strip()) == 0 or len(texto.strip()) == 0:
            return redirect('escrever')

        diario = Diario(
            titulo=titulo,
            texto=texto
        )
        diario.set_tags(tags)
        diario.save()
        
        pessoa_objs = Pessoa.objects.filter(id__in=pessoas)
        diario.pessoas.add(*pessoa_objs)
        diario.save()

        '''for i in pessoas:
            pessoa = Pessoa.objects.get(id=i)
            diario.pessoas.add(pessoa)'''

        return redirect('escrever')
       
        
def cadastrar_pessoa(request):
    if request.method == 'GET':
        return render(request, 'pessoa.html')  
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        foto = request.FILES.get('foto')
    
        pessoa = Pessoa(
            nome=nome,
            foto=foto
        )
        pessoa.save()
        return redirect('escrever')
