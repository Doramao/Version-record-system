#!/usr/bin/python

import os, time

# the files and dirs to be backed up are specifiedin a list
source = ['./ceshi']

# the backup must be stored up into a zip file
target_dir = './backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print('Create dir ' + target_dir + 'successfully')

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = input("Enter a comment -->")
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Create dir ' + target + ' successfully')

zip_cmd = "zip -rq '%s' %s" % (target, ' '.join(source))

if os.system(zip_cmd) == 0:
    print
    'Successful backup to ', target
else:
    print('Backup Failed' )