from setuptools import find_packages,setup #will automatically find packages
from typing import List

HYPRN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return a list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPRN_E_DOT in requirements:
            requirements.remove(HYPRN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Prateek',
    author_email='prateeklk24@gmail.com',
    description='Machine Learning Project',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)