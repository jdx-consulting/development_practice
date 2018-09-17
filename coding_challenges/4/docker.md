# Containerisation #

## What is it? ##

Containers are an abstraction at the app layer that packages code and dependencies together. Multiple containers can run on the same machine and share the OS kernel with other containers, each running as isolated processes in user space. Containers take up less space than VMs (container images are typically tens of MBs in size), can handle more applications and require fewer VMs and Operating systems.

## What are the advantages? ##

* Because the OS is shared there is less load on the host machine, and reduced licencing and operational cost.
* Containers are lighter to ship and faster to start than VMs.
* Well aligned to the devOps model of automation and shipping infrastructure as code, and multiple staging environments.
* Simplifies deployment of granular (micro-service) architectures, and dependency management.

## Challenge ##

* Pick a coding language that has dependencies (e.g. .net framework, Java runtime ...)
  * Code an application that writes an environment configured message ```ENV_MSG```, to /logs/, at an environment configured interval ```ENV_DELAY```.
  * Exceptions should be written to /logs/errors
  * If the configured message ```ENV_MSG``` is missing, or the configured interval ```ENV_DELAY``` is missing (or < 0 or > 60), then log an error and exit.
* Using Docker create an image that:
  * Contains the application and all it's dependencies.
  * Uses volume mapping, at runtime, to link the /logs/ path in the container to a logging path on the host.
  * Uses environment variables, at runtime, to set:
    * A message to be logged ```ENV_MSG```.
    * The interval, in secs, between log messages ```ENV_DELAY```.
  * Commit the image to this repo with instructions for running.

