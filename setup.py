from distutils.core import setup

setup(name='API test',
      version='1.0',
      description='Sample api testing project for ci',
      packages=['api_test'],
      install_requires=['pytest',
                        'requests',
                        'pylint==2.14.5',
                        'pylint-gitlab',
                        'pylint-pytest',
                        'pytest-html',
                        'pytest-html-reporter'
                        ]
      )
