# Autonomous Self-Driving Car Simulation using CARLA 

## 🚗 Overview
This project sets up an **autonomous self-driving car simulation** using the **CARLA simulator (v0.9.15)** and **Python** on **Windows 10**. The vehicle spawns in the CARLA environment and drives autonomously using the built-in autopilot feature.

---
## 🛠 Prerequisites
### 1️⃣ Install CARLA 0.9.15
1. Download CARLA 0.9.15 from [CARLA Releases](https://github.com/carla-simulator/carla/releases/tag/0.9.15)
2. Extract it to a suitable directory, e.g., `C:\CARLA_0.9.15`
3. Open **Command Prompt** and navigate to the CARLA folder:
   ```sh
   cd C:\CARLA_0.9.15
   ```
4. Run the simulator:
   ```sh
   CarlaUE4.exe -windowed -ResX=800 -ResY=600 -carla-server
   ```
   Keep this window open; it runs the Unreal Engine simulation.

### 2️⃣ Install Dependencies
1. Open **PowerShell** or **cmd** and create a Python virtual environment:
   ```sh
   python -m venv carla-env
   carla-env\Scripts\activate  # Activate virtual environment
   ```
2. Install required Python packages:
   ```sh
   pip install carla==0.9.15 numpy pygame
   ```

### 3️⃣ Install Required System Components
✅ **DirectX Runtime**: [Download Here](https://www.microsoft.com/en-us/download/details.aspx?id=35)  
✅ **Visual C++ Redistributables**: [Download Here](https://aka.ms/vs/17/release/vc_redist.x64.exe)

---
## 🚦 Running the Simulation
1. Ensure **CARLA is running** (`CarlaUE4.exe`).
2. Run the Python script to spawn an autonomous vehicle:
   ```sh
   python main.py
   ```
3. The Tesla Model 3 should spawn and start driving autonomously.

---

### **Error: Python Module Not Found (`carla`)**
Ensure CARLA Python API is installed:
```sh
pip install carla
```

---
## 🎯 Future Enhancements
- ✅ Add **LIDAR and camera sensors** for perception
- ✅ Implement **Deep Learning-based path planning**
- ✅ Use **Reinforcement Learning (RL)** for autonomous control

---
## 📌 References
- [CARLA Documentation](https://carla.readthedocs.io/)
- [CARLA GitHub Repository](https://github.com/carla-simulator/carla)


