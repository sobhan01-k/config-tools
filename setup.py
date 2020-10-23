from setuptools import setup,find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="config_tools",
    version="0.0.1",
    author="sobhan01-k",
    description="The easy way to work with config files in python 3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),

)