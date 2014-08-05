# Git Workflow for Mac

[xkcd git commit fun](http://xkcd.com/1296/)

This workflow assumes you are starting in your **home directory on OS X** and that you will only use the command line (no GitHub GUI here!).

This means /Users/*username*
	
	mymac:~ gavin$ pwd 
	/Users/gavin
	mymac:~ gavin$
	
## Lectures Repository

You do not need to fork the [Lectures](https://github.com/gavinmh/GADS12-NYC) repository because **you will never be pushing to the Lectures repository**.

### Clone the GADS12-NYC Lectures Repository

	git clone https://github.com/gavinmh/GADS12-NYC.git

**Example**:

	mymac:~ gavin$ git clone https://github.com/gavinmh/GADS12-NYC.git
	Cloning into 'GADS12-NYC'...
	remote: Counting objects: 824, done.
	remote: Compressing objects: 100% (432/432), done.
	remote: Total 824 (delta 360), reused 716 (delta 298)
	Receiving objects: 100% (824/824), 19.42 MiB | 1.48 MiB/s, done.
	Resolving deltas: 100% (360/360), done.
	mymac:~ gavin$
	
### Update For Every Class

	cd GADS12-NYC
	git pull origin master

**Example:**

	mymac:~ gavin$ cd GADS12-NYC
	mymac:GADS12-NYC gavin$ git pull origin master
	From https://github.com/gavinmh/GADS12-NYC
	 * branch            master     -> FETCH_HEAD
	Already up-to-date.
	mymac:GADS12-NYC gavin$
	
### Change Directory to the Current Lesson

	cd lecture-01
	
### Do the Lesson

But don't push any changes.

	ipython notebook
	
## Students Repository

You will fork the [Students](https://github.com/gavinmh/GADS12-NYC-Students) repository so that you have access rights to push changes. This is a standard model used by many git-controlled projects.

### Fork the datadave Students Repository

Log into [GitHub](https://github.com). Browse to the [datadave Students repository](https://github.com/gavinmh/GADS12-NYC-Students). Click the ``Fork`` button near the top right of the page.

### Clone Your Forked Repository
Replace *username* with your GitHub username

	git clone https://github.com/username/GADS12-NYC-Students.git
	
**Example:**

	mymac:~ gavin$ git clone https://github.com/gavinmh/GADS12-NYC-Students.git
	Cloning into 'GADS12-NYC-Students'...
	remote: Counting objects: 784, done.
	remote: Compressing objects: 100% (392/392), done.
	remote: Total 784 (delta 269), reused 784 (delta 269)
	Receiving objects: 100% (784/784), 13.27 MiB | 243 KiB/s, done.
	Resolving deltas: 100% (269/269), done.
	mymac:~ gavin$ 

### Add an Upstream Link to datadave
This step is critical to getting the latest *lab_submissions/lab0x* directories.

	cd GADS12-NYC-Students	
	git remote -v
	git remote add upstream https://github.com/gavinmh/GADS12-NYC-Students.git
	git remote -v	
Note: *git remote -v* will show you where git knows to look for different items. You will notice that git is unaware of *upstream* before running the *git remote add upstream ...* command.	

**Example:**
	
	mymac:~ gavin$ cd GADS12-NYC-Students
	mymac:GADS12-NYC-Students gavin$ git remote -v
	origin	https://github.com/gavinmh/GADS12-NYC-Students.git (fetch)
	origin	https://github.com/gavinmh/GADS12-NYC-Students.git (push)
	mymac:GADS12-NYC-Students gavin$ git remote add upstream https://github.com/gavinmh/GADS12-NYC-Students.git
	mymac:GADS12-NYC-Students gavin$ git remote -v
	origin	https://github.com/gavinmh/GADS12-NYC-Students.git (fetch)
	origin	https://github.com/gavinmh/GADS12-NYC-Students.git (push)
	upstream	https://github.com/gavinmh/GADS12-NYC-Students.git (fetch)
	upstream	https://github.com/gavinmh/GADS12-NYC-Students.git (push)
	mymac:GADS12-NYC-Students gavin$

### Merge the Official datadave Updates
We are going to fetch datadave (*upstream*), which puts the updates in a local branch called *upstream/master*. We'll make sure we are in our master branch, then perform the merge.

	git fetch upstream
	git checkout master
	git merge upstream/master
	
**Example:**

	mymac:GADS12-NYC-Students gavin$ git fetch upstream
	remote: Counting objects: 187, done.
	remote: Compressing objects: 100% (148/148), done.
	remote: Total 187 (delta 67), reused 77 (delta 22)
	Receiving objects: 100% (187/187), 60.51 KiB, done.
	Resolving deltas: 100% (67/67), done.
	From https://github.com/gavinmh/GADS12-NYC-Students
	 * [new branch]      dir_struct_for_repo -> upstream/dir_struct_for_repo
	 * [new branch]      lesson03   -> upstream/lesson03
	 * [new branch]      lesson1    -> upstream/lesson1
	 * [new branch]      lesson2    -> upstream/lesson2
	 * [new branch]      master     -> upstream/master
	 * [new branch]      python_and_data_lesson -> upstream/python_and_data_lesson
	mymac:GADS12-NYC-Students gavin$ git checkout master
	Already on 'master'
	mymac:GADS12-NYC-Students gavin$ git merge upstream/master
	Updating 0804e21..358897f
	...
	mymac:GADS12-NYC-Students gavin$

### Do Your Work!
Always remember to create an *flastname* directory beneath *lab_submissions/lab0x*, where you will save your work!

	cd lab_submissions
	cd lab0x_...
	mkdir flastname
	cd flastname
	[do work here]
	
**Example** (assuming the work we want to do is in lab02):

	mymac:GADS12-NYC-Students gavin$ cd lab_submissions/
	mymac:lab_submissions gavin$ cd lab02
	mymac:lab02 gavin$ mkdir gavinhackeling
	mymac:lab02 gavin$ cd gavinhackeling
	mymac:gavinhackeling gavin$ vi lab02.py
	mymac:gavinhackeling gavin$ vi mydata.csv
	
### Add Your Work
We need to tell git that we want to begin tracking the work you've just done.

	git add fileA fileB ... fileN
	-- Or --
	git add .
	
**Example** (assuming two files are to be added, *lab02.py* and *mydata.csv*):

	mymac:gavinhackeling gavin$ git add lab02.py mydata.csv 
	mymac:gavinhackeling gavin$

### Commit Your Work
Pro tip: Leaving off *-m &lt;msg&gt;* will bring up your default text editor. The comments in the editor will show you which files are being added, removed, or modified. *-m &lt;msg&gt;* is a convenience feature.

	git commit -m "Your commit message here"
	
**Example:**

	mymac:gavinhackeling gavin$ git commit -m "Committing Mac lab02 GitHub workflow sample files"
	[master 58206fc] Committing Mac lab02 GitHub workflow sample files
	 2 files changed, 11 insertions(+)
	 create mode 100644 lab_submissions/lab02/gavinhackeling/lab02.py
	 create mode 100644 lab_submissions/lab02/gavinhackeling/mydata.csv
	mymac:gavinhackeling gavin$
	
### Push Your Work
Remember *git remote -v* and how it showed that *origin* referred to your personal fork of the Students repository? That's where you want to push your changes changes. *master* refers to the branch name you are pushing--since you didn't change branches, your changes should be in your (local) master branch.

	git push origin master
	
**Example:**

	mymac:gavinhackeling gavin$ git push origin master
	Username for 'https://github.com': gavinmh
	Password for 'https://gavinmh@github.com': 
	To https://github.com/gavinmh/GADS12-NYC-Students.git
	   0804e21..58206fc  master -> master
	mymac:gavinhackeling gavin$

### Issue a Pull Request From Your Repository

Find and click the ```Pull Request``` link above your repository's file listing. Click the green ```Create Pull Request``` on the resulting page, add a title and comments as appropriate, and finally click ```Send pull request```.
