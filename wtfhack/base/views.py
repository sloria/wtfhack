""" Views for the base application """

from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from wtfhack.base.models import *
import random


def home(request):
    """ View for the home page """
    if Repo.objects.all():
        languages = Language.all()
        random_language = random.choice(languages)
        return HttpResponseRedirect(reverse('get_repo', args=(random_language,)))
    else:
        return HttpResponse('WTF. No Repos. Try back later.')


def get_repo(request, language):
    language_obj = get_object_or_404(Language, name=language)
    repos = Repo.objects.filter(language=language_obj)
    # If there are repos with the chosen language
    if repos.exists():
        # Choose a random repo
        repo = random.choice(repos)
    else:
        repo = None
    return render(request, 
                    'base/home.html', 
                    {'all_languages': Language.objects.all(),
                    'selected': language,
                    'repo': repo
                    }
                )
