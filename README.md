# LOL DATA

This repo aims to serve less common statistics from League of Legends game.

For now, it's just pulling from top 5 players of a certain region, the top 10 most common champs from last 10 matches.

So, if the platform is NA1 and region is Americas:

- will get top 5 players on the ladder (LIVE)
- for each player, it will get all champions used in player's last 10 games
- matches are processed only once, so if two or more players from the top 5 were in the same match, it will be processed
only once
- finally it will print the top 5 players of the region and the top 10 most used champions from their games, with counts

**_Important_**: this is a simple statistic to pull. Use cases will be enhanced and at some point the plan is to deliver a
*self serve platform* to run ad hoc analysis.

# Why this project

As a Data Engineer, I want to learn or improve on some of the cool tech used nowadays in the industry:

- Python
- SQL
- Data modeling
- Data analysis
- Cloud Platforms
- dbt
- Testing

I want to treat this as a Data Product and will put more effort on all things Data.

If there's something on a data level that can be improved - it will be improved. But if it's software engineering things
that are out of my knowledge I'll might have to skip those :-)

# Setting Up the Project Environment

Follow these steps to install Python 3.12 (or the latest available version), set up a virtual environment, and install
the project dependencies:

## 1. Install Python 3.12 (or Latest Version)

1. **Check if Python 3.12 is already installed:**

    ```bash
      python3 --version
    ```

2. **Download Python 3.12:**

   - Visit the [official Python downloads page](https://www.python.org/downloads/) and download the latest version
     compatible with your system.

   - Follow the installation instructions for your operating system:
     - Windows: Ensure the "Add Python to PATH" option is checked during installation.
     - macOS: Use the downloaded installer or Homebrew:
       ```bash
       brew install python
       ```
     - Linux: Use your package manager. For example, on Ubuntu:
       ```bash
       sudo apt update
       sudo apt install -y python3.12 python3.12-venv python3.12-dev
       ```

3. **Verify the Installation:**

```bash
  python3 --version
```

## 2. Set Up a Virtual Environment

It is recommended to use a virtual environment to isolate depdendencies for the project.
    
  1. **Create a Virtual Environment:**
      ```bash
      python3.12 -m venv venv
      ```
  2. **Activate the Virtual Environment:**
     - Windows:
       ```bash
       venv\Scripts\activate
       ```
     - macOS/Linux:
       ```bash
       source venv/bin/activate
       ```
  3. **Verify the Virtual Environment is Active**: When the virtual environment is active, the terminal prompt will show
     `(venv)`.

## 3. Install Dependencies

  1. Ensure you are in the project directory (where requirements.txt is located). Install the required packages:
        
     ```bash
     python3 -m pip install -r requirements.txt
     ```

  2. Verify the installation:
      ```bash
      python3 -m pip list
      ```

  3. Run the Project:
  
      > [!WARNING]
      > 
      > You'll need an API key from Riot Games until I can provide one for the application without expiring every 24h. 
      > Get the API key [here](https://developer.riotgames.com/) (requires signing in with a Riot Games account). 
      > Paste the API key in [API CLient](./APIClient.py#L11).
  
      After setting up the environment and installing dependencies, you can run the project by simply executing:

      ```bash
      python3 main.py
      ```
     
