from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Nome(models.Model):
	codigo_nome = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Código do Nome')
	nome = models.CharField(max_length=50)
	significado = models.CharField(max_length=50)
	detalhes = models.TextField()
	slug = models.SlugField()
	data_cadastro = models.DateTimeField(auto_now_add=True)

	#referente ao usuário que inseriu o nome
	autor_nome = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

	def __str__(self):
		return self.nome

	def snippet(self):
		return self.detalhes[:50] + '...'
