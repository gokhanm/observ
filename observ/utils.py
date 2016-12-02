# Copyright 2016 Gokhan MANKARA <gokhan@mankara.org> 

from __future__ import print_function
from contextlib import contextmanager
import io
import sys
from subprocess import Popen, PIPE

from observ import PY3
from observ.exceptions import ObservPipCommandException


class RedirectStdOut():
    """
        RedirectStdOut class used if PY3 is False
        in python 2.7.x redirect_stdout not found in contextlib
    """
    
    @contextmanager
    def stdout_redirector(self, stream):
        old_stdout = sys.stdout
        sys.stdout = stream
        try:
            yield
        finally:
            sys.stdout = old_stdout


class Util():
    def command(self, cmd):
        """
            Run the cmd command
            :return: a tuple of stdout, stderr and returncode
        """
        try:
            p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
            output, error = p.communicate()
            returncode = p.returncode
        
            return output, error, returncode
        except OSError:
            output = False
            error = False
            returncode = False

            return output, error, returncode

    def list(self, parse=False):
        """
            :param parse: When the --list parameter is used. parse is False
                          When the --notify parameter is used. parse is True
        """
        #FIXME: find pythonic way
        up_to_date = False

        cmd2 = ['pip2', 'list', '--outdated', '--format=columns']
        result2, error2, returncode2 = self.command(cmd2)
    
        cmd3 = ['pip3', 'list', '--outdated', '--format=columns']
        result3, error3, returncode3 = self.command(cmd3)

        if parse:
            if PY3:
                f = io.StringIO()
                from contextlib import redirect_stdout
            else:
                f = io.BytesIO()
                redirect_stdout = RedirectStdOut().stdout_redirector

            with redirect_stdout(f):
                # result is False when command not found
                if result2 is not False and len(result2) != 0:
                    print('Python 2.7.x pip outdated packages', result2, sep='\n')
                else:
                    if result2 is False:
                        raise ObservPipCommandException('pip2 command not found')
                    # If there is no result on the output. len(result) == 0
                    up_to_date = True

                # result is False when command not found
                if result3 is not False and len(result3) != 0:
                    print('Python 3.x pip outdated packages', result3, sep='\n')
                else:
                    if result3 is False:
                        raise ObservPipCommandException('pip3 command not found')
                    # If there is no result on the output. len(result) == 0
                    up_to_date = True

            if up_to_date:
                print('All packages are up-to-date')
                exit(0)

            return f.getvalue()
        # if parse is False.
        else:
            up_to_date = False

            if result2 is not False and len(result2) != 0:
                if PY3:
                    result2 = result2.decode('utf-8')
                print('Python 2.7.x pip outdated packages\n', result2, sep='\n')
            else:
                if result2 is False:
                    raise ObservPipCommandException('pip2 command not found')                
                up_to_date = True

            if result3 is not False and len(result3) != 0:
                if PY3:
                    result3 = result3.decode('utf-8')
                print('Python 3.x pip outdated packages\n', result3, sep='\n')
            else:
                if result3 is False:
                    raise ObservPipCommandException('pip3 command not found')
                up_to_date = True

            if up_to_date:
                print('All packages are up-to-date')
                exit(0)

