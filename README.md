# MML Website


Welcome to the MML's website source code, this page is intended for members of the MML to learn about editing the website.

We have a static-website (meaning it is composed entirely of html and css). It is built by a program called [hugo](https://gohugo.io/) which transforms the content (formatted in markdown) into the html/css. As an initial primer you should read [the cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) as an introduction to this mini-language.

## Maintaining the site


### Quick and dirty

If you want to quickly make a **small** edit you can use GitHub's online interface:

1. Fork (button in top right) the [mml repository](https://github.com/ConorWilliams/mml).
2. Navigate to the content file you wish to edit.
3. Press the edit button (small pencil).
4. Make your changes.
5. Fill in the commit changes box with a description of the change and press "Commit change".
6. Now go to your branches home page and press "Contribute" then "Open a pull request".
7. Fill in any metadata and the press "Create pull request".
8. Wait for an admin to confirm your changes!

You can repeat steps 2-5 on multiple files before opening a pull request if you want to modify multiple files at once.

If your fork gets out of sync with the main repository (i.e. if the main repository has some other content added by an admin) the you can always press the sync fork button.

### The proper way

If you want to make many edits and test what you're doing as you go, then you should really be using Git and compiling the website as you go to make sure you have not broken anything.

1. [Install hugo](https://gohugo.io/installation/). On ubuntu this is just ``sudo snap install hugo``.
2. Fork (button in top right) the [mml repository](https://github.com/ConorWilliams/mml).
3. Clone your fork i.e: ``git clone --recurse-submodules https://github.com/your_user_name/mml.git``. 
4. Make your changes locally.
5. Run ``python pubs.py`` from the top level of the repository to populate the publications.
6. Run ``hugo server`` from the top level of the repository.
7. Navigate to the web address the server command tells you the site is available (e.g. ``//localhost:1313/mml/``).
8. Make sure your changes are as-intended.
9. Commit your changes ``git add -A`` then ``git commit -m"my awesome changes"``.
10. Push your changes ``git push``.
11. Follow steps 6-8 of quick-and-dirty method to submit a pull request.

### TLDR - for people who just want to edit the content.

Have a look inside the ``content/`` directory for examples of how to do anything e.g. add a new group member just extend ``content/people/index.md``.

### In detail

The site uses the [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme which has extensive documentation. 

### Publications

The script ``pubs.py`` will populate ``content/posts`` with the data in ``pubs.bib``.