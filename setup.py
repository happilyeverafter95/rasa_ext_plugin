import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# perform the setup
setup(name='rasa-ext-plugin',
      version='0.0.2',
      description='Rasa plugins to extend state and store functionalities',
      long_description=README,
      long_description_content_type="text/markdown",
      url='http://github.com/appliedsoul/rasa_ext_plugin',
      author='Noel Gaur',
      author_email='noel.gaur@analyticservice.net',
      license='MIT',
      classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
      ],
      packages=['rasa_ext_plugin'],
      install_requires=['rasa']
    )
