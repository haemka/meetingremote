# meetingremote

A simple command line remote for common meeting software within the GNOME desktop environment. It's only function is to
toggle microphone mute and camera. 

Currently supported meeting software:
- Zoom

Planned implementations:

- Teams for Linux

## Requirements

The command relies on special DBus calls which are implemented in GNOME extensions. Needed GNOME extensions are:

- Window Calls Extended by hseliger (https://github.com/hseliger/window-calls-extended)
- Activate Window By Title by lucaswerkmeister (https://github.com/lucaswerkmeister/activate-window-by-title)

## Installation

```{bash}
python -m pip install --user git+https://github.com/haemka/meetingremote.git
```

## Usage

```
usage: meetingremote [-h] (-m | -c)

Remote control Zoom Desktop client.

options:
  -h, --help        show this help message and exit
  -m, --microphone  Toggle microphone.
  -c, --camera      Toggle camera.
```