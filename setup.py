from setuptools import setup, find_packages

setup(
    name='multisched',
    version='0.1.4',
    author='Adam Tauber <asciimoo>',
    author_email='asciimoo@faszkorbacs.hu',
    packages=find_packages(),
    scripts=['multisched.py', 'README.markdown'],
    py_modules=['multisched' ],
    keywords='threaded scheduler',
    url='http://pypi.python.org/pypi/multisched/',
    license='AGPLv3+',
    description='',
    long_description=open('README.markdown').read(),
    classifiers = ["Development Status :: 4 - Beta",
                   "License :: OSI Approved :: GNU Affero General Public License v3",
    ],

)