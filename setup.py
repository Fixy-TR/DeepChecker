import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DeepChecker",
    version="0.0.1",
    author="Ümit Yılmaz",
    author_email="umitylmz98@gmail.com",
    description="This is a deep learning based library for handling Turkish clitics such as da, de, ki and mi.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
          'tensorflow',
          'keras',
      ],
    include_package_data=True,
)
