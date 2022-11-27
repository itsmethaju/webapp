
from django.db import models
from embed_video.fields import EmbedVideoField
# Create your models here.

class Service(models.Model):
    titel =models.CharField(max_length=150)
    img = models.ImageField(upload_to='img')
    rol1 = models.CharField(max_length=150)
    rol2 = models.CharField(max_length=150)
    rol3 = models.CharField(max_length=150)
    desc =models.TextField()
    price =models.FloatField()

    def __str__(self):
        return self.titel

class Resume(models.Model):
    company_name =models.CharField(max_length=250)
    st_end_year =models.CharField(max_length=250)
    project_name =models.CharField(max_length=250)
    desc =models.TextField()
    import_word1=models.CharField(max_length=250)
    import_mord2 =models.CharField(max_length=250)
    import_word3 = models.CharField(max_length=250)
    short_desc =models.TextField()

    def __str__(self):
        return self.company_name

class Testimonials(models.Model):
    name =models.CharField(max_length=250)
    img =models.ImageField(upload_to='img')
    words =models.TextField()
    fb_link =models.URLField()

    def __str__(self):
        return self.name

class Logos(models.Model):
    img =models.ImageField(upload_to='img')

# end index html pages

# prot folio 


class Portfolio(models.Model):
    project_titel =models.CharField(max_length=250)
    img =models.ImageField(upload_to='img')
    desc =models.TextField()
    date =models.DateField()
    client =models.CharField(max_length=150)
    project_domain = models.CharField(max_length=200)
    project_link =models.URLField()

    def __str__(self):
        return self.client

class Gallery(models.Model):
    portfolio =models.ForeignKey(Portfolio,on_delete=models.CASCADE)
    img =models.ImageField(upload_to='img')

class Detail_opations(models.Model):
    protfolio =models.ForeignKey(Portfolio,on_delete=models.CASCADE)
    heading =models.CharField(max_length=250)
    desc =models.TextField()

    def __str__(self):
        return self.desc
#

class BlogCatgory(models.Model):
    name =models.CharField(max_length=200)

    def __str__(self):
        return self.name

class BlogTages(models.Model):
    name =models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Bloge(models.Model):
    titel = models.CharField(max_length=250)
    author_name =models.CharField(max_length=200)
    deate =models.DateField()
    category =models.ForeignKey(BlogCatgory,on_delete=models.CASCADE, null=True, default=None,)
    tages =models.ForeignKey(BlogTages,on_delete=models.CASCADE, null=True, default=None,)
    video =models.URLField()
    desc =models.TextField()
    quotes =models.TextField()
    author_img =models.ImageField(upload_to='img')
    comment_word =models.TextField()
    fb_link =models.URLField()
    inst_link =models.URLField()
    twt_link =models.URLField()
    wk_link =models.URLField()

    def __str__(self):
        return self.titel

class Blog_image(models.Model):
    blog = models.ForeignKey(Bloge,on_delete=models.CASCADE)
    img =models.ImageField(upload_to='img')




class Team(models.Model):
    name = models.CharField(max_length=250)
    img =models.ImageField(upload_to='img')
    roll =models.CharField(max_length=200)
    desc = models.TextField()
    fb_link=models.URLField()
    inst_link =models.URLField()
    twt_link =models.URLField()
    wk_link =models.URLField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email =models.EmailField()
    comments = models.TextField()

    def __str__(self):
        return self.name

class Subscribe(models.Model):
    email =models.EmailField()

    def __str__(self):
        return self.email


class VideoPresentation(models.Model):
    titel =models.CharField(max_length=250)
    img = models.ImageField(upload_to='img')
    video_url =models.URLField()
    desc = models.TextField()
    youtub_chanel_url = models.URLField()

    def __str__(self):
        return self.titel
