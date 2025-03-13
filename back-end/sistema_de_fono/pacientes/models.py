from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    email= models.EmailField()
    telefone = models.DateField(max_length=20)
    data_nascimento = models.DateField()

class Atendimento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    tipo_paciente = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    data_atendimento = models.DateTimeField()
    status = models.CharField(max_length=20, default='Pendente')

class Pagamento(models.Model):
    atendimento = models.ForeignKey(Atendimento, on_delete=models.CASCADE)
    valor_pago = models.DecimalField(max_digits=6, decimal_places=2)
    data_pagamento = models.DateTimeField()
