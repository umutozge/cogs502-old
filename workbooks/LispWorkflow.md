# Lisp workflow

The following guide is for people who would like to edit their files with `vim`. If you'd like to use `emacs`, try `slime`.

## How to install 

The workflow outlined here is based on the following components:

* `screen` -- a handy terminal window system
* `sbcl` -- a development environment for ANSI Common Lisp
* `vim` -- a fully customizable editor
* `rlwrap` -- a utility that makes life easier in `sbcl` command-line


Besides these, you will also need `git` to fetch some configuration files.

If you are working  on `lfcs.ii.metu.edu.tr`, you do not need to install anything. If you are on your own machine, install any missing packages by:

```bash
sudo apt-get update
sudo apt-get install <package-name1> <package-name2> ...
```


Now we will configure `vim`, so that you can use it efficiently to write and run lisp code. First you need to get necessary stuff, which are located at a `git` repository on `github.com`. Nowadays many people and institutions develop and share their projects on this platform. From time to time you will need to get and contribute content to this platform; therefore I strongly advise to have a github directory somewhere on your account. For the present tutorial let us assume you want to have it under your home folder. First change to your home folder by:

```
cd ~
```

The `~` sign stands for your home folder; wherever you are, typing `cd ~` will bring you home. Now create and change into your `github` directory, name is not important. 

```
mkdir github
cd github
```

Now we will clone the repository we need for customizing `vim` for lisp. 


```
git clone https://github.com/umutozge/dotfiles.git
```

This command will create a directory named `dotfiles`. If you are new to `vim`, I suggest you do the following:

```
rsync -av ~/github/dotfiles/vimrc ~/.vimrc
rsync -av ~/github/dotfiles/vim/ ~/.vim/
```

Be careful to type everything exactly as above; especially the dots are important and easy to miss.

If you have some experience in using and customizing `vim`, then what you need for lisp interaction are `screen` plugin and the `lisp.vim` file type plugin. You might also want to check other goodies in my vim configuration tree and `vimrc`. Most probably you would not want to have everything.  

## How to use

Assuming everything worked fine so far, start to edit a Lisp file:

```
vim test.lisp
```

Type a procedure that you would want to evaluate in `sbcl`, e.g.\

```lisp
(defun factorial (n)
  (if (= n 0)
      1
      (* n (factorial (- n 1)))))
```

You will observe that you do not have to do anything to get the indentation right, whenever you create a newline `vim` will decide how much to indent the next line.

There are two ways of evaluating code. 

### Evaluation without opening a separate window for `sbcl`

If you do not need to see the code itself while testing it in `sbcl`:

* go to the beginning of the region you want to evaluate;
* press `V` in normal mode to enter into visual mode;
* go down to the end of the region;
* typing `,e` opens up an internal `sbcl` session and evaluates whatever is in the region;
* when you are done, quit `sbcl` by pressing `Ctrl-D` or evaluating `(exit)`;
* you are back in `vim`


Now you do some more editing. If your additions are all between the start and end of the region you evaluated last, you do not need to select a region again, just type `,,e` -- two commas instead of one -- to switch to `sbcl` for evaluation. It doesn't matter how much the region grows with your additions or shrinks by your deletions, as long as nothing is before the start and after the end of the last selection. If you edit the code beyond the limits of the last selection, you will need to do the visual region selection again.

### Evaluation with opening a separate window for `sbcl`

If you do want to see the code while you work in `sbcl` do this:

* In normal mode type `,s`;
* This will open a separate window below your editor which runs `sbcl`;
* Select a region to evaluate as above;
* This time type `,r` to send the region to `sbcl`;
* To shift to `sbcl` window type `Ctrl-A` and then `TAB`;
* When you are finished with `sbcl`, return to `vim` by the same sequence: `Ctrl-A` and then `TAB`.

Whenever you want to close the `sbcl` window, type `,q` in `vim` normal mode.

### Commenting

To comment a region:

* select it;
* type `,c`

To uncomment a region:

* select it;
* type `,u`

### Dealing with parentheses

If you open and close a parenthesis without waiting too much in between, the cursor will end up between the parenthesis and in insert mode. This way there is no need to think about closing the parentheses you opened. See  `.vimrc` for other goodies you might find useful.



## How to update

Please let me know about functionalities you would want to have; so that I integrate them. Whenever there is such an update, you will need to get the updated files. To do this go to the repository directory:

```
cd ~/github/dotfiles
```

Get whatever is updated in the repository by:


```
git pull origin master
```

You will need to do the copying with `rsync` again. If you do not want to do the copying every time there is an update, you may create symbolic links as follows:


```
ln -s ~/github/dotfiles/vimrc ~/.vimrc
ln -s ~/github/dotfiles/vim ~/.vim
```

If you have these links, it would be enough to `pull` to update everything.

Of course these update methods do not apply if you have your own customization files besides those coming from my repository.

