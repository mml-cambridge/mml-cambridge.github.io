# MML Website


## General

This is a static-website (meaning it is composed entirely of html and css). It is built by a program called [hugo](https://gohugo.io/) which transforms the content (formatted in markdown) into the html/css. As an initial primer you should read [the cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) as an introduction to this mini-language.


## Maintaining the site

### Quick and dirty

If you want to quickly make a **small** edit you can use GitHub's online interface:

1. Fork (button in top right) the [mml repository](https://github.com/ConorWilliams/mml/fork).
2. Navigate to the content file you wish to edit.
3. Press the edit button (small pencil).
4. Make your changes.
5. Fill in the commit changes box with a description of the change and press "Commit change".
6. Now go to your branches home page and press "Contribute" then "Open a pull request".
7. Fill in any metadata and the press "Create pull request".
8. Wait for an admin to confirm your changes!

You can repeat steps 2-5 on multiple files before opening a pull request if you want to modify multiple files at once.

### The proper way

If you want to make many edits and test what you're doing as you go, then you should really be using Git and compiling the website as you go to make sure you have not broken anything.

To build the website you will need to [install hugo](https://gohugo.io/installation/). On ubuntu this is just ``sudo snap install hugo``





Some instructions about maintaining this...

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew install hugo

pandas