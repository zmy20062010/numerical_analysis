#!/usr/bin/env python
# coding: utf-8

# <!--BOOK_INFORMATION-->
# <img align="left" style="padding-right:10px;" src="images/book_cover.jpg" width="120">
# 
# *This notebook contains an excerpt from the [Python Programming and Numerical Methods - A Guide for Engineers and Scientists](https://www.elsevier.com/books/python-programming-and-numerical-methods/kong/978-0-12-819549-9), the content is also available at [Berkeley Python Numerical Methods](https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html).*
# 
# *The copyright of the book belongs to Elsevier. We also have this interactive book online for a better learning experience. The code is released under the [MIT license](https://opensource.org/licenses/MIT). If you find this content useful, please consider supporting the work on [Elsevier](https://www.elsevier.com/books/python-programming-and-numerical-methods/kong/978-0-12-819549-9) or [Amazon](https://www.amazon.com/Python-Programming-Numerical-Methods-Scientists/dp/0128195495/ref=sr_1_1?dchild=1&keywords=Python+Programming+and+Numerical+Methods+-+A+Guide+for+Engineers+and+Scientists&qid=1604761352&sr=8-1)!*

# <!--NAVIGATION-->
# < [14.5 Solve Systems of Linear Equations in Python](chapter14.05-Solve-Systems-of-Linear-Equations-in-Python.ipynb)  | [Contents](Index.ipynb) | [14.7 Summary and Problems](chapter14.07-Summary-and-Problems.ipynb) >

# # Matrix Inversion

