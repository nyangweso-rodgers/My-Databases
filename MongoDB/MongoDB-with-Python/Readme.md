# MongoDB with Python

## Table of Contents

- [Further Reading]()
  1. [MongoDB Developer - Python](https://www.mongodb.com/developer/languages/python/)
  2. [Dev.to - Working with MongoDB and Python](https://dev.to/dev0928/working-with-mongodb-and-python-1e2i)
  3. [Dev.to - Learn MongoDB + Python basics in 5 minutes !](https://dev.to/siddheshshankar/learn-mongodb-python-basics-in-10-minutes-8ld)

# Introduction

# Configure VS Code for Python Environment

## Python Extension

- Install [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) from Microsoft.
- This is actually an extension pack that contains two extensions.
  - The first extension is the Python extension. It lays the foundation for Python development in Visual Studio Code.
  - The other one is [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance), which is a very performant language server for Python.

## Ruff Linter

- Ruff is an extremely fast Python linter written in Rust that imposes stricter linting rules than Pylint.
- Install [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)

## Isort

- Like a linter, [isort](https://marketplace.visualstudio.com/items?itemName=ms-python.isort) is another utility that's sole purpose is sorting import statements.
- The utility sorts all the imports alphabetically, while also dividing them into sections.

## InteiCode

- [InteiCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode) provides AI assisted code completion in Visual Studio Code.

## Error Lens

- While not related to Python specifically, [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens) is a great extension that embeds errors right by the side of the line of code.

## Indent Rainbow

- [indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow) adds some color to the identation.

# Setting Up Virtual Environment

1. Navigate to the root directory of your project using the terminal or command prompt.

2. Run the following command to create a new virtual environment: This will create a new directory called **env** in your project directory, which contains the virtual environment.

   ```sh
       python -m venv venv
   ```

3. Activate the virtual environment by running the following command: This will activate the virtual environment and change your shell's prompt to indicate that you're working within the virtual environment.

   ```sh
       source env/bin/activate  # For Linux or macOS
       source venv/Scripts/activate  # For Windows
   ```

4. You can now install any required modules using pip, which will install them within the virtual environment. For example:

   ```sh
       pip install numpy
   ```

   This will install the numpy module within the virtual environment, making it available for use in your project.

5. Remarks:

   - When you're done working on your project, you can deactivate the virtual environment by running the `deactivate` command in the terminal.
   - By creating a virtual environment within your project directory, you can easily share your project with others, since they can create their own virtual environment and install the required dependencies using the `requirements.txt` file (which lists the required packages and versions) that you can provide along with your code.
   - it's a best practice to use a separate file, usually called `requirements.txt` or **Pipfile**, to list the required dependencies for your project. You can generate this file automatically using `pip freeze`, which will list all of the installed packages and their versions within your virtual environment.
   - Here's an example of how to generate a `requirements.txt` file:

   ```sh
       # Generate requirements.txt file
       pip freeze > requirements.txt
   ```

   - This will create a `requirements.txt` file in your project directory that lists all of the installed packages and their versions.
   - Commit the `requirements.txt` file to your `git` repository.
   - With this approach, others can create their own virtual environment and install the required dependencies using the `requirements.txt` file, by running the following command:

   ```sh
       pip install -r requirements.txt
   ```

# How to work with MongoDB in Python?

- To work with **MongoDB** in `Python`, install `PyMongo` driver using command - `python -m pip install pymongo`

# Create a `collection` in `MongoDB`
- create a `database` called `users-v2` containing `users` collections
  