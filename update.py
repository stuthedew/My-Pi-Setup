#!/usr/bin/env python
import subprocess, sys, time

print("Starting Update.py")
print(time.strftime("%b  %d %X", time.localtime()))
agUpdate = "apt-get -q update"
agUpgrade = "apt-get -qy upgrade"
rpiUpdate = "rpi-update"
reboot = "/sbin/shutdown -r +1"
pipUpgrade = "pip-review --auto"
commands = [agUpdate, agUpgrade, pipUpgrade, rpiUpdate]

try:
	for cmd in commands:
		try:
			subprocess.call(cmd, shell=True)
		except Exception, e:
			print(e)

finally:
	subprocess.Popen(reboot, shell=True)
	sys.exit()
