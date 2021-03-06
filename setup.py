from setuptools import setup

setup(name='YourAppName',
      version='1.0',
      description='OpenShift App',
      author='Your Name',
      author_email='example@example.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=['Flask>=0.7.2',
                        'transliteration>=0.3',
                        'spellchecker>=0.2.1',
                        'hyphenation>=1.1',
                        'inexactsearch>=0.2',
                        'normalizer>=0.1',
                        'soundex>=0.2',
                        'payyans>=0.1',
                        'chardetails>=0.2.1'],
     )
