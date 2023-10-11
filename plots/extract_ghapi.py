# ghapi way
# This only sort of works
import matplotlib
import pandas as pd
from pathlib import Path
with open(Path('~/.ghoauth').expanduser(), 'r') as fin:
    token = fin.read()
from ghapi.all import GhApi, pages
from fastcore.net import HTTP403ForbiddenError
from urllib.error import HTTPError
import time
import datetime
api = GhApi(owner='matplotlib', repo='matplotlib', token=token)

def get_all_the_issues(api_call):
    api = api_call.client
    cooloff = 90
    N = 10
    for j in range(N):
        try:
            # hit the API once to get to the right last page
            _ = api_call(state='all')
            print(f"{api.last_page()=}")
            if api.last_page() == 0:
                continue
            issues = pages(api_call, api.last_page(), state='all').concat()
        except (HTTP403ForbiddenError, HTTPError) as e:
            print(e)
            # for reasons that are unclear this can produces 403
            # errors sometimes it works if you give it time and hit it
            # again?!  Assume for very old pages GH does not keep them
            # up and has to regenerate, that times out which ends up
            # coming back as a 403?
            time.sleep(cooloff)
        else:
            return issues
    else:
        raise TimeoutError(f'failed to get all of {api_call} in {N} tries with {cooloff}')

# sometimes this takes a while, if at first it fails, try again!
all_pulls = get_all_the_issues(api.pulls.list)
all_issues_and_pulls = get_all_the_issues(api.issues.list_for_repo)

import json

with open('/tmp/gh_dump.json', 'w') as fout:
    json.dump(d_issues, fout)
