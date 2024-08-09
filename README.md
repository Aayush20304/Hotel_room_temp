# Hotel_room_temp
 
 # IoT Temperature Monitoring Solution

This repository contains a Python-based IoT solution designed for a hotel chain to monitor and maintain optimal room temperature. The solution involves a Publisher Program that simulates temperature sensor data and sends it to an MQTT broker, a Subscriber Program that monitors the data for threshold breaches, and a Server Program that exposes the sensor data via an HTTP API.

## Components

### 1. Publisher Program
A forever executable Python program that reads data from a simulated temperature sensor and publishes it on a specific topic to the MQTT broker every 60 seconds.

### 2. Subscriber Program
A Python program that subscribes to the topic on MQTT, reads the sensor data, compares the data points with a predefined threshold, and saves the data locally. It raises an alarm if the temperature exceeds the threshold continuously for 5 minutes (i.e., 5 data points).

### 3. Server Program
A simple HTTP server built with Flask that exposes the sensor data through an endpoint, returning the last recorded value.

## Installation

### Prerequisites
- Python 3.7+
- MQTT broker (e.g., [Eclipse Mosquitto](https://mosquitto.org/))
- [pip](https://pip.pypa.io/en/stable/)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/iot-temperature-monitoring.git
cd iot-temperature-monitoring
