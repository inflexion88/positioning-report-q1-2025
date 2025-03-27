import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as mcolors
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
import os

# Create output directory if it doesn't exist
output_dir = "visualization_output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Set up the figure with higher resolution and better quality
plt.rcParams['figure.figsize'] = [12, 10]
plt.rcParams['figure.dpi'] = 100
plt.rcParams['font.size'] = 12
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']

# Define a custom 3D arrow for visualization
class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)

# Create a figure for the 3D visualization
fig = plt.figure(figsize=(12, 10), facecolor='black')
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('black')

# Remove grid and axes for cleaner look
ax.grid(False)
ax.set_axis_off()

# Set the title with better visibility
title = ax.set_title('Gravitational Authority Model', fontsize=20, color='white', y=0.95)

# Create a central "perfect positioning" sphere
center_sphere = ax.scatter([0], [0], [0], s=500, c='#00FF7F', alpha=0.8, edgecolors='white')

# Add a text label for the central sphere with improved visibility
ax.text(0, 0, 0.5, 'Perfect\nPositioning', color='white', fontsize=14, 
        horizontalalignment='center', verticalalignment='bottom', fontweight='bold')

# Define the five dimensions of the Gravitational Authority Model
dimensions = [
    "Perceptual Gravity",
    "Experiential Density",
    "Temporal Consistency",
    "Ecosystem Attraction",
    "Adaptive Resilience"
]

# Create dimension labels with better positioning and visibility
dimension_positions = [
    (2.5, 0, 0),    # Perceptual Gravity
    (0, 2.5, 0),    # Experiential Density
    (0, 0, 2.5),    # Temporal Consistency
    (-2.5, 0, 0),   # Ecosystem Attraction
    (0, -2.5, 0)    # Adaptive Resilience
]

# Add dimension labels with improved visibility
for i, (label, pos) in enumerate(zip(dimensions, dimension_positions)):
    ax.text(pos[0], pos[1], pos[2], label, color='white', fontsize=14, 
            horizontalalignment='center', verticalalignment='center', fontweight='bold',
            bbox=dict(facecolor='black', alpha=0.7, edgecolor='#00FF7F', boxstyle='round,pad=0.5'))

# Define companies with their positioning strengths across the five dimensions
# Format: [name, [perceptual_gravity, experiential_density, temporal_consistency, ecosystem_attraction, adaptive_resilience]]
companies = [
    ["Apple", [0.9, 0.9, 0.9, 0.9, 0.8]],
    ["Tesla", [0.9, 0.8, 0.7, 0.8, 0.9]],
    ["Amazon", [0.8, 0.7, 0.8, 0.9, 0.8]],
    ["Nike", [0.9, 0.7, 0.9, 0.6, 0.7]],
    ["Disney", [0.7, 0.9, 0.9, 0.8, 0.6]],
    ["Airbnb", [0.6, 0.9, 0.5, 0.7, 0.8]],
    ["Coca-Cola", [0.9, 0.6, 0.9, 0.5, 0.6]],
    ["Microsoft", [0.7, 0.6, 0.8, 0.9, 0.8]],
    ["Netflix", [0.8, 0.8, 0.6, 0.7, 0.9]],
    ["Peloton", [0.5, 0.9, 0.4, 0.6, 0.7]]
]

# Calculate positions for companies based on their positioning strengths
company_positions = []
for company in companies:
    # Convert the five dimensions into a 3D position
    # We'll use the first three dimensions directly for x, y, z
    # and use the other two to modify the size and color
    x = company[1][0] * 2.0 - 1.0  # Perceptual Gravity
    y = company[1][1] * 2.0 - 1.0  # Experiential Density
    z = company[1][2] * 2.0 - 1.0  # Temporal Consistency
    
    # Calculate distance from center (0,0,0) - lower is better
    distance = np.sqrt(x**2 + y**2 + z**2)
    
    # Calculate size based on Ecosystem Attraction
    size = 100 + company[1][3] * 200
    
    # Calculate color based on Adaptive Resilience
    # Higher values are greener (better), lower values are redder
    color_value = company[1][4]
    
    company_positions.append({
        'name': company[0],
        'position': (x, y, z),
        'distance': distance,
        'size': size,
        'color_value': color_value
    })

# Sort companies by distance for better layering in visualization
company_positions.sort(key=lambda x: x['distance'])

# Create a custom colormap from red to green
cmap = plt.cm.RdYlGn

