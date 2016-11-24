#!/usr/bin/env python
# coding: utf-8
import subprocess
#Команда 1
uname = "uname"
uname_arg = "-a"
print "Gathering susrystem information with %s command:\n" % uname
subprocess.call([uname, uname_arg])
#Команда 2
diskspace = "df"
diskspace_arg = "-h"
print "Gathering diskspace information %s command:\n" % diskspace
subprocess.call([diskspace, diskspace_arg])
