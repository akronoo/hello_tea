import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hello_tea",
    version="0.1",
    author="akronoo",
    author_email="",
    description="hello tea oss projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/akronoo/hello_tea",
    packages=setuptools.find_packages(),
    install_requires=['Pillow','numpy'],
    entry_points={
        'console_scripts': [
            'hello_tea=hello_tea:main'
        ],
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)