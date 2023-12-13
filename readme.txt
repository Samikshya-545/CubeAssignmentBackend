You can find the version numbers of the packages that your project is currently using by running:
pip freeze > requirements.txt

This command generates a requirements.txt file with the current versions of all installed packages in your virtual environment.

When deploying your application, you can use this requirements.txt file to install the required dependencies by running:
pip install -r requirements.txt
