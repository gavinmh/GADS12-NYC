# General Assembly Data Science 12


## Questions and Discussions:

* [Closed and Open Issue List (via pulse)](https://github.com/gavinmh/GADS12-NYC/pulse#closed-issues)
* [Create a new issue](https://github.com/gavinmh/GADS12-NYC/issues/new)

## Git Workflow and Command Line Tips:

* [Tips](https://github.com/gavinmh/GADS12-NYC/tree/master/tips)

Using a virtual machine
----

For further help/troubleshooting, feel free to come by the office hours or contact us for further help.

In case you're running into issues setting the environment up on your local environment, you can download a machine image from the following link: 

 https://www.dropbox.com/s/7nt0rt54m7jtxj5/GADS-InstalledEnv_1%28import%29.ova

Use the following user info to login: 

User: GADS

Password: gadspassword

**NOTE**: VMWare Player appears to occassionaly throw errors when dealing with this image.  Therefore, it would probably be easier to use [VirtualBox]

To install the virtual machine on VirtualBox

* Install VirtualBox
* Select File>Import Appliance
* When prompted, select 'GADS-InstalledEnv_1(import).ova' (or whatever you decided to name the downloaded image)
* Click through the rest of the import process
* In the main menu of VirtualBox, highlight the name of the machine (it should be whatever you named the ova file), and press 'Start'.

The image has Ubuntu 14.04 installed.  I found that the default RAM allocation (512 MB) was running a bit slow, so I adjusted the default allocation to 1024 MB.  If you're running into performance issues, you may need to adjust the memory allocation settings.

The image has the following libraries installed on it:

* [scikit-learn] (v 0.15.1)
* [numpy] (v 1.8.1)
* [pandas] (v 0.13.1)
* [scipy] (v 0.13.3)
* [pip] (v 1.5.6)
* [matplotlib] (v 1.3.1)
* [git]
* [nltk] (v 2.0.4)


#####  Git Repository in VM image

The class's git repo has been cloned as the following directory:

~/Desktop/courseGit/GADS12-NYC

There is a small bash script (~/Desktop/courseGit/GADS12-NYC/update) that allows you to type 'update-GADS' in order to clone the latest version from the repo.  The command is only soft-linked to the script, meaning that if 'update' is moved, the command won't work anymore.  Even if that happens though, you can just type 'git pull' in the repo's directory to update your local repo.


[scikit-learn]:http://scikit-learn.org/stable/
[numpy]:http://www.numpy.org/
[pandas]:http://pandas.pydata.org/
[scipy]:http://www.scipy.org/
[pip]:https://pypi.python.org/pypi/pip
[matplotlib]:http://matplotlib.org/
[git]:http://git-scm.com/
[nltk]:http://www.nltk.org/
[VirtualBox]:https://www.virtualbox.org/

## Classes

### Lecture 1: Introduction to Data Science
_Thursday, 2014/08/07_

#### Class Materials

* [Lecture](https://docs.google.com/presentation/d/1r2pWzZ3-ZvA4OiRVqTzDCSMj33RSI7_UrLn6kt9BZzQ/edit?usp=sharing)
* [lab_01a.md](https://github.com/gavinmh/GADS12-NYC/blob/master/lecture-1/lab-1a.md)
* [lab-1a-submission-example.md](https://github.com/gavinmh/GADS12-NYC/blob/master/lecture-1/lab-1a-submission-example.md)
* [lab_01b.md](https://github.com/gavinmh/GADS12-NYC/blob/master/lecture-1/lab-1b.md)


### Lecture 2: Simple Linear Regression
_Tuesday, 2014/08/12_

#### Class Materials

* [Lecture](https://docs.google.com/presentation/d/1b9bYZ9MIBqEmsJ3x5dBVlwxbSW-v0n-SazICmxh_iwU/edit?usp=sharing)
* [lab2.pdf](https://github.com/gavinmh/GADS12-NYC/blob/master/lecture-2/lab2.pdf)
* [lab_01b.md](https://github.com/gavinmh/GADS12-NYC/blob/master/lecture-2/lab-2b.md)
* [lab_01c.md](https://github.com/gavinmh/GADS12-NYC/blob/master/lecture-2/lab-2c.md)


### Lecture 3: Introduction to scikit-learn
_Thursday, 2014/08/14_

#### Class Materials


### Lecture 4: From Simple Linear Regression to Multiple Linear Regression
_Tuesday, 2014/08/19_

#### Class Materials


### Lecture 5: From Multiple Linear Regression to Polynomial Regression
_Thursday, 2014/08/21_

#### Class Materials


### Lecture 6: From Multiple Linear Regression to Generalized Linear Models
_Thursday, 2014/08/26_

#### Class Materials


### Lecture 7: Non-linear Classification and Regression with K-Nearest Neighbors
_Thursday, 2014/08/28_

#### Class Materials


### Lecture 8: (optional) Machine Learning Review
_Thursday, 2014/09/02_

#### Class Materials


### Lecture 9: Non-linear Classification and Regression with Decision Trees and Ensemble Learning
_Thursday, 2014/09/04_

#### Class Materials


### Lecture 10: Cluster Analysis with K-Means
_Thursday, 2014/09/09_

#### Class Materials

