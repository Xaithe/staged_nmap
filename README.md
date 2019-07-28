# staged_nmap
staged_nmap is a fairly basic python script to automate the intial scanning process for CTFs and Hack the Box
A T4 speed scan is first run against all ports, then a deeper scan is run against any open ports. This will save time against doing this manually, or running a -A scan against all ports

The script isn't finished yet, so don't bother trying it!

## Prerequisites
The script only uses modules from the _The Python Standard Library_ so you shouldn't have to install anything via Pip etc.

## Usage
The script is fairly simple, any outputs will be saved to the current working directory (A future development is to be able to specify)

```
Python3 staged_nmap.py <host>
```
