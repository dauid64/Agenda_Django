from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages

def index(request):
    contatos = Contato.objects.order_by('-id').filter(
        mostrar=True
    ) #Ordenando o id do maior pro menor e filtrando somente os que estão com campo "mostrar" true
    paginator = Paginator(contatos, 5) # Paginação limite de 10 dados
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html',
    {
        'contatos': contatos # passando para o html a informações do BD
    })

def ver_contato(request, contato_id):
    #contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id) #se não encontrar a pagina dar o erro 404

    if not contato.mostrar: # se mostrar estiver false não carregar a pagina individual dele
        raise Http404

    return render(request, 'contatos/ver_contato.html',
    {
        'contato': contato # passando para o html a informações do BD
    })

def busca(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        messages.add_message(request, messages.ERROR, 'O campo termo não pode ficar vazio.')
        return redirect('index')

    campos = Concat('nome', Value(' '),'sobrenome') # Concatenar os dois para a pesquisa
    contatos = Contato.objects.annotate(
        nome_completo = campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo) 
    )# __iconstains é busca parcial do nome e o Q server para na consulta sql usar o OR em vez de AND

    paginator = Paginator(contatos, 5) # Paginação limite de 10 dados
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/busca.html',
    {
        'contatos': contatos # passando para o html a informações do BD
    })
