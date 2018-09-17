# Containerisation #

## What is it? ##

Containers are an abstraction at the app layer that packages code and dependencies together. Multiple containers can run on the same machine and share the OS kernel with other containers, each running as isolated processes in user space. Containers take up less space than VMs (container images are typically tens of MBs in size), can handle more applications and require fewer VMs and Operating systems.

## What are the advantages? ##

* Because the OS is shared there is less load on the host machine, and reduced licencing and operational cost.
* Containers are lighter to ship and faster to start than VMs.
* Well aligned to the devOps model of automation and shipping infrastructure as code, and multiple staging environments.
* Simplifies deployment of granular (micro-service) architectures, and dependency management.

## Challenge ##

* Use Docker
* Pick a coding language that has dependencies (e.g. .net framework, Java runtime ...)

