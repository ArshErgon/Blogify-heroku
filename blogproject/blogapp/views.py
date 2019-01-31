
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Owner, OwnerAbout, Contact, Comment, Eye_Catcher_Post, Popular_Post
from django.contrib.auth import get_user_model
from .forms import SignInForm


def index(request):
	post_context = Post.objects.all()
	owner_context = Owner.objects.all()
	latest_post = Post.objects.all().order_by('post_date')
	eye_catcher_post = Eye_Catcher_Post.objects.all()
	popular_post_context = Popular_Post.objects.all()
	print(popular_post_context)
	# print(eye_catcher_post)
	# print(len(owner_context))
	print(len(Post.objects.filter(post_category='programming'.upper())))
	return render(request, 'blogapp/index.html', {
							'post_context'			:		post_context,
							'owner_context'			:	    owner_context,
							'latest_post'			:	    latest_post,
							'eye_catcher_post'		:		eye_catcher_post,
							'popular_post_context'	:		popular_post_context,
							}
					)

#  DONT TOUCH THIS REALLY REALLY CONFUSING CODE

def blog_post_view(request, pk):
	home = request		#  this is doing something really werid taking the data which have same id it saprate them maybe its not the right way of doing it but I am still learning I will find another way
	# print(str(home))
	if 'home' in str(home): # make string the value url
		blog_view = get_object_or_404(Eye_Catcher_Post, pk=pk)
	else:
		blog_view = get_object_or_404(Post, pk=pk)
	latest_post = Post.objects.all().order_by('post_date')
	keyword = blog_view.post_tages
	if keyword.upper() == 'django'.upper():
		related_context = Post.objects.filter(post_tages=keyword.upper())
		print(related_context, 'context data')
		print(keyword, 'actual data')
	# 	print(related_context)
	elif keyword.upper() == 'python'.upper():
		related_context = Post.objects.filter(post_tages=keyword.upper())
		print(related_context, 'context data')
		print(keyword, 'actual data')
	elif keyword.upper() == 'web-development'.upper():
		related_context = Post.objects.filter(post_tages=keyword.upper())
	else:
		related_context = Post.objects.filter(post_tages='')

	# print(request.method)

	if request.method == "POST":
		name = request.POST.get('name')
		message = request.POST.get('comment')
		person_comments = Comment(person_name=name, person_message=message)
		x = person_comments
		person_comments.blog_view = blog_view
		person_comments.save()
		person_comments = Comment()
		return HttpResponseRedirect(request.path_info)


	show_comments = Comment.objects.all()
	comment_length = len(show_comments)
	comment_len = {
		'comment_length'		:		comment_length,
	}


	return render(request, 'blogview/blog-single.html', {
							'blog_view'			:		blog_view,
							'latest_post'		:	    latest_post,
							'related_context'	:		related_context,
							'show_comments'		:		show_comments,
							'comment_len'		:		comment_len,
							}
					)



def blog_about_page(request):
	owner_about_context = OwnerAbout.objects.all()
	latest_post = Post.objects.all().order_by('post_date')
	owner_post_context = Post.objects.filter(author=request.user.id)
	owner_context = Owner.objects.all()
	post_context = Post.objects.all()
	popular_post_context = Popular_Post.objects.all()
	# print(len(owner_about_context))
	# print(owner_post_context)
	return render(request, 'aboutme/about.html', {
							'owner_about_context'		:		owner_about_context,
							 'owner_post_context'		:		owner_post_context,
							 'owner_context'			:		owner_context,
							 'latest_post'				:		latest_post,
							 'post_context'				:		post_context,
							 'popular_post_context'		:		popular_post_context,
							 }
			 	    )


def category_view(request):
	print(request.POST.get('keyword-search'))
	latest_post = Post.objects.all().order_by('post_date')
	latest_post = Post.objects.all().order_by('post_date')

	#  try this in future may be it work ??

	#  ________________________________________

	# try:
	# 	a = request.POST.get('keyword-search').upper()
	# except AttributeError:
	# 	# a = 'life'
	# 	a = request.POST.get('keyword-search').upper()
	#
	# 	x = 'programming'
	# 	# print(dir(a))

	# _______________________________________

	post_context = Post.objects.all()
	keyword = request.POST.get('keyword-search')
	if keyword == None:
		keyword = 'l'
	else:
		keyword = request.POST.get('keyword-search')
	category_filter_context = Post.objects.filter(post_tages=keyword.upper())
	if keyword == 'L'.lower():
		 keyword = ''

	# print(category_filter_context, 'filter data')

	return render(request, 'blogapp/category.html', {
							'category_filter_context'		:		category_filter_context,
							 'keyword'						:		keyword,
							 'post_context'					:		post_context,
							 'latest_post'					:		latest_post,
							 'latest_post'					:		latest_post,
							 }
					)



def contact_page(request):
	latest_post = Post.objects.all().order_by('post_date')
	post_context = Post.objects.all()
	owner_context = Owner.objects.all()
	# print(owner_context)

	# print(name, email, subject, message)
	if request.method == 'POST':
		name = request.POST.get('your_name')
		email  = request.POST.get('your_email')
		subject = request.POST.get('your_subject')
		message = request.POST.get('your_message')
		if name == '' and email == '' and subject == '' and message == '':
			raise ValueError('Fill everything')
		contact_me = Contact(your_name=name, your_email=email, your_subject=subject, your_message=message)
		contact_me.save()
		x = contact_me
		if contact_me == x:
			del contact_me
		contact_me = Contact()
		return redirect('/')

	return render(request, 'aboutme/contact.html', {
							'owner_context'			:		owner_context,
							'latest_post'			:		latest_post,
							'post_context'			:		post_context,
							}
			)

def comment_view(request):
	return render(request, 'blogview/blog-single.html')

def eye_catcher_post_view(request, pk):
	blogview = get_object_or_404(Eye_Catcher_Post, pk=pk)
	return render(request, 'blogview/blog-single.html', {'blogview':blogview,})



def write_for_us(request):
	latest_post = Post.objects.all().order_by('post_date')
	return render(request, 'registration/write4us.html', {
							'latest_post'			:		 latest_post,})

User = get_user_model()
def signin_page(request): # sign in method
	form = SignInForm(request.POST or None)
	print(form)
	username = request.POST.get('username')
	user_email = request.POST.get('email')
	password = request.POST.get('password')
	print(type(username), user_email, password)
	if form.is_valid():
		context = {
		'form':form,
		}
		new_user = User.objects.create_user(username, user_email, password)
		print(new_user)
		return redirect('/admin')

	# print(dir(form))


	return render(request, 'registration/sign.html', {
								'form':form
							}
						)

def login_page(request):
	return render(request, 'registration/login.html')


def try_page(request):
	form = Popular_Post.objects.all()
	# print(dir(form))
	for x in form:
		print(x)
	# print(dir(x))
	print(x.posts.post_tages)
	# print(form.posts)

	post = 'get_object_or_404(Eye_Catcher_Post, pk=pk)'
	return render(request, 'blogapp/try.html', {
							'post':post,
							'form':form,
							}
				)
