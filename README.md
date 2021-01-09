# vimrc file using vim-plug

## What is it
The vimrc file contains some vim plugins that are common to developers as well
as specific ones for python and rust languages.

I tried to select the most popular plugins that have dependencies as few as
possible. See the comments in _vimrc.legacy & _vimrc.modern for the details.

The vimrc works on MacOS, Linux and Windows.

## Usage

For MacOS and Linux, clone it to ~/.vim and then copy _vimrc.* to ~/ and rename
it to .vimrc.

For Windows, clone it to C:\Users\your_username\vimfiles and then copy _vimrc.*
to C:\Users\your_username\ and rename it to _vimrc. Comment out line 17 and
uncomment line 18 with your username changing in _vimrc.

At last, open the .vimrc or _vimrc with vim and run :PlugInstall
