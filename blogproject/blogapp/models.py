from django.db import models

# change auth image of post panel
# change authImg to post Img in post panel

class Owner(models.Model):
    owner_name              =           models.CharField(max_length=50)
    owner_message           =           models.TextField(blank=True, default='Some message')
    owner_image             =           models.ImageField(upload_to='OwnerImg', blank=True)
    see_my_portfolio        =           models.URLField(max_length=200, blank=True)
    owner_twitter           =           models.URLField(max_length=200, blank=True)
    owner_facebook          =           models.URLField(max_length=200, blank=True)
    owner_youtube           =           models.URLField(max_length=200, blank=True)
    owner_linkedin          =           models.URLField(max_length=200, blank=True)

    def __str__(self):
        return "%s"%(self.owner_name)

class OwnerAbout(models.Model):
    owner_Name                      =          models.ForeignKey(Owner, on_delete=models.CASCADE)
    owner_about_title               =          models.CharField(max_length=50)
    owner_about_message             =          models.TextField()
    owner_about_image               =          models.ImageField(upload_to='AboutImg')


    def __str__(self):
        return "%s" % (str(self.owner_Name))



class Author(models.Model):
    author_name              =           models.CharField(max_length=50)
    author_image             =           models.ImageField(upload_to='authImg')
    author_email             =           models.EmailField()
    author_bio               =           models.CharField(max_length=50)
    author_portfolio         =           models.URLField(max_length=50, default='if have one :p', blank=True)
    author_facebook          =           models.URLField(max_length=200, blank=True)
    author_twitter           =           models.URLField(max_length=200, blank=True)
    author_instagram         =           models.URLField(max_length=200, blank=True)
    author_youtube           =           models.URLField(max_length=200, blank=True)
    author_linkedin          =           models.URLField(max_length=200, blank=True)

    def __str__(self):
        return '%s'% (self.author_name)



class Post(models.Model):
    POST_CATEGORY =(
        ('TECHNICAL', 'tech'),
        ('PROGRAMMING', 'programming'),
        ('LIFE', 'life'),
    )
    POST_CHOICES = (
        ('DJANGO','django'),
        ('PYTHON', 'python'),
        ('WEB-DEVELOPMENT', 'web-development'),
    )

    author                              =           models.ForeignKey(Author, on_delete=models.CASCADE)
    post_title                          =           models.CharField(max_length=50)
    post_message_first_para             =           models.TextField()
    post_message_second_para            =           models.TextField(default='working', blank=True)
    post_message_third_para             =           models.TextField(default='this too', blank=True)
    post_image                          =           models.ImageField(upload_to='authImg')
    post_image_optional                 =           models.ImageField(upload_to='authImg', blank=True)
    post_image_optional1                =           models.ImageField(upload_to='authImg', blank=True)
    post_category                       =           models.CharField(max_length=30, choices=POST_CATEGORY)
    post_tages                          =           models.CharField(max_length=30, choices=POST_CHOICES)
    post_date                           =           models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title[:30]

class Contact(models.Model):
    your_name                   =           models.CharField(max_length=30)
    your_email                  =           models.EmailField()
    your_subject                =           models.CharField(max_length=30)
    your_message                =           models.TextField()

    def __str__(self):
        return '%s, subject: %s'%(self.your_name, self.your_subject[:15])


class Comment(models.Model):
    person_name                 =           models.CharField(max_length=50)
    person_message              =           models.TextField()
    comment_date                =           models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s, message %s' % (self.person_name, self.person_message[:30])

class Eye_Catcher_Post(models.Model):
    POST_CATEGORY = (
        ('TECHNICAL', 'technical'),
        ('LIFE', 'life'),
        ('PROGRAMMING', 'programming'),
    )
    POST_TAGES = (
        ('PYTHON','python'),
        ('DJANGO','django'),
        ('ANDROID','android'),
    )
    author                          =           models.ForeignKey(Author, on_delete=models.CASCADE)
    post_title                      =           models.CharField(max_length=50)
    post_message_first_para         =           models.CharField(max_length=100)
    post_image                      =           models.ImageField(upload_to='PostImg', null=True)
    post_message_second_para        =           models.CharField(max_length=100, blank=True, null=True)
    post_image_second_para          =           models.ImageField(upload_to='PostImg', blank=True, null=True)
    post_message_third_para         =           models.CharField(max_length=100, blank=True, null=True)
    post_image_third_para           =           models.ImageField(upload_to='PostImg', blank=True, null=True)
    post_category                   =           models.CharField(max_length=30, choices=POST_CATEGORY)
    post_tages                      =           models.CharField(max_length=30, choices=POST_TAGES)
    post_date                       =           models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s by: %s' % (self.post_title[:30], self.author.author_name)

class Popular_Post(models.Model):
    posts                           =           models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.posts.post_title[:20]
