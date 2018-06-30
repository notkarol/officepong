from setuptools import setup, find_packages

setup(name='officepong',
      version='0.2',
      description='Keep track of ELO in your office',
      long_description=__doc__,
      author='Karol Zieba',
      author_email='notkarol@gmail.com',
      license='GNUv3',
      include_package_data=True,
      zip_safe=False,
      packages=['officepong'],
      install_requires=find_packages()
      )

