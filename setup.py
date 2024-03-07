from setuptools import find_packages, setup

import versioneer

with open("requirements.txt") as install_requires_file:
    install_requires = install_requires_file.read().strip().split("\n")

with open("requirements-dev.txt") as dev_requires_file:
    dev_requires = dev_requires_file.read().strip().split("\n")

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name="prefect-firestore",
    description="Prefect-firestore contians that basics needed to connect and load data to a firestore database",
    license="Apache License 2.0",
    author="Adeeb Doyle",
    author_email="Adeebd16@gmail.com",
    keywords="prefect",
    url="https://github.com/adeebdvlpr/prefect-firestore",
    long_description=readme,
    long_description_content_type="text/markdown",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(exclude=("tests", "docs")),
    python_requires=">=3.8",
    install_requires=install_requires,
    extras_require={"dev": dev_requires},
    entry_points={
        "prefect.collections": [
            "prefect_firestore = prefect_firestore",
        ]
    },
    classifiers=[
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
    ],
)
