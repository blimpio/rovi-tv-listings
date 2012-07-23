from distutils.core import setup

setup(
    name='python-rovi',
    version='0.0.2',
    packages=['rovi'],
    install_requires=[
        'requests >= 0.13.3',
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
