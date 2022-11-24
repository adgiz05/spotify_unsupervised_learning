import pandas as pd
import sys


def main(num_per_genre):
    spotify = pd.read_csv('./dataset/spotify_tracks.csv')

    spotify['genre'].loc[spotify['genre'] == "Children’s Music"] = "Children's Music" 
    a_capella = spotify[spotify.genre == 'A Capella']
    spotify = spotify[spotify.genre != 'A Capella']

    spotify_reduced = spotify.groupby(['genre']).sample(1000)
    spotify_reduced = spotify_reduced.sample(frac=int(num_per_genre)/1000)
    spotify_reduced = pd.concat([spotify_reduced, a_capella])

    spotify_reduced.to_csv('./dataset/spotify_tracks_reduced.csv', index=False)

if __name__ == '__main__':
    main(sys.argv[1])