# prime-hexagon
The Prime Hexagon
![alt text](https://github.com/kaustubhcs/prime-hexagon/blob/master/poster/RISE%20Poster%20Prime%20Hexagon%202078%20(1)-1.jpg)
# NUCAR Cluster:computer:
## Overview
We have two login nodes that one can ssh into. From there **SLURM** allocates a compute
node for you to ssh into.
![alt text](https://github.com/kaustubhcs/prime-hexagon/blob/master/poster/tree.svg)
## Usage Guidelines
1. An account is required to access the cluster
2. Abide by applicable laws and university policies
3. Users will limit reasonably so as not to interfere with other users
4. Your ~ (home) directory should not be used for file staging
5. Sessions will be terminated after 24 hours, so please be wary so as not to lose work
6. Please contact us if you have any doubts about what you are doing
## Getting an Account
To request an account please fill out this form: (add form or email to send info to)
## Connecting to the Cluster
A working knowledge of Linux/UNIX commands is required for cluster use

To use the cluster begin by using ssh to connect to the login node.
You can use ssh with the -X option to enable X11 forwarding.
This will allow you to launch GUI's from the nodes. Your login should look like this
`bash-3.2$ ssh -X -p 27 username@nucar1.ece.neu.edu`
Where `username` is your assigned username from your cluster application.

To login from a Windows client we suggest using PuttY to to connct.

To manaage tasks we will use SLURM. More information is to come about how exactly
you can schedule tasks without interfering with other's tasks.

## Cluster Information
4 hybrid nodes, each housing:
+ 2CPU with 64 cores each, 128 cores per node
+ 256GB of RAM

Hybrid 1 and 2 have two NVIDIA Telsa V100's:
+ 640 Tensor Cores
+ 5,120 CUDA cores
+ 16 GB of memory

## Contact Us
