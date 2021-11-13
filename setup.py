#!bin/bash
import setuptools

setuptools.setup(
    name='mipack',
    version='0.0.1',
    author='swyo',
    author_email='l22491360@gmail.com',
    description='My implemented packages for python',
    url='https://github.com/swyo/mipack',
    install_requires=[],
    keywords=['python', 'packaging'],
    python_requires='>=3.9',
    packages=setuptools.find_packages('.', exclude=('docs', 'tests')),
    zip_safe=False,
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
