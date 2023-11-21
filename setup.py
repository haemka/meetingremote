from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name='MeetingRemote',
    description='A simple remote control for common meeting software.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/haemka/meetingremote",
    author="haemka",
    author_email="github@haemka.de",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Communications :: Conferencing",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        "pydbus",
        "pynput"
    ],
    entry_points={  # Optional
        "console_scripts": [
            "meetingremote=MeetingRemote.meetingremote:main",
        ],
    },
)