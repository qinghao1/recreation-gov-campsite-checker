from setuptools import find_packages, setup


README_FILE = "README.md"
REQUIREMENTS_FILE = "requirements.txt"


setup(
    name="recreation_gov_campsite_checker",
    packages=[""],
    version=1.0,
    description="Scrape recreation.gov for campsite availability",
    long_description=open(README_FILE).read(),
    url="https://github.com/qinghao1/recreation-gov-campsite-checker",
    author="Forked from Daniel Porteous and contributors by qinghao1",
    install_requires=open(REQUIREMENTS_FILE).read().splitlines(),
    include_package_data=True,
)
