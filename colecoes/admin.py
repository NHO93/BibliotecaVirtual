from django.contrib import admin
from .models import Livro, Colecao  # Certifique-se de que está importando do app correto

admin.site.register(Livro)
admin.site.register(Colecao)
