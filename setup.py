""" Setup module for kervi generating setup package used with pip """
from distutils.core import setup
import distutils
try:
    from kervi.version import VERSION
except:
    VERSION = "0.0"

try:
    distutils.dir_util.remove_tree("dist")
except:
    pass

setup(
    name='kervi-core',
    packages=[
        'kervi',
        'kervi/actions',
        'kervi/config',
        'kervi/controllers',
        'kervi/dashboards',
        'kervi/hal',
        'kervi/sensors',
        'kervi/spine',
        'kervi/core/utility',
        'kervi/values',
        'kervi/version',
        
    ],
    version=VERSION,
    description="""
    Core components for the Kervi framework .
    """,
    author='Tim Wentzlau',
    author_email='tim.wentzlau@gmail.com',
    url='https://github.com/kervi/kervi-core',
    download_url='https://github.com/kervi/kervi/archive/v1.0-alpha.tar.gz',
    keywords=['raspberry pi', 'robotic', 'automation'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
        "Topic :: Software Development :: Documentation",
        "Topic :: System :: Monitoring",
        "Environment :: Console",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.4"
    ],
    
)