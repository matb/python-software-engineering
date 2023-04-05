## Testing: 
- TDD 
- BDD 
- Red Green Refactoring 


## What is TDD 
- TDD is short for Test-Driven Development and an approach in  software that emphasizes writing automated tests for code before writing the code itself.
- This approach should help ensure that the code is thoroughly tested, all requirements are met, and that the code is maintainable , save and easy to change in the future. 
- The TDD process typically involves the following steps:
1.  Write a test: The developer writes a test for a particular piece of functionality that needs to be implemented.
2.  Run the test: The developer runs the test to confirm that it fails, indicating that the desired functionality has not yet been implemented.
3.  Write code: The developer writes the code necessary to make the test pass.
4.  Run the test: The developer runs the test again to confirm that it now passes.
5.  Refactor code: The developer refactors the code to improve its design, without changing its behaviour.
6.  Repeat: The developer repeats this process, writing additional tests and code until all desired functionality is implemented.


## Why should you use TDD:

1.  **Improved code quality** since  TDD encourages you to write code that is tested and satisfies the  requirements.
    
2.  **Faster feedback and less time spent debugging** as TDD provides quick feedback loop of how and if your code works as expected. This will enable you to catch bugs and issues early in the process.
    
3.  By following the development style one will result with a **better overall code design** as your code becomes more modular and less coupled.
    
4. Finally you also create a good technical documentation due to TDD requiring developers to write clear and concise tests, which can show the use and intention of the code.
    

## Risks of TDD:

While offering several benefit, before you and your team change to a TDD based workflow - you should address the following risks: 

1. **TDD will increased development time**: Writing tests for code can take additional time, which can slow down the development process.
    
2.  Dont assume that it will solve all your problems - there might be a ""false sense of security"" - Just because code passes a test does not guarantee that it is free of bugs or issues.
    
3.  Some types of code, such as code that relies heavily on external resources, can be **difficult to test with TDD**. 
    
4.  **Resistance to change**: Some developers may be resistant to the idea of TDD, which can make it difficult to implement within a development team.


## BDD - Behavior-Driven Development

- BDD is an agile software development methodology that extends TDD by focusing on the behavior of the software rather than just the code. 
- It emphasizes collaboration between developers, testers, and business stakeholders to ensure that the software being developed meets the needs of the business.
- In BDD, the development team starts by defining the desired behavior of the software in the form of user stories or scenarios.
- These scenarios are typically written in plain language and describe the expected behavior of the software from the perspective of the user.
- The scenarios are then used to guide the development process, with automated tests being written to ensure that the software behaves as expected.


## BDD - Behavior-Driven Development

BDD typically involves the following steps:

1.  Define behavior: The development team works with business analysts to define the desired behavior of the software in the form of scenarios or user stories.
    
2.  Write scenarios: The scenarios are written in plain language and describe the expected behavior of the software.
    
3.  Implement scenarios: The development team implements the scenarios as automated tests, using a testing framework such as Cucumber or SpecFlow.
    
4.  Write code: The development team writes code to make the tests pass, with a focus on delivering the desired behavior.
    

## BDD - Behavior-Driven Development

Why should you use BDD:

1.  Improved collaboration: BDD encourages collaboration between developers, testers, and business stakeholders, which can help ensure that everyone is working towards the same goals.
    
2.  Better requirements: BDD helps ensure that the software being developed meets the needs of the business and behaves as expected from the perspective of the user.
    
3.  Faster feedback: BDD provides quick feedback on the behavior of the software, which can help catch issues early in the development process.
    
4.  Increased test coverage: BDD encourages the development of automated tests, which can increase test coverage and ensure that the software behaves as expected.
    
5.  Improved documentation: BDD scenarios serve as a form of documentation, describing the behavior of the software in plain language that can be easily understood by business stakeholders.
    

## BDD - Behavior-Driven Development

What you need to keep in mind:

1.  Increased development time: BDD can require additional time to write and implement scenarios, which can slow down the development process.
    
2.  Difficulty in defining behavior: Defining behavior in the form of scenarios or user stories can be challenging, particularly if the business requirements are complex or unclear.
    
3.  Over-reliance on testing: BDD can sometimes lead to an over-reliance on automated testing, which may result in code that is difficult to maintain or change.
    
4.  Resistance to change: Some developers may be resistant to the idea of BDD, which can make it difficult to implement within a development team.
    
5.  Need for specialized tools: BDD typically requires the use of specialized testing frameworks and tools, which may require additional training and resources to implement effectively.


## TDD & BDD 

- TDD and BDD are two complementary methodologies that can be used together to improve software development.
- **TDD** focuses on **writing automated tests before writing code** , ensuring that the code meets specific requirements and behaves as expected. **BDD**, on the other hand, focuses on the **behavior of the software from the perspective of the user or business stakeholder** - with scenarios and user stories. 
- following a process involves writing automated tests to implement the behavior described in scenarios.
- The process typically looks like this:

1.  **Define behavior**: Use BDD to define the desired behavior of the software in the form of scenarios or user stories.
    
2.  **Write tests**: Use TDD to write automated tests that implement the behavior described in the BDD scenarios.
    
3.  **Write code**: Write code to make the tests pass and implement the desired behavior.
    
4.  **Repeat**: Repeat this process, adding more scenarios and tests as needed to ensure that the software meets the desired behavior.

- Using TDD & BDD together, development teams can ensure that the software they are developing is thoroughly tested and meets the needs of the business


## RGR - Red-Green-Refactoring

RGR is a technique where TDD is applied in code refactoring :

1.  Red: Write a failing test case (i.e., a test that fails because the code being tested does not yet exist or does not behave as expected).
    
