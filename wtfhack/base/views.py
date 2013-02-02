""" Views for the base application """

from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from wtfhack.base.models import Repo
import random


def home(request):
    """ View for the home page """
    if Repo.objects.all():
        languages = Repo.all_languages()
        random_language = random.choice(languages)
        return HttpResponseRedirect(reverse('get_repo', args=(random_language,)))
    else:
        return HttpResponse('WTF. No Repos. Try back later.')


def get_repo(request, language):
    repos = Repo.objects.filter(language=language)
    # If there are repos with the chosen language
    if repos.exists():
        # Choose a random repo
        repo = random.choice(repos)
    else:
        repo = None
    return render(request, 
                    'base/home.html', 
                    {'all_languages': Repo.all_languages(),
                    'selected': language,
                    'repo': repo
                    }
                )
