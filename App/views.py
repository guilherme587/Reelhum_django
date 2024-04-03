from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Produto, CustoAquisicao, MargemLucro, Venda
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django, logout as logout_django
from django.contrib.auth.decorators import login_required, user_passes_test

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = User.objects.filter(username=request.POST.get('nomeusuario')).first()
        email = User.objects.filter(email=request.POST.get('nomeusuario')).first()
        if email == None and username == None:
            return HttpResponse('Usuário ou senha incorretos. Favor tente novamente ou efetue um nov cadastro.')
        user = authenticate(username=request.POST.get('nomeusuario'), password=request.POST.get('senha'))
        login_django(request, user)
        if not user:
            return HttpResponse('Usuário ou senha incorretos. Favor tente novamente.')
        
        return redirect(home)

def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser, login_url='/reelhum/home/')
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = User.objects.filter(username=request.POST.get('nomeusuario')).first()
        email = User.objects.filter(email=request.POST.get('nomeusuario')).first()
        if email == None and username == None:
            user = User.objects.create_user(username=request.POST.get('nomeusuario'), password=request.POST.get('senha'))
            user.save()
            return redirect(login)
        else:
            return HttpResponse('Usuário com nome ou e-mail já cadastrado. Favor use outro.')

def logout(request):
    logout_django(request)
    return redirect(login)

def index(request):
    return redirect(login)

@login_required(login_url='/reelhum/')
def home(request):
    custos_aquisicao = CustoAquisicao.objects.first()
    CA = 0
    if custos_aquisicao:
        CA = custos_aquisicao.CA = custos_aquisicao.CA *100
        calcula_custo_aquisicao_e_salva()
    vendas = Venda.objects.all()
    receita_atual = 0
    for venda in vendas:
        receita_atual += venda.receita_mes()

    return render(request, 'index.html', {'custos_aquisicao': custos_aquisicao, 'receita_atual': receita_atual})

@login_required(login_url='/reelhum/')
def vendas(request):
    produtos = Produto.objects.all()
    vendas = Venda.objects.all()
    receita_atual = 0
    for venda in vendas:
        receita_atual += venda.receita_mes()

    return render(request, 'vendas.html', {'vendas': vendas, 'produtos': produtos, 'receita_atual': receita_atual})

def calcula_custo_aquisicao_e_salva():
    custos_aquisicao = CustoAquisicao.objects.first()
    if custos_aquisicao:
        custos_aquisicao.CA = custos_aquisicao.calcula_custo_aquisicao_e_salva()

@login_required(login_url='/reelhum/')
def estoque(request):
    produtos = Produto.objects.all()
    custos_aquisicao = CustoAquisicao.objects.first()
    CA = 0
    if custos_aquisicao:
        CA = custos_aquisicao.CA = custos_aquisicao.CA *100
        calcula_custo_aquisicao_e_salva()
    margem_lucro = MargemLucro.objects.first()


    return render(request, 'estoque.html', {'produtos': produtos, 'custos_aquisicao': custos_aquisicao, 'CA': CA, 'margem_lucro': margem_lucro})

@login_required(login_url='/reelhum/')
def criar_produto(request):
    produto = Produto.objects.create(
        referencia=request.POST.get('referencia'),
        descricao=request.POST.get('descricao'),
        valor_aquisicao=float(request.POST.get('valoraquisicao')),
        fornecedor=request.POST.get('fornecedor'),
        margem_lucro=float(request.POST.get('margemlucro')),
        quantidade=int(request.POST.get('quantidade')),
        )
    produto.save()

    calcula_custo_aquisicao_e_salva()

    return redirect(estoque)

@login_required(login_url='/reelhum/')
def editar_produto(request, id):
    produto = Produto.objects.get(id=id)
    produto.referencia = request.POST.get('referencia')
    produto.descricao = request.POST.get('descricao')
    produto.valor_aquisicao = float(request.POST.get('valoraquisicao'))
    produto.fornecedor = request.POST.get('fornecedor')
    produto.margem_de_lucro = float(request.POST.get('margemlucro'))
    produto.quantidade = int(request.POST.get('quantidade'))
    produto.save()
    return redirect(estoque)

@login_required(login_url='/reelhum/')
def adicionar_produto(request, id): 
    produto = Produto.objects.get(id=id)
    produto.quantidade += 1
    produto.save()

    calcula_custo_aquisicao_e_salva()

    return redirect(estoque)

@login_required(login_url='/reelhum/')
def subtrair_produto(request, id):
    if Produto.objects.get(id=id).quantidade == 0:
        return redirect(estoque)
    produto = Produto.objects.get(id=id)
    produto.quantidade -= 1
    produto.save()

    calcula_custo_aquisicao_e_salva()

    return redirect(estoque)

@login_required(login_url='/reelhum/')
def deletar_produto(requeste, id):
    Produto.objects.get(id=id).delete()
    
   

    return redirect(estoque)

@login_required(login_url='/reelhum/')
def custos_aquisicao(request):
    CustoAquisicao.objects.all().delete()
    custos_aquisicao = CustoAquisicao.objects.create(
        frete=float(request.POST.get('frete')),
        hospedagem=float(request.POST.get('hospedagem')),
        alimento=float(request.POST.get('alimento')),
        luz=float(request.POST.get('luz')),
        internet=float(request.POST.get('internet')),
        sacola=float(request.POST.get('sacola')),
        aluguel=float(request.POST.get('aluguel')),
        trafego_pago=float(request.POST.get('trafego_pago')),
        salario=float(request.POST.get('salario')),
        taxa_cartao=float(request.POST.get('taxa_cartao')),
        ICMS=float(request.POST.get('ICMS')),
    )
    custos_aquisicao.CA = custos_aquisicao.calcula_custo_aquisicao_e_salva()

    return redirect(estoque)

@login_required(login_url='/reelhum/')
def margem_lucro(request):
    if MargemLucro.objects.first():
        MargemLucro.objects.first().delete()
    margem_lucro = MargemLucro.objects.create(
        praia=request.POST.get('praia'),
        casual=request.POST.get('casual'),
        intima=request.POST.get('intima'),
        fitness=request.POST.get('fitness'),
        jeans=request.POST.get('jeans'),
    )

    return redirect(estoque)

@login_required(login_url='/reelhum/')
def criar_venda(request):
    venda = Venda.objects.create(
        referencia=request.POST.get('referencia'),
        cliente=request.POST.get('cliente'),
        tamanho=str(request.POST.get('tamanho')),
        quantidade=int(request.POST.get('quantidade')),
        parcelas=int(request.POST.get('parcelas')),
        desconto=float(request.POST.get('desconto')),
        )
    venda.save()

    return redirect(vendas)

@login_required(login_url='/reelhum/')
def editar_venda(request, id):
    venda = Venda.objects.get(id=id)
    venda.referencia=request.POST.get('referencia')
    venda.cliente=request.POST.get('cliente')
    venda.tamanho=str(request.POST.get('tamanho'))
    venda.quantidade=int(request.POST.get('quantidade'))
    venda.parcelas=int(request.POST.get('parcelas'))
    venda.desconto=float(request.POST.get('desconto'))
    venda.save()

    return redirect(vendas)

@login_required(login_url='/reelhum/')
def deletar_venda(request, id):
    Venda.objects.get(id=id).delete()
    return redirect(vendas)