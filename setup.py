"""Setup file for TomoTools package."""

from setuptools import setup

setup(
    name='tomotools',
    version='0.4.0',
    author='Andrew A. Herzing',
    description='Suite of data processing algorithms for processing electron '
            'tomography data',
    packages=[
        'tomotools',
        ],
    install_requires=[
        # 'tomopy @ git+http://github.com/tomopy/tomopy.git',
    ]
)
