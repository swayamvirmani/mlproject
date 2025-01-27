from setuptools import find_packages, setup
from typing import List
HYPEH_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this func will return list of req
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        if HYPEH_E_DOT in requirements:
            requirements.remove(HYPEH_E_DOT)
    return requirements
setup(
    name='mlproject',
    version='0.0.1',
    author='Swayam',
    author_email='swayam23974@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)