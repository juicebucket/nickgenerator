Application version: 0.1.0. / Last Update: 23.06.2024

> [!NOTE]
> This website is a fan-made website and was made for myself. I realized a website with this idea back in 2020, but it was realized very simply and poorly. Now, I decided to completely redesign it by changing the technology and its design. Unfortunately, the site is only available in Russian, as it was originally intended for the Russian-speaking audience.

## Overview
**ROLEPLAY NICKNAME GENERATOR** is a web application designed to generate unique and memorable nicknames for RolePlay games such as SAMP, CRMP, GTA5, Garry's Mod, and more. By selecting the character's gender and nationality, you can quickly generate a nickname that fits your character's profile.


## Technologies
Certain technologies were used to develop the project, each playing a different function:

- **Flask:** Used for back-end, namely nickname generation.
- **HTML/CSS:** Used to create the structure and styling of the user interface.
- **JavaScript:** Adds interactivity to the web page, including features like copying the generated nickname to the clipboard.
- **JSON**: Used to store first and last names and sort them into categories.


## Key Features
- **User-Friendly Interface:** Intuitive and minimalistic design that any user can understand. Optimized also for use on small screens.
- **Variety of Options:** Users can select the gender and nationality of the character to generate a suitable nickname.
- **Extensive Name Database:** The JSON file stores a large number of first and last names for generation, with different sorting settings: by gender and nationality.


## Screenshot
<img width="1506" alt="image" src="https://github.com/juicebucket/nickgenerator/assets/92608350/2f5ff581-e18c-4f15-a44c-b991a9c1aff1">


## Installation
To run this project, make sure that you have installed Python. Use Terminal.

To install Flask use:
'''
pip install Flask
'''

To switch to the project directory use:
'''
cd path/to/nickgenerator
'''

Run Python's built-in HTTP server:
'''
python generator.py
'''

Go to your browser and open http://127.0.0.1:5000 to use the nickname generator

