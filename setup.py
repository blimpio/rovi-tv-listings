from distutils.core import setup

setup(
    name='rovi-tv-listings',
    py_modules=['rovi'],
    install_requires=[
        'requests >= 0.13.3',
    ]
)
