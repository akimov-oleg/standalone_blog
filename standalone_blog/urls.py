"""standalone_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls   import url
from django.contrib     import admin
from auth_app.views     import *
from admin_app.views    import *
from main_app.views     import *

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', index_page),
    url(r'^login/$', login_page),    
    url(r'^user/login/$', login),
    url(r'^user/logout/$', logout),
    url(r'^user/registration/$', registration),
]

# основное приложение
urlpatterns += [
    url(r'^post_headers/$', post_headers),    
    url(r'^post_text/(\d+)$', post_text), 
]

# администрирование 
urlpatterns += [
    # администрирование пользователей
    url(r'^admin/$', admin_page),
    url(r'^admin/delete/user/(\d+)$', delete_user),
    url(r'^admin/get_user_form/(\d+)$', get_user_form),
    url(r'^admin/create/user/(\d*)$', create_user),    

    # администрирование публикаций
    url(r'^admin/posts/$', admin_posts),
    url(r'^admin/create/post/$', create_post),
    url(r'^admin/update/post/(\d+)$', update_post),
    url(r'^admin/delete/post/(\d+)$', delete_post),

    # администрирование комментариев
    url(r'^admin/create/comment/(\d+)/(\d+)/$', create_comment),
    url(r'^admin/update/comment/(\d+)$', update_comment),
    url(r'^admin/delete/comment/(\d+)$', delete_comment),
    
]
