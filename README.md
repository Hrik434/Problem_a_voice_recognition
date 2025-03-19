# Problem A - Voice Recognition for TurtleBot3 

## Overview  

This project implements a **voice-assisted control system** for **TurtleBot3** using ROS Noetic. The system consists of two main Python nodes:  

- **Control_Node.py**: Handles movement and energy tracking.  
- **Speaker__Node.py**: Listens for voice commands and sends them to the control node.  

## Running the Nodes  

### 1. Control_Node.py (ROS Noetic)  
This node must be run inside the **Docker container** or **Linux (ROS Noetic)** environment.  

### 2. Speaker__Node.py (Windows PowerShell)  
This node must be run on **Windows PowerShell**.  

## Dependencies  

### Dependencies for Speaker__Node.py (Windows PowerShell)  

Before running `Speaker__Node.py`, install the required dependencies:  

1. Open **PowerShell as Administrator**.  
2. Run the following commands:  

   ```powershell
   python -m pip install --upgrade pip
   pip install websocket-client SpeechRecognition pyaudio
3. After installing dependencies, navigate to the script’s directory and run the script:

   cd path\to\script\directory
   python Speaker__Node.py

