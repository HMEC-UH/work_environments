This section introduces the workflow HMEC uses to create, maintain, and publish documentation using MkDocs.

This is not intended to be a comprehensive guide to MkDocs itself. If you would like to learn more about the project, visit the [official MkDocs website](https://www.mkdocs.org/).

In short, MkDocs uses Markdown files to generate modern, searchable documentation websites. Contributors can focus on writing content while MkDocs handles navigation, formatting, search, and site generation. Markdown is intentionally simple and easy to learn, making it accessible to both technical and non-technical contributors.

Many online resources are available to help you get started, including the official documentation, tutorials, videos, and AI-assisted tools such as ChatGPT, Claude, or GitHub Copilot.

In a previous section, we discussed the value of GitHub for collaboration and version control. In this section, we focus on the practical workflow used to create and publish documentation:

* Adding documentation to existing repository
* Configure and launch a local development environment using VS Code
* Create and edit documentation pages
* Commit and push changes to GitHub
* Publish documentation using GitHub Pages

By following this workflow, contributors can develop documentation locally, preview changes before publication, and collaborate through familiar GitHub-based processes.

## Set up repository
GitHub natively supports and renders Markdown files (e.g., the "Readme.md" file). However, we want to go a bit further to create a more rich documentation for our repository using MkDocs.

1. Start by launching VS Code then open the explorer:
![explorer](assets/images/open_A.png){#explorer}

2. The explorer gives you two options. The first is open a **local** directory/folder and the second is to clone a **remote** repository. We have already gone over how to clone a repository from GitHub to your **local** machine, so we'll assume we can just point to it with option 1:
![open](assets/images/open_B.png){#open}

You should now see a list of your repository contents in the explorer window. 

## Set up VS Code
VS Code is great in that it allows you to do almost everything from within a single software application. This makes it perfect for creating Markdown documentation for your repository.

1. From the VS Code menu bar, select `Terminal > New Terminal`
![open_terminal](assets/images/open_terminal.png){#open_terminal}

2. At the bottom of your screen, you should see the "Terminal" panel now open. By default, the path should match the repository location in your explorer. The first thing we'll want to do is **activate** your Conda virtual environment, which I called "docs". After you activate it, you should see the name listed in parenthesis to the left:
![activate_env](assets/images/activate_env.png){#activate_env}

3. In the "Explorer" (or from the "Terminal"), create a new directory/folder called "docs". This is where we will store the documentation in your repository.

    !!! note "Explorer vs Terminal"
        If you're not comfortable or familiar with the "Terminal", you can just use the "Explorer". The "Terminal" is more likely to be new to Windows users, whereas Linux users should be very familiar...Mac, you're comfortably in the middle.

4. Move into the new directory/folder called "docs" and create
    * a new file called "mkdocs.yml"
    * a nested directory/folder called "src"
    
    You can do this in either the "Explorer" or "Terminal". If executing in the "Terminal", you'd type the following commmands:

    `touch mkdocs.yml`

    `mkdir ./src`
    
5. We'll go over the contents of 


## Publish to GitHub