# Plot company spheres
company_spheres = []
company_labels = []
for company in company_positions:
    # Plot the company sphere
    sphere = ax.scatter(
        company['position'][0], 
        company['position'][1], 
        company['position'][2],
        s=company['size'],
        c=[cmap(company['color_value'])],
        alpha=0.7,
        edgecolors='white'
    )
    company_spheres.append(sphere)
    
    # Add company name with improved visibility
    label = ax.text(
        company['position'][0], 
        company['position'][1], 
        company['position'][2] + 0.2,
        company['name'],
        color='white',
        fontsize=12,
        horizontalalignment='center',
        verticalalignment='bottom',
        fontweight='bold',
        bbox=dict(facecolor='black', alpha=0.7, edgecolor='white', boxstyle='round,pad=0.2')
    )
    company_labels.append(label)
    
    # Draw a line from the center to each company
    line = ax.plot(
        [0, company['position'][0]],
        [0, company['position'][1]],
        [0, company['position'][2]],
        color='white',
        alpha=0.3,
        linestyle='--'
    )

# Set the viewing limits
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(-3, 3)

# Create a legend explaining the visualization
legend_text = (
    "Sphere Position: Based on Perceptual Gravity, Experiential Density, and Temporal Consistency\n"
    "Sphere Size: Based on Ecosystem Attraction\n"
    "Sphere Color: Based on Adaptive Resilience (Green = High, Red = Low)\n"
    "Distance from Center: Overall Gravitational Authority Strength"
)

# Add the legend with better visibility
fig.text(0.5, 0.02, legend_text, color='white', fontsize=12, 
         horizontalalignment='center', verticalalignment='bottom',
         bbox=dict(facecolor='black', alpha=0.7, edgecolor='#00FF7F', boxstyle='round,pad=0.5'))

# Function to update the plot for each animation frame
def update(frame):
    # Rotate the view
    ax.view_init(elev=20, azim=frame)
    
    # Return all objects that need to be updated
    return [center_sphere] + company_spheres + company_labels

# Create the animation with smooth rotation (360 frames for a full rotation)
# This ensures the model doesn't reset halfway through
frames = 360
ani = FuncAnimation(fig, update, frames=np.linspace(0, 360, frames, endpoint=False), 
                   interval=50, blit=False)

# Save the animation as a GIF with higher quality
ani.save(f'{output_dir}/gravitational_model_3d.gif', writer='pillow', fps=30, dpi=100)

# Save a static image from a good viewing angle
ax.view_init(elev=20, azim=45)
plt.savefig(f'{output_dir}/gravitational_model_static.png', dpi=300, bbox_inches='tight', facecolor='black')

# Create a 2D quadrant visualization
plt.figure(figsize=(12, 10), facecolor='black')
ax2d = plt.subplot(111)
ax2d.set_facecolor('black')

# Set up the quadrant
ax2d.axhline(y=0.5, color='white', linestyle='-', alpha=0.3)
ax2d.axvline(x=0.5, color='white', linestyle='-', alpha=0.3)

# Label the quadrants
plt.text(0.25, 0.75, "Experiential\nAttractors", color='#00BFFF', fontsize=16, 
         horizontalalignment='center', verticalalignment='center', fontweight='bold')
plt.text(0.75, 0.75, "Dominant\nGravitational Forces", color='#00FF7F', fontsize=16, 
         horizontalalignment='center', verticalalignment='center', fontweight='bold')
plt.text(0.25, 0.25, "Emerging\nGravitational Bodies", color='#A9A9A9', fontsize=16, 
         horizontalalignment='center', verticalalignment='center', fontweight='bold')
plt.text(0.75, 0.25, "Perceptual\nAttractors", color='#FFD700', fontsize=16, 
         horizontalalignment='center', verticalalignment='center', fontweight='bold')

