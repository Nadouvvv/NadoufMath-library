from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="my-library",
    version="0.1.0",
    author="Ваше Имя",
    author_email="your.email@example.com",
    description="Краткое описание библиотеки",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/username/my-library",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        # зависимости
        "requests>=2.25.0",
    ],
)