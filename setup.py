# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Pdf-check-fraud",
    version="0.0.1",                        # Update this for every new version
    author="J.f. Hellings",
    author_email="jan@famhellings.nl",
    description= "Program checks simularity of pdf files to detect fraud. PDF files are converted to Text files They are compared and the results are writen to a csv file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[                      # Add project dependencies here
       'autopep8>=2.0.1',
        'certifi>=2022.12.7',
        'charset-normalizer>=3.1.0',
        'cli-exit-tools>=1.2.3.2',
        'click>=8.1.3',
        'colorama>=0.4.6',
        'distlib>=0.3.6',
        'filelock>=3.10.1',
        'idna>=3.4', 
        'joblib>=1.2.0',
        'lib-detect-testenv>=2.0.3',
        'numpy>=1.24.1',
        'pathlib3x>=2.0.2.1',
        'platformdirs>=3.1.1',
        'psgdemos>=1.12.1',
        'pycodestyle>=2.10.0',
        'pycryptodome>=3.17',
        'pypdf>=3.4.0',
        'PyPDF2>=3.0.1',
        'pysimilar>=0.5',
        'PySimpleGUI>=4.60.4',
        'requests>=2.28.2',
        'scikit-learn>=1.2.1',
        'scipy>=1.10.0',
        'threadpoolctl>=3.1.0',
        'urllib3>=1.26.15',
        'virtualenv>=20.21.0'                                     
        ],
    python_requires='>=3.10',                                             
    url="https://github.com/jansloopes/github/project",  
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3",     
        "License :: OSI Approved :: MIT License", 
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Microsoft :: Windows :: Windows 11",  
    ],
)
