from typing import Iterable
from django.db import models

class CustoAquisicao(models.Model):
    frete = models.FloatField(default=0.0)
    hospedagem = models.FloatField(default=0.0)
    alimento = models.FloatField(default=0.0)
    luz = models.FloatField(default=0.0)
    internet = models.FloatField(default=0.0)
    sacola = models.FloatField(default=0.0)
    aluguel = models.FloatField(default=0.0)
    trafego_pago = models.FloatField(default=0.0)
    salario = models.FloatField(default=0.0)
    taxa_cartao = models.FloatField(default=0.0)
    ICMS = models.FloatField(default=0.0)
    CA = models.FloatField(default=0)
    custo_venda = models.FloatField(default=0)
    total_adquirido = models.FloatField(default=0)
    total_adquirido_revenda = models.FloatField(default=0)

    @staticmethod
    def get_instance():
        if CustoAquisicao.objects.exists():
            return CustoAquisicao.objects.get()
        else:
            return None
    
    def calcula_toral_revenda(self):
        self.save()
        total = 0
        produtos = Produto.objects.all()
        for produto in produtos:
            total += (produto.total() * produto.quantidade)
        
        self.total_adquirido_revenda = round(total, 2)

    
    def calcula_custo_aquisicao_e_salva(self):  
        if not isinstance(self, CustoAquisicao):
            return
        self.custo_venda = self.frete + self.hospedagem + self.alimento + self.luz + self.internet + self.sacola + self.aluguel + self.trafego_pago + self.salario
        self.total_adquirido = float(Produto.total_adquirido_revenda())
        self.CA =  float(self.custo_venda / self.total_adquirido)
        self.CA = round(self.CA, 4)
        self.calcula_toral_revenda()
        self.save()
        return self.CA

class MargemLucro(models.Model):
    praia = models.FloatField(default=0.0)
    casual = models.FloatField(default=0.0)
    intima = models.FloatField(default=0.0)
    fitness = models.FloatField(default=0.0)
    jeans = models.FloatField(default=0.0)

    @staticmethod
    def get_instance():
        if MargemLucro.objects.exists():
            return MargemLucro.objects.get()
        else:
            return None
    
    @staticmethod
    def margem_lucro(obj):
        return

class Produto(models.Model):
    referencia = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    valor_aquisicao = models.FloatField(default=0.0)
    fornecedor = models.CharField(max_length=100)
    margem_lucro = models.FloatField(default=0.7)
    quantidade = models.IntegerField(default=0)
    
    def total(self):
        if not CustoAquisicao.objects.first():
            return self.valor_aquisicao
        t = (self.valor_aquisicao + self.ICMS() + self.taxa_cartao() + self.margem_de_lucro() + self.custo_aquisicao())
        t = round(t, 2)
        return t

    def ICMS(self):
        return self.valor_aquisicao * (CustoAquisicao.get_instance().ICMS if CustoAquisicao.get_instance().ICMS != None else 0.2)
    
    def taxa_cartao(self):
        return self.valor_aquisicao * (CustoAquisicao.get_instance().taxa_cartao if CustoAquisicao.get_instance().ICMS != None else 0.1365)
    
    def custo_aquisicao(self):
        return self.valor_aquisicao * (CustoAquisicao().get_instance().CA if CustoAquisicao.get_instance().ICMS != None else 0.3)

    def margem_de_lucro(self):
        ml = self.valor_aquisicao * self.margem_lucro
        return float(ml)
    
    @staticmethod
    def quantidade_de_produtos():
        return Produto.objects.all().count()

    @staticmethod
    def total_adquirido_revenda():
        produtos = Produto.objects.all()
        valor_total_revenda = 0
        for produto in produtos:
            valor_total_revenda += (produto.valor_aquisicao * produto.quantidade)
        
        return valor_total_revenda if valor_total_revenda != 0 else 1
    

class Venda(models.Model):
    referencia = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    cliente = models.CharField(max_length=150)
    tamanho = models.CharField(max_length=5)
    valor = models.FloatField(default=0)
    quantidade = models.IntegerField(default=1)
    parcelas = models.IntegerField(default=0)
    desconto = models.FloatField(default=0)

    def receita_mes(self):
        produtos = Produto.objects.all()
        for produto in produtos:
            if self.referencia == str(produto.referencia):
                return (self.quantidade * (produto.total()/self.parcelas) )

        return self.valor

    def total(self):
        produtos = Produto.objects.all()
        for produto in produtos:
            if self.referencia == str(produto.referencia):
                self.valor = (self.quantidade * produto.total())
                break
        self.valor = round(self.valor, 2)
        self.save()

        return self.valor