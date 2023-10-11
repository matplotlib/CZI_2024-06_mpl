# gidgethub way
import aiohttp
import gidgethub
import gidgethub.aiohttp
import re
import pymongo
import asyncio

conn = pymongo.MongoClient()
db = conn.get_database('mpl_info')
col = db.get_collection('log')
m_cache = db.get_collection('cache')
issues = db.get_collection('issues')


def dump_cache(cache, m_cache):
    for k, v in cache.items():
        m_cache.replace_one({'k': k}, {'k': k, 'v': v}, upsert=True)


def restore_cache(cache, m_cache):
    for doc in m_cache.find():
        cache[doc['k']] = doc['v']


try:
    with open(os.path.expanduser('~/.ghoauth'), 'r') as f:
        oauth_token = f.read()
except FileNotFoundError:
    oauth_token = None

try:
    cache
except NameError:
    cache = {}
    restore_cache(cache, m_cache)

async def get_issues(org, repo, oauth_token):
    async with aiohttp.ClientSession() as session:
        gh = gidgethub.aiohttp.GitHubAPI(session, 'tacaswell',
                                         oauth_token=oauth_token, cache=cache)
        data = []
        async for d in gh.getiter(f"/repos/{org}/{repo}/issues{{?state}}",
                                  {'state': 'all'}):
            data.append(d)

        dump_cache(cache, m_cache)
        return data

async def get_new_contributor_prs(org, repo, oauth_token):
    async with aiohttp.ClientSession() as session:
        gh = gidgethub.aiohttp.GitHubAPI(session, 'tacaswell',
                                         oauth_token=oauth_token, cache=cache)
        data = []
        async for d in gh.getiter(f"/repos/{org}/{repo}/issues{{?state}}",
                                  {'state': 'open'}):
            if (d['author_association'] in {'CONTRIBUTOR', 'FIRST_TIME_CONTRIBUTOR'} and
                'pull_request' in d):

                data.append(d)
            if len(data) > 10:
                break

        dump_cache(cache, m_cache)
        return data

#d_issues = await get_issues('matplotlib', 'matplotlib', oauth_token)
# for d in new_issues:
#    print(f"{d['user']['login']: <20} {d['author_association']: <24} {d['pull_request']['url']}")

import json

with open('/tmp/gh_dump.json', 'w') as fout:
    json.dump(d_issues, fout)
