from setuptools import setup

setup(name='pylint_fileout',
      version='0.1.0',
      description='A fileout plugin for Pylint',
      long_description=open('README.md').read(),
      author='Alex Dow',
      author_email='adow@psikon.com',
      license='MIT',
      packages=['pylint_fileout'],
      zip_safe=False,
      keywords='pylint plugin fileout',
      classifiers=[
        'Development Status :: 2 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: PYthon :: 3.5'
    ]
)

