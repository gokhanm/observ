import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "observ",
    version = "0.1.0",
    author = "Gokhan Mankara",
    author_email = "gokhan@mankara.org",
    description = ("pip outdated packages notifier"),
    license = "GNU GENERAL PUBLIC LICENSE",
    keywords = ["pip", "notifier"],
    url = "https://github.com/gokhanm/observ",
    packages=find_packages(),
    include_package_data=True,
    long_description=read('README.rst'),
    entry_points={
        'console_scripts': [
                'observ = observ.__main__:main',
            ],
    },
    install_requires=list(filter(None, [
        'docopt',
    ])),
    data_files = [
                    ('/etc', ['observ/conf/observ.conf'])
        ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: System :: Systems Administration',
    ]
)

