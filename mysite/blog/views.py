from django.views.generic import ListView
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .forms import EmailPostForm

# Create your views here.
# def post_list(request):
# 	object_list = Post.published.all()
# 	paginator = Paginator(object_list, 3) # 3 posts in each page
# 	page = request.GET.get('page')
# 	try:
# 		posts = paginator.page(page)
# 	except PageNotAnInteger:
# 		# If page is not an integer deliver the first page
# 		posts = paginator.page(1)
# 	except EmptyPage:
# 		# If page is out of range deliver last page of results
# 		posts = paginator.page(paginator.num_pages)
# 	return render(request,'blog/post/list.html',{'page': page, 'posts': posts})

class PostListView(ListView):
	queryset = Post.published.all()
	context_object_name = 'posts'
	paginate_by = 3
	template_name = 'blog/post/list.html'

def post_detail(request, year, month, day, post):
	post = get_object_or_404(Post, slug=post,
								status = 'published',
								publish__year=year,
								publish__month=month,
								publish__day=day)
	return render(request,
				'blog/post/detail.html',
				{'post': post}
				)

def post_share(request, post_id):
	# Retrieve post by id
	post = get_object_or_404(Post, id=post_id, status='published')
	sent = False

	if request.method == 'POST':
		# Form was submitted
		form = EmailPostForm(request.POST)
		if form.is_valid():
			# Form fields passed validation
			cd = form.cleaned_data
			# ... send email
			post_url = request.build_absolute_uri(
										post.get_absolute_url()
										)
			# Since we have to include a link to the post in
			# the e-mail, we retrieve the absolute path of the post using its get_absolute_url()
			# method. We use this path as input for request.build_absolute_uri() to build a
			# complete URL including HTTP schema and hostname.
			
			subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
			message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
			send_mail(subject, message, 'prakhar13.cool@gmail.com', [cd['to']])
			sent = True
	else:
		form = EmailPostForm()

	return render(request, 'blog/post/share.html', {'post':post, 'form': form, 'sent':sent})
				