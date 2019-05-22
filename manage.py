#!/usr/bin/env python
import os
import sys

port = 8000
def kill_process():
        ret = os.popen("netstat -nao|findstr " + str(port))
        #注意解码方式和cmd要相同，即为"gbk"，否则输出乱码
        str_list = ret.read().decode('gbk')
 
        ret_list = re.split('',str_list)
        try:
                process_pid = list(ret_list[0].split())[-1]
                os.popen('taskkill /pid ' + str(process_pid) + ' /F')
                print ("端口已被释放")
        except:
                print ("端口未被使用")


if __name__ == "__main__":
    # kill_process()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_intrduction.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
