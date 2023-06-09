from setuptools import setup, find_packages

setup(
    name="igbloks",
    version="1.0.0a",
    packages=find_packages(include=["igbloks", "igbloks.*"]),
    include_package_data=True,
    author="novitae",
    description="A library to work with instagram `bloks` technology",  # Add a description
    url="https://github.com/novitae/igbloks",
    python_requires=">=3.9",  # Specify your Python version requirements
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",  # Specify the license used
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        # Add or remove Python versions as needed
    ],
    install_requires=[
        "pyparsing",
    ],
)
