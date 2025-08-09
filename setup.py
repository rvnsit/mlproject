from setuptools import find_packages, setup
from typing import List

hyp = "-e ."

def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the list of requirements
    
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if hyp in requirements:
            requirements.remove(hyp)

setup(
name = 'MLProject',
version = '0.0.1',
author='RV',
author_email='ranvijay.nsit@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')

)