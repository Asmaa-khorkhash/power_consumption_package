import setuptools

setuptools.setup(
    name="Power_consumption",
    version="0.1.0",
    url="https://github.com/Asmaa-khorkhash/power_consumption",
    author="Asmaa khorkhash",
    author_email="asmaakhorkhash@gmail.com",
    description=" Measurements of electric power consumption in one household with a one-minute sampling rate over a period of almost 4 years. Different electrical quantities and some sub-metering values are available.",  
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    include_package_data=True,
    package_data={'': ['data/*.csv']},
)