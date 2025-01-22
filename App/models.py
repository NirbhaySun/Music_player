from django.db import models

# Create your models here.
class Song(models.Model):
    title=models.TextField()
    artist=models.TextField()
    image=models.ImageField(upload_to='images/')
    audio_file=models.FileField(upload_to='songs/')
    audio_link=models.CharField(max_length=200,blank=True,null=True)
    lyrics=models.TextField(blank=True,null=True)
    duration=models.CharField(max_length=20)
    paginate_by=2
    
    def __str__(self):
        return self.title
    