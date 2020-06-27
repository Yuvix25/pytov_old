import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytov", # Replace with your own username
    version="0.2",
    license='MIT',
    author="Yuval Rosen",
    author_email="yuv.rosen@gmail.com",
    description="Write python with C like syntax",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Yuvix25/pytov",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[            # I get to this in a second
          'importlib'
      ],
)