from django.contrib import admin
from .models import Post
from .models import Autor
from .models import Genero
from .models import Livro

admin.site.register(Post)
admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Livro)
