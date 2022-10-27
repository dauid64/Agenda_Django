from django.contrib import admin
from .models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria', 'mostrar') #mostrar
    list_display_links = ('id', 'nome', 'sobrenome') #link para ir editar
    list_per_page = 10 #quantos dados por pagina
    search_fields = ('nome', 'sobrenome', 'telefone') #pesquisar
    list_editable = ('telefone', 'mostrar') #editar

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
