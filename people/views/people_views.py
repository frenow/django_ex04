from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from django.shortcuts import render
from datetime import datetime
from ..models import Pessoa, Endereco, Setor, Cargo

@require_http_methods(["GET","POST"])
def home(request):
	return render(request, 'index.html')

@csrf_exempt
@require_http_methods(["POST","GET"])
def listar(request):
	result = Pessoa.objects.all()
	#result = Pessoa.objects.retorna_C()
	template = loader.get_template('listar.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))

def detalhar(request, id_pessoa):
	pessoa = Pessoa.objects.get(id=id_pessoa)
	context = {'pessoa':pessoa}
	return render(request, 'detalhe.html', context)

#query costumizada filtro idade = 20
def querycustom1(request):
	pessoa = Pessoa.objects.filter(idade = 20)
	context = {'pessoa': pessoa}
	return render(request, 'detalhe.html', context)

#query costumizada filtro nasceu em 01/01/1980
def querycustom2(request):
	pessoa = Pessoa.objects.filter(data_nascimento = '1980-01-01')
	context = {'pessoa': pessoa}
	return render(request, 'detalhe.html', context)

#query costumizada listagem dos 3 primeiros registros
def querycustom3(request):
	result = Pessoa.objects.all()[:3]
	template = loader.get_template('listar.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))

#query costumizada filtro nome like/contem 'emerson'
def querycustom4(request):
	pessoa = Pessoa.objects.get(nome__contains='emerson')
	context = {'pessoa': pessoa}
	return render(request, 'detalhe.html', context)

def excluir(request, id_pessoa):
	try:
		pessoa = Pessoa.objects.get(id=id_pessoa)
		pessoa.delete()		
		return HttpResponse(f"Excluiu {pessoa.nome} (id={pessoa.id})")
	except ObjectDoesNotExist:
		return HttpResponse("Pessoa não encontrada")

def cadastro(request):
	sexos = ['Masculino','Feminino']
	template = loader.get_template('cadastrar.html')
	context = {
		'sexos': sexos,
	}
	return HttpResponse(template.render(context, request))

def editar(request, id_pessoa):
	pessoa = Pessoa.objects.get(id=id_pessoa)
	context = {'pessoa':pessoa}
	return render(request, 'editar.html', context)

@csrf_exempt
@require_http_methods(["POST","GET"])
def edit(request):
	p = Pessoa.objects.edit(
			request.POST['id'],
			request.POST['nome'],
			request.POST['idade'],
			request.POST['cpf'])
	return HttpResponse(f"{p} alterado com sucesso")


def cadastro_setor(request):
	template = loader.get_template('cadastrar_setor.html')
	context = {
	}
	return HttpResponse(template.render(context, request))

def cadastro_cargo(request):
	template = loader.get_template('cadastrar_cargo.html')
	context = {
	}
	return HttpResponse(template.render(context, request))

def cadastrar(request):
	dtNascimento = datetime.strptime(request.POST['dtNascimento'], "%d/%m/%Y").date()
	p = Pessoa.objects.nova(
			request.POST['nome'],
			request.POST['idade'],
			dtNascimento,
			request.POST['cpf'],
			request.POST['logradouro'],
			request.POST['numero'],
			request.POST['bairro'],
			request.POST['cep'])

	return HttpResponse(f"{p} cadastrado com sucesso")

def cadastrar_setor(request):
	s = Setor(descricao=request.POST['descricao'])
	s.save()
	return HttpResponse(f"{s.descricao} cadastrado com sucesso")

@csrf_exempt
@require_http_methods(["POST","GET"])
def listar_setor(request):
	result = Setor.objects.all()
	template = loader.get_template('listar_setor.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))

def detalhar_setor(request, id_setor):
	setor = Setor.objects.get(id=id_setor)
	context = {'setor':setor}
	return render(request, 'detalhe_setor.html', context)

def excluir_setor(request, id_setor):
	try:
		setor = Setor.objects.get(id=id_setor)
		setor.delete()		
		return HttpResponse(f"Excluiu {setor.descricao} (id={setor.id})")
	except ObjectDoesNotExist:
		return HttpResponse("Setor não encontrado")

def editar_setor(request, id_setor):
	setor = Setor.objects.get(id=id_setor)
	context = {'setor':setor}
	return render(request, 'editar_setor.html', context)

@csrf_exempt
@require_http_methods(["POST","GET"])
def edit_setor(request):
	s = Setor.objects.get(id=request.POST['id'])
	s.descricao = request.POST['descricao']
	s.save()
	return HttpResponse(f"{s.descricao} alterado com sucesso")

def cadastrar_cargo(request):
	c = Cargo(
		descricao=request.POST['descricao'], 
		cbo=request.POST['cbo'])
	c.save()
	return HttpResponse(f"{c.descricao} cadastrado com sucesso")

def listar_cargo(request):
	result = Cargo.objects.all()
	template = loader.get_template('listar_cargo.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))

def detalhar_cargo(request, id_cargo):
	cargo = Cargo.objects.get(id=id_cargo)
	context = {'cargo':cargo}
	return render(request, 'detalhe_cargo.html', context)

def excluir_cargo(request, id_cargo):
	try:
		cargo = Cargo.objects.get(id=id_cargo)
		cargo.delete()		
		return HttpResponse(f"Excluiu {cargo.descricao} (id={cargo.id})")
	except ObjectDoesNotExist:
		return HttpResponse("Cargo não encontrado")

def editar_cargo(request, id_cargo):
	cargo = Cargo.objects.get(id=id_cargo)
	context = {'cargo':cargo}
	return render(request, 'editar_cargo.html', context)

@csrf_exempt
@require_http_methods(["POST","GET"])
def edit_cargo(request):
	c = Cargo.objects.get(id=request.POST['id'])
	c.descricao = request.POST['descricao']
	c.cbo = request.POST['cbo']
	c.save()
	return HttpResponse(f"{c.descricao} alterado com sucesso")
