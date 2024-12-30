# Flood Fill Algorithm 🎨

## 📖 Overview
The Flood Fill algorithm is a technique commonly used in graphics applications, such as the "paint bucket" tool in image editing software. It traverses a region of connected pixels in a 2D image and replaces them with a new color. This project demonstrates a Python implementation of the Flood Fill algorithm using **Breadth-First Search (BFS)**.

---

## 🛠 Features
- Handles a 2D grid representing an image.
- Uses graph traversal techniques to process regions.
- Ensures boundary checks and efficient memory usage with visited tracking.

---

## 🧠 How It Works
1. Start from a specified pixel (`row, col`) in the grid.
2. Use **Breadth-First Search (BFS)** to explore all adjacent pixels with the same starting color.
3. Replace each traversed pixel's color with the new color.
4. Ensure no pixel is visited twice using a `visited` set.

---

## 📂 File Structure
- `flood_fill.py`: Contains the Flood Fill algorithm implementation.
- `README.md`: This file with explanations, examples, and visualizations.

---

## 🚀 Example
### Input Image

```text
1 0 2 2 0
0 0 2 2 0
0 2 2 2 2
0 0 2 0 2
1 0 0 0 0
```

### Function Call
```python
result = flood_fill(image, 2, 2, 9)
```

### Output Image

```text
1 0 9 9 0
0 0 9 9 0
0 9 9 9 9
0 0 9 0 9
1 0 0 0 0
```

---


## 📋 Why This Approach?
- **Breadth-First Search (BFS)** ensures we traverse level by level, minimizing stack overflow issues compared to Depth-First Search (DFS).
- We use helper functions for modularity:
  - `get_neighbors`: Finds valid neighbors of a pixel.
  - `is_valid_pixel`: Checks if a pixel lies within the grid boundaries.

---



## 🌟 Contributions
Feel free to fork this repository, suggest improvements, and submit pull requests. Let's make it better together! 🚀

---


