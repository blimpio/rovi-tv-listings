import os
from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='python-rovi',
    description='Python Wrapper for Rovi TV Listings API',
    license='MIT License',
    version='0.0.3',
    zip_safe=False,
    platforms='any',
    packages=['rovi'],
    install_requires=[
        'requests>=0.13.3',
    ],

    author='Giovanni Collazo',
    author_email='hello@getblimp.com',
    url='https://github.com/GetBlimp/rovi-tv-listings',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
    ),
)
