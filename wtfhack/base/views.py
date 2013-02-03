""" Views for the base application """

from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson
from django.views.decorators.csrf import ensure_csrf_cookie

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
        return render(request, 'base/home.html', {})


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
                    {'all_languages': Language.objects.order_by('name'),
                    'selected': language,
                    'repo': repo
                    }
                )

@ensure_csrf_cookie		
def submit(request):
    """ View for the submit page.

    Must be a POST request """
    if request.user.is_active:
        user = UserSocialAuth.objects.filter(provider='github').get(user_id=request.user.id)
        github = Github(user.tokens[u'access_token'])
        repos = [repo for repo in github.get_user().get_repos()]
        return render(request, 'base/submit.html', {'repos': repos})
    else:
        return HttpResponseRedirect(reverse('socialauth_begin', args=('github',)))

def add_repo(request):
    """ View for adding a repo """
    user = UserSocialAuth.objects.filter(provider='github').get(user_id=request.user.id)
    github = Github(user.tokens[u'access_token'])
    name = request.POST['name']
    repo = github.get_user().get_repo(name)
    message = {'success': None}
    try:
        language_str = repo.language.lower()
    except AttributeError:
        message['success'] = False
        message['message'] = "Could not add repo because it doesn't have a language. Try specifying the language in your Github repo settings."
        json = simplejson.dumps(message)
        return HttpResponse(json, mimetype='application/json')

    # TODO: exception handling here
    language_obj, created_lang = Language.objects.get_or_create(name=repo.language.lower())
    repo_obj, created_repo = Repo.objects.get_or_create(full_name=repo.full_name,
                                                description=repo.description,
                                                language=language_obj)

    if not created_repo:
        message['success'] = False
        message['message'] = '{} is already in our collection'.format(name)
    else:
        message['success'] = True
        message['message'] = 'Successfully added {}.'.format(name)
    json = simplejson.dumps(message)
    return HttpResponse(json, mimetype='application/json')


