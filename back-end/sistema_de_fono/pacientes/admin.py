from django.contrib import admin
from .models import Paciente, Atendimento, Pagamento

admin.site.register(Paciente)
admin.site.register(Atendimento)
admin.site.register(Pagamento)