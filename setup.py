import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rico-ricardo-munduruca",
    version="0.0.1",
    author="Ricardo Munduruca",
    author_email="ricardo.munduruca@gmail.com",
    description="The data toolkit",
    long_description=long_description,
    long_description_content_type="For those who need to do some quick and effective data magic",
    url="https://github.com/Munduruca/rico",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)