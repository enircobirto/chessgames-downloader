# chessgames-downloader
Simple scraper to get games from chessgames.com

## Example usage:
> on playerlist.txt:
```
Anderssen
Morphy
Blackburne
```

### Run:
```bash
python main.py -pf "playerlist.txt" -p "Henry Bird, Charousek" -o "Romantics.pgn" 
```

This will export the games of ```Anderssen```, ```Morphy```, ```Blackburne```, ```Bird``` and ```Charousek``` into ```Romantics.pgn```.

# Extra options:
```bash
python main.py -pf "playerlist.txt" -p "Henry Bird, Charousek" -o "Romantics.pgn" --white-only
```
> Export only games that those players have played with the white pieces

```bash
python main.py -pf "playerlist.txt" -p "Henry Bird, Charousek" -o "Romantics.pgn" --black-only
```

> Export only games that those players have played with the black pieces

# Additional info:

## Output file is appendable, which means:

Running:
```
python main.py -pf "playerlist.txt" -o "Romantics.pgn"
```

#### And then:
```
python main.py -p "Henry Bird, Charousek" -o "Romantics.pgn"
```

#### Will first write the games of ```Anderssen```, ```Morphy```, and ```Blackburne```,
#### Then will add the games of ```Bird``` and ```Charousek``` to the same file, keeping the results of the first operation.

## The file 'gamelist' is emptied at the end of every run, so:

#### You can add invididual games to it before the program runs, and those games will be downloaded.
(Just remember to put ```?player="PreferredPlayer"``` at the end of the link, or else the program will crash)
