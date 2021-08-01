
from cmd import Cmd
import signal, os

def handler(signum, frame):
    print ('Signal handler called with signal', signum)

    # Set the signal handler
    signal.signal(signal.SIGINT, handler)

class MyPrompt(Cmd):

    def emptyline(self):
        pass
    def do_cve_2019_11510(self, args):
        """Check for Pulse vulnerability"""
        if len(args) == 0:
            print ("Usage: cve_2019_11510 <ip or hostname>")
        else:
            oscom = '/bin/nmap -sV -vv --script cve-2019-11510.nse %s' % args
            os.system(oscom)

    def do_cve_2018_13379(self, args):
        """Check for Fortinet vulnerability"""
        if len(args) == 0:
            print ("Usage: cve_2018_13379 <ip or hostname>")
        else:
            oscom = '/bin/nmap -sV -vv --script cve-2018-13379.nse %s' % args
            os.system(oscom)

    def do_cve_2017_11882(self, args):
        """Check for Microsoft RCE vulnerability"""
        if len(args) == 0:
            print ("Usage: cve_2017_11882 <ip or hostname>")
        else:
            oscom = '/bin/nmap -sV -vv --script cve-2017-11882.nse %s' % args
            os.system(oscom)

    def do_cve_2019_18935(self, args):
        """Check for Telerik RCE vulnerability"""

        if len(args) == 0:
            print("Usage: cve_2019_18935 <ip or hostname>")
        else:
            oscom = '/bin/nmap -sV -vv --script cve-2019-18935.nse %s' % args
            os.system(oscom)

    def do_cve_2019_19781(self, args):
        """Check for Citrix vulnerability"""

        if len(args) == 0:
            print("Usage: cve_2019_19781 <ip or hostname>")
        else:
            oscom = '/bin/nmap -sV -vv --script cve-2019-19781.nse %s' % args
            os.system(oscom)

    def do_exit(self, args):
        """Exit Snode_OS CLI."""

        print("Quitting.")
        raise SystemExit

    def do_cve_2019_18935(self, args):
        """Check for Telerik RCE vulnerability"""
        if len(args) == 0:
            print ("Usage: cve_2019_18935 <ip or hostname>")
        else:
            oscom = '/bin/nmap -sV -vv --script cve-2019-18935.nse %s' % args
            os.system(oscom)

def do_cve_2019_19781(self, args):
    """Check for Citrix vulnerability"""
    if len(args) == 0:
        print ("Usage: cve_2019_19781 <ip or hostname>")
    else:
        oscom = '/bin/nmap -sV -vv --script cve-2019-19781.nse %s' % args
        os.system(oscom)

def do_exit(self, args):
    """Exit Snode_OS CLI."""
    print ("Quitting.")
    raise SystemExit

if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.prompt = 'Snode_OS > '
    prompt.cmdloop('\n  _________                 .___     \n /   _____/ ____   ____   __| _/____    _______________________________ \n \_____  \ /    \ /  _ \ / __ |/ __ \   ___  __ )__  ____/__  __/__    |\n /        \   |  (  <_> ) /_/ \  ___/   __  __  |_  __/  __  /  __  /| |\n/_______  /___|  /\____/\____ |\___  >  _  /_/ /_  /___  _  /   _  ___ |\n        \/     \/            \/    \/   /_____/ /_____/  /_/    /_/  |_|\n          --------------------------------------\n\n')