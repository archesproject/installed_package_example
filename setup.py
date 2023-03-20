from setuptools import setup, find_packages

setup(
    name='installed_package_example',
    version='0.0.1',    
    description='foo description',
    url='',
    author='foo author',
    author_email='foo@foo.com',
    license='GNU AGPL3',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Information Technology",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Framework :: Django :: 1.11",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)