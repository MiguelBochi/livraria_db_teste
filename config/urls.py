from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from livraria.views import AutorViewSet,CategoriaViewSet, EditoraViewSet, LivroViewSet

router = DefaultRouter()
router.register("autores", AutorViewSet)
router.register("categorias", CategoriaViewSet)
router.register("editoras", EditoraViewSet)
router.register("livros", LivroViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
