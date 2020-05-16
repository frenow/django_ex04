from django.urls import path

from .views import people_views as pv

urlpatterns = [
	path('', pv.home, name="index"),
	path('listar/', pv.listar, name="listar"),
	path('detalhar/<int:id_pessoa>/', pv.detalhar, name="detalhar"),
	path('excluir/<int:id_pessoa>/', pv.excluir, name="excluir"),
	path('cadastro/', pv.cadastro, name="cadastro"),
	path('cadastro_setor/', pv.cadastro_setor, name="cadastro_setor"),
	path('cadastro_cargo/', pv.cadastro_cargo, name="cadastro_cargo"),
	path('cadastrar/', pv.cadastrar, name="cadastrar"),
	path('querycustom1/', pv.querycustom1, name="querycustom1"),
	path('querycustom2/', pv.querycustom2, name="querycustom2"),
	path('querycustom3/', pv.querycustom3, name="querycustom3"),
	path('querycustom4/', pv.querycustom4, name="querycustom4"),
	path('cadastrar_setor/', pv.cadastrar_setor, name="cadastrar_setor"),
	path('listar_setor/', pv.listar_setor, name="listar_setor"),
	path('excluir_setor/<int:id_setor>/', pv.excluir_setor, name="excluir_setor"),
	path('detalhar_cargo/<int:id_cargo>/', pv.detalhar_cargo, name="detalhar_cargo"),
	path('cadastrar_cargo/', pv.cadastrar_cargo, name="cadastrar_cargo"),
	path('listar_cargo/', pv.listar_cargo, name="listar_cargo"),
	path('excluir_cargo/<int:id_cargo>/', pv.excluir_cargo, name="excluir_cargo"),
	path('detalhar_cargo/<int:id_cargo>/', pv.detalhar_cargo, name="detalhar_cargo")
]