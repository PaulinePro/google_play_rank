from distutils.core import setup

license = open('LICENSE.txt').read()

setup(
    name = 'google_play_rank',
    packages = ['google_play_rank'],
    version = '0.1.4',
    description = 'Input package name, then find the google play ranking for you.',
    author = 'davidyen1124',
    author_email = 'davidyen1124@gmail.com',
    url = 'https://github.com/davidyen1124/google_play_rank',
    license = license,
    keywords = ['google play', 'ranking', 'android', 'package name'],
    install_requires = [
        'requests',
        'BeautifulSoup4',
    ],
    entry_points = {
        'console_scripts': [
            'play_rank = google_play_rank:play_parser:main'
        ]
    }
)
