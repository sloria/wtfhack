""" Basic models, such as user profile """
from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=40, null=False)
    learn_url = models.URLField(null=True, blank=True)

    @staticmethod
    def all():
        return [l.name for l in Language.objects.all()]
    def __unicode__(self):
        return self.name

class Repo(models.Model):
    # Full name is required
    full_name = models.CharField(max_length=30, null=False)
    url = models.URLField(null=True)
    language = models.ForeignKey(Language, related_name='repos')
    description = models.CharField(max_length=300, null=True, blank=True)


    def save(self, *args, **kwargs):
        '''Override save method to set default url.'''
        BASE = 'https://github.com/'
        # Default url to base url + full_name
        if not self.url:
            self.url = BASE + self.full_name
        super(Repo, self).save(*args, **kwargs)


    def __unicode__(self):
        return "{full_name}: {language}".format(full_name=self.full_name,
                                                language=self.language.name)


