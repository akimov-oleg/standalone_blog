from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
from auth_app.forms import MyRegistrationForm, UserChangeForm
from django.http import Http404, JsonResponse
from django.template import loader
from django.template.context_processors import csrf
from django.contrib.auth.decorators import user_passes_test
from main_app.models import *
from main_app.forms import PostForms, CommentForms
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# доступ у админке только суперпользователю
@user_passes_test(lambda u: u.is_superuser)
def admin_page(request):
    users = User.objects.all()
    user_form = MyRegistrationForm()

    return render(request, 'admin_page.html', {'users': users, 'form': user_form})


def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return HttpResponseRedirect('/admin')


def get_user_form(request, user_id):
    """
    Возвращает заполненную форму для редактирования Пользователя(User) с заданным user_id
    """
    if request.is_ajax():
        user = get_object_or_404(User, id=user_id)
        user_form = MyRegistrationForm(instance=user)
        context = {'form': user_form, 'id': user_id}
        context.update(csrf(request))
        html = loader.render_to_string('reg_form_include.html', context)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)
    raise Http404


def create_user(request, user_id=None):
    """
    Создает Пользователя(User)
    Или редактирует существующего, если указан  user_id
    """
    if request.is_ajax():
        print('user_id = ', user_id)
        if not user_id:
            print('Not user_id')
            user = User(request.POST)
        else:
            user = get_object_or_404(User, id=user_id)
            user = UserChangeForm(request.POST or None, instance=user)
        if user.is_valid():
            user.save()
            users = User.objects.all()
            html = loader.render_to_string('users_list_include.html', {'users': users}, request=request)
            data = {'errors': False, 'html': html}
            return JsonResponse(data)
        else:
            errors = user.errors.as_json()
            return JsonResponse({'errors': errors})

    raise Http404


def admin_posts(request):
    posts = Post.objects.all()
    return render(request, 'admin_posts.html', {'posts': posts})



def create_post(request):
    if request.method == 'POST':
        form = PostForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/posts/')
        context = {'form': form}
        return render(request, 'update_post.html', context)
    context = {'form': PostForms()}
    return render(request, 'update_post.html', context)



def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return HttpResponseRedirect('/admin/posts/')
    
def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        # form = PostForms(request.POST or None, instance=post)
        form = PostForms(request.POST, instance=post)
        if form.is_valid():
            post.save()
            return HttpResponseRedirect('/admin/posts/')
        context = {'form': form}
        return render(request, 'update_post.html', context)
    context = {'form': PostForms(instance=post)}
    return render(request, 'update_post.html', context)


'''class create_comment(CreateView):
    model = Comment
    template_name = 'comment_create.html'
    success_url = '/admin/comments/'
    fields = ('__all__')'''


def create_comment(request, post_id, user_id):    
    if request.method == 'POST':
        form = CommentForms(request.POST)
        if form.is_valid():
            post = Post.objects.get(id = post_id)
            user = User.objects.get(id = user_id)

            comment = form.save(commit=False)
            comment.post_id = post
            comment.user_id = user
            comment.save()

            return HttpResponseRedirect('/post_text/{}'.format(post_id))
        context = {'form': form}
        return render(request, 'create_comment.html', context)
    context = {'form': CommentForms()}
    return render(request, 'create_comment.html', context)

def update_comment(request, comment_id):    
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        # form = PostForms(request.POST or None, instance=post)
        form = CommentForms(request.POST, instance=comment)
        if form.is_valid():
            comment.save()
            return HttpResponseRedirect('/post_text/{}#comments_header'.format(comment.post_id.id))
        context = {'form': form}
        return render(request, 'create_comment.html', context)
    context = {'form': CommentForms(instance=comment)}
    return render(request, 'create_comment.html', context)

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return HttpResponseRedirect('/post_text/{}'.format(comment.post_id.id))


"""def admin_posts_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'admin_post_detail.html', {'post':post})"""



# Demo-views
# def send_json(request):
#     # Если данные были отправлены ajax'ом
#     if request.is_ajax():
#         # Данные хранятся также в атрибуте POST или GET, в зависимости от методы отправки данных
#         request_data = request.POST
#         # Словарик при отправке автоматически будет преобразован к json
#         send_data = {'key': 'value'}
#         return JsonResponse(send_data)
#     raise Http404


