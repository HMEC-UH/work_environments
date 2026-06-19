MATLAB has been a staple of engineering education for decades. Many students encounter it through inexpensive academic licenses, become comfortable with the ecosystem, and continue using it throughout their careers. If you ask me, it is a brilliantly executed long-term business strategy. Nevertheless, the software is excellent, and as an academic research unit we continue to rely heavily on the extensive toolbox ecosystem it provides.

The goal of the instructions below is to get WEC-Sim up and running within MATLAB. The material provided here is intended to complement the official [WEC-Sim documentation](https://wec-sim.github.io/WEC-Sim/main/user/getting_started.html) by offering additional explanation, alternative approaches, and beginner-oriented insights that may help clarify the setup process. If you encounter any issues during installation or configuration, please refer to the official WEC-Sim documentation as the primary reference. If you are still stuck or have questions, do not hesitate to reach out for assistance.

# MATLAB
[MATLAB](https://www.mathworks.com/) is a numerical computing environment built around a core programming language and a collection of specialized toolboxes. Different engineering workflows often require different toolboxes depending on the type of analysis, modeling, or simulation being performed.

Throughout this course, MATLAB will primarily be used for simulation, data analysis, and marine energy engineering workflows. Course activities will follow the setup and software requirements established by the [WEC-Sim documentation](https://wec-sim.github.io/WEC-Sim/main/user/getting_started.html), which serves as one of the primary modeling frameworks used in the course.

Course participants should **install MATLAB Version 9.9 (R2020b) or newer** to ensure compatibility with WEC-Sim and associated toolboxes. In addition to the core MATLAB installation, the following toolboxes are required:

| Toolbox              | Minimum Version        |
| -------------------- | ---------------------- |
| Simulink             | Version 10.2 (R2020b) |
| Simscape             | Version 5.0 (R2020b)  |
| Simscape Multibody   | Version 7.2 (R2020b)  |


!!! note "MATLAB for Students"
    MATLAB offers an annual [student license](https://www.mathworks.com/store/link/products/student/STUDENT?s_tid=ac_buy_sv_but1) for about $150 (after adding "Simscape Multibody")

MATLAB provides a dedicated *installation executable* that guides users through the setup process, including account authentication, license selection, installation location, and toolbox selection. Overall, the installation process is fairly straightforward.

After completing the installation, start MATLAB and enter the following command into the "Command Window" (then press enter):

    ver

It should output a list containing the installed version of MATLAB and toolboxes. Below is an example following installation with the minimum requirements:
    
    >> ver
    -----------------------------------------------------------------------------------------------------------------
    MATLAB                                                Version 24.2        (R2024b)
    Simulink                                              Version 24.2        (R2024b)
    Simscape                                              Version 24.2        (R2024b)
    Simscape Multibody                                    Version 24.2        (R2024b)

You have now successfully installed MATLAB and the required toolboxes for this course.

