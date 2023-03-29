from django.db import models
from rest_framework.serializers import ValidationError
from mptt.models import MPTTModel, TreeForeignKey
from django.db.models.signals import pre_save
from django.dispatch import receiver
import logging



class Content(models.Model):
    files = models.CharField(max_length=30)
    type_file = models.CharField(max_length=5)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length = 200)
    authors = models.CharField(max_length = 30)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)

class Channel(MPTTModel):
    title = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    picture = models.CharField(max_length=30)
    content = models.OneToOneField(Content, on_delete=models.CASCADE, blank=True, null=True, related_name='channel')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['title']

    # def save(self, *args, **kargs):

    #     # if self.is_branch and self.content:
    #     #     raise ValidationError("A channel with subchannels cannot have any content underneath.")

    #     # if self.is_leaf and self.children.exists():
    #     #     raise ValidationError("A channel with contents cannot have any subchannel underneath.")
    #     if self.children.exists() and self.content.exists():
    #         raise ValidationError("A channel needs a content or a subchannel.")

    #     if self.children == None and self.content == None:
    #         raise ValidationError("A channel needs a content or a subchannel.")
    #     if True:
    #         raise ValidationError("jeje")
    #     super(Channel, self).save(*args, **kargs)


@receiver(pre_save, sender = Channel)
def channel_pre_save_handler(sender, instance, *args, **kargs):

    # if not instance.content and not instance.children.all():
    #     raise ValidationError("A channel needs a content or a subchannel.")

    if instance.content and instance.children:
        raise ValidationError("A channel with contents cannot have any subchannel.")






