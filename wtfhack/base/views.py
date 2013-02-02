""" Views for the base application """

from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson

from wtfhack.base.models import *
from social_auth.models import UserSocialAuth
from github import Github

import random

from pprint import pprint

def home(request):
    """ View for the home page """
    if Repo.objects.exists():
        languages = Language.all()
        random_language = random.choice(languages)
        return HttpResponseRedirect(reverse('get_repo', args=(random_language,)))
    else:
        return render(request, 'base/home.html')


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
				
def submit(request):
    """ View for the submit page """
    user = UserSocialAuth.objects.filter(provider='github').get(id=request.user.id)
    print user.tokens[u'access_token']
    github = Github(user.tokens[u'access_token'])
    repos = [repo for repo in github.get_user().get_repos()]
    print repos
    return render(request, 'base/submit.html', {'repos': repos})


