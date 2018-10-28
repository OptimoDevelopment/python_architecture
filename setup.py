import os

from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install

try:
    from pip._internal import main as pip_main
except ImportError:
    from pip import main as pip_main

PACKAGE_NAME = "the_shop"
SOURCES = {"bf_shop": "shop", "bf_ram_db": "ram_db", "bf_api": "api"}


def install_libs(sources, develop=False):
    print(
        "installing all libs in {} mode".format("development" if develop else "normal")
    )
    wd = os.getcwd()

    for k, v in sources.items():
        try:
            os.chdir(os.path.join(wd, v))
            if develop:
                pip_main(["install", "-v", "-e", "."])
            else:
                pip_main(["install", "."])
        except Exception as e:
            print("Oops, something went wrong installing", k)
            print(e)
        finally:
            os.chdir(wd)


class DevelopCmd(develop):
    """ Add custom steps for the develop command """

    def run(self):
        develop.run(self)
        install_libs(SOURCES, develop=True)


class InstallCmd(install):
    """ Add custom steps for the install command """

    def run(self):
        install_libs(SOURCES, develop=False)
        install.run(self)


setup(
    name=PACKAGE_NAME,
    cmdclass={"install": InstallCmd, "develop": DevelopCmd},
    python_requires=">=3.7",
    use_scm_version={"root": ".", "relative_to": __file__},
    setup_requires=["pip>=10", "setuptools>=40", "setuptools_scm"],
)
