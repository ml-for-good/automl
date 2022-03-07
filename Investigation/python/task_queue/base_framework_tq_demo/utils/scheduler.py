import os
import time
import subprocess
from flask_apscheduler import APScheduler
from GLOBAL_KEY import *

schedule = APScheduler()

def replace_global_key(var_name, var_new):
    var_line = subprocess.getoutput('cat GLOBAL_KEY.py | grep {}'.format(var_name))
    var_line_lst = var_line.split('=')
    var_line_lst[1] = str(var_new)
    var_new_line = '='.join(var_line_lst)
    os.system("sed -i '' 's/{}/{}/g' GLOBAL_KEY.py".format(var_line, var_new_line))

@schedule.task("cron", id="exec_reload_config", second="*/1")
def reload_config():
    for f_path in LAST_CONFIG_MODIFY_TIME:
        modified = os.stat(f_path).st_mtime
        if modified != LAST_CONFIG_MODIFY_TIME[f_path]:
            LAST_CONFIG_MODIFY_TIME[f_path] = modified
            replace_global_key("MODIFIED_TOKEN", modified)