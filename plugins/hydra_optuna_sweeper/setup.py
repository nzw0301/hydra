# Copyright (c) Kento Nozawa. All Rights Reserved
# type: ignore
from setuptools import find_namespace_packages, setup

with open("README.md", "r") as fh:
    LONG_DESC = fh.read()
    setup(
        name="hydra-optuna-sweeper",
        version="0.1",
        author="Kento Nozawa",
        author_email="nozawa.kento@gmail.com",
        description="Hydra Optuna Sweeper plugin",
        long_description=LONG_DESC,
        long_description_content_type="text/markdown",
        url="https://github.com/nzw0301/hydra/",
        packages=find_namespace_packages(include=["hydra_plugins.*"]),
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Operating System :: POSIX :: Linux",
            "Operating System :: MacOS",
            "Development Status :: 4 - Beta",
        ],
        install_requires=["hydra-core>=1.0.0", "optuna>=2.1.0"],
        include_package_data=True,
    )
