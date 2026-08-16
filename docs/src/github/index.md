Engineering and scientific projects rarely consist of a single file created by one person and never changed again. Source code, analysis scripts, documentation, configuration files, and other project resources evolve continuously as work progresses. Files are modified, new features are added, mistakes are corrected, and multiple people may contribute to the same project. As projects grow, keeping track of these changes becomes increasingly important.

# Git and GitHub
**Git** is a version control system designed to track changes to files over time. Rather than maintaining separate copies of files with names such as `analysis_final.py`, `analysis_final_v2.py`, and `analysis_final_revised.py`, Git records the history of a project in a structured **repository**.

!!! note "Repository"
    A **repository**, often shortened to **repo**, is a project directory managed by Git. It contains the project's files along with a recorded history of changes made to them.

Git allows developers and researchers to create checkpoints in the development of a project, compare changes between versions, restore earlier versions when necessary, and work on new ideas without immediately affecting the primary version of the project.

This provides several important benefits:

* **Version control** — maintaining a structured history of how a project changes over time
* **Traceability** — documenting what changed, when it changed, and why
* **Collaboration** — allowing multiple people to contribute to the same project
* **Experimentation** — developing and testing changes without disrupting a working version
* **Recovery** — returning to an earlier version when a change introduces problems
* **Reproducibility** — preserving the code and configuration associated with technical analyses and research

Although Git manages the version history, it operates locally and does not inherently require an internet connection or cloud service. A Git repository can exist entirely on a single computer.

**GitHub** is an online platform that hosts Git repositories and provides additional tools for collaboration, project management, documentation, and software development. By storing a copy of a repository on GitHub, project files and their version history can be shared among computers and collaborators.

!!! note "Git vs. GitHub"
    **Git** is the version control system that tracks changes to a project. **GitHub** is an online service used to host and collaborate on Git repositories.

For an organization such as HMEC, GitHub provides a central location where software, documentation, examples, and other technical resources can be maintained and shared. Rather than distributing files through email or maintaining independent copies on individual computers, contributors can work from a common repository while Git records how the project evolves.

GitHub also provides organizational tools built around the Git workflow, including **branches**, **issues**, **pull requests**, and project documentation. These tools make it possible to develop changes independently, discuss proposed modifications, review contributions, and merge completed work into a shared project.

Throughout these materials, we will introduce Git and GitHub gradually through practical use. The objective is not to explore every feature of either platform, but to establish a reliable workflow for obtaining HMEC resources, tracking changes to technical work, collaborating with others, and contributing improvements back to shared projects.

Like virtual environments in Python, version control may initially appear to add complexity to tasks that could otherwise be accomplished by simply copying and editing files. As projects become larger, longer-lived, or more collaborative, however, version control becomes increasingly valuable. Git and GitHub are therefore fundamental tools for modern software development, scientific computing, engineering research, and technical documentation.
