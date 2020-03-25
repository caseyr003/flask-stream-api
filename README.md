# Publishing Messages to Oracle Cloud Infrastructure Streaming Service

This project contains a flask application with an endpoint that demonstrates pushing mock data to an oci stream using the oci python sdk.

## Built With

* [Python 3](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Oracle Cloud Infrastructure Streaming](https://www.oracle.com/big-data/streaming/)

## Prerequisites

You will need the following things properly installed on your computer:

* [Git](http://git-scm.com/)
* [Oracle Cloud Python SDK](https://docs.cloud.oracle.com/en-us/iaas/Content/API/SDKDocs/pythonsdk.htm)

## Installation

* run `git clone https://github.com/caseyr003/flask-stream-api.git`

## Setup

* update the `stream_config_example.py` file with your Oracle Cloud Infrastructure account configuration and Streaming Service details

## Running

To run the project locally follow the following steps:

* change into the project directory
* `python app.py`

## JSON API

The JSON API has sample endpoints to start development

* `http://localhost:5001/api/v1/publish`
(Post request that publishes a random JSON object to the stream)