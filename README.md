# AniListGiveawayBot
A simple bot that picks giveaway winners from an AniList user's followers list

## Arguments
```
usage: bot.py [-h] -u USER -w WINNERS [-d]

options:
  -h, --help            show this help message and exit
  -u USER, --user USER  The ID of the user to draw contestants from
  -w WINNERS, --winners WINNERS
                        The amount of winners to be drawn
  -d, --debug           Run the script in debug mode, logs extra information to console
```

## Requirements
- [loguru](https://github.com/Delgan/loguru)
- [requests](https://github.com/psf/requests)
- [black](https://github.com/psf/black)

## Grabbing user ID
The bot relies on the user's internal AniList ID currently rather than their username. You can open your user page in your browser and grab the ID from any of your browsers `/graphql` requests under the Network tab. Adding support for using the username rather than the numerical ID is a quality of life feature I would like to support in the future.
