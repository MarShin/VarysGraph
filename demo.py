from graph.alert import Alert
from neomodel import db, config
# from twitter import settings
from twitter.models import Company, Event
config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'
# db.set_connection(settings.NEO4J_URL)

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()
if (getch.__call__() == 'k'):
    # Alert.send_email('martinshin95@gmail.com', 'Varys Alert: There is a score change Tesla')
    # Alert.send_sms('+85262308397', 'Varys Alert: There is a score change in the Tesla')
    Event(name='Model 3 Delivered').save()
    event = Event.nodes.get(name='Model 3 Delivered')
    print 'event node '
    print event
    tesla = Company.nodes.get(name='Tesla')
    event.related_to.connect(tesla)
