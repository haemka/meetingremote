import json
from pydbus import SessionBus
from pynput.keyboard import Key, Controller


class MeetingRemote:
    def __init__(self):
        self.bus = SessionBus()
        self.zoom_window_name = 'Zoom Meeting'

    def get_current_window_name(self):
        path = self.bus.get('org.gnome.Shell', '/org/gnome/Shell/Extensions/WindowsExt')
        return path.FocusTitle()

    def activate_window_by_name(self, window_title):
        path = self.bus.get('org.gnome.Shell', '/de/lucaswerkmeister/ActivateWindowByTitle')
        path.activateByTitle(window_title)

    def toggle(self, option):
        if self.check_for_zoom_window():
            self.toggle_zoom(option)

    def toggle_zoom(self, option):
        '''Toggles the microphone or camera button of a Zoom Meeting window

        :param option: A string defining what to toggle. Can be either 'microphone' or 'camera'.
        :type option: str
        '''
        current_window_name = self.get_current_window_name()

        self.activate_window_by_name(self.zoom_window_name)

        if option == 'camera':
            self.toggle_zoom_camera()
        if option == 'microphone':
            self.toggle_zoom_microphone()

        self.activate_window_by_name(current_window_name)

    def check_for_zoom_window(self):
        '''Checks for a running instance of a Zoom Meeting window

        :rtype: bool
        :return: True if at least one is Zoom Metting window instance is found, False otherwise
        '''
        path = self.bus.get('org.gnome.Shell', '/org/gnome/Shell/Extensions/WindowsExt')
        window_list = json.loads(path.List())
        zoom_windows_list = [d['id'] for d in window_list if d['title'] in [self.zoom_window_name]]
        if len(zoom_windows_list) >= 1:
            return True
        else:
            return False

    @staticmethod
    def toggle_zoom_microphone():
        keyboard = Controller()
        with keyboard.pressed(Key.alt_l):
            keyboard.press('a')
            keyboard.release('a')

    @staticmethod
    def toggle_zoom_camera():
        keyboard = Controller()
        with keyboard.pressed(Key.alt_l):
            keyboard.press('v')
            keyboard.release('v')





