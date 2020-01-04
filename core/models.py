from django.db import models
from django.urls import reverse_lazy
from django.forms import ModelForm

class Acao(models.Model):
    acao = models.CharField('Ação',max_length=8)
    dividendos = models.FloatField('Dividendos')
    cotas = models.IntegerField('Cotas')
    valor_cota = models.FloatField('Valor por cota')

    def __str__(self):
        return self.acao
    
    def valor_investido(self):
        return self.cotas * self.valor_cota
    
    def dividendos_totais(self):
        return self.cotas * self.dividendos

class AcaoForm(ModelForm):
    class Meta:
        model = Acao
        fields = ('__all__')