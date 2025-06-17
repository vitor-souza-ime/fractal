Fractal Visualization 🌌
 
A Python project to generate and visualize stunning fractals using NumPy and Matplotlib. Explore the beauty of mathematics through the Koch Snowflake, Mandelbrot Set, Fractal Binary Tree, and Dragon Curve.

📜 Overview
This project creates visualizations of four iconic fractals, each showcasing the intricate patterns of recursive mathematics. The script measures computation times and displays the fractals with a clean, minimalistic style. Perfect for learning about fractals, Python, or simply enjoying mathematical art!
Fractals Included

Koch Snowflake: A recursive curve forming a snowflake-like shape.
Mandelbrot Set: A complex plane visualization of iterative quadratic functions.
Fractal Binary Tree: A branching structure mimicking natural tree growth.
Dragon Curve: A twisting curve built from iterative turn sequences.

🚀 Getting Started
Prerequisites

Python 3.8 or higher
Required libraries:pip install numpy matplotlib



Installation

Clone the repository:git clone https://github.com/your-username/fractal-visualization.git


Navigate to the project directory:cd fractal-visualization


Run the script:python fractals.py



🎨 Visualizations
Below are example outputs for N=4 (fractal complexity/depth):



Koch Snowflake
Mandelbrot Set










Fractal Tree
Dragon Curve







Note: Replace placeholder images with actual fractal outputs by saving plots (e.g., plt.savefig('koch_snowflake.png')) and uploading them to your repository.
⚙️ Customization

Fractal Complexity: Modify the N variable in fractals.py to adjust the depth or resolution.
Mandelbrot Settings: Increase mandelbrot_res or mandelbrot_iter for finer details (scales with N).
Plot Styles: Edit Matplotlib parameters (e.g., cmap for Mandelbrot, line colors) for custom aesthetics.

Example console output for N=4:
Koch Snowflake: 0.012 segundos
Mandelbrot Set: 0.245 segundos
Fractal Tree: 0.008 segundos
Dragon Curve: 0.004 segundos

📚 How It Works

Koch Snowflake: Recursively divides line segments, adding equilateral triangles.
Mandelbrot Set: Iterates Z = Z² + C on a complex grid, coloring based on divergence.
Fractal Binary Tree: Recursively draws branches at fixed angles with shrinking lengths.
Dragon Curve: Builds a sequence of turns (L, R) to plot a twisting path.

🛠️ Future Improvements

Add interactive controls for real-time parameter adjustments.
Optimize Mandelbrot computation using Numba or parallel processing.
Export fractals as high-resolution images or animations.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.
🙌 Contributing
Contributions are welcome! Please open an issue or submit a pull request for bug fixes, enhancements, or new fractal implementations.

