# AniListGiveawayBot
A simple bot that picks giveaway winners from an AniList user's followers list

## Arguments
```
usage: bot.py [-h] -u USER -w WINNERS [-d]

options:
  -h, --help            show this help message and exit
  -u USER, --user USER  The username of the user to draw contestants from
  -w WINNERS, --winners WINNERS
                        The amount of winners to be drawn
  -d, --debug           Run the script in debug mode, logs extra information to console
```

## Requirements
- [loguru](https://github.com/Delgan/loguru)
- [requests](https://github.com/psf/requests)
- [black](https://github.com/psf/black)