# Plot companies in the quadrant
for company in companies:
    # Calculate position
    x = (company[1][0] + company[1][4]) / 2  # Average of Perceptual Gravity and Adaptive Resilience
    y = (company[1][1] + company[1][2]) / 2  # Average of Experiential Density and Temporal Consistency
    
    # Calculate size based on Ecosystem Attraction
    size = 500 + company[1][3] * 1000
    
    # Determine quadrant and color
    if x >= 0.5 and y >= 0.5:
        color = '#00FF7F'  # Green for Dominant Gravitational Forces
    elif x < 0.5 and y >= 0.5:
        color = '#00BFFF'  # Blue for Experiential Attractors
    elif x >= 0.5 and y < 0.5:
        color = '#FFD700'  # Gold for Perceptual Attractors
    else:
        color = '#A9A9A9'  # Gray for Emerging Gravitational Bodies
    
    # Plot the company
    plt.scatter(x, y, s=size, color=color, alpha=0.7, edgecolors='white')
    
    # Add company name
    plt.text(x, y, company[0], color='white', fontsize=12, 
             horizontalalignment='center', verticalalignment='center', fontweight='bold')

# Set the axis labels
plt.xlabel('External Positioning Elements\n(Perceptual Gravity + Adaptive Resilience)', color='white', fontsize=14)
plt.ylabel('Internal Positioning Elements\n(Experiential Density + Temporal Consistency)', color='white', fontsize=14)

# Set the title
plt.title('Gravitational Positioning Quadrants', color='white', fontsize=20)

# Remove ticks for cleaner look
plt.xticks([])
plt.yticks([])

# Add a border around the plot
for spine in ax2d.spines.values():
    spine.set_edgecolor('white')
    spine.set_linewidth(2)

# Save the quadrant visualization
plt.savefig(f'{output_dir}/positioning_quadrants.png', dpi=300, bbox_inches='tight', facecolor='black')

# Create a development pathway visualization
plt.figure(figsize=(14, 8), facecolor='black')
ax_path = plt.subplot(111)
ax_path.set_facecolor('black')

# Define the four phases
phases = [
    "Gravitational Core\nFormation",
    "Gravitational Field\nExpansion",
    "Gravitational\nDominance",
    "Gravitational\nRenewal"
]

# Define key activities for each phase
activities = [
    [
        "Define distinctive positioning",
        "Establish foundational experiences",
        "Develop core messaging",
        "Build initial measurement"
    ],
    [
        "Extend positioning across touchpoints",
        "Develop signature experiences",
        "Build ecosystem partnerships",
        "Establish consistent application"
    ],
    [
        "Shape category definitions",
        "Influence competitor behavior",
        "Develop proprietary metrics",
        "Build organizational capabilities"
    ],
    [
        "Evolve for market conditions",
        "Refresh while maintaining consistency",
        "Expand into adjacent categories",
        "Develop next-gen capabilities"
    ]
]

# Plot the development pathway
for i, phase in enumerate(phases):
    # Calculate position
    x = i * 0.25 + 0.125
    y = 0.5
    
    # Plot the phase circle
    circle = plt.Circle((x, y), 0.1, color='#00FF7F', alpha=0.8)
    ax_path.add_patch(circle)
    
    # Add phase number
    plt.text(x, y, str(i+1), color='black', fontsize=16, 
             horizontalalignment='center', verticalalignment='center', fontweight='bold')
    
    # Add phase name
    plt.text(x, y + 0.15, phase, color='white', fontsize=14, 
             horizontalalignment='center', verticalalignment='bottom', fontweight='bold')
    
    # Add activities
    for j, activity in enumerate(activities[i]):
        plt.text(x, y - 0.15 - j*0.07, f"• {activity}", color='white', fontsize=12, 
                 horizontalalignment='center', verticalalignment='top')
    
    # Add connecting line (except for the last phase)
    if i < len(phases) - 1:
        plt.arrow(x + 0.1, y, 0.15, 0, color='white', width=0.005, head_width=0.02, 
                  head_length=0.02, length_includes_head=True)

# Set the axis limits
plt.xlim(0, 1)
plt.ylim(0, 1)

# Remove ticks for cleaner look
plt.xticks([])
plt.yticks([])

# Set the title
plt.title('Gravitational Authority Development Pathway', color='white', fontsize=20)

# Remove axis spines for cleaner look
for spine in ax_path.spines.values():
    spine.set_visible(False)

# Save the development pathway visualization
plt.savefig(f'{output_dir}/development_pathway.png', dpi=300, bbox_inches='tight', facecolor='black')

print("Visualizations created successfully in the 'visualization_output' directory:")
print("1. gravitational_model_3d.gif - 3D animated model of the Gravitational Authority concept")
print("2. gravitational_model_static.png - Static image of the 3D model")
print("3. positioning_quadrants.png - 2D quadrant visualization of positioning types")
print("4. development_pathway.png - Development pathway for building gravitational positioning")
