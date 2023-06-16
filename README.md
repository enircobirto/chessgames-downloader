# chessgames-downloader
Simple scraper to get games from chessgames.com

## Example usage:
```
Anderssen
Morphy
Blackburne
```
> playerlist.txt

```bash
python main.py -pf "playerlist.txt" -p "Henry Bird, Charousek" -o "Romantics.pgn" 
```

This will export the games of ```Anderssen```, ```Morphy```, ```Blackburne```, ```Bird``` and ```Charousek``` into ```Romantics.pgn```.

## Extra options:
```bash
python main.py -pf "playerlist.txt" -p "Henry Bird, Charousek" -o "Romantics.pgn" --white-only
```
> Export only games that those players have played with the white pieces

```bash
python main.py -pf "playerlist.txt" -p "Henry Bird, Charousek" -o "Romantics.pgn" --black-only
```

> Export only games that those players have played with the black pieces
