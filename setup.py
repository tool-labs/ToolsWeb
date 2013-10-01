from distutils.core import setup

with open('requirements.txt') as f:
    reqs = f.read().splitlines()

setup(
    name='ToolsWeb',
    version='0.1dev',
    author='Robin Krahl',
    author_email='me@robin-krahl.de',
    packages=['toolsweb',],
    license='LICENSE',
    long_description=open('README.txt').read(),
    install_requires=reqs,
)
