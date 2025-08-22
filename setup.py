"""
The setup.py file is an essential part of any Python project. 
It is used for packaging and distributing the project, as well as 
managing dependencies and installation requirements. This file 
typically includes metadata about the project, such as its name, version, 
author and description, as well as a list of required packages and modules.
"""

from setuptools import find_packages, setup # This function is going to scan all the folders and whenever there is __init__.py file, it is consider that particular folder to a package.
from typing import List

#Basically in this function we are reading the requirements.txt file
def get_requirements()->List[str]:
    """
    This function will return list of requirements

    """
    requirement_list:List[str] = []

    try:
        with open("requirements.txt", 'r') as file:
            #Read lines from the file
            lines = file.readlines()
            # Process each line
            for line in lines:
                requirement = line.strip() #remove any empty spaces from every line that I am getting
                ## ignore empty lines and -e.(Here -e. is nothing but it is refering to the setup.py file)
                if requirement and requirement != '-e .':
                    #Here we appending whatever the requirement come over here
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file is not found. No dependencies will be installed.")

    return requirement_list

setup(
    name="Network_Security_System",          # ✅ Project Name
    version="0.0.1",                       # ✅ Version of your package
    author="Anjali Prasad",                # ✅ Your Name
    author_email="prasadanji280@gmail.com",# ✅ Your Email
    description="An ML-based Network Security System with End-to-End MLOps pipeline.",
    packages=find_packages(),              # ✅ Automatically finds all packages with __init__.py
    install_requires=get_requirements()   # ✅ Reads from requirements.txt

)

print("Dependencies from requirements.txt:", get_requirements())
