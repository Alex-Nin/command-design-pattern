# Command Pattern Database System

This Python project demonstrates the Command design pattern through a database management system. Commands encapsulate operations (such as add, update, and remove) on a Database object, allowing for actions to be executed and undone, enabling a flexible command history system.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Project Overview](#project-overview)
4. [Key Features](#key-features)
5. [Purpose and Lessons Learned](#purpose-and-lessons-learned)

## Installation

To set up and run this project locally:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/alex-nin/command-design-pattern.git
   cd command-design-pattern
   ```
2. **Install Dependencies:** Ensure you have Python 3.x installed.

## Usage

To run the program, execute the following command in your terminal in the program directory, depending on your Python environment:

```bash
python command.py
```
or
```bash
python3 command.py
```

This program simulates command executions for adding, updating, and removing entries in a database. Commands can be undone, demonstrating the flexibility of the Command pattern.

## Project Overview

The main components include:
- **Database:** This class represents a simple key-value store database with operations to add, update, retrieve, remove, and display entries.
- **Command Interface:** An abstract base class defining the structure for executing and undoing commands.
- **Concrete Commands**: Each command implements specific database operations. The `AddCommand`, `UpdateCommand`, and `RemoveCommand` classes encapsulate these operations, including the ability to undo changes.
- **Invoker:** A part of the system that issues commands and can reverse them through undo() calls.

## Key Features

- **Command Encapsulation:** Each database operation is encapsulated in a command, allowing the system to execute commands independently and consistently.
- **Undo Functionality:** Commands can be undone, enabling reversible operations in the database, useful for features like undo stacks.
- **Flexible Command Execution:** New commands can be added without changing existing code, enhancing the system's extensibility.
- **Separation of Concerns:** The Command pattern decouples command execution from the database, organizing code for clarity and maintainability.

## Purpose and Lessons Learned

Working on this project gave me a practical understanding of the Command design pattern. Implementing database operations as commands helped me see how encapsulating actions as objects improves code flexibility, especially when adding undo functionality. This approach made it easier to modify and expand the system while keeping responsibilities separate, enhancing the maintainability and scalability of the application.
