# Lempel-Ziv-Data-compression-technique

## Overview
This project implements the **Lempel-Ziv (LZ) data compression algorithm** in Python. The Lempel-Ziv algorithm is a lossless data compression technique widely used in file compression formats such as ZIP and PNG.  

This implementation:
- Reads an input string from a file (`text.txt`) or user input.
- Segments the input string based on repeated patterns.
- Encodes the segments using ASCII and binary representations.
- Generates a **final compressed code word**.

---

## Features
- Handles any plain text input.
- Produces both **ASCII** and **binary encoding** for segments.
- Saves outputs automatically in `results.txt`.
- Modular and easy to extend for larger datasets.

---

## Getting Started

### Prerequisites
- Python 3.x
- Optionally, VS Code or any Python IDE