# We defined the inverse of a square matrix $M$ is a matrix of the same size, $M^{-1}$, such that $M \cdot M^{-1} = M^{-1} \cdot M = I$. If the dimension of the matrix is high, the analytic solution for the matrix inversion will be complicated. Therefore, we need some other efficient ways to get the inverse of the matrix. 
# 
# Let us use a $4 \times 4$ matrix for illustration. If we have $M = \begin{bmatrix}
# m_{1,1} & m_{1,2} & m_{1,3} & m_{1,4}\\
# m_{2,1} & m_{2,2} & m_{2,3} & m_{2,4}\\
# m_{3,1} & m_{3,2} & m_{3,3} & m_{3,4} \\
# m_{4,1} & m_{4,2} & m_{4,3} & m_{4,4}
# \end{bmatrix}$, and the inverse of $M$ is $X = \begin{bmatrix}
# x_{1,1} & x_{1,2} & x_{1,3} & x_{1,4}\\
# x_{2,1} & x_{2,2} & x_{2,3} & x_{2,4}\\
# x_{3,1} & x_{3,2} & x_{3,3} & x_{3,4} \\
# x_{4,1} & x_{4,2} & x_{4,3} & x_{4,4}
# \end{bmatrix}$, therefore, we will have:
# 
# $$M \cdot X = \begin{bmatrix}
# m_{1,1} & m_{1,2} & m_{1,3} & m_{1,4}\\
# m_{2,1} & m_{2,2} & m_{2,3} & m_{2,4}\\
# m_{3,1} & m_{3,2} & m_{3,3} & m_{3,4} \\
# m_{4,1} & m_{4,2} & m_{4,3} & m_{4,4}
# \end{bmatrix} \begin{bmatrix}
# x_{1,1} & x_{1,2} & x_{1,3} & x_{1,4}\\
# x_{2,1} & x_{2,2} & x_{2,3} & x_{2,4}\\
# x_{3,1} & x_{3,2} & x_{3,3} & x_{3,4} \\
# x_{4,1} & x_{4,2} & x_{4,3} & x_{4,4}
# \end{bmatrix} = \begin{bmatrix}
# 1 & 0 & 0 & 0\\
# 0 & 1 & 0 & 0\\
# 0 & 0 & 1 & 0\\
# 0 & 0 & 0 & 1
# \end{bmatrix}$$
# 
# We can rewrite the above equation to four separate equations, such as:
# 
# $$
# \begin{bmatrix}
# m_{1,1} & m_{1,2} & m_{1,3} & m_{1,4}\\
# m_{2,1} & m_{2,2} & m_{2,3} & m_{2,4}\\
# m_{3,1} & m_{3,2} & m_{3,3} & m_{3,4} \\
# m_{4,1} & m_{4,2} & m_{4,3} & m_{4,4}
# \end{bmatrix}\left[\begin{array}{c} x_{1,1} \\x_{2,1} \\ x_{3,1} \\x_{4,1} \end{array}\right] =
# \left[\begin{array}{c} 1\\0 \\0 \\0 \end{array}\right]$$
# 
# $$
# \begin{bmatrix}
# m_{1,1} & m_{1,2} & m_{1,3} & m_{1,4}\\
# m_{2,1} & m_{2,2} & m_{2,3} & m_{2,4}\\
# m_{3,1} & m_{3,2} & m_{3,3} & m_{3,4} \\
# m_{4,1} & m_{4,2} & m_{4,3} & m_{4,4}
# \end{bmatrix}\left[\begin{array}{c} x_{1,2} \\x_{2,2} \\ x_{3,2} \\x_{4,2} \end{array}\right] =
# \left[\begin{array}{c} 0\\1 \\0 \\0 \end{array}\right]$$
# 
# $$
# \begin{bmatrix}
# m_{1,1} & m_{1,2} & m_{1,3} & m_{1,4}\\
# m_{2,1} & m_{2,2} & m_{2,3} & m_{2,4}\\
# m_{3,1} & m_{3,2} & m_{3,3} & m_{3,4} \\
# m_{4,1} & m_{4,2} & m_{4,3} & m_{4,4}
# \end{bmatrix}\left[\begin{array}{c} x_{1,3} \\x_{2,3} \\ x_{3,3} \\x_{4,3} \end{array}\right] =
# \left[\begin{array}{c} 0\\0 \\1 \\0 \end{array}\right]$$
# 
# $$
# \begin{bmatrix}
# m_{1,1} & m_{1,2} & m_{1,3} & m_{1,4}\\
# m_{2,1} & m_{2,2} & m_{2,3} & m_{2,4}\\
# m_{3,1} & m_{3,2} & m_{3,3} & m_{3,4} \\
# m_{4,1} & m_{4,2} & m_{4,3} & m_{4,4}
# \end{bmatrix}\left[\begin{array}{c} x_{1,4} \\x_{2,4} \\ x_{3,4} \\x_{4,4} \end{array}\right] =
# \left[\begin{array}{c} 0\\0 \\0 \\1 \end{array}\right]$$
# 
# Therefore, if we solve the above four system of equations, we will get the inverse of the matrix. We can use any method we introduced previously to solve these equations, such as Gauss Elimination, Gauss-Jordan, and LU decomposition. Here, we will just show an example of matrix inversion using Gauss-Jordan method. 
# 
# Recall that, in Gauss-Jordan method, we convert our problem from 
# 
# $$
# \begin{bmatrix}
# m_{1,1} & m_{1,2} & m_{1,3} & m_{1,4}\\
# m_{2,1} & m_{2,2} & m_{2,3} & m_{2,4}\\
# m_{3,1} & m_{3,2} & m_{3,3} & m_{3,4} \\
# m_{4,1} & m_{4,2} & m_{4,3} & m_{4,4}
# \end{bmatrix}\left[\begin{array}{c} x_1 \\x_2 \\ x_3 \\x_4 \end{array}\right] =
# \left[\begin{array}{c} y_1 \\y_2 \\ y_3 \\y_4 \end{array}\right]$$
# 
# to 
# 
# $$
# \begin{bmatrix}
# 1 & 0 & 0 & 0\\
# 0 & 1 & 0 & 0\\
# 0 & 0 & 1 & 0\\
# 0 & 0 & 0 & 1
# \end{bmatrix} \left[\begin{array}{c} x_1 \\x_2 \\ x_3 \\x_4 \end{array}\right] =
# \left[\begin{array}{c} y_1' \\y_2' \\ y_3' \\y_4' \end{array}\right]$$
# 
# and get the solution. Essentially, we are converting 
# 
# $$
# \begin{bmatrix}
# m_{1,1} & m_{1,2} & m_{1,3} & m_{1,4} & y_1\\
# m_{2,1} & m_{2,2} & m_{2,3} & m_{2,4} & y_2\\
# m_{3,1} & m_{3,2} & m_{3,3} & m_{3,4} & y_3 \\
# m_{4,1} & m_{4,2} & m_{4,3} & m_{4,4} & y_4
# \end{bmatrix}
# $$
# 
# to 
# 
# $$
# \begin{bmatrix}
# 1 & 0 & 0 & 0 & y_1'\\
# 0 & 1 & 0 & 0 & y_2'\\
# 0 & 0 & 1 & 0 & y_3'\\
# 0 & 0 & 0 & 1 & y_4'
# \end{bmatrix}
# $$
# 
# Let us generalize it here, all we need to do is to convert 
# 
# $$
# \begin{bmatrix}
# m_{1,1} & m_{1,2} & m_{1,3} & m_{1,4} & 1 & 0 & 0 & 0\\
# m_{2,1} & m_{2,2} & m_{2,3} & m_{2,4} & 0 & 1 & 0 & 0\\
# m_{3,1} & m_{3,2} & m_{3,3} & m_{3,4} & 0 & 0 & 1 & 0\\
# m_{4,1} & m_{4,2} & m_{4,3} & m_{4,4} & 0 & 0 & 0 & 1
# \end{bmatrix}
# $$
# 
# to 
# 
# $$
# \begin{bmatrix}
# 1 & 0 & 0 & 0 & m_{1,1}' & m_{1,2}' & m_{1,3}' & m_{1,4}'\\
# 0 & 1 & 0 & 0 & m_{2,1}' & m_{2,2}' & m_{2,3}' & m_{2,4}'\\
# 0 & 0 & 1 & 0 & m_{3,1}' & m_{3,2}' & m_{3,3}' & m_{1,4}'\\
# 0 & 0 & 0 & 1 & m_{4,1}' & m_{4,2}' & m_{4,3}' & m_{1,4}'
# \end{bmatrix}
# $$
# 
# Then the matrix 
# 
# $$
# \begin{bmatrix}
#  m_{1,1}' & m_{1,2}' & m_{1,3}' & m_{1,4}'\\
#  m_{2,1}' & m_{2,2}' & m_{2,3}' & m_{2,4}'\\
#  m_{3,1}' & m_{3,2}' & m_{3,3}' & m_{1,4}'\\
#  m_{4,1}' & m_{4,2}' & m_{4,3}' & m_{1,4}'
# \end{bmatrix}
# $$
# 
# is the inverse of $M$ we are looking for. 
# 
# Can you explain how to use LU decomposition to get the inverse of a matrix?

# <!--NAVIGATION-->
# < [14.5 Solve Systems of Linear Equations in Python](chapter14.05-Solve-Systems-of-Linear-Equations-in-Python.ipynb)  | [Contents](Index.ipynb) | [14.7 Summary and Problems](chapter14.07-Summary-and-Problems.ipynb) >
