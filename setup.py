from setuptools import setup

setup(
    name='webficrecs',
    packages=['app'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)