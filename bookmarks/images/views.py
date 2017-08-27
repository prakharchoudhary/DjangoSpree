
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from .models import Image
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from common.decorators import ajax_required
# Create your views here.

@login_required
def image_create(request):

	if request.method=="POST":
		# form is sent
		form = ImageCreateForm(request.POST)
		if form.is_valid():
			# form data is valid
			cd = form.cleaned_data
			new_item = form.save(commit=False)

			# assign current user to the item
			new_item.user = request.user
			new_item.save()
			messages.success(request, 'Image added successfully.')

			item = get_object_or_404(Image, title=new_item.title, url=new_item.url)
			return redirect(reverse('images:detail', args=[item.id, item.slug]))
	else:
		# build form with data provided by the bookmarklet via GET
		form = ImageCreateForm(data=request.GET)

	return render(request, 'images/image/create.html', {'section': 'images', 'form': form})	

def image_detail(request, id, slug):
	image = get_object_or_404(Image, id=id, slug=slug)
	return render(request,
					'images/image/detail.html',
					{'section': 'images', 'image': image})

@ajax_required
@login_required
@require_POST
def image_like(request):
	image_id = request.POST.get('id')
	action = request.POST.get('action')
	if image_id and action:
		try:
			image = Image.objects.get(id=image_id)
			if action == 'like':
				image.users_like.add(request.user)
			else:
				image.users_like.remove(request.user)
			return JsonResponse({'status': 'ok'})
		except:
			pass
	return JsonResponse({'status': 'ko'})


@login_required
def image_list(request):
	images = Image.objects.all()
	paginator = Paginator(images, 8)
	page = request.GET.get('page')
	try:
		images = paginator.page(page)
	
	except PageNotAnInteger:
		if request.is_ajax():
			# If page is not an integer deliver the first page
			images = paginator.page(1)
	
	except EmptyPage:
		if request.is_ajax():
			# If the request AJAX and the page is out of range
			# return an empty page
			return HttpResponse('')
		# If page is out of range deliver last page of results
		images = paginator.page(paginator.num_pages)
	
	if request.is_ajax():
		return render(request, 'images/image/list_ajax.html',{'section': 'images', 'images': images})
	
	return render(request, 'images/image/list.html', {'section': 'images', 'images': images})