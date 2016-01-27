from subprocess import call
from time import sleep

import yaml
from travispy import TravisPy


with open('config.yaml', 'r') as f:
    config = yaml.load(f)

t = TravisPy.github_auth(config['gh_token'])
repo = t.repo(config['gh_repo'])

while True:
    old_id = open('last', 'r').readline()
    new_id = str(repo.last_build_id)

    latest_build = t.build(new_id)

    if new_id != old_id:
        print 'New build available'

        if not latest_build.successful:
            print 'Last build ID is failing, skipping deployment'
            sleep(60)
	    continue
        
        print 'Latest build ID is "%s" and was successful, now deploying...' % new_id

        call(['./deploy.sh'])

        with open('last', 'w') as f:
            f.write(new_id)

    servers_not_running = call(['pgrep', '-f', 'runserver'])

    if servers_not_running:
        print 'Server not running, starting now...'
        call(['./deploy.sh'])
    else:
        print 'Server already running on http://0.0.0.0:8080'

    sleep(60)
