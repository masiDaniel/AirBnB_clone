# Airbnb Console Project

## Overview

This project aims to develop a console application for managing objects related to an Airbnb clone. The console serves as the first step towards managing Airbnb objects effectively, providing functionalities for creating, retrieving, updating, and deleting objects.

This project marks the initial phase of developing a full-fledged web application. The functionalities and structures implemented here will serve as the foundation for subsequent projects, including HTML templating, database storage, API development, front-end integration, etc.

## Project Structure

The project follows a structured approach with the following key steps:

1. **BaseModel Creation**: A parent class named BaseModel is created to handle the initialization, serialization, and deserialization of future instances.

2. **Serialization/Deserialization Flow**: Establishing a simple flow of serialization/deserialization between instances, dictionaries, JSON, strings, and files.

3. **Class Creation**: Creation of classes representing various Airbnb objects such as User, State, City, and Place, all inheriting from the BaseModel class.

4. **Storage Engine Development**: Implementation of the first abstracted storage engine for the project, starting with file storage.

5. **Unit Testing**: Creation of comprehensive unit tests to validate the functionality of all classes and the storage engine.

## Command Interpreter

The console application functions as a command interpreter, similar to the Shell but tailored for managing objects specific to the project. The main functionalities include:

- **Object Creation**: Creating new objects such as User, Place, etc.
- **Object Retrieval**: Retrieving objects from files, databases, etc.
- **Object Operations**: Performing operations on objects, such as counting, computing stats, etc.
- **Attribute Updates**: Updating attributes of existing objects.
- **Object Deletion**: Deleting objects from the system.

## Next Steps

- Further expansion of functionalities to accommodate the requirements of the Airbnb clone project.
- Integration with HTML templates for web interface development.
- Implementation of database storage for persistent data management.
- Development of APIs for external interactions.
- Integration of front-end components for user interaction.

This README serves as an introduction to the Airbnb Console project, providing an overview of its objectives, structure, and functionalities. Further documentation and detailed instructions can be found within the project files.
