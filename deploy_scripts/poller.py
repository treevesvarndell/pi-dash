from time import sleep
from subprocess import call

from travispy import TravisPy


t = TravisPy.github_auth('e6ce5645b787d809e949d2341eaf962592d72b69')
repo = t.repo('treevesvarndell/dashboard')

while True:
    old_id = open('last.txt', 'r').readline()
    new_id = str(repo.last_build_id)

    latest_build = t.build(new_id)

    if new_id != old_id:
        print 'New build available'

        if not latest_build.successful:
            print 'Latest build not successful'
            continue

        print 'Last build ID is failing, skipping deployment'
        print 'Latest build ID is "%s" and was successful, now deploying...' % new_id

        call(['./deploy.sh'])

        with open('last.txt', 'w') as f:
            f.write(new_id)

    servers_not_running = call(['pgrep', '-f', 'runserver'])

    if servers_not_running:
        print 'Server not running, starting now...'
        call(['./deploy.sh'])
    else:
        print 'Server already running on http://0.0.0.0:8080'

    sleep(60)
