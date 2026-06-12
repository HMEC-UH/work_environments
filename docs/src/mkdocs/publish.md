In the previous [Workflow](workflow.md) section, we focused on developing documentation locally using VS Code and a web browser for live previews. Once you are satisfied with the content, the documentation can be published directly through GitHub Pages.

## Publish with GitHub Pages
In the [VS Code terminal](config.md#open-a-terminal), with your virtual environment active, navigate to the directory containing ++"mkdocs.yml"++ and run:

    mkdocs gh-deploy


![deploy](assets/images/deploy.png){#deploy}

MkDocs will automatically:

* build the documentation website,
* create or update a gh-pages branch,
* push the generated site to GitHub.

In the figure above, you can see `gh-deploy` automatically created a new branch called ++"gh-pages"++. Log in to GitHub, navigate to your repository, and you should now see two branches:

![new_branch](assets/images/new_branch.png){#new_branch}

!!! warning "Do Not Edit ++"gh-pages"++ Branch"
    You generally do not need to interact with the ++"gh-pages"++ branch directly. Continue working on the ++"main"++ branch and let MkDocs manage deployment automatically.
    
    The ++"gh-pages"++ branch contains the generated website files and is recreated each time `mkdocs gh-deploy` is executed. Any manual changes made to this branch will likely be overwritten during the next deployment.


If this is the first time you have published documentation from the repository, verify the following settings in GitHub:

1. The repository is set to ++"public"++ (required for GitHub Pages on free personal accounts).
2. GitHub Pages is configured to deploy from the ++"gh-pages"++ branch.

These settings can be found in your repository ++"Settings"++ menu. The GitHub Pages configuration is located under the ++"Pages"++ settings:

![deploy_from_branch](assets/images/deploy_from_branch.png){#deploy_from_branch}

Once GitHub Pages is configured, your documentation should become available within a few minutes at the URL provided in the ++"Pages"++ settings.

If you need to change the repository visibility, navigate to the  ++"Settings > General"++ menu and scroll to the bottom of the page under ++"Danger Zone > Change repository visibility"++.

## Commit Changes to GitHub
Publishing documentation makes the generated website available online, but it does not replace normal version control practices.

Remember to commit and push your source files back to the repository so that changes are preserved and available to other contributors:

    git add .
    git commit -m "Updated documentation"
    git push

Avoid leaving changes only on your local machine. The source files stored in the repository are the authoritative version of the documentation and should be kept synchronized with the published website.