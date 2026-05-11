# Currency Converter

A lightweight, optimized Python script for currency conversion. 

## Core Architecture
This converter avoids the computational and storage overhead of an `O(N^2)` direct-pair matrix. Instead, it utilizes a **hub-and-spoke model** with USD acting as the central pivot. 

By storing only the exchange rates relative to USD in a Python dictionary, the script achieves `O(1)` instantaneous rate retrieval. Any cross-currency conversion (e.g., EUR to JPY) is calculated dynamically by routing through the USD base rate.

## Features
* **Optimized Data Structure:** Dictionary-based mapping ensures maximum execution speed.
* **Hub-and-Spoke Logic:** Calculates cross-rates on the fly, keeping the codebase minimal and easy to update.
* **Strict Input Validation:** Actively intercepts and rejects unsupported or malformed currency codes, preventing runtime errors.
* **Zero Dependencies:** Pure Python implementation requiring no external libraries.

## Usage
1. Clone the repository to your local machine.
2. Execute the script via terminal:
   ```bash
   python converter.py
