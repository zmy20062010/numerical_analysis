#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# <!--BOOK_INFORMATION-->
# <img align="left" style="padding-right:10px;" src="images/book_cover.jpg" width="120">
# 
# *This notebook contains an excerpt from the [Python Programming and Numerical Methods - A Guide for Engineers and Scientists](https://www.elsevier.com/books/python-programming-and-numerical-methods/kong/978-0-12-819549-9), the content is also available at [Berkeley Python Numerical Methods](https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html).*
# 
# *The copyright of the book belongs to Elsevier. We also have this interactive book online for a better learning experience. The code is released under the [MIT license](https://opensource.org/licenses/MIT). If you find this content useful, please consider supporting the work on [Elsevier](https://www.elsevier.com/books/python-programming-and-numerical-methods/kong/978-0-12-819549-9) or [Amazon](https://www.amazon.com/Python-Programming-Numerical-Methods-Scientists/dp/0128195495/ref=sr_1_1?dchild=1&keywords=Python+Programming+and+Numerical+Methods+-+A+Guide+for+Engineers+and+Scientists&qid=1604761352&sr=8-1)!*

# <!--NAVIGATION-->
# < [14.1 Basics of Linear Algebra](chapter14.01-Basics-of-Linear-Algebra.ipynb) | [Contents](Index.ipynb) | [14.3 Systems of Linear Equations](chapter14.03-Systems-of-Linear-Equations.ipynb) >

# # Linear Transformations

# For vectors $x$ and $y$, and scalars $a$ and $b$, it is sufficient to say that a function, $F$, is a **linear transformation** if  
# 
# $$
# F(ax + by) = aF(x) + bF(y).
# $$
# 
# It can be shown that multiplying an ${m} \times {n}$ matrix, $A$, and an ${n} \times {1}$ vector, $v$, of compatible size is a linear transformation of $v$. Therefore from this point forward, a matrix will be synonymous with a linear transformation function.
# 
# **TRY IT!** Let $x$ be a vector and let $F(x)$ be defined by $F(x) = Ax$ where $A$ is a rectangular matrix of appropriate size. Show that $F(x)$ is a linear transformation.
# 
# Proof:
# Since $F(x) = Ax$, then
# for vectors $v$ and $w$, and scalars $a$ and $b$, $F(av +
# bw) = A(av + bw)$ (by definition of $F$)$=$$aAv + bAw$ (by
# distributive property of matrix multiplication)$=$$aF(v) +
# bF(w)$ (by definition of $F$).
# 
# If $A$ is an ${m} \times {n}$ matrix, then there are two important subpsaces associated with $A$, one is ${\mathbb{R}}^n$, the other is ${\mathbb{R}}^m$. The **domain** of $A$ is a subspace of ${\mathbb{R}}^n$. It is the set of all vectors that can be multiplied by $A$ on the right. The **range** of $A$ is a subspace of ${\mathbb{R}}^m$. It is the set of all vectors $y$ such that $y=Ax$. It can be denoted as $\mathcal{R}(\mathbf{A})$, where $\mathcal{R}(\mathbf{A}) = \{y \in {\mathbb{R}}^m: Ax = y\}$. Another way to think about the range of $A$ is the set of all linear combinations of the columns in $A$, where $x_i$ is the coefficient of the ith column in $A$. The **null space** of $A$, defined as $\mathcal{N}(\mathbf{A}) = \{x \in {\mathbb{R}}^n: Ax = 0_m\}$, is the subset of vectors in the domain of $A, x$, such that $Ax = 0_m$, where $0_m$ is the **zero vector** (i.e., a vector in ${\mathbb{R}}^m$ with all zeros).
# 
# **TRY IT!** Let $A = [[1, 0, 0], [0, 1, 0], [0, 0, 0]]$ and let the domain of $A$ be ${\mathbb{R}}^3$. Characterize the range and nullspace of $A$.
#   
# Let $v = [x,y,z]$ be a vector in ${\mathbb{R}}^3$. Then $u = Av$ is the vector $u = [x,y,0]$. Since $x,y\in {\mathbb{R}}$, the range of $A$ is the $x$-$y$ plane at $z = 0$.
# 
# Let $v = [0,0,z]$ for $z\in {\mathbb{R}}$. Then $u = Av$ is the vector $u = [0, 0, 0]$. Therefore, the nullspace of $A$ is the $z$-axis (i.e., the set of vectors $[0,0,z]$ $z\in {\mathbb{R}}$).
# 
# Therefore, this linear transformation "flattens" any $z$-component from a vector.

# <!--NAVIGATION-->
# < [14.1 Basics of Linear Algebra](chapter14.01-Basics-of-Linear-Algebra.ipynb) | [Contents](Index.ipynb) | [14.3 Systems of Linear Equations](chapter14.03-Systems-of-Linear-Equations.ipynb) >
