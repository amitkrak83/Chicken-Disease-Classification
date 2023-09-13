import setuptools

with open('README.md', 'r', encoding="utf-8") as f:
    long_desciption = f.read()


__version__ = "0.0.0"

REPO_NAME = "Chicken-Disease-Classification"
AUTHOUR_USER_NAME = "amitkrak83"
SRC_REPO = "CNN_Classifier"
AUTHOUR_EMAIL = "amitkrak83@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOUR_USER_NAME,
    author_email=AUTHOUR_EMAIL,
    long_description=long_desciption,
    # long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOUR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOUR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="Chicken-Disease-Classification/src")
)
