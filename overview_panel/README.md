# Bsread source overview panel
The goal of this project is to provide the beamline scientists with the current status of the sources they need to record while running an experiment.

This project is to be implemented in Python (3.6), using Flask and [Dash](https://plot.ly/products/dash/).

Please use this git repository for your source code. It is expected from your project:

- To have a README.md with clear instructions on how to build and run your code. Additional insight into your project are also welcome. As a minimum it should also include the configuration instructions and how to do the most common tasks that need to be performed on your project.
- To generate an anaconda package to be later deploy into production. All dependencies should also be managed by Anaconda.
- To have an automated build on Travis.
- To have meaningful unit tests.
- To have at least basic performance tests.

## Background
The SwissFEL data acquisition happens over bsread. Bsread is a protocol and library based on zmq. All data transferred over bsread is correlated to pulse ids - you know exactly for which machine shot the value was colleted.

All bsread sources are collected together in the dispatching layer. This is a server that aggregates all sources and writes them to disk for long term storage.

Users can access data live - subscribe to a stream from the dispatching layer, that send them the requested data as soon as it receives it, or they can access data after it has been written to disk - requesting a range of pulses or time.

Currently experiments access data after it has been written to disk. 1 minute after the experiment has finished, the data is collected from the dispatching layer and written into an experiment file. The data in this file is later used to calibrate the experiment data, so it is very important that the requested data is actually available.

## Problem
Because of the large number of sources and big volume of data, all kind of problems can happen in the data acquisition system. Scientists currently have no way of knowing if channels they need to calibrate their data are actually being recorded and will be later available for calibration.

Once the experiment is finished they collect data from the dispatching layer and see if the channels they need are present. This is a problem, because if they knew in advance that the data will not be there, they might not even start the experiment. They cannot properly calibrate the experiment, so the experiment results might be inconclusive.

## Proposed solution
A web based overview panel, where users can add channels they need for the particular experiment they are conducting, that shows live the status of this channels and alerts the users when there is a problem with one of the sources. The users can then decide if they want to continue with the experiment or stop and contact someone for fixing the problem.

# Your task
Create a web based interface, where users can add any channel they want. After they added the channels, the interface will show them if their channels are currently being recorded and if any channel has some problems.

How to get this info for the channels the user selected? You can talk with Fabian about this - he will be the best to advise you on how to do that efficiently.

Your web application will probably run continuously as a status panel on one of the screens in the control room, so it should be designed in a way that users are capable of seeing the status at a distance.

Once this functionality is completed, you can continue by adding the possibility to save the current channel configuration, and later retrieve it. The same kind of experiemnts usually need the same channels, so having a possibility to store them will come usuful.

# Requested features
- Have a Python REST API to access the data.
