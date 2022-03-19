#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Managing-packages-using-package-managers" data-toc-modified-id="Managing-packages-using-package-managers-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Managing packages using package managers</a></span><ul class="toc-item"><li><span><a href="#Install-a-package" data-toc-modified-id="Install-a-package-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Install a package</a></span></li><li><span><a href="#Upgrade-a-package" data-toc-modified-id="Upgrade-a-package-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Upgrade a package</a></span></li><li><span><a href="#Uninstall-a-package" data-toc-modified-id="Uninstall-a-package-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Uninstall a package</a></span></li><li><span><a href="#Other-useful-commands" data-toc-modified-id="Other-useful-commands-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Other useful commands</a></span></li></ul></li><li><span><a href="#Install-packages-from-source" data-toc-modified-id="Install-packages-from-source-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Install packages from source</a></span></li></ul></div>

# <!--BOOK_INFORMATION-->
# <img align="left" style="padding-right:10px;" src="images/book_cover.jpg" width="120">
# 
# *This notebook contains an excerpt from the [Python Programming and Numerical Methods - A Guide for Engineers and Scientists](https://www.elsevier.com/books/python-programming-and-numerical-methods/kong/978-0-12-819549-9), the content is also available at [Berkeley Python Numerical Methods](https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html).*
# 
# *The copyright of the book belongs to Elsevier. We also have this interactive book online for a better learning experience. The code is released under the [MIT license](https://opensource.org/licenses/MIT). If you find this content useful, please consider supporting the work on [Elsevier](https://www.elsevier.com/books/python-programming-and-numerical-methods/kong/978-0-12-819549-9) or [Amazon](https://www.amazon.com/Python-Programming-Numerical-Methods-Scientists/dp/0128195495/ref=sr_1_1?dchild=1&keywords=Python+Programming+and+Numerical+Methods+-+A+Guide+for+Engineers+and+Scientists&qid=1604761352&sr=8-1)!*

# <!--NAVIGATION-->
# < [1.2 Python as a Calculator](chapter01.02-Python-as-A-Calculator.ipynb) | [Contents](Index.ipynb) | [1.4 Introduction to Jupyter Notebooks](chapter01.04-Introduction-to-Jupyter-Notebook.ipynb) >

# # Managing Packages

# One feature makes Python really great is the various packages/modules developed by the community. Most of the time, when you want to use some functions or algorithms, you will find there maybe already multiple packages from the community coded that for you, and all you need to do is to install the packages and use them in your code. Therefore, managing packages is one of the most important skills you need to learn to fully take advantage of Python. In this section, we will show you how to manage the packages in Python. 

# ## Managing packages using package managers
# 
# At the beginning of this book, we installed some packages using pip by typing *pip install package_name*. This is the most common and easy way these days to install Python packages. Pip is a package manager that automates the process of installing, updating, and removing the packages. It could install packages that published on [Python Package Index (PyPI)](https://pypi.org/). When we installed the Miniconda installer, it also installed pip for you to use.
# 
# First of all, you can use *pip help* to get help for different commands as shown below.
# 
# ![Pip_help](./images/01.03.01-pip_help.png "The help document of pip")
# 
# But the most used commands usually include: the install, upgrade, and uninstall a package. 
# 
# ### Install a package
# 
# To install the latest version of package_name:
# ```bash
# pip install package_name
# 
# ```
# 
# To install a specific version:
# 
# ```bash
# pip install package_name==1.5
# 
# ```
# 
# Pip will install the package as well as the dependencies for you to use.
# 
# ### Upgrade a package
# 
# To upgrade an installed package to the latest version from PyPI. 
# 
# ```bash
# pip install --upgrade package_name
# ```
# or simply
# 
# ```bash
# pip install -U package_name
# ```
# 
# ### Uninstall a package
# 
# ```bash
# pip uninstall package_name
# ```
# 
# ### Other useful commands
# 
# There are some other useful commands that you usually use to get information about the installed packages. For example, if you want to get a list of all the installed packages, you can use the command:
# 
# ```bash
# pip list
# ```
# ![Pip_list](./images/01.03.02-pip_list.png "Using pip list to show all the packages installed on your machine")
# 
# If you want to know more about an installed package, such as the location of the package, the required dependencies, and so on, you can use:
# 
# ```bash
# pip show package_name
# ```
# ![Pip_show](./images/01.03.03-pip_show.png "Using pip show to get detailed information about a installed package")
# 
# 
# There are other package managers, like conda that shipped with the Anaconda distribution, but for usage, it is similar to pip, therefore, we won't talk too much here, you can find more information by reading the [documentation](https://conda.io/docs/user-guide/getting-started.html). 
# 

# ## Install packages from source
# 
# Occasionally, you need to download the source file for some project that is not in the PyPI, then you need a different way to install the package. After uncompressing the file you downloaded, usually you can see the folder contains a setup script *setup.py*, and a file named README, which documents how to build and install the module. For most cases, you just need to run one command from the terminal to install the package:
# 
# ```bash
# python setup.py install
# ```
# 
# Note, for the Windows users, you need to run your command from a command prompt window:
# 
# ```
# setup.py install
# ```
# 

# Now you know how to manage the packages in Python, which is a big step forward to use Python correctly, and in the next section, we will talk more about the Jupyter notebook that we will use for the rest of the book. 

# <!--NAVIGATION-->
# < [1.2 Python as a Calculator](chapter01.02-Python-as-A-Calculator.ipynb) | [Contents](Index.ipynb) | [1.4 Introduction to Jupyter Notebooks](chapter01.04-Introduction-to-Jupyter-Notebook.ipynb) >
