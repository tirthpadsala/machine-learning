from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->list[str]:
    reqirements=[]
    with open(file_path) as f1:
        reqirements=f1.readlines()
        reqirements = [req.replace("\n",'') for req in reqirements]

    if '-e .' in reqirements:
        reqirements.remove('-e .')
    return reqirements


setup(
    name='machine learning',
    version='0.0.1',
    author='tirth padsala',
    author_email='tirthpadsala2@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)