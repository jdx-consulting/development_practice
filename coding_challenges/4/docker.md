# Containerisation #

## What is it? ##

Containers are an abstraction at the app layer that packages code and dependencies together. Multiple containers can run on the same machine and share the OS kernel with other containers, each running as isolated processes in user space. Containers take up less space than VMs (container images are typically tens of MBs in size), can handle more applications and require fewer VMs and Operating systems.

## What are the advantages? ##

* Because the OS is shared there is less load on the host machine, and reduced licencing and operational cost.
* Containers are lighter to ship and faster to start than VMs.
* Well aligned to the devOps model of automation and shipping infrastructure as code, and multiple staging environments.
* Simplifies deployment of granular (micro-service) architectures, and dependency management.

## Challenge ##

Build a containerised solution consisting of 2 services.
Use a coding language that has dependencies (e.g. .net framework, Java runtime ...).

* Service 1 - ```Ping```
  * Periodically pings the Pong service with a simple text string ```PING```.
  * Interval between pings according to environment configured interval ```ENV_DELAY```.
  * Pong service endpoint according to environment configured url ```ENV_PONG_AT```.
  * Exposes a Ping endpoint
    * Ping service endpoint according to environment configured url ```ENV_PING_AT```.
    * On receipt of a ```PONG``` post to the endpoint, writes the received text string to /logs/[service name]/[env stage]/audit
* Service 2 - ```Pong```
  * Exposes a Pong endpoint
    * Pong service endpoint according to environment configured url ```ENV_PONG_AT```.
    * On receipt of a ```PING``` post to the endpoint
      * Writes the received text string to /logs/[service name]/[env stage]/audit
      * Pongs the Ping service with a simple text string ```PONG```.
   
Exceptions should be written to /logs/[service name]/[env stage]/errors.

* Using Docker create images for the ```Ping``` and ```Pong``` services
  * Contains the application and all it's dependencies.
  * Uses volume mapping, at runtime, to link the /logs/ path in the container to a logging path on the host.
  * Uses environment variables, at runtime, to set: 
    * ```ENV_DELAY``` ```ENV_PONG_AT``` for ```Ping``` service.
    * ```ENV_PING_AT``` for the ```Pong``` service.
    * ```ENV_STAGE``` (DEV or QA) for both services.
  * Commit the images to this repo with instructions for downloading.
* Using Docker Compose create comfiguration to stand up a DEV or QA instance of the solution. 
  * Commit the compose yaml to this repo, with instructions for running a DEV or QA instance locally.

