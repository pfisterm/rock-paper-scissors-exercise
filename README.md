# rock-paper-scissors-exercise

Set up the repository by downloading from GitHub
Navigate to the respository from the command-line

# Third-Party Packages
Follow the requirements.txt file to install the third-party packages required by the app.
The following code will be required for installation:
    ```pip install python-dotenv```

# Environment Setup
1. Create a project-specific environment. I titled my environment my-game-env using the following code
    ``` conda create my-game-env ```
2. Activate the project-specific environment using the following code
    ``` conda activate my-game-env ```

# Environment Variables
In the repository create a .env file. In the .env file create a variable titled PLAYER_NAME.
The .env file should state:
    PLAYER_NAME="Jon Snow"
The user can customize the player name on the right side of the equal sign.

# Run the App
Once the setup is complete. Run the game.py file from the command line using the code 
    ```python game.py```