import setuptools
print(setuptools.find_packages())

setuptools.setup(
    name="pytov",
    version="0.1.9",
    license='MIT',
    author="Yuval Rosen",
    author_email="yuv.rosen@gmail.com",
    description="Write python with C like syntax",
    long_description=''.join(open('README.txt', encoding='utf-8').readlines()),
    long_description_content_type="text/markdown",
    url="https://github.com/Yuvix25/pytov",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[],

    entry_points={
        'console_scripts': [
            'pytov=pytov.pytov:run',
        ],
    },
)