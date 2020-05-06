from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Lambdata-Voltaire", # the name that you will install via pip
    version="1.0",
    author="Connor Clark",
    author_email="connor-clark@lambdastudents.com",
    description="Confusion matrix and date time functions",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/Voltaire01-W/Voltaire22",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)