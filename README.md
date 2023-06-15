# This is messenger app.


## It's key features include:
- User Registration: Users can create an account by providing necessary details, such as their username, password, and email address.
- Login Functionality: Registered users can securely log in to their accounts using their credentials.
- Messaging Capability: Users can compose and send messages to selected recipients of their choice.
- Message History: The app maintains a record of all conversations, allowing users to view their entire message history with any selected recipient.


## To run the messenger app, follow these steps:
- Download the repository containing the app's source code.
- Ensure that Docker is installed on your system.
- Open the terminal or command prompt and navigate to the main app folder.
- Run the command "docker-compose up" to create and start both containers required for the app.
- Once both containers are successfully created, access the container named "messenger-app-1" by executing the command "docker exec -it messenger-app-1 sh".
- Within the container, start the app by running the command "python3.11 -m main_folder.main".