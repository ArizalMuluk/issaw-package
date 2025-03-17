from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='issaw',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
    author='ArizalMuluk',
    author_email='monsterkikuk@gmail.com',
    description='Python library for implementing the Simple Additive Weighting (SAW) method.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ArizalMuluk/issaw',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Mathematics'
    ],
    python_requires='>=3.10',
)