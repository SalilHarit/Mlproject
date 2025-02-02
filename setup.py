from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
  '''
    Read requirements file and return list of requirements
  
  '''

  requirements=[]
  if "-e" in requirements:
      requirements.remove("-e")
  with open(file_path) as f:
    requirements = f.read().splitlines()
   

setup(
    name='mlproject',
    version='0.1',
    author='Salil Harit',
    author_email='salilharit2001@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)

