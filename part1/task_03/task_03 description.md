![images (1)](https://github.com/user-attachments/assets/8406017c-c847-43fd-b88c-d5bc6c3c115f)

# UML HBNB


## introduction

This document provides an in-depth overview of the architecture and design for the HBB project. It brings together essential diagrams, including system architecture, class structures, and API interaction workflows, accompanied by detailed notes that explain the different components and how they interact. The goal of this document is to serve as a clear reference for developers and stakeholders during the development stages, ensuring a unified and well-organized approach to constructing the HBB application.

### High-Level Package Diagram

```mermaid
classDiagram
class PresentationLayer {
    <<Interface>>
    +ServiceAPI
}
class BusinessLogicLayer {
    +User
    +place
    +Review
    +Amenity
}
class PersistenceLayer {
    +DatabaseAccess
}
PresentationLayer --> BusinessLogicLayer : Facade Pattern
BusinessLogicLayer --> PersistenceLayer : Database Operations
```

### Class Diagram Overview

The class diagram illustrates the three-layer architecture of the HBB project:

1- Presentation Layer:

Exposes the ServiceAPI and interacts with the Business Logic Layer via the Facade Pattern, providing a simple interface for users or external services.

2- Business Logic Layer:

Contains key entities such as User, Place, Review, and Amenity. It handles core application logic and communicates with the Persistence Layer for database operations.

3- Persistence Layer:

Manages database access through the DatabaseAccess class, ensuring data transactions are isolated from business logic.

The Facade Pattern and clear separation between layers promote maintainability and simplicity in the system’s design.

# Detailed Class Diagram
```mermaid 
classDiagram
    class User {
    - UUID4 id
    - string first name
    - string last name
    - string email
    - string password
    - DATETIME create_at
    - DATETIME update_at
    + bool verificationConnexion()
    + void create_login()
    + void login()
}
    class Review {
    - UUID4 id
    - string comment
    - string place
    - string user
    + float rating
    + get_review()
    + creat_message()
    + update_message()
    + list_by_places()
}

User "1" --> "*" Review : composition

class Place {
    - UUID4 id
    - string title
    - string description
    + float price
    + float latitude
    + float longitude
    + list review
    + get_review()
    + get_picture()
    + upadate()
    + delete()

}

Place "1" --> "*" Review : receives

class Amenity {
    - UUID4 id
    + string name
    + string description
    + list Amenity
    - DATETIME create_at
    - DATETIME update_at
    + create()
    + update()
    + delete()
}

Place "1" o-- "*" Amenity : Composotion
```
### Detailed Class Diagram overview

User: Manages user data and handles login/verification. Users can write multiple reviews.

Review: Represents reviews with comments, ratings, and associated places.

Place: Describes a location, manages reviews, and links to amenities.

Amenity: Defines features of a place, with methods to create, update, and delete.

Relationships:

User → Review (composition).
Place → Review (receives) and Place → Amenity (composition).

# Sequence Diagrams for API Calls

```mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: Register User
API->>BusinessLogic: Validate and Create a User
BusinessLogic->>Database: Save user in Data
Database-->>BusinessLogic: Confirm Save
BusinessLogic-->>API: Return Succes/Failure
API-->>User: Return registration validation
```

User Registration:

The User sends a registration request to the API.
The API forwards the request to the Business Logic layer to validate and create the user.
The Business Logic then saves the user data in the Database.
Upon confirmation from the Database, the Business Logic returns a success or failure response to the API.
Finally, the API responds to the User with the registration validation outcome.

```mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: Create New Place
API->>BusinessLogic: Validate and Create a Place
BusinessLogic->>Database: Save Place in Data
Database-->>BusinessLogic: Confirm Save
BusinessLogic-->>API: Return Succes/Failure
API-->>User: Return Place creation validation
```

Create New Place:

The User initiates a request to create a new place via the API.
The API sends the request to the Business Logic, which validates and creates the place.
The place data is saved in the Database.
After receiving a confirmation, the Business Logic informs the API of the result.
The API then returns the creation validation to the User.

```mermaid
sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: request a list of places
API->>BusinessLogic: Validate request and Retrieve a list
BusinessLogic->>Database: Research Places
Database-->>BusinessLogic: list of the places
BusinessLogic-->>API: Return Data place
API-->>User: Return displays a list of Places
```

Request List of Places:

The User requests a list of places through the API.
The API communicates with the Business Logic to validate the request and retrieve the list.
The Business Logic queries the Database for the places.
After fetching the data, the Database sends the list back to the Business Logic.
The Business Logic returns the place data to the API, which then displays the list to the User.

# Conclusion

The sequence diagrams presented in this document outline the critical interactions between the User, API, Business Logic, and Database within the HBB project. Each operation, from user registration to creating new places and retrieving lists, illustrates a structured flow of data and validation, ensuring a seamless user experience. By clearly defining these interactions, we promote a robust architecture that supports maintainability, scalability, and ease of integration for future enhancements. This foundational design serves as a roadmap for developers and stakeholders, guiding the implementation of features in the HBB application.


