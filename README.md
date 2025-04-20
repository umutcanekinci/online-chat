# Online Chat

This project is a simple online chat application developed with Python. It allows multiple users to communicate in real-time over a local network. The main goal of this project is to demonstrate the use of socket programming and threading in Python.

Unfortunately, this project is still a work in progress. The basic functionality is implemented, but there are plans to add more features in the future.

## Features

- Real-time messaging
- Multi-client support
- Simple and intuitive interface

## Getting Started

### Requirements

To run the project, you'll need the following software:

- Python 3.x
- Required libraries:
    - socket
    - threading

### Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/umutcanekinci/online-chat.git
    cd online-chat
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3. Install required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

Start the server:
```sh
python server.py
```

Start the client:
```sh
python client.py
```

### How to Use

1. Run the server script on the host machine.
2. Run the client script on any machine within the same network.
3. Enter the server's IP address and port when prompted.
4. Start chatting!

### Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.

2. Clone the forked repository to your local machine:
    ```sh
    git clone https://github.com/umutcanekinci/online-chat.git
    cd online-chat
    ```

3. Create your feature branch:
    ```sh
    git checkout -b feature/your-feature
    ```

4. Commit your changes:
    ```sh
    git commit -am 'Add some feature'
    ```

5. Push to the branch:
    ```sh
    git push origin feature/your-feature
    ```

6. Open a Pull Request.

### License

Distributed under the MIT License. See LICENSE for more information.

### Contact

Feel free to reach out for any recommendations or questions.  
Umutcan Ekinci - umutcannekinci@gmail.com  