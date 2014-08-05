# Git Workflow for Windows

[xkcd git commit fun](http://xkcd.com/1296/)

This workflow assumes you are starting in your your **personal Documents folder on Windows** (this makes finding things in Windows Explorer super easy) and that you will only use the command line (```Start > run > cmd.exe```) for git interaction.

This means C:\\Users\\*username*\\Documents
	
## Lectures Repository

You do not need to fork the [Lectures](https://github.com/gavinmh/GADS12-NYC) repository because **you will never be pushing to the Lectures repository**.

### Clone the gavinmh Lectures Repository

	git clone https://github.com/gavinmh/GADS12-NYC.git

**Example**:

	C:\Users\Gavin\Documents>git clone https://github.com/gavinmh/GADS12-NYC.git
	Cloning into 'GADS12-NYC'...
	remote: Counting objects: 824, done.
	remote: Compressing objects: 100% (432/432), done.
	Remote: Total 824 (delta 360), reused 716 (delta 298)eceiving objects:  93% (76
	Receiving objects: 100% (824/824), 19.42 MiB | 882.00 KiB/s, done.

	Resolving deltas: 100% (360/360), done.
	Checking connectivity... done.

	C:\Users\Gavin\Documents>

### Update For Every Class

	cd GADS12-NYC
	git pull origin master

**Example:**
	
	C:\Users\Gavin\Documents>cd GADS12-NYC

	C:\Users\Gavin\Documents\GADS12-NYC>git pull origin master
	From https://github.com/gavinmh/GADS12-NYC
	 * branch            master     -> FETCH_HEAD
	Already up-to-date.

	C:\Users\Gavin\Documents\GADS12-NYC>

### Change Directory to the Current Lesson

	cd lecture-01
	
**Example:**

	C:\Users\Gavin\Documents\GADS12-NYC>cd lecture-01

	C:\Users\Gavin\Documents\GADS12-NYC\lecture-01>dir
	 Volume in drive C has no label.
	 Volume Serial Number is 6C01-BBC7

	 Directory of C:\Users\Gavin\Documents\GADS12-NYC\lecture-01

	04/18/2014  09:11 PM    <DIR>          .
	04/18/2014  09:11 PM    <DIR>          ..
	04/18/2014  09:11 PM    <DIR>          lesson01_intro_to_data_science
	04/18/2014  09:11 PM    <DIR>          lesson02_data_collection_and_extraction
	04/18/2014  09:11 PM    <DIR>          lesson03a_numpy
	04/18/2014  09:11 PM    <DIR>          lesson03b_pandas
	04/18/2014  09:11 PM    <DIR>          lesson04_matplotlib_and_EDA
	04/18/2014  09:11 PM                43 README.md
    	           1 File(s)             43 bytes
        	       7 Dir(s)  37,088,002,048 bytes free

	C:\Users\Gavin\Documents\GADS12-NYC\lecture-01>cd lesson04_matplolib_and_EDA

	C:\Users\Gavin\Documents\GADS12-NYC\lecture-01\lesson04_matplotlib_and_EDA>dir
	 Volume in drive C has no label.
	 Volume Serial Number is 6C01-BBC7

	 Directory of C:\Users\Gavin\Documents\GADS12-NYC\lecture-01\lesson04_matplotlib_and_EDA

	04/18/2014  09:11 PM    <DIR>          .
	04/18/2014  09:11 PM    <DIR>          ..
	04/18/2014  09:11 PM    <DIR>          .ipynb_checkpoints
	04/18/2014  09:11 PM    <DIR>          data
	04/18/2014  09:11 PM         1,429,481 DataVizLecture_v2.pdf
	04/18/2014  09:11 PM               988 readme.md
	04/18/2014  09:11 PM            95,844 Visualization_Instructional_Set.ipynb
    	           3 File(s)      1,526,313 bytes
        	       4 Dir(s)  37,088,002,048 bytes free

	C:\Users\Gavin\Documents\GADS12-NYC\lecture-01\lesson04_matplotlib_and_EDA>

### Do the Lesson

But don't push any changes.

	ipython notebook

## Students Repository

You will fork the [Students](https://github.com/gavinmh/GADS12-NYC-Students) repository so that you have access rights to push changes. This is a standard model used by many git-controlled projects.

### Fork the GADS12-NYC Students Repository

Log into [GitHub](https://github.com). Browse to the [GADS12-NYC Students repository](https://github.com/gavinmh/GADS12-NYC-Students). Click the ``Fork`` button near the top right of the page.

### Clone Your Forked Repository
Replace *username* with your GitHub username

	git clone https://github.com/username/GADS12-NYC-Students.git

**Example:**

	C:\Users\Gavin\Documents>git clone https://github.com/gavinmh/GADS12-NYC-Students.git
	Cloning into 'GADS12-NYC-Students'...
	remote: Counting objects: 784, done.
	remote: Compressing objects: 100% (392/392), done.
	remote: Total 784 (delta 269), reused 784 (delta 269)
	Receiving objects: 100% (784/784), 13.27 MiB | 247.00 KiB/s, done.
	Resolving deltas: 100% (269/269), done.
	Checking connectivity... done.

	C:\Users\Gavin\Documents>

### Add an Upstream Link to gavinmh
This step is critical to getting the latest *lab_submissions/lab0x* directories.

	cd GADS12-NYC-Students	
	git remote -v
	git remote add upstream https://github.com/gavinmh/GADS12-NYC-Students.git
	git remote -v	
Note: *git remote -v* will show you where git knows to look for different items. You will notice that git is unaware of *upstream* before running the *git remote add upstream ...* command.	

**Example:**

	C:\Users\Gavin\Documents>cd GADS12-NYC-Students

	C:\Users\Gavin\Documents\GADS12-NYC-Students>git remote -v
	origin  https://github.com/gavinmh/GADS12-NYC-Students.git (fetch)
	origin  https://github.com/gavinmh/GADS12-NYC-Students.git (push)

	C:\Users\Gavin\Documents\GADS12-NYC-Students>git remote add upstream https://github.com/gavinmh/GADS12-NYC-Students.git

	C:\Users\Gavin\Documents\GADS12-NYC-Students>git remote -v
	origin  https://github.com/gavinmh/GADS12-NYC-Students.git (fetch)
	origin  https://github.com/gavinmh/GADS12-NYC-Students.git (push)
	upstream        https://github.com/gavinmh/GADS12-NYC-Students.git (fetch)
	upstream        https://github.com/gavinmh/GADS12-NYC-Students.git (push)

	C:\Users\Gavin\Documents\GADS12-NYC-Students>

### Merge the Official gavinmh Updates
We are going to fetch gavinmh (*upstream*), which puts the updates in a local branch called *upstream/master*. We'll make sure we are in our master branch, then perform the merge.

	git fetch upstream
	git checkout master
	git merge upstream/master

**Example:**

	C:\Users\Gavin\Documents\GADS12-NYC-Students>git fetch upstream
	remote: Counting objects: 187, done.
	remote: Compressing objects: 100% (148/148), done.
	remote: Total 187 (delta 67), reused 77 (delta 22)
	Receiving objects: 100% (187/187), 60.51 KiB | 0 bytes/s, done.
	Resolving deltas: 100% (67/67), done.
	From https://github.com/gavinmh/GADS12-NYC-Students
	 * [new branch]      dir_struct_for_repo -> upstream/dir_struct_for_repo
	 * [new branch]      lesson03   -> upstream/lesson03
	 * [new branch]      lesson1    -> upstream/lesson1
	 * [new branch]      lesson2    -> upstream/lesson2
	 * [new branch]      master     -> upstream/master
	 * [new branch]      python_and_data_lesson -> upstream/python_and_data_lesson

	C:\Users\Gavin\Documents\GADS12-NYC-Students>git checkout master
	Already on 'master'
	Your branch is up-to-date with 'origin/master'.

	C:\Users\Gavin\Documents\GADS12-NYC-Students>git merge upstream/master
	Updating 0804e21..358897f
	...
	C:\Users\Gavin\Documents\GADS12-NYC-Students>
	
### Do Your Work!
Always remember to create an *flastname* directory beneath *lab_submissions/lab0x*, where you will save your work!

	cd lab_submissions
	cd lab0x_...
	mkdir flastname
	cd flastname
	[do work here]

**Example** (assuming the work we want to do is in lab02):

	C:\Users\Gavin\Documents\GADS12-NYC-Students>cd lab_submissions

	C:\Users\Gavin\Documents\GADS12-NYC-Students\lab_submissions>cd lab02

	C:\Users\Gavin\Documents\GADS12-NYC-Students\lab_submissions\lab02>mkdir gavinmh

	C:\Users\Gavin\Documents\GADS12-NYC-Students\lab_submissions\lab02>cd gavinmh

	C:\Users\Gavin\Documents\GADS12-NYC-Students\lab_submissions\lab02\gavinmh>notepad lab02_windows.py

	C:\Users\Gavin\Documents\GADS12-NYC-Students\lab_submissions\lab02\gavinmh>notepad mydata_windows.csv

	C:\Users\Gavin\Documents\GADS12-NYC-Students\lab_submissions\lab02\gavinmh>

	
### Add Your Work
We need to tell git that we want to begin tracking the work you've just done.

	git add fileA fileB ... fileN
	-- Or --
	git add .
	
**Example** (assuming two files are to be added, *lab02_windows.py* and *mydata_windows.csv*):

	C:\Users\Gavin\Documents\GADS12-NYC-Students\lab_submissions\lab02\gavinmh>git add lab02_windows.py mydata_windows.csv

	C:\Users\Gavin\Documents\GADS12-NYC-Students\lab_submissions\lab02\gavinmh>
	
### Commit Your Work
Pro tip: Leaving off *-m &lt;msg&gt;* will bring up your default text editor. The comments in the editor will show you which files are being added, removed, or modified. *-m &lt;msg&gt;* is a convenience feature.

	git commit -m "Your commit message here"

**Example:**

	C:\Users\Gavin\Documents\GADS12-NYC-Students\lab_submissions\lab02\gavinmh>git commit -m "Commiting the lab02 Windows GitHub workflow sample files"
	[master cc6e9fc] Commiting the lab02 Windows GitHub workflow sample files
	 2 files changed, 11 insertions(+)
	 create mode 100644 lab_submissions/lab02/gavinmh/lab02_windows.py
	 create mode 100644 lab_submissions/lab02/gavinmh/mydata_windows.csv

	C:\Users\Gavin\Documents\GADS12-NYC-Students\lab_submissions\lab02\gavinmh>
	
### Push Your Work
Remember *git remote -v* and how it showed that *origin* referred to your personal fork of the Students repository? That's where you want to push your changes changes. *master* refers to the branch name you are pushing--since you didn't change branches, your changes should be in your (local) master branch.

	git push origin master

**Example:**
	
	C:\Users\Gavin\Documents\GADS12-NYC-Students\lab_submissions\lab02\gavinmh>git push origin master
	Username for 'https://github.com': gavinmh
	Password for 'https://gavinmh@github.com':
	Counting objects: 31, done.
	Compressing objects: 100% (11/11), done.
	Writing objects: 100% (12/12), 1.14 KiB | 0 bytes/s, done.
	Total 12 (delta 6), reused 0 (delta 0)
	To https://github.com/gavinmh/GADS12-NYC-Students.git
	   8c406f3..e0eb34a  master -> master

	C:\Users\Gavin\Documents\GADS12-NYC-Students\lab_submissions\lab02\gavinmh>
	
### Issue a Pull Request From Your Repository

Find and click the ```Pull Request``` link above your repository's file listing. Click the green ```Create Pull Request``` on the resulting page, add a title and comments as appropriate, and finally click ```Send pull request```.# Git Workflow for Windows

[xkcd git commit fun](http://xkcd.com/1296/)

This workflow assumes you are starting in your your **personal Documents folder on Windows** (this makes finding things in Windows Explorer super easy) and that you will only use the command line (```Start > run > cmd.exe```) for git interaction.

This means C:\\Users\\*username*\\Documents

	C:\Users\Gavin\Documents>cd
	C:\Users\Gavin\Documents

	C:\Users\Gavin\Documents>
	
## Lectures Repository

You do not need to fork the [Lectures](https://github.com/gavinmh/GADS12-NYC) repository because **you will never be pushing to the Lectures repository**.

### Clone the gavinmh Lectures Repository

	git clone https://github.com/gavinmh/GADS12-NYC.git

**Example**:

	C:\Users\Gavin\Documents>git clone https://github.com/gavinmh/GADS12-NYC
	4-Lectures.git
	Cloning into 'GADS12-NYC'...
	remote: Counting objects: 824, done.
	remote: Compressing objects: 100% (432/432), done.
	Remote: Total 824 (delta 360), reused 716 (delta 298)eceiving objects:  93% (76
	Receiving objects: 100% (824/824), 19.42 MiB | 882.00 KiB/s, done.

	Resolving deltas: 100% (360/360), done.
	Checking connectivity... done.

	C:\Users\Gavin\Documents>

### Update For Every Class

	cd GADS12-NYC
	git pull origin master

**Example:**
	
	C:\Users\Gavin\Documents>cd GADS12-NYC

	C:\Users\Gavin\Documents\GADS12-NYC>git pull origin master
	From https://github.com/gavinmh/GADS12-NYC
	 * branch            master     -> FETCH_HEAD
	Already up-to-date.

	C:\Users\Gavin\Documents\GADS12-NYC>

### Change Directory to the Current Lesson

	cd lecture-01
	cd lesson0x_abc
	
**Example:**

	C:\Users\Gavin\Documents\GADS12-NYC>cd lecture-01

	C:\Users\Gavin\Documents\GADS12-NYC\lecture-01>dir
	 Volume in drive C has no label.
	 Volume Serial Number is 6C01-BBC7

	 Directory of C:\Users\Gavin\Documents\GADS12-NYC\lecture-01

	04/18/2014  09:11 PM    <DIR>          .
	04/18/2014  09:11 PM    <DIR>          ..
	04/18/2014  09:11 PM    <DIR>          lesson01_intro_to_data_science
	04/18/2014  09:11 PM    <DIR>          lesson02_data_collection_and_extraction
	04/18/2014  09:11 PM    <DIR>          lesson03a_numpy
	04/18/2014  09:11 PM    <DIR>          lesson03b_pandas
	04/18/2014  09:11 PM    <DIR>          lesson04_matplotlib_and_EDA
	04/18/2014  09:11 PM                43 README.md
    	           1 File(s)             43 bytes
        	       7 Dir(s)  37,088,002,048 bytes free

	C:\Users\Gavin\Documents\GADS12-NYC\lecture-01>cd lesson04_matplolib_and_EDA

	C:\Users\Gavin\Documents\GADS12-NYC\lecture-01\lesson04_matplotlib_and_EDA>dir
	 Volume in drive C has no label.
	 Volume Serial Number is 6C01-BBC7

	 Directory of C:\Users\Gavin\Documents\GADS12-NYC\lecture-01\lesson04_matplotlib_and_EDA

	04/18/2014  09:11 PM    <DIR>          .
	04/18/2014  09:11 PM    <DIR>          ..
	04/18/2014  09:11 PM    <DIR>          .ipynb_checkpoints
	04/18/2014  09:11 PM    <DIR>          data
	04/18/2014  09:11 PM         1,429,481 DataVizLecture_v2.pdf
	04/18/2014  09:11 PM               988 readme.md
	04/18/2014  09:11 PM            95,844 Visualization_Instructional_Set.ipynb
    	           3 File(s)      1,526,313 bytes
        	       4 Dir(s)  37,088,002,048 bytes free

	C:\Users\Gavin\Documents\GADS12-NYC\lecture-01\lesson04_matplotlib_and_EDA>

### Do the Lesson

But don't push any changes.

	ipython notebook

## Students Repository

You will fork the [Students](https://github.com/gavinmh/GADS12-NYC-Students) repository so that you have access rights to push changes. This is a standard model used by many git-controlled projects.

### Fork the gavinmh Students Repository

Log into [GitHub](https://github.com). Browse to the [gavinmh Students repository](https://github.com/gavinmh/GADS12-NYC-Students). Click the ``Fork`` button near the top right of the page.

### Clone Your Forked Repository
Replace *username* with your GitHub username

	git clone https://github.com/username/GADS12-NYC-Students.git

**Example:**

	C:\Users\Gavin\Documents>git clone https://github.com/gavinmh/GADS12-NYC-Students.git
	Cloning into 'GADS12-NYC-Students'...
	remote: Counting objects: 784, done.
	remote: Compressing objects: 100% (392/392), done.
	remote: Total 784 (delta 269), reused 784 (delta 269)
	Receiving objects: 100% (784/784), 13.27 MiB | 247.00 KiB/s, done.
	Resolving deltas: 100% (269/269), done.
	Checking connectivity... done.

	C:\Users\Gavin\Documents>

### Add an Upstream Link to gavinmh
This step is critical to getting the latest *lab_submissions/lab0x* directories.

	cd GADS12-NYC-Students	
	git remote -v
	git remote add upstream https://github.com/gavinmh/GADS12-NYC-Students.git
	git remote -v	
Note: *git remote -v* will show you where git knows to look for different items. You will notice that git is unaware of *upstream* before running the *git remote add upstream ...* command.	

**Example:**

	C:\Users\Gavin\Documents>cd GADS12-NYC-Students

	C:\Users\Gavin\Documents\GADS12-NYC-Students>git remote -v
	origin  https://github.com/gavinmh/GADS12-NYC-Students.git (fetch)
	origin  https://github.com/gavinmh/GADS12-NYC-Students.git (push)

	C:\Users\Gavin\Documents\GADS12-NYC-Students>git remote add upstream https://github.com/gavinmh/GADS12-NYC-Students.git

	C:\Users\Gavin\Documents\GADS12-NYC-Students>git remote -v
	origin  https://github.com/gavinmh/GADS12-NYC-Students.git (fetch)
	origin  https://github.com/gavinmh/GADS12-NYC-Students.git (push)
	upstream        https://github.com/gavinmh/GADS12-NYC-Students.git (fetch)
	upstream        https://github.com/gavinmh/GADS12-NYC-Students.git (push)

	C:\Users\Gavin\Documents\GADS12-NYC-Students>

### Merge the Official gavinmh Updates
We are going to fetch gavinmh (*upstream*), which puts the updates in a local branch called *upstream/master*. We'll make sure we are in our master branch, then perform the merge.

	git fetch upstream
	git checkout master
	git merge upstream/master

**Example:**

	C:\Users\Gavin\Documents\GADS12-NYC-Students>git fetch upstream
	remote: Counting objects: 187, done.
	remote: Compressing objects: 100% (148/148), done.
	remote: Total 187 (delta 67), reused 77 (delta 22)
	Receiving objects: 100% (187/187), 60.51 KiB | 0 bytes/s, done.
	Resolving deltas: 100% (67/67), done.
	From https://github.com/gavinmh/GADS12-NYC-Students
	 * [new branch]      dir_struct_for_repo -> upstream/dir_struct_for_repo
	 * [new branch]      lesson03   -> upstream/lesson03
	 * [new branch]      lesson1    -> upstream/lesson1
	 * [new branch]      lesson2    -> upstream/lesson2
	 * [new branch]      master     -> upstream/master
	 * [new branch]      python_and_data_lesson -> upstream/python_and_data_lesson

	C:\Users\Gavin\Documents\GADS12-NYC-Students>git checkout master
	Already on 'master'
	Your branch is up-to-date with 'origin/master'.

	C:\Users\Gavin\Documents\GADS12-NYC-Students>git merge upstream/master
	Updating 0804e21..358897f
	...
	C:\Users\Gavin\Documents\GADS12-NYC-Students>
	
### Do Your Work!
Always remember to create an *flastname* directory beneath *lab_submissions/lab0x*, where you will save your work!

	cd lab_submissions
	cd lab0x_...
	mkdir flastname
	cd flastname
	[do work here]

**Example** (assuming the work we want to do is in lab02):

	C:\Users\Gavin\Documents\GADS12-NYC-Students>cd lab_submissions

	C:\Users\Gavin\Documents\GADS12-NYC-Students\lab_submissions>cd lab02

	C:\Users\Gavin\Documents\GADS12-NYC-Students\lab_submissions\lab02>mkdir gavinmh

	C:\Users\Gavin\Documents\GADS12-NYC-Students\lab_submissions\lab02>cd gavinmh

	C:\Users\Gavin\Documents\GADS12-NYC-Students\lab_submissions\lab02\gavinmh>notepad lab02_windows.py

	C:\Users\Gavin\Documents\GADS12-NYC-Students\lab_submissions\lab02\gavinmh>notepad mydata_windows.csv

	C:\Users\Gavin\Documents\GADS12-NYC-Students\lab_submissions\lab02\gavinmh>

	
### Add Your Work
We need to tell git that we want to begin tracking the work you've just done.

	git add fileA fileB ... fileN
	-- Or --
	git add .
	
**Example** (assuming two files are to be added, *lab02_windows.py* and *mydata_windows.csv*):

	C:\Users\Gavin\Documents\GADS12-NYC-Students\lab_submissions\lab02\gavinmh>git add lab02_windows.py mydata_windows.csv

	C:\Users\Gavin\Documents\GADS12-NYC-Students\lab_submissions\lab02\gavinmh>
	
### Commit Your Work
Pro tip: Leaving off *-m &lt;msg&gt;* will bring up your default text editor. The comments in the editor will show you which files are being added, removed, or modified. *-m &lt;msg&gt;* is a convenience feature.

	git commit -m "Your commit message here"

**Example:**

	C:\Users\Gavin\Documents\GADS12-NYC-Students\lab_submissions\lab02\gavinmh>git commit -m "Commiting the lab02 Windows GitHub workflow sample files"
	[master cc6e9fc] Commiting the lab02 Windows GitHub workflow sample files
	 2 files changed, 11 insertions(+)
	 create mode 100644 lab_submissions/lab02/gavinmh/lab02_windows.py
	 create mode 100644 lab_submissions/lab02/gavinmh/mydata_windows.csv

	C:\Users\Gavin\Documents\GADS12-NYC-Students\lab_submissions\lab02\gavinmh>
	
### Push Your Work
Remember *git remote -v* and how it showed that *origin* referred to your personal fork of the Students repository? That's where you want to push your changes changes. *master* refers to the branch name you are pushing--since you didn't change branches, your changes should be in your (local) master branch.

	git push origin master

**Example:**
	
	C:\Users\Gavin\Documents\GADS12-NYC-Students\lab_submissions\lab02\gavinmh>git push origin master
	Username for 'https://github.com': gavinmh
	Password for 'https://gavinmh@github.com':
	Counting objects: 31, done.
	Compressing objects: 100% (11/11), done.
	Writing objects: 100% (12/12), 1.14 KiB | 0 bytes/s, done.
	Total 12 (delta 6), reused 0 (delta 0)
	To https://github.com/gavinmh/GADS12-NYC-Students.git
	   8c406f3..e0eb34a  master -> master

	C:\Users\Gavin\Documents\GADS12-NYC-Students\lab_submissions\lab02\gavinmh>
	
### Issue a Pull Request From Your Repository

Find and click the ```Pull Request``` link above your repository's file listing. Click the green ```Create Pull Request``` on the resulting page, add a title and comments as appropriate, and finally click ```Send pull request```.
