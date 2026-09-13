# Algorithm Visualizer

An interactive algorithm visualizer built in **Python** that allows users to create graphs and observe algorithms as they execute step-by-step.

The project was designed to make algorithmic behaviour easier to understand while providing practical experience with **data structures, algorithms, state management, and interactive application design**.

## Overview

The visualizer represents a graph using nodes and edges and provides an interactive environment for experimenting with graph algorithms.

Rather than displaying only the final result, the application updates the graph as an algorithm executes, allowing users to see how the algorithm explores and modifies the graph at each stage.

## Features

* Interactive graph creation
* Node and edge manipulation
* Visual representation of algorithm execution
* Step-by-step algorithm progression
* Dynamic graph state updates
* User interaction with graph elements
* Separation between algorithmic logic and visualisation

## Technologies

* **Python**
* **Data Structures & Algorithms**
* **Graph Theory**
* **Object-Oriented Programming**

## Project Structure

```text
alg-visualizer/
├── algorithms/       # Algorithm implementations
├── graph/            # Graph, node and edge structures
├── interaction/      # User interaction and controls
├── state/            # Application and graph state
└── README.md
```

## How It Works

The application maintains a graph consisting of nodes and edges and updates its state as an algorithm executes.

The general execution flow is:

1. Create or modify a graph using the interactive interface.
2. Select an algorithm to run on the graph.
3. Initialise the algorithm's state.
4. Execute the algorithm incrementally.
5. Update the graph state after each step.
6. Visually represent the algorithm's progress.

This approach allows the user to observe not only the final output, but also the intermediate states produced during execution.

## Data Structures

The project uses graph-based data structures to represent relationships between nodes.

Nodes store information about individual vertices, while edges represent connections between them. The separation of these structures allows algorithms to operate on the graph independently of the visualisation layer.

## Algorithms

The visualizer provides an environment for implementing and demonstrating graph algorithms.

Each algorithm is implemented separately from the visualisation and interaction code, allowing new algorithms to be added without significantly changing the rest of the application.

## Design

The project separates the main responsibilities of the application into different components:

```text
User Interaction
       │
       ▼
Graph State
       │
       ▼
Algorithm
       │
       ▼
State Updates
       │
       ▼
Visualisation
```

This separation makes it possible to run an algorithm independently of how its results are displayed.

## Running the Project

Clone the repository:

```bash
git clone https://github.com/mo-b1/alg-visualizer.git
cd alg-visualizer
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

> The exact entry point may vary depending on the current project configuration.

## What I Learned

This project strengthened my understanding of **graph data structures, algorithm design, state management, and object-oriented programming**.

Building the visualisation also required thinking about how an algorithm's internal state can be represented and updated incrementally, rather than simply calculating a final result.

 Improving visual feedback for different algorithm states
