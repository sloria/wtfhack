from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
import subprocess


class Command(BaseCommand):
    args = '<app_name>'
    help = 'Compiles coffeescript into javascript'
    option_list = BaseCommand.option_list + (
        make_option('-w', '--watch',
            action='store_true',
            dest='watch',
            default=False,
            help='Turn on watch mode for the coffee/ directory in the given app.'),
    )

    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError('Please provide one app name')
        app_name = args[0]
        target_path = 'sqk/%s/static/js' % (app_name)
        src_path = 'sqk/%s/static/coffee/*.coffee' % (app_name)
        if options['watch']:
            print "Watching .coffee files in %s and compiling them to %s" % (app_name + '/static/coffee', src_path)
            command = "coffee -o %s -cw %s" % (target_path, src_path)
        else:
            print "Compiling .coffee files in %s to .js files in %s" % (app_name + '/static/coffee', target_path)
            command = "coffee -o %s -c %s" % (target_path, src_path)
        subprocess.call(command, shell=True)
        print 'Done.'
