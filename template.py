# to create a template for the directory structure


import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s]: %(message)s"
)
while True:
    project_name= input('Enter the project name: ')
    if project_name != '':
        break


list_of_files=[f"{project_name}/components/__init__.py"
    ,f"{project_name}/entity/__init__.py"
    ,f"{project_name}/pipeline/__init__.py"
    ,f"{project_name}/logger/__init__.py"
    ,f"{project_name}/config.py"
    ,f"{project_name}/exception.py"
    ,f"{project_name}/predictor.py"
    ,f"{project_name}/utils.py"
    ,"configs/config.yaml"
    ,"requirements.txt"
    ,"setup.py"
    ,"main.py"
    ,"data_dump.py" #for dumping file to the DB
    ,"README.md"
    ,"github/workflows/.gitkeep"
    ,"github/workflows/main.yaml"
]


for foldername in list_of_files:

    filepath= Path(foldername)
    filedir, filename= os.path.split(filepath)
    if filedir !='':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating  new directory at : {filedir} for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"creating a new file : {filename} for path: {filepath}")
    else:
        logging.info(f"file already present at path : {filepath}")
        