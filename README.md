# IT3212-project

Repository for the group project in the course IT3212 Data Driven Software at NTNU

# Setup

Start the virtual environment by running the command:

```bash
source setup.sh
```

in the terminal. This will install the packages in the requirements.txt and start the virtual environment.

If you need to install more packages, do it in the virtual environment and then run the command

```bash
pip freeze > requirements.txt
```

in the terminal to update the requirements.txt file.

# Data

The .csv files must be placed in the repository yourselves as they are too large to be uploaded to GitHub. They are available on the course page on Blackboard in "project material". They are included in the .gitignore file so they will not be uploaded to the repository.

The same goes for the .zip files for the land and ocean data. They can be found under course information, project material on Blackboard. They should be placed in the datasets folder.

# Issues with pushing to github:

You may experience issues when pushing to github. This may be due to the outputs in the .ipynb files being too large. You can try to fix this by removing the outputs from the .ipynb files before pushing.
