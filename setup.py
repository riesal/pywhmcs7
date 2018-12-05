from setuptools import setup, find_packages
import sys
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.0.1'

install_requires = [
    'requests',
]


setup(
    name='pywhmcs6',
    version=version,
    description="WHMCS 6.x Client Library",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Natural Language :: Indonesia",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
    ],
    keywords='whmcs v.6.x library http api',
    author='Muhammad Fahrizal Rahman',
    author_email='riesal@gmail.com',
    url='https://github.com/riesal/pywhmcs7',
    license='Gnu General Public License v3',
    packages=find_packages('src'),
    package_dir={'': 'src'}, include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['pywhmcs6=pywhmcs6:main']
    }
)
