from setuptools import setup, find_packages

setup(
    name='api',
    version='2.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        'requests',
        'marshmallow',
        'waitress',
    ],

)
