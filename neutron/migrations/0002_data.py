from django.db import migrations
from django.core.management import call_command


def loadfixture(apps, schema_editor):
    fixtures = 'newsOrganizations references articles'.split(' ')
    call_command('loaddata', *fixtures)


class Migration(migrations.Migration):

    dependencies = [
        ('neutron', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(loadfixture),
    ]
