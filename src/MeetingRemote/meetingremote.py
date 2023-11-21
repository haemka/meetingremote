import argparse
from . import MeetingRemote


def main():
    parser = argparse.ArgumentParser(prog='ZoomRemote', description='Remote control Zoom Desktop client.',
                                     epilog='Requires GNOME extensions "Window Calls Extended by hseliger" ('
                                            'https://github.com/hseliger/window-calls-extended) and "Activate Window '
                                            'By Title by lucaswerkmeister" ('
                                            'https://github.com/lucaswerkmeister/activate-window-by-title).')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-m', '--microphone', action='store_true', help='Toggle microphone.')
    group.add_argument('-c', '--camera', action='store_true', help='Toggle camera.')
    args = parser.parse_args()

    remote = MeetingRemote()

    if args.microphone:
        remote.toggle('microphone')
    if args.camera:
        remote.toggle('camera')


if __name__ == '__main__':
    main()

