
import setuptools


def read_requirements(filename: str):
    with open(filename) as f:
        return [line.strip() for line in f]


setuptools.setup(
    name="tickex",
    version='0.0.0',
    description="Ticker data for Forex",
    long_description="Ticker data for Forex",
    author="Nathan McCoy",
    maintainer="Nathan McCoy",
    python_requires='>=3.10',
    install_requires=read_requirements('requirements.txt'),
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": ['tickex=tickex.cli:main'],
    },
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
)
