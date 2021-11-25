from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
class PostAdmin(admin.ModelAdmin):
    
    #se crea una funcion para mostrar un nuevo campo dentro de la lista 
    #en este caso se muestran todas las categorias del blog
    def post_categories(self, obj):
        return  ", ".join([c.name for c in obj.categories.all().order_by('name')])
    #cambia el nombre del nuevo item
    post_categories.short_description = "Categorias"
    
    readonly_fields = ('created', 'updated')
    #muestra varios campos en la lista de visualicion del administrador
    list_display = ('title', 'author', 'published', 'post_categories')
    #ordena la lista en el administrador
    oredering = ('author', 'published')
    #opciones de busqueda dentro de la base de datos
    search_fields = ('title','author__username', 'categories__name')
    #metodo para filtrar por fecha mas comodamente dentro del administrador
    date_hierarchy = 'published'
    #muestra opciones de filtrado
    list_filter = ('author__username', 'categories__name')
    
    
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)