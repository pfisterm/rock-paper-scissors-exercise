# rock-paper-scissors-exercise

Clone the repository from GitHub and save onto your local device.
Navigate to the respository from the command-line using the following code: <br>
    ``` cd ~/Desktop/rock-paper-scissors-exercise ```

# Third-Party Packages
Use the following code to install the third-party packages required by the app. <br>
    ```pip install -r requirements.txt```

# Environment Setup
1. Create a project-specific environment. I titled my environment my-game-env using the following code <br>
    ``` conda create my-game-env ```
2. Activate the project-specific environment using the following code <br>
    ``` conda activate my-game-env ```

# Environment Variables
In the repository create a .env file. In the .env file create a variable titled PLAYER_NAME.
The .env file should state: <br>
    PLAYER_NAME="Jon Snow" <br>
The user can customize the player name on the right side of the equal sign. Make sure to save the .env file prior to running the app.

# Run the App
Once the setup is complete. Run the game.py file from the command line using the code <br>
    ```python game.py```