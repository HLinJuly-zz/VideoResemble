__author__ = 'ZHANGLIN'

import os
import sys

#     convert to other format
def convert(input, output):
    if getattr(sys, 'frozen', None):
        path = sys.MEIPASS
    else:
        path = os.path.abspath(os.path.dirname(sys.argv[0]))

    if sys.platform == 'win32':
        cmd = 'ffmpeg.exe'
    elif sys.platform == 'darwin':
        cmd = 'ffmpeg'
    else:
        raise BaseException("just support Windows and OS X'")

    cmd_path = os.path.join(path, cmd)
    encoding = 'utf-8' if sys.platform == 'darwin' else 'gbk'

    os.popen3(u"{0} -i {1} {2}".format(cmd_path, input, output).encode(encoding))
