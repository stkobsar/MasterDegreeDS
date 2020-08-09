import setuptools


setuptools.setup(name='pec4_ds_skobsar',
      version="1.0.0",
      url = "https://github.com/stkobsar/pec4_ds_skobsar",
      description='This package allows to analyse the data in a bitcoin transaction, diving into the key variables in each block and the data in it. ',
      author='Stephi Kobsar',
      author_email='skobsar@uoc.edu',
      packages=setuptools.find_packages(),
      install_requires=["matplotlib", "numpy"],
      classifiers=[
       "Programming Language :: Python :: 3",
       "License :: OSI Approved :: MIT License",
       "Operating System :: OS Independent",
       ],
     )