import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-v8n",
    version="0.1.0a1",
    author="Nicolas A. Schejtman",
    author_email="nschejtman93@gmail.com",
    description="Python fluent validation",
    long_description=long_description,
    url="https://github.com/nschejtman/py-v8n",
    packages=setuptools.find_packages(exclude=(['test'])),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
