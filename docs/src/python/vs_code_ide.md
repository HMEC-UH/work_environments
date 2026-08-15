Visual Studio Code (VS Code) is a free, cross-platform source code editor developed by Microsoft. Unlike a traditional integrated development environment (IDE), VS Code starts as a relatively lightweight editor and can be extended with additional functionality depending on the languages and tools you use.

For Python development, VS Code provides a flexible environment for writing, running, and debugging Python code. With the appropriate extensions installed, VS Code can provide many of the features commonly associated with a full Python IDE, including:

- Syntax highlighting and code completion to make Python code easier to read and write.
- Integrated debugging for stepping through code, setting breakpoints, and inspecting variables.
- Python environment selection for working with Conda and other virtual environments.
- An integrated terminal for running Python, managing environments, installing packages, and using command-line tools without leaving the editor.
- Jupyter support for working interactively with notebooks and individual code cells.
- Project and file management for organizing larger Python projects containing multiple scripts, modules, data files, and documentation.
- Git integration for tracking changes and working with version-controlled projects.

One of the major advantages of VS Code is that the same development environment can grow with your workflow. It works well for relatively simple Python scripts, but it is also well suited to larger projects that combine Python with tools such as Git, Jupyter notebooks, documentation, configuration files, and command-line applications.

In the following sections, we will install VS Code, add the extensions needed for Python development, and configure it to work with our Python environments.


## Install
VS Code is cross-platform and is available for Windows, macOS, and Linux. Head over to the VS Code [download page](https://code.visualstudio.com/download?_exp_download=fb315fc982) and download the installer appropriate for your operating system.

Follow the installation instructions provided for your platform. For most users, the default installation options are appropriate.

Once the installation is complete, launch Visual Studio Code. The first time you open VS Code, you will be presented with the Welcome page. At this point, VS Code is primarily a general-purpose code editor. In the next section, we will install a few recommended extensions that provide additional tools and features for Python development.

## Terminal

    git config user.email
    git config user.name

If they return empty, then you should define these with the following

    git config --global user.email "your_github_email@example.com"
    git config --global user.name "your_github_username"


## Sign in with GitHub
VS Code can connect directly to your GitHub account, allowing you to work with GitHub repositories and integrate GitHub with your development environment.

To get started, click the ++"Sign In"++ button located near the upper-right corner of the VS Code window, as shown below.

![VS Github](assets/images/vs_github.png){#vs_github}

*Figure 1: Login with Github.*

