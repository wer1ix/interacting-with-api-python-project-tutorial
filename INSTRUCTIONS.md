# Interacting with Spotify's API

Spotify can be used as a data source for various data science projects. In this exercise, we will learn how to interact with the API of this social network. `Spotipy` is an open-source and Python library that allows high-level use of the Spotify API.

## Step 1: Create a Spotify Developer Account

Before starting to code, you need access to Spotify developer credentials. Visit [developer.spotify.com](https://developer.spotify.com/documentation/web-api).

- Log in with your Spotify account (or create one if you don't have one yet).

- Go to the Dashboard and click on Create an App. Fill in the required fields. In Redirect URI, enter: `http://localhost/`

![Spotify create app](https://github.com/4GeeksAcademy/interacting-with-api-python-project-tutorial/blob/main/assets/spotify_1.PNG?raw=true)

Once the app is created, go to the **Settings** section to copy your `Client ID` and `Client Secret`. You will use them later to authenticate with the API.

## Step 2: Initial Setup

- Open the terminal and ensure you have the `Spotipy` library installed, as it will be used to connect to the Spotify API:

    ```bash
    pip install spotipy
    ```

## Step 3: Environment Variables

You already have the `.env` file in the root of the project. Make sure it contains the following variables with your Spotify credentials (replace the content with your own data):

```env
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
```

> ⚠️ It is important to place your data in environment variables to avoid exposing your credentials if you upload the project to a repository.

Now, in the `app.py` file, add the following code to read the environment variables:

```python
import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# Get credential values
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
```

With this, your credentials will be ready to use for authentication with the Spotify API.

## Step 4: Initialize the Spotipy Library

- Import Spotipy.
- Connect to the API. To do this, you can use the `spotipy.Spotify()` function.

    ```python
    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials

    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    spotify = spotipy.Spotify(auth_manager=auth_manager)
    ```

    > 💡 NOTE: Use the following documentation as a guide for the parameters: https://spotipy.readthedocs.io/en/2.22.1

## Step 5: Make API Requests

- Start interacting with the Spotify API: Get the top 10 songs of your favorite artist. To do this, you will need to find the artist's `ID` to use it with the library. This identifier is the web address of the artist on Spotify:

![Find the artist's identifier on Spotify](https://github.com/4GeeksAcademy/interacting-with-api-python-project-tutorial/blob/main/assets/spotify_2.png?raw=true)

- Once you have the API response, focus on the `tracks` element, which will contain the most played songs of the artist. Extract the song name, popularity, and duration (in minutes).

> ⚠️ **NOTE** about possible messages when running the code. You might encounter a message like the following after executing the script:

```
 Exception ignored in: <function Spotify.__del__ ...>
 TypeError: isinstance() arg 2 must be a type, a tuple of types, or a union
```

This message originates from the `spotipy` library and **does not affect the functionality of your code or the API results**. You can safely ignore it; it is an internal object cleanup detail (**garbage collection**) that does not interrupt your analysis.

## Step 6: Transform to Pandas DataFrame

Since the result obtained in these steps is likely to be in table format, convert it to a DataFrame by importing the data in its dictionary format. Next, sort the songs by increasing popularity and display the resulting top 3.

## Step 7: Analyze statistical relationship

Does duration have a relationship with popularity? Could we say that a song that lasts a short time may be more popular than a song that lasts longer? Analyze it by plotting a `scatter plot` and argue your answer.
