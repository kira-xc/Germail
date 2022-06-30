# -*- coding: utf-8 -*-
from setuptools import setup,find_packages

packages = ['germail']

package_data = {'': ['*']}

install_requires = ['random-username>=1.0.2,<2.0.0', 'requests']

with open("README.md", "r") as stream:
    long_description = stream.read()

setup(
    name='germail',
    license='MIT',
    version='1.0.0',
    description='A python api create temporary mail',
    author='kira_xc',
    url='https://github.com/kira-xc/Germail',
    packages=find_packages(),
    package_data=package_data,
    install_requires=install_requires,
    keywords=[
        'geras',
        'geras email',
        'temp email',
        'temp mail',
        'germail',
        'geras mail',
        'gerasmail',
        'kira_xc',
        'python3.x',
        'kira-xc',
        'temporary',
        'temporary mail',
        'temporary email',
        'mail.tm',
        'mohmal',
        'temp-mail',
        'ايميل',
        'ايميل مؤقت',
        'مهمل',
        'بايثون',
        'tempmail',
        'temp-mail',
        'جيرس'
    ],
    python_requires='>=3.7',
)



