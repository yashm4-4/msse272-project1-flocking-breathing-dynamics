import numpy as np
import matplotlib.pyplot as plt
import imageio
import os

# -----------------------------------------------------
# Initialization
# -----------------------------------------------------
def initialize_particles(N, box_size):
    x = np.random.uniform(-box_size, box_size, N)
    y = np.random.uniform(-box_size, box_size, N)
    vx = np.random.normal(0, 1, N)
    vy = np.random.normal(0, 1, N)
    masses = np.random.uniform(1, 10, N)
    return x, y, vx, vy, masses

# -----------------------------------------------------
# Force calculation
# -----------------------------------------------------
def compute_forces(x, y, c):
    Fx = -c * x**2 * np.sign(x)
    Fy = -c * y**2 * np.sign(y)
    return Fx, Fy

# -----------------------------------------------------
# Integration (semi-Verlet)
# -----------------------------------------------------
def update_positions(x, y, vx, vy, Ax, Ay, dt):
    vx = vx + Ax * dt
    vy = vy + Ay * dt
    x = x + vx * dt + 0.5 * Ax * dt**2
    y = y + vy * dt + 0.5 * Ay * dt**2
    return x, y, vx, vy

# -----------------------------------------------------
# Save frame
# -----------------------------------------------------
def save_frame(x, y, masses, step, folder):
    # Save frames for GIF building only
    path = os.path.join(folder, f"frame_{step:05d}.png")

    plt.figure(figsize=(6, 6))
    plt.scatter(x, y, s=masses, alpha=0.5)
    plt.title(f"Iteration {step}")
    plt.xlim(-150, 150)
    plt.ylim(-150, 150)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.savefig(path, dpi=130)
    plt.close()

# -----------------------------------------------------
# GIF builder
# -----------------------------------------------------
def build_gif(folder):
    frames = sorted(f for f in os.listdir(folder) if f.endswith(".png"))
    images = [imageio.imread(os.path.join(folder, f)) for f in frames]
    gif_path = os.path.join(folder, "simulation.gif")
    imageio.mimsave(gif_path, images, duration=0.06)

    # Clean up frames
    for f in frames:
        os.remove(os.path.join(folder, f))

    print(f"GIF saved → {gif_path}")
    print("Frame images cleaned up.")

# -----------------------------------------------------
# Main simulation
# -----------------------------------------------------
def simulate(N=200, c=0.001, dt=1e-3, iterations=100000, interval=100, box_size=100):
    folder = "results"
    os.makedirs(folder, exist_ok=True)

    x, y, vx, vy, masses = initialize_particles(N, box_size)

    for step in range(iterations):
        Fx, Fy = compute_forces(x, y, c)
        Ax = Fx / masses
        Ay = Fy / masses

        x, y, vx, vy = update_positions(x, y, vx, vy, Ax, Ay, dt)

        if step % interval == 0:
            save_frame(x, y, masses, step, folder)

    build_gif(folder)

if __name__ == "__main__":
    simulate()
