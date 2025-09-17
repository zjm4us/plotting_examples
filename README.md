# plotting_examples

The included Jupyter notebook gives additional examples of making basic plots needed to work on upcoming exercises.  

Exercise 1:
- Complete cells at the bottom of the notebook and include your updated notebook in your repo.

The most convenient way to work on the notebook on Rivanna to spin up a Jupyterlab session after making a local clone of your repository.  Make sure to select the Phys56xx kernel.

This repo also contains basic examples of using ROOT in your C++ or Python programs to generate plots.  To build the C++ program, first make sure you are in the phys56xx environment, then type ```make```.  This will create a program called cpp_example. Run the program with ```./cpp_program```.  The equivalent Python example can be run using ```python python_example.py```. 

The C++ example is more advanced.  This is provided as a first example of one way to incorpaorate graphing in a a compiled C++ program.  The Makefile contains the necessary definitions build the program.  These definitions include the location of header files so the compiler can check that the ROOT classes are being used properly and the location of the shared libraries so the linker can utilize the precompiled code in your program.  You will not be responsible for writing Makefiles from scratch in this class, examples will be provided as needed.

Exercise 2: 
- Use Matplotlib/numpy to generate the plots shown in this example.

Exercise 3 (PHYS5630 only):
- Modify both the C++ and Python examples as follows (Use program names: cpp_example2.cpp , python_example2.py and push these to your github repo)
  - Turn each of the Gaussian distributions into a 2D Gaussian with the same $\mu, \sigma$ in each dimension as in the original example
  - Similarly include 2D versions of the background distributions
  - For the C++ version, include a second build definition to make the cpp_example2.cpp program.
- Again use Matplotlib/numpy to generate the equivalent plots.

