#mhacks_gitogether.py

from urllib.request import urlretrieve, Request, urlopen
import pprint
import json
import traceback

def get_repos(username):

    account_url = "https://github.com/%s?tab=repositories"%username

    href_list = []

    req = Request(account_url, headers={'User-Agent': 'Mozilla/5.0'})

    # Splits the file into its components
    with urlopen(req) as response:
        extracted_file = str(response.read())[2:][:-3]

    # Finds the beginning of the repo listings
    repo_header = extracted_file.find('<li class="col-12 d-block width-full py-4 border-bottom public source" itemprop="owns" itemscope itemtype="http://schema.org/Code">')

    # Finds the end of the repo listings
    repo_footer = extracted_file.find('<div class="paginate-container">')

    # Prepares HTML for extraction
    extracted_file = extracted_file[repo_header:repo_footer].split('\\n')

    # Extracts hrefs from html
    for line in extracted_file:
        if 'href="/%s/' % username in line and 'itemprop="name codeRepository">' in line:
            # Isolates repo names
            line = line[line.find('href="/%s/' % username) + 8 + len(username):line.find('itemprop="') - 2]

            # Adds to list of known repos
            href_list.append(line)

    return href_list

def get_langs(username, repo):
    repo_url = "https://github.com/%s/%s"%(username, repo)

    lang_dict = {}

    req = Request(repo_url, headers={'User-Agent': 'Mozilla/5.0'})

    # Splits the file into its components
    with urlopen(req) as response:
        extracted_file = str(response.read())[2:][:-3]

    # Finds the beginning of the repo listings
    repo_header = extracted_file.find('<div class="repository-lang-stats-graph js-toggle-lang-stats" title="Click for language details" data-ga-click="Repository, language bar stats toggle, location:repo overview">')

    # Finds the end of the repo listings
    repo_footer = extracted_file.find('<div class="file-navigation in-mid-page">')

    # Prepares HTML for extraction
    extracted_file = extracted_file[repo_header:repo_footer].split('\\n')

    # Extracts langs from html
    for line in extracted_file:

        if '<span class="language-color" aria-label="' in line:

            # Isolates repo names
            line = line[line.find('aria-label="') + 12:line.find('" style="')].split()

            # Adds to list of known repos
            lang_dict[line[0]] = float(line[-1][:-1])

    return lang_dict

def get_master(username):
    repos = get_repos(username)

    langs = {'name':username}

    for repo in repos:
        new_lang = get_langs(username, repo)

        for lang in new_lang:
            if lang in langs:
                langs[lang] += new_lang[lang]

            else:
                langs[lang] = new_lang[lang]

    return langs

username = input("Username: ")

json_data = get_master(username)

with open('%s.rah'%username, 'w') as outfile:
    json.dump(json_data, outfile)

#pprint.pprint(get_langs(get_repos('henrytwo')))
