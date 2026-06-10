# Linking Python (optional)
MATLAB also provides the ability to directly interface with Python, allowing MATLAB scripts to call Python functions, libraries, and external environments. This can be particularly useful when combining MATLAB-based simulation workflows with Python tools for data analysis, machine learning, visualization, or custom scientific software.

The connection between MATLAB and Python is managed through the `pyenv` command, which tells MATLAB which Python interpreter should be used. In this course, this is especially useful when working with isolated Python virtual environments created using Miniconda. 

To identify the active Python environment in MATLAB, enter the following in the "Command Window" (then press enter):

    pyenv

To change the interpreter to a specific Conda environment, use: 

    pyenv("Version", "C:\Users\troy\miniconda3\envs\capytaine\python.exe")

This command configures MATLAB to use the Python interpreter associated with the ++"capytaine"++ virtual environment (we'll create this later). Once linked, MATLAB can directly execute Python code and access installed Python packages **within that environment**.

!!! note "Path is Installation Dependent"
    The ++"path"++ in the command above will depend on: 1) where you [installed Miniconda](python.md#miniconda) and 2) the environment name. Therefore, don't just copy-paste the command above.

Because Python environments are isolated, it is important to point MATLAB to the correct interpreter associated with the desired virtual environment rather than the system-wide Python installation.

This functionality is entirely optional for the course, but it can become extremely powerful for more advanced workflows that combine MATLAB simulation tools with the broader Python scientific computing ecosystem.

As a simple example, MATLAB can import Python modules, execute Python functions, and exchange data between the two environments:

```matlab
% Import the Python NumPy module
np = py.importlib.import_module('numpy');

% Create a Python array
x = np.array([1, 2, 3, 4]);

% Convert Python array to MATLAB array
x_matlab = double(x);

% Display result
disp(x_matlab)
```

In this example, MATLAB imports the Python ++"numpy"++ package from the active Conda environment, creates a Python array, and then converts the result into a native MATLAB array using the double() conversion function. Once converted, the data behaves like any normal MATLAB variable.
