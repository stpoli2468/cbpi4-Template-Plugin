from setuptools import setup

setup(name='cbpi4-Template-Plugin',
      version='0.0.1',
      description='cbpi4-Template-Plugin',
      author='',
      author_email='',
      url='https://github.com/stpoli2468/cbpi4-Template-Plugin',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4-Template-Plugin': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-Template-Plugin'],
     )
