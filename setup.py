from distutils.core import setup
from pip.req import parse_requirements

pip_reqs = parse_requirements('requirements.txt')
reqs = [str(req.req) for req in pip_reqs]

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
