Python code can be written using any text editor. However, development is often made much easier through additional tools such as debuggers, variable explorers, integrated terminals, and code completion utilities. These features are commonly bundled into what is known as an integrated development environment (IDE).

While many IDE options are available, the [Spyder](https://www.spyder-ide.org/) IDE is often chosen because of its straightforward scientific computing workflow and MATLAB-like interface.

While you can install Spyder directly on your OS, we will instead create a dedicated Conda virtual environment.

Open a new terminal (or Anaconda Prompt for Windows users) and type the following command:

    conda create -n spyder

This command creates a new virtual environment named ++"spyder"++.

To see a list of all available Conda environments, run:

    conda env list


Next, activate the ++"spyder"++ environment:

    conda activate spyder

You should now see ++"(spyder)"++, as opposed to ++"(base)"++, next to your name in the command prompt (see [Figure 1](#conda-prompt)).

!!! note "Deactivate"
    To leave the current environment, use `conda deactivate`

Once the ++"spyder"++ environment is active, install Spyder with:

    conda install spyder

To start Spyder, run:

    spyder

We will explore additional settings and features of Spyder later, after installing the remaining software requirements.
