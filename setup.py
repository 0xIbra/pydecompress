import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pydecompress',
    version='0.0.1',
    author='Ibragim Abubakarov',
    author_email='ibragim.ai95@gmail.com',
    maintainer='Ibragim Abubakarov',
    maintainer_email='ibragim.ai95@gmail.com',
    description='PyDecompress eases the process of extracting contents from different types of archives.',
    long_description=long_description,
    url='https://github.com/ibragim64/pydecompress',
    packages=['pydecompress'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers"
    ]
)