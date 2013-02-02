""" Basic models, such as user profile """
from django.db import models
from github import Github

class Repo(models.Model):
    # Full name is required
    full_name = models.CharField(max_length=30, null=False)
    url = models.URLField(null=True)
    language = models.CharField(max_length=40, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)


    @staticmethod
    def all_languages():
        '''Return a list of all the available languages.'''
        return list(Repo.objects.values_list('language', flat=True))

    def save(self, *args, **kwargs):
        '''Override save method to set default url.'''
        BASE = 'https://github.com/'
        # Default url to base url + full_name
        if not self.url:
            self.url = BASE + self.full_name
        super(Repo, self).save(*args, **kwargs)


    def __unicode__(self):
        return "{full_name}: {language}".format(full_name=self.full_name,
                                                language=self.language)