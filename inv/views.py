from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect 
from django.contrib import messages

from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.decorators import login_required, permission_required

from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto

from django.urls import reverse_lazy

from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UMForm, ProductoForm 
 
from bases.views import SinPrivilegios

class CategoriaView(SinPrivilegios, \
                     generic.ListView):
    
    permission_required = "inv.view_categoria"
    
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
   

class CategoriaNew(SuccessMessageMixin,SinPrivilegios,\
                   
                   generic.CreateView):
    permission_required ="inv.view_categoria"
    model= Categoria
    template_name= "inv/categoria_form.html"
    context_object_name= "obj"
    form_class= CategoriaForm
    success_url= reverse_lazy("inv:categoria_list")
   
    success_message="Categoria creada satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)



class CategoriaEdit(SuccessMessageMixin,SinPrivilegios,\
                    generic.UpdateView):
    model= Categoria
    template_name= "inv/categoria_form.html"
    context_object_name= "obj"
    form_class= CategoriaForm
    success_url= reverse_lazy("inv:categoria_list")
    login_url= "base:login"
    success_message="Categoria actualizada satisfactoriamente"
    permission_required="inv.change_categoria"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    

class CategoriaDel(SuccessMessageMixin, SinPrivilegios, generic.DeleteView):
    permission_required ="inv.delete_categoria"
    model=Categoria
    template_name= 'inv/catalogos_del.html'
    context_object_name= 'obj'
    success_url= reverse_lazy("inv:categoria_list") 
    success_message="Categoria eliminada satisfactoriamente"
    


class SubCategoriaView( SinPrivilegios, \
                        generic.ListView):
    permission_required ="inv.view_subcategoria"
    model = SubCategoria
    template_name = "inv/subcategoria_list.html"
    context_object_name = "obj"
    


class SubCategoriaNew(SuccessMessageMixin, SinPrivilegios,generic.CreateView):
    model= SubCategoria
    template_name= "inv/subcategoria_form.html"
    context_object_name= "obj"
    form_class= SubCategoriaForm
    success_url= reverse_lazy("inv:subcategoria_list")
    success_message="Sub categoria creada satisfactoriamente" 
    permission_required="inv.add_subcategoria"
    

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    

class SubCategoriaEdit(SuccessMessageMixin, SinPrivilegios,generic.UpdateView):
    model= SubCategoria
    template_name= "inv/subcategoria_form.html"
    context_object_name= "obj"
    form_class= SubCategoriaForm
    success_url= reverse_lazy("inv:subcategoria_list")
    success_message="Sub categoria actualizada satisfactoriamente"
    permission_required="inv.change_subcategoria"
   

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    

class SubCategoriaDel(SuccessMessageMixin,SinPrivilegios, generic.DeleteView):
    model=SubCategoria
    template_name= 'inv/catalogos_del.html'
    context_object_name= 'obj'
    success_url= reverse_lazy("inv:subcategoria_list") 
    success_message="Sub categoria eliminada"
    permission_required="inv.delete_subcategoria"



class MarcaView( SinPrivilegios,\
                 generic.ListView):
    permission_required ="inv.view_marca"
    model = Marca
    template_name = "inv/marca_list.html"
    context_object_name = "obj"
    


class MarcaNew(SuccessMessageMixin,SinPrivilegios,generic.CreateView):
    model= Marca
    template_name= "inv/marca_form.html"
    context_object_name= "obj"
    form_class= MarcaForm
    success_url= reverse_lazy("inv:marca_list")
    success_message="marca creada" 
    permission_required="inv.add_marca"
   

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
    
class MarcaEdit(SuccessMessageMixin,SinPrivilegios,generic.UpdateView):
    model= Marca
    template_name= "inv/marca_form.html"
    context_object_name= "obj"
    form_class= MarcaForm
    success_url= reverse_lazy("inv:marca_list")
    success_message="Marca editada"
    permission_required="inv.change_marca"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
@login_required(login_url='/login/')
@permission_required('inv.change_marca', login_url='bases:sin_privilegios')
def marca_inactivar(request,id):
    marca= Marca.objects.filter(pk=id).first()
    contexto= {}
    template_name="inv/catalogos_del.html"

    if not marca:
        redirect("inv:marca_list")

    if request.method=='GET':
        contexto={'obj':marca}

    if request.method=='POST':
        marca.estado = False
        marca.save()
        messages.success(request, 'Marca inactivada')
        return redirect("inv:marca_list")

    return render(request, template_name, contexto)


class UMView(SinPrivilegios, generic.ListView):
    model = UnidadMedida
    template_name = "inv/um_list.html"
    context_object_name = "obj"
    permission_required="inv.view_unidadmedida"


class UMNew(SuccessMessageMixin,SinPrivilegios,generic.CreateView):
    model= UnidadMedida
    template_name= "inv/um_form.html"
    context_object_name= "obj"
    form_class= UMForm
    success_url= reverse_lazy("inv:um_list")
    success_message="unidad de medida creada" 
    permission_required="inv.add_unidadmedida"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        print(self.request.user.id)
        return super().form_valid(form)
    

class UMEdit(SuccessMessageMixin,SinPrivilegios,generic.UpdateView):
    model= UnidadMedida
    template_name= "inv/um_form.html"
    context_object_name= "obj"
    form_class= UMForm
    success_url= reverse_lazy("inv:um_list")
    success_message="Unidad de medida editada"
    permission_required="inv.change_unidadmedida"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    

@login_required(login_url="/login/")
@permission_required("inv.change_unidadmedida",login_url="/login/")
def um_inactivar(request,id):
    um= UnidadMedida.objects.filter(pk=id).first()
    contexto= {}
    template_name="inv/catalogos_del.html"

    if not um:
        redirect("inv:um_list")

    if request.method=='GET':
        contexto={'obj':um}

    if request.method=='POST':
        um.estado = False
        um.save()
        return redirect("inv:um_list")

    return render(request, template_name, contexto)


class ProductoView(SinPrivilegios, generic.ListView):
    model = Producto
    template_name = "inv/producto_list.html"
    context_object_name = "obj"
    permission_required="inv.view_producto"
    


class ProductoNew(SuccessMessageMixin, SinPrivilegios,generic.CreateView):
    model= Producto
    template_name= "inv/producto_form.html"
    context_object_name= "obj"
    form_class= ProductoForm
    success_url= reverse_lazy("inv:producto_list")
    success_message="Producto Creado"
    permission_required="inv.add_producto"


    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    


class ProductoEdit(SuccessMessageMixin, SinPrivilegios,
                   generic.UpdateView):
    model= Producto
    template_name= "inv/producto_form.html"
    context_object_name= "obj"
    form_class= ProductoForm
    success_url= reverse_lazy("inv:producto_list")
    success_message="Producto Editado"
    permission_required="inv.change_producto"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
@login_required(login_url="/login/")
@permission_required("inv.change_producto",login_url="/login/")
def producto_inactivar(request,id):
    prod= Producto.objects.filter(pk=id).first()
    contexto= {}
    template_name="inv/catalogos_del.html"

    if not prod:
        return redirect("inv:producto_list")

    if request.method=='GET':
        contexto={'obj':prod}

    if request.method=='POST':
        prod.estado = False
        prod.save()
        return redirect("inv:producto_list")

    return render(request, template_name, contexto)