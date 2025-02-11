import carla
import time

# CARLA server
client = carla.Client('localhost', 2000)
client.set_timeout(5.0)

# World & blueprint 
world = client.get_world()
blueprint_library = world.get_blueprint_library()

# Vehicle 
vehicle_bp = blueprint_library.filter('model3')[0]  # Tesla Model 3

# Spawn point
spawn_points = world.get_map().get_spawn_points()
spawn_point = spawn_points[0]

# Spawn vehicle
vehicle = world.spawn_actor(vehicle_bp, spawn_point)

time.sleep(2)

# Autopilot
vehicle.set_autopilot(True)

print("Autonomous vehicle is driving...")
time.sleep(30)  # 30s

# End 
vehicle.destroy()
print("Simulation ended.")
