# Create your views h
from django.http import Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render 
from posts.models import Post,PostType
from django.views.generic import CreateView
from posts import forms as PostForms
from django.forms.models import modelform_factory
import pdb
def PostView(request, title):    
    try:
        post = Post.objects.get(titulo=title.replace("-"," "))
        autor = post.usuario.usuario
    except Post.DoesNotExist:
        raise Http404
    return render(request, "posts/Post.html",{'post':post,'autor':autor})

@login_required
def now(request):
    return render(request,"posts/newPost.html")

@login_required
def newPostMusic(request):
    tipos = PostType.objects.get(tipo='Music')
    nuevo = Post(usuario=request.user.profile, tipoPublicacion=tipos)
    tipoForm = PostForms.formMusic(request.POST or None, instance=nuevo)
    
    if tipoForm.is_valid():
        tipoForm.save()
        return HttpResponseRedirect('/Now/')
    return render(request,"posts/newPost.html",{'form':tipoForm})

@login_required
def newPostMovies(request):
    tipos = PostType.objects.get(tipo='Movies')
    nuevo = Post(usuario=request.user.profile, tipoPublicacion=tipos)
    tipoForm = PostForms.formMovies(request.POST or None, instance=nuevo)
    
    if tipoForm.is_valid():
        tipoForm.save()
        return HttpResponseRedirect('/Now/')
    return render(request,"posts/newPost.html",{'form':tipoForm})

@login_required
def newPostSeries(request):
    tipos = PostType.objects.get(tipo='Series')
    nuevo = Post(usuario=request.user.profile, tipoPublicacion=tipos)
    tipoForm = PostForms.formSeries(request.POST or None, instance=nuevo)
    
    if tipoForm.is_valid():
        tipoForm.save()
        return HttpResponseRedirect('/Now/')
    return render(request,"posts/newPost.html",{'form':tipoForm})

@login_required
def newPostPosters(request):
    tipos = PostType.objects.get(tipo='Posters')
    nuevo = Post(usuario=request.user.profile, tipoPublicacion=tipos)
    tipoForm = PostForms.formPosters(request.POST or None, instance=nuevo)
    
    if tipoForm.is_valid():
        tipoForm.save()
        return HttpResponseRedirect('/Now/')
    return render(request,"posts/newPost.html",{'form':tipoForm})

@login_required
def newPostArtBooks(request):
    tipos = PostType.objects.get(tipo='ArtBooks')
    nuevo = Post(usuario=request.user.profile, tipoPublicacion=tipos)
    tipoForm = PostForms.formArtBooks(request.POST or None, instance=nuevo)
    
    if tipoForm.is_valid():
        tipoForm.save()
        return HttpResponseRedirect('/Now/')
    return render(request,"posts/newPost.html",{'form':tipoForm})