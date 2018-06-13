from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Autor(models.Model):
    cod_autor=models.CharField(max_length=10, primary_key=True)
    nome=models.CharField(max_length=32)

    def __str__(self):
        return self.nome

class Genero(models.Model):
    cod_genero=models.CharField(max_length=12, primary_key=True)
    nome=models.CharField(max_length=15)

    def __str__(self):
        return self.cod_genero+"-"+str(self.nome)

class Livro(models.Model):
    cod_autor1=models.ForeignKey(Autor)
    genero=models.ForeignKey(Genero)

    def __str__(self):
        return str(self.cod_autor1)+" - "+str(self.genero)