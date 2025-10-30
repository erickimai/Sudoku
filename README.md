# 🧩 Sudoku Solver in Python

A Sudoku puzzle solver implemented in **Python** using the **Backtracking algorithm**.  
This project was developed as part of my university coursework to explore recursion, search algorithms, and problem-solving strategies.

---

## 🚀 Features

- Solves any valid 9×9 Sudoku puzzle.
- Uses an optimized **backtracking search**.
- Validates Sudoku constraints:
  - Each number (1–9) appears only once per row, column, and 3×3 subgrid.
- Can handle partially filled boards (reads from lists or text files).
- Clear, modular code for educational and demonstrative purposes.

---

## 🧠 Algorithm Overview

This solver uses a **Depth-First Search (DFS)** approach with **backtracking**:

1. Find the next empty cell.  
2. Try placing digits `1–9` that satisfy Sudoku constraints.  
3. Recursively continue with the next cell.  
4. If no valid number fits, **backtrack** and try a new path.

This ensures all possibilities are explored until a valid board configuration is found.

---

## 📂 Project Structure

