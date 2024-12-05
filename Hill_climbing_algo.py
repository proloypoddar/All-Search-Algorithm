# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# # Generate a complex hill-like graph
# def generate_complex_hill(size=100):
#     x = np.linspace(-5, 5, size)
#     y = np.linspace(-5, 5, size)
#     x, y = np.meshgrid(x, y)
    
#     # Base hill with a global maximum
#     z = np.exp(-(x**2 + y**2))
    
#     # Add local maxima
#     z += 0.5 * np.exp(-((x - 3)**2 + (y - 3)**2))  # Local maximum
#     z += 0.4 * np.exp(-((x + 2)**2 + (y + 2)**2))  # Another local maximum
    
#     # Add a flat region
#     z += (np.abs(x) < 1) * (np.abs(y) < 1) * 0.2  # Flat region near the center
    
#     # Add a ridge
#     z += 0.3 * np.exp(-((y)**2)) * (np.abs(x) < 0.5)  # Ridge along y-axis
    
#     return x, y, z

# # Hill Climbing Algorithm with logging
# def hill_climbing_with_logging(x, y, z, start):
#     current_pos = start
#     path = [current_pos]
    
#     def get_neighbors(pos):
#         neighbors = []
#         x, y = pos
#         for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             neighbors.append((x + dx, y + dy))
#         return neighbors

#     def heuristic(pos):
#         i, j = pos
#         return z[i, j] if 0 <= i < z.shape[0] and 0 <= j < z.shape[1] else -np.inf

#     step = 0
#     while True:
#         step += 1
#         yield current_pos, path, step  # Yield for visualization
#         neighbors = get_neighbors(current_pos)
#         best_neighbor = max(neighbors, key=heuristic)
#         if heuristic(best_neighbor) <= heuristic(current_pos):
#             break  # Stop at local maximum or flat region
#         current_pos = best_neighbor
#         path.append(current_pos)
    
#     yield current_pos, path, step  # Final position

# # Visualization with step annotations
# def visualize_complex_hill_steps(x, y, z, start):
#     fig = plt.figure(figsize=(12, 8))
#     ax = fig.add_subplot(111, projection='3d')
#     ax.plot_surface(x, y, z, cmap='viridis', alpha=0.8)
    
#     path_gen = hill_climbing_with_logging(x, y, z, start)
#     path = []
    
#     for current_pos, path, step in path_gen:
#         px, py = [], []
#         for i, j in path:
#             px.append(x[i, 0])
#             py.append(y[0, j])
#         pz = [z[i, j] for i, j in path]
        
#         ax.clear()
#         ax.plot_surface(x, y, z, cmap='viridis', alpha=0.8)
        
#         # Plot the path so far
#         ax.plot(px, py, pz, color='red', marker='o', markersize=5, label='Path')
#         ax.scatter(px[0], py[0], pz[0], color='blue', label='Start Point')
#         ax.scatter(px[-1], py[-1], pz[-1], color='green', label='Current Point')
        
#         # Add annotation for each step
#         annotation = f"Step: {step}\nCurrent Pos: {current_pos}\nHeuristic: {z[current_pos]}"
#         ax.text2D(0.05, 0.95, annotation, transform=ax.transAxes, fontsize=12, color='black', bbox=dict(boxstyle="round", alpha=0.5))
        
#         ax.set_title("Hill Climbing with Local Maxima, Flat Regions, and Ridges")
#         ax.set_xlabel("X-axis")
#         ax.set_ylabel("Y-axis")
#         ax.set_zlabel("Z-axis")
#         ax.legend()
#         plt.pause(0.8)  # Pause to show each step

#     plt.show()

# # Main execution
# if __name__ == "__main__":
#     size = 50
#     x, y, z = generate_complex_hill(size)
    
#     # Random starting point
#     start = (np.random.randint(0, size), np.random.randint(0, size))
#     print(f"Starting Position: {start}")
    
#     # Visualization with steps
#     visualize_complex_hill_steps(x, y, z, start)
######################################################
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate a hill graph with local maxima and flat regions
def generate_complex_hill(size=100):
    x = np.linspace(-5, 5, size)
    y = np.linspace(-5, 5, size)
    x, y = np.meshgrid(x, y)

    z = np.exp(-(x**2 + y**2))  # Global maximum
    z += 0.5 * np.exp(-((x - 3)**2 + (y - 3)**2))  # Local maximum
    z += 0.4 * np.exp(-((x + 2)**2 + (y + 2)**2))  # Another local maximum
    z += (np.abs(x) < 1) * (np.abs(y) < 1) * 0.2  # Flat region near the center
    z += 0.3 * np.exp(-((y)**2)) * (np.abs(x) < 0.5)  # Ridge along y-axis
    return x, y, z

# Hill Climbing Algorithm
def hill_climbing_with_goal(x, y, z, start, goal):
    current_pos = start
    path = [current_pos]

    def get_neighbors(pos):
        neighbors = []
        i, j = pos
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbors.append((i + di, j + dj))
        return neighbors

    def heuristic(pos):
        i, j = pos
        return z[i, j] if 0 <= i < z.shape[0] and 0 <= j < z.shape[1] else -np.inf

    step = 0
    while True:
        step += 1
        yield current_pos, path, step  # Yield state for visualization
        if current_pos == goal:
            break  # Reached goal
        
        neighbors = get_neighbors(current_pos)
        best_neighbor = max(neighbors, key=heuristic)
        
        if heuristic(best_neighbor) <= heuristic(current_pos):
            # Handle local maximum or flat region
            if np.isclose(heuristic(best_neighbor), heuristic(current_pos), atol=1e-3):
                event = "Flat Region"
            else:
                event = "Local Maximum"
            yield current_pos, path, step, event
            break

        current_pos = best_neighbor
        path.append(current_pos)
    
    yield current_pos, path, step, "Goal Reached"  # Final state

# Visualization
def visualize_hill_climbing(x, y, z, start, goal):
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis', alpha=0.8)
    
    path_gen = hill_climbing_with_goal(x, y, z, start, goal)
    path = []

    for step_data in path_gen:
        if len(step_data) == 4:
            current_pos, path, step, event = step_data
        else:
            current_pos, path, step = step_data
            event = None

        px, py, pz = [], [], []
        for i, j in path:
            px.append(x[i, 0])
            py.append(y[0, j])
            pz.append(z[i, j])

        ax.clear()
        ax.plot_surface(x, y, z, cmap='viridis', alpha=0.8)
        
        # Plot path
        ax.plot(px, py, pz, color='red', marker='o', label='Path')
        ax.scatter(px[0], py[0], pz[0], color='blue', label='Start Point', s=100)
        ax.scatter(x[goal[0], 0], y[0, goal[1]], z[goal[0], goal[1]], color='green', label='Goal Point', s=100)
        ax.scatter(px[-1], py[-1], pz[-1], color='yellow', label='Current Position', s=100, edgecolors='black')

        # Title update with step and events
        title = f"Hill Climbing | Step {step}"
        if event:
            title += f" | {event}"
        ax.set_title(title)
        
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.set_zlabel("Z-axis")
        ax.legend()
        plt.pause(0.8)

    plt.show()


if __name__ == "__main__":
    size = 50
    x, y, z = generate_complex_hill(size)
    

    start = (np.random.randint(0, size), np.random.randint(0, size))
    goal = (size // 2, size // 2)  
    print(f"Starting Position: {start}")
    print(f"Goal Position: {goal}")
    

    visualize_hill_climbing(x, y, z, start, goal)
