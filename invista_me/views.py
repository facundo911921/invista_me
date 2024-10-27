from django.shortcuts import render, HttpResponse, redirect
from .models import Investimento
from .forms import InvestimentoForm
from django.contrib.auth.decorators import login_required


def investimentos(request):
    dados = {"dados": Investimento.objects.all()}
    return render(request, "investimentos\investimentos.html", dados)


def contato_html(request):
    contato = {"nome": "Facundo", "idade": "24", "profissao": "Desenvolvedor"}
    return render(request, "investimentos\contato.html", contato)


def detalhe(request, id_investimento):
    dados = {"dados": Investimento.objects.get(pk=id_investimento)}
    return render(request, "investimentos\detalhe.html", context=dados)

@login_required
def criar(request):
    if request.method == 'POST':
        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect('investimentos')
    else: # Não entendi
        investimento_form = InvestimentoForm()
        formulario = {
            'formulario': investimento_form
        }
        return render(request, r'investimentos\novo_investimento.html', context=formulario)
    
@login_required
def editar(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    # Os campos já devem estar preenchidos, já que é uma edição
    if request.method == 'GET':
        # Parâmetro 'instance' serve para pupular o form, fazendo com que a página já venha preenchida
        formulario = InvestimentoForm(instance=investimento)
        return render(request, r'investimentos\novo_investimento.html', {'formulario': formulario})
    # Ao editar, estaremos mandando um POST, enviando novos dados ao backend
    else:
        formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')
    
@login_required
def excluir(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimentos')
    return render(request, 'investimentos\confirmar_exclusao.html', {'item': investimento})