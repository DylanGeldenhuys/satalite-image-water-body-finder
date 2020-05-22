import setuptools

#with open("README.md", "r") as fh:
#    long_description = fh.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()


setuptools.setup(
    name="example-pkg-YOUR-USERNAME-HERE",  # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    #description="A small example package",
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    install_requires=requirements,
    packages=setuptools.find_packages(),
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
