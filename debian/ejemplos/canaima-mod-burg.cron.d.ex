#
# Regular cron jobs for the canaima-mod-burg package
#
0 4	* * *	root	[ -x /usr/bin/canaima-mod-burg_maintenance ] && /usr/bin/canaima-mod-burg_maintenance
