> [!NOTE]
> I implemented this website for myself back in 2020. However, it was implemented with a lot of errors and poor quality. Now, I decided to return to my idea and realize the website from scratch using new technologies. Unfortunately, the site is only available in Russian (maybe in the near future I will add English localization), as it was originally intended for the Russian-speaking audience. 

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
```
pip install Flask
```

To switch to the project directory use:
```
cd path/to/nickgenerator
```

Run Python's built-in HTTP server:
```
python generator.py
```

Go to your browser and open http://127.0.0.1:5000 to use the nickname generator

