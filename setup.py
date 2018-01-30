from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='py_qualtrics_api',
    version='0.1.4',
    description='Library for facilitating survey administration with Qualtrics. Requires Qualtrics API.',
    long_description=long_description,
    url='https://github.com/cwade/py_qualtrics_api',
    author='cwade',
    author_email='pysurveyhelper@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='python qualtrics api survey_administration',
    packages=['py_qualtrics_api'],
    install_requires=['requests', 'PyYAML', 'pandas'],
    data_files=[('config', ['config_sample.yml']),
                ('tests', ['tests.ipynb', 'test_mailing_list.csv'])]
)
