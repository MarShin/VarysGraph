from graph.alert import Alert
from neomodel import config
# from twitter import settings
from twitter.models import Company, Event
config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'


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
        import tty
        import sys

    def __call__(self):
        import sys
        import tty
        import termios
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


def clean_event():
    events = Event.nodes
    if events is not None:
        for event in events:
            print('deleting: ' + str(event))
            event.delete()


getch = _Getch()
if (getch.__call__() == 'k'):

    # Alert.send_email('martinshin95@gmail.com', 'Varys Alert: There is a score change Tesla')
    # Alert.send_sms('+85262308397', 'Varys Alert: There is a score change in the Tesla')
    clean_event()

    event = Event.nodes.get_or_none(name='Model 3 Delivered')
    if event is None:  # no Event node found
        new_event = Event(name='Model 3 Delivered').save()
        tesla = Company.nodes.get(name='Tesla')
        new_event.related_to.connect(tesla)
    else:
        tesla = Company.nodes.get(name='Tesla')
        event.related_to.connect(tesla)
