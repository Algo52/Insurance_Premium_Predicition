from setuptools import setup,find_packages
from typing import List


def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readline()


# Declaring variables for setup function
PROJECT_NAME = 'Insurance_Premium_prediction'
VERSION = '0.0.3'
AUTHOR = 'Hemanth'
DESCRIPTION = "ML Project Deployment Process"
REQUIREMENT_FILE_NAME = 'requirements.txt'




setup(
    name = PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description = DESCRIPTION,
    packages = find_packages(),
    install_requires = get_requirements_list()
)

if __name__ == "__main__":
    print(get_requirements_list())