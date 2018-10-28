from typing import List

from setuptools import find_packages, setup

lib_name = "bf_shop"


def get_requirements(prefix: str = "") -> List[str]:
    return [
        x.strip() for x in open("{}requirements.txt".format(prefix), "r").readlines()
    ]


extra_requires = {"test": get_requirements(prefix="test")}

setup(
    name=lib_name,
    packages=find_packages(),
    install_requires=get_requirements(),
    extra_requires=extra_requires,
    python_requires=">=3.7",
    use_scm_version={"root": "..", "relative_to": __file__},
    setup_requires=["pip>=10", "setuptools>=40", "setuptools_scm"],
)