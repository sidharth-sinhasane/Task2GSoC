import random

def estimate_pi(num_samples=1000000):
    inside_circle = 0

    for _ in range(num_samples):
        x, y = random.uniform(0, 1), random.uniform(0, 1)  # Generate random (x, y)
        if x**2 + y**2 <= 1:  # Check if inside quarter-circle
            inside_circle += 1

    return 4 * (inside_circle / num_samples)

pi_estimate = estimate_pi()
print(f"Estimated π: {pi_estimate}")