2.  Green: Write the simplest possible code that passes the test.
    
3.  Refactor: Improve the code's structure, design, and performance without changing its behavior, while ensuring that all tests still pass.



## RGR Summary 
- The RGR process is iterative, meaning that it is repeated many times over the course of the development cycle.
- Each iteration results in the addition of new tests, the implementation of new code to make those tests pass, and the refinement of existing code to improve its design and performance.
- RGR is popular in TDD because it helps developers to focus on writing small, modular, and testable code, resulting in software that is easier to maintain, debug, and extend. By following the RGR process, developers can also ensure that all code is thoroughly tested and meets the requirements of the business or end-users. 



## Test Frameworks
There are several test frameworks available for Python, each with its own set of features and benefits. Here are some of the most popular ones:

-  unittest: This is Python's built-in test framework, which provides a basic framework for writing and executing tests. It is easy to use and is a good choice for simple test cases.
    
-  pytest: This is a popular third-party test framework that offers many features such as automatic test discovery, detailed failure reporting, and fixtures that allow for setup and teardown of test environments. It is also highly extensible, allowing for the creation of custom plugins.
    
-  nose: This is another popular third-party test framework that extends unittest with additional features such as test discovery, test grouping, and plugin support.
    
-  doctest: This is a built-in test framework that allows developers to embed tests in documentation strings, making it easy to write tests that also serve as documentation.
    
-  tox: This is a test automation tool that allows developers to easily run tests in multiple environments and configurations.
    
-  Hypothesis: This is a property-based testing framework that generates test data automatically, making it useful for testing complex algorithms and data structures.
    

- When deciding which test framework to use, it is important to consider the specific needs of your project. For example, if you are working on a large project with many tests, pytest may be a good choice due to its advanced features and extensibility. If you are working on a simple project with fewer tests, the built-in unittest framework may be sufficient. Ultimately, the choice of test framework will depend on the specific needs and requirements of your project.


## Macro Design
- Refers to the high-level design of a software system
- Focuses on the overall architecture and organization of the system
- Defines the major components and their interactions


## Examples of Macro Design and Monoliths
- Monoliths are a common form of macro design
- Examples include traditional web applications and enterprise software
- Often designed as a single, monolithic codebase with tightly-coupled components


## Micro Design
- Refers to the low-level design of a software system
- Focuses on the design of individual components and services
- Defines the APIs and communication protocols between components


## Comparison of Macro and Micro Designs
- Macro designs are typically simpler to implement and maintain
- Micro designs offer greater flexibility and scalability
- Micro designs can be more complex and require more effort to implement and manage


## Why Use Micro Design?
- Enables greater scalability and flexibility
- Allows for easier testing and deployment of individual components
- Supports the use of modern development practices like DevOps and agile methodologies


## Implementing Micro Design in Python
- Python is a popular language for microservice architectures
- Microservices can be implemented using frameworks like Flask, FastAPI, and Django
- Microservices can also be implemented using asynchronous programming models like asyncio


## Flask
- Lightweight web framework for building microservices
- Supports routing, request handling, and response generation
- Allows for easy integration with other Python libraries and frameworks


## FastAPI
- Modern web framework for building APIs
- Designed for high performance and easy scalability
- Supports automatic documentation generation and validation of API requests and responses


## Django
- Full-stack web framework for building complex applications
- Includes support for object-relational mapping, authentication, and administration interfaces
- Can be used to build microservices by disabling unnecessary features and using a lightweight server like gunicorn


## Docker and Micro Design
- Docker is a containerization technology that supports microservice architectures
- Allows for easy deployment and scaling of individual services
- Enables consistent and reproducible deployment environments


## Important Docker Commands
- `docker build`: Builds a new Docker image from a Dockerfile
- `docker run`: Runs a Docker container from an image
- `docker stop`: Stops a running container
- `docker rm`: Removes a stopped container
- `docker images`: Lists all Docker images on the system
- `docker ps`: Lists all running Docker containers on the system
- `docker exec`: Runs a command inside a running container
- `docker logs`: Shows the logs of a running container
- `docker push`: Pushes a Docker image to a remote registry
- `docker pull`: Pulls a Docker image from a remote registry


## Creating a FastAPI with Code

::: columns 

:::: column
1. This imports the FastAPI class from the fastapi module and creates an instance of it called app. 
2. This defines an endpoint at the root URL (/) using the HTTP GET method. When a request is made to this endpoint, the function read_root is executed, which simply returns a dictionary containing the message "Hello, World".
3. This defines a second endpoint with a path parameter item_id and an optional query parameter q. When a request is made to this endpoint, the function read_item is executed, which returns a dictionary containing the values of the item_id and q parameters.

::::

:::: column
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```
::::

## Dockerizing the API 

::: columns 

:::: column
The Dockerfile uses an official FastAPI Docker image as a base
Copies the source code from the local machine into the container
Sets the necessary environment variables and exposes the necessary port
Defines the command to run the application using Uvicorn
The application can then be built and run using the docker build and docker run commands, respectively.

::::

:::: column
```
# Dockerfile
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./app /app

ENV MODULE_NAME=myapp.main
ENV VARIABLE_NAME=app

EXPOSE 80

CMD ["uvicorn", "myapp.main:app", "--host", "0.0.0.0", "--port", "80"]

```
::::
## Effiziente Programmierung mit Python 

Zum Abschluss des Trainings erlernen die Teilnehmer best-practices für die Verwendung von Python. Dabei liegt der Fokus auf Speicher-Effizienz, Performance, Wartbarkeit und Erweiterbarkeit. In den Übungen refactoren die Teilnehmer bestehende Anwendung zur Verbesserung der zuvor genannten Aspekte. 

