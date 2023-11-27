import json
from pydbus import SessionBus
from pynput.keyboard import Key, Controller


class MeetingRemote:
    def __init__(self):
        self.bus = SessionBus()
        self.skype_window_name = 'Skype'
        self.zoom_window_name = 'Zoom Meeting'

        self.keyboard = Controller()

    def get_current_window_name(self):
        path = self.bus.get('org.gnome.Shell', '/org/gnome/Shell/Extensions/WindowsExt')
        return path.FocusTitle()

    def activate_window_by_name(self, window_title):
        path = self.bus.get('org.gnome.Shell', '/de/lucaswerkmeister/ActivateWindowByTitle')
        path.activateByTitle(window_title)

    def toggle(self, option):
        if self.check_for_zoom_window():
            self.toggle_zoom(option)
        elif self.check_for_skype_window():
            self.toggle_skype(option)

    def toggle_skype(self, option):
        """Toggles the microphone or camera button of a Skype Meeting window

        :param option: A string defining what to toggle. Can be either 'microphone' or 'camera'.
        :type option: str
        """
        current_window_name = self.get_current_window_name()

        self.activate_window_by_name(self.skype_window_name)

        if option == 'camera':
            self.toggle_skype_camera()
        if option == 'microphone':
            self.toggle_skype_microphone()

        self.activate_window_by_name(current_window_name)

    def toggle_zoom(self, option):
        """Toggles the microphone, camera or raised hand button of a Zoom Meeting window

        :param option: A string defining what to toggle. Can be either 'microphone', 'camera' or 'hand'.
        :type option: str
        """
        current_window_name = self.get_current_window_name()

        self.activate_window_by_name(self.zoom_window_name)

        if option == 'camera':
            self.toggle_zoom_camera()
        if option == 'microphone':
            self.toggle_zoom_microphone()
        if option == 'hand':
            self.toggle_zoom_hand()

        self.activate_window_by_name(current_window_name)

    def check_for_skype_window(self):
        """Checks for a running instance of a Skype Meeting window

        :rtype: bool
        :return: True if at least one is Skype Meeting window instance is found, False otherwise
        """
        path = self.bus.get('org.gnome.Shell', '/org/gnome/Shell/Extensions/WindowsExt')
        window_list = json.loads(path.List())
        skype_windows_list = [d['id'] for d in window_list if d['title'] in [self.skype_window_name]]
        if len(skype_windows_list) >= 1:
            return True
        else:
            return False

    def check_for_zoom_window(self):
        """Checks for a running instance of a Zoom Meeting window

        :rtype: bool
        :return: True if at least one is Zoom Meeting window instance is found, False otherwise
        """
        path = self.bus.get('org.gnome.Shell', '/org/gnome/Shell/Extensions/WindowsExt')
        window_list = json.loads(path.List())
        zoom_windows_list = [d['id'] for d in window_list if d['title'] in [self.zoom_window_name]]
        if len(zoom_windows_list) >= 1:
            return True
        else:
            return False

    def toggle_skype_microphone(self):
        with self.keyboard.pressed(Key.ctrl_l):
            self.keyboard.press('m')
            self.keyboard.release('m')

    def toggle_skype_camera(self):
        with self.keyboard.pressed(Key.ctrl_l):
            with self.keyboard.pressed(Key.shift_l):
                self.keyboard.press('k')
                self.keyboard.release('k')

    def toggle_zoom_microphone(self):
        with self.keyboard.pressed(Key.alt_l):
            self.keyboard.press('a')
            self.keyboard.release('a')

    def toggle_zoom_camera(self):
        with self.keyboard.pressed(Key.alt_l):
            self.keyboard.press('v')
            self.keyboard.release('v')

    def toggle_zoom_hand(self):
        with self.keyboard.pressed(Key.alt_l):
            self.keyboard.press('y')
            self.keyboard.release('y')
