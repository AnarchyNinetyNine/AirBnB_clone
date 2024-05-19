# AirBnB Clone - The Console

## Description

This project is a clone of the AirBnB website, focusing on the backend functionality of the application. The goal of the project is to create a command-line interpreter that allows users to create, update, delete, and retrieve objects from a storage system. The project is built in Python and utilizes JSON for data serialization.

## Command Interpreter

The command interpreter is a shell-like tool that allows users to interact with the backend of the AirBnB clone. It provides several commands to manage the application's data models.

### How to Start It

1. Clone the repository:
    ```bash
    git clone https://github.com/AnarchyNinetyNine/AirBnB_clone.git
    ```
2. Navigate to the project directory:
    ```bash
    cd AirBnB_clone
    ```
3. Start the command interpreter:
    ```bash
    ./console.py
    ```

### How to Use It

The command interpreter supports several commands:

- `create <class name>`: Creates a new instance of the specified class and prints its id.
- `show <class name> <id>`: Prints the string representation of an instance based on the class name and id.
- `destroy <class name> <id>`: Deletes an instance based on the class name and id.
- `all [class name]`: Prints all string representations of instances, optionally filtered by class name.
- `update <class name> <id> <attribute name> "<attribute value>"`: Updates an instance based on the class name and id by adding or updating an attribute.

### Examples

- Create a new `BaseModel` instance:
    ```bash
    (hbnb) create BaseModel
    3f157223-ed8e-41f4-ae60-2111939f148a
    ```

- Show a `BaseModel` instance:
    ```bash
    (hbnb) show BaseModel 3f157223-ed8e-41f4-ae60-2111939f148a
    [BaseModel] (3f157223-ed8e-41f4-ae60-2111939f148a) {'id': '3f157223-ed8e-41f4-ae60-2111939f148a', 'created_at': '2024-05-18T09:09:36.247538', 'updated_at': '2024-05-18T09:09:36.248065'}
    ```

- Update a `BaseModel` instance:
    ```bash
    (hbnb) update BaseModel 3f157223-ed8e-41f4-ae60-2111939f148a name "New Name"
    (hbnb) show BaseModel 3f157223-ed8e-41f4-ae60-2111939f148a
    [BaseModel] (3f157223-ed8e-41f4-ae60-2111939f148a) {'id': '3f157223-ed8e-41f4-ae60-2111939f148a', 'created_at': '2024-05-18T09:09:36.247538', 'updated_at': '2024-05-18T09:09:36.248065', 'name': 'New Name'}
    ```

- Delete a `BaseModel` instance:
    ```bash
    (hbnb) destroy BaseModel 3f157223-ed8e-41f4-ae60-2111939f148a
    (hbnb) show BaseModel 3f157223-ed8e-41f4-ae60-2111939f148a
    ** no instance found **
    ```

## Contributors

Please see the `AUTHORS` file for a list of contributors.

---
