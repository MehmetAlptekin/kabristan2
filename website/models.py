import email
from statistics import mode

from unicodedata import category, name
from django.db import models
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File

from ckeditor.fields import RichTextField
from unidecode import unidecode
from django.utils.text import slugify
import datetime
import random


class systemImageBilgi(models.Model):
    banner_title = models.CharField(max_length = 150, null=True, blank=True)
    banner_link = models.CharField(max_length = 150, null=True, blank=True)
    banner_description = RichTextField(max_length = 1000, null=True, blank=True) 
    image = models.ImageField(null = False,blank=True,default='profile_pics/default.jpg')
    class Meta:
        verbose_name_plural = "Slider"
    def __str__(self):
          return self.banner_title+ " - " + self.banner_link+ " - " + self.banner_description+ " - "




class KisiDetay(models.Model):
    url=models.URLField(default="Some String")
    name = models.CharField(max_length=200,blank=True,null=True)
    surname = models.CharField(max_length=200,blank=True,null=True)
    birth_date = models.DateField(max_length=200,blank=True,null=True)
    phone_number = models.CharField(max_length=200,blank=True,null=True)
    image = models.ImageField(upload_to='qrcode',blank=True)
    city = models.CharField(max_length=200,blank=True,null=True)

    def save(self,*args,**kwargs):
        qrcode_img=qrcode.make(self.url)
        canvas=Image.new("RGB", (245,220),"white")
        draw=ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        buffer=BytesIO()
        canvas.save(buffer,"PNG")
        self.image.save(f'image{random.randint(0,9999)}',File(buffer),save=False)
        canvas.close()
        super().save(*args,**kwargs)


    # def get_unique_slug(self):
    #     sayi=0
    #     slug = slugify(unidecode(self.name))
    #     new_slug=slug
    #     while KisiDetay.objects.filter(slug=new_slug).exists():
    #         sayi+=1
    #         new_slug="%s-%s"%(slug,sayi)
    #     slug = new_slug
    #     return slug

    # def save(self, *args, **kwargs):
    #     if self.id is None:
    #         name = self.get_unique_slug()
    #         self.slug = slugify(unidecode(name))
    #     else:
    #         detay=KisiDetay.objects.get(slug=self.slug)
    #         if detay.name != self.name:
    #             self.slug=self.get_unique_slug()
    #     super(KisiDetay,self).save()

    def __str__(self):
        return self.name




class BlogCategory(models.Model):
    name = models.CharField(max_length = 250,null=True,blank=True)
    def __str__(self):
        return self.name


class blogBilgi(models.Model):
    blog_date = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    blog_title = models.CharField(max_length = 150, null=True, blank=True)
    blog_description = models.CharField(max_length = 100, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True,null=True)
    image = models.ImageField(null = False,blank=True, default='profile_pics/default.jpg')
    class Meta:
        verbose_name_plural = "Blog"
    def __str__(self):
        return self.blog_title + " - " + self.blog_description

    def get_unique_slug(self):
        sayi=0
        slug = slugify(unidecode(self.blog_title))
        new_slug=slug
        while blogBilgi.objects.filter(slug=new_slug).exists():
            sayi+=1
            new_slug="%s-%s"%(slug,sayi)
        slug = new_slug
        return slug

    def save(self, *args, **kwargs):
        if self.id is None:
            blog_title = self.get_unique_slug()
            self.slug = slugify(unidecode(blog_title))
        else:
            blog=blogBilgi.objects.get(slug=self.slug)
            if blog.blog_title != self.blog_title:
                self.slug=self.get_unique_slug()
        super(blogBilgi,self).save()


