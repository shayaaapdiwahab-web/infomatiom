from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in infomation/__init__.py
from infomation import __version__ as version

setup(
	name="infomation",
	version=version,
	description="Sample",
	author="Shayaa",
	author_email="shayaaabdiwahab@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
