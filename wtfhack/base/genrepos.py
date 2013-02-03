#!/usr/bin/env python
from wtfhack.base.models import *
import random
from github import Github


LANGUAGES = ['Android',
            'PHP',
            'Clojure',
            'Haskell',
            'Java',
            'Javascript',
            'Cofeescript',
            'Objective-C',
            'Python',
            'R',
            'Ruby',
            'Scala',
            ]

def get_repos(language, query='popular'):
    '''Returns 100 most popular or random repos.

    Arguments:
    language (str) - The language to search for 
    query (str) - Search from either 'popular' repos or
                    'random'.
    '''

    g = Github()
    repos = None
    search = g.legacy_search_repos(language)
    if query == 'popular':
        repos = search.get_page(0)
    elif query == 'random':
        page = random.randint(2, 150)
        repos = search.get_page(page)
    else:
        raise ValueError("query must be either 'popular' or 'random'")
    return repos

def save_to_db(n=5):
    '''Saves n repos for each language to the database.'''
    for language in LANGUAGES:
        print "Generating {n} repos written in {lang}".format(n=n, lang=language)
        language_obj, created_lang = Language.objects.get_or_create(name=language.lower())
        repos = get_repos(language, query='random')
        for i in range(n):
            repo = repos.pop(random.randint(0, len(repos)))
            repo_obj, created_repo = Repo.objects.get_or_create(full_name=repo.full_name,
                                                description=repo.description,
                                                language=language_obj)

    return True

if __name__ == '__main__':
    save_to_db(n=5)