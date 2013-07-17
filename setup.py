from distutils.core import setup

setup(
    name='mixpanel-py',
    version='1.0.0',
    author='Mixpanel, Inc.',
    author_email='dev@mixpanel.com',
    packages=['mixpanel', 'mixpanel.test'],
    url='https://github.com/mixpanel/mixpanel-python',
    license='LICENSE.txt',
    description='Official Mixpanel library for Python',
    long_description=open('README.txt').read(),
    install_requires=[
    ],
)
