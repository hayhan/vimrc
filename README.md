# vimrc file using vim-plug

## What is it
The vimrc file contains some vim plugins that are common to developers as well
as specific ones for python and rust languages.

I tried to select the most popular plugins that have dependencies as few as
possible. See the comments in my_vimrc for the details.

The vimrc works well on MacOS, Linux and Windows 10.

## Usage

For MacOS and Linux, clone it to ~/.vim and then copy my_vimrc to ~/ and rename
it to .vimrc.

For Windows, clone it to C:\Users\your_username\vimfiles and then copy
my_vimrc to vim installation directory, e.g. C:\Program Fiels\Vim, and change
its name to _vimrc. Comment out line 15 and uncomment line 16 with your
username in _vimrc.

At last, open the .vimrc or _vimrc with vim and run :PlugInstall
