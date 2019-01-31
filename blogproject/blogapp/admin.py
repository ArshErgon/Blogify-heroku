from django.contrib import admin

from .models import Author,  Post, Owner,  Contact, Comment, Eye_Catcher_Post, Popular_Post


admin.site.register(Owner)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(Eye_Catcher_Post)
admin.site.register(Popular_Post)
