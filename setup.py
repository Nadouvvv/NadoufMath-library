from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nadouf-math",
    version="0.1.0",
    author="Nadouf",
    author_email="nadoufmail@gmail.com",
    description="A simple Python library for mathematical operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nadouvvv/nadouf-math",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.6",
    install_requires=[],

    keywords="math, mathematics, calculator, arithmetic, trigonometry, nadouf, Nadouf, maths",
    project_urls={
        "Source": "https://github.com/Nadouvvv/NadoufMath-library",
        "Bug Reports": "https://github.com/Nadouvvv/NadoufMath-library/issues",
    },
)