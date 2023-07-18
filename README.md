# SpeedCheck
A simple Internet speed monitoring application with a client-server architecture.

The client application runs on the host machine and measures the download and upload speeds of the Internet connection.
It then sends this data to the server.

The server application runs on AWS and receives the speed data from the client.
It stores the data in a database and displays a dashboard with graphs showing the speed over time.

This allows the user to monitor and track changes in their Internet connection speed.

### Features

- Measures download and upload speeds using speedtest-cli API
- Sends speed data from client to server
- Stores speed data in a database (MySQL)
- Displays a dashboard with graphs of speed over time using Flask
- Runs client on host machine and server on AWS EC2 instance

### Technologies Used

- Python 3
- speedtest-cli library
- MySQL
- Flask
- AWS EC2

### Getting Started

Clone this repository and follow the instructions in the README files within the client and server folders to
set up and run the application.

### Setting up the development environment

To set up the project for development follow the instructions in the repository `wiki` page.
https://github.com/eugene-chekan/SpeedCheck/wiki
