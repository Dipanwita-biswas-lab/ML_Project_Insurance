# defining versions for the prject which will be benefical to add any idependency information
from setuptools import find_packages, setup
from typing import List


REQUIREMENT_FINENAME='requirements.txt'
REMOVE_PACKAGE= '-e .'

def get_requirements()->List[str]:
    with open(REQUIREMENT_FINENAME) as requirement_file:
        requirement_list= requirement_file.readline()
    requirement_list= [requirement_name.replace('\n', '')for requirement_name in requirement_list]

    if REMOVE_PACKAGE in requirement_list:
        requirement_list.remove(REMOVE_PACKAGE)
    return requirement_list



setup(name='Insurance',
      version='0.0.1',
      description='Industry level project',
      author='dipanwita Biswas',
      author_email='dippybiswas@gmail.com',
      #url='',
      packages=find_packages(),
      # finds in which folder the init .py is available in insurance file
      install_reqires=get_requirements()
     )