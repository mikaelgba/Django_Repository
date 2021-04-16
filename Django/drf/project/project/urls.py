from django.contrib import admin
from django.urls import path, include

# aqui posso chamar as rotas da minha camada de negocio dentro do diretorio 'app"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]
