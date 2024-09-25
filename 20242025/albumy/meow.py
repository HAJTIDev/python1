class Albumy:
    def __init__(self, artist, title, tracks, year, downloads):
        self.artist = artist
        self.title = title
        self.tracks = tracks
        self.year = year
        self.downloads = downloads

class main:
    def __init__(self):
        self.albums = []
        self.albums_count = 0
        self.current_index = 0
        self.load_album_data()

    def load_album_data(self):
        with open("data.txt") as file:
            data_lines = file.readlines()
        artist = ""
        title = ""
        tracks = ""
        year = ""
        downloads = ""
        for i, line in enumerate(data_lines):
            line_index = (i % 6) + 1
            if line_index == 1:
                artist = line.strip()
            elif line_index == 2:
                title = line.strip()
            elif line_index == 3:
                tracks = line.strip()
            elif line_index == 4:
                year = line.strip()
            elif line_index == 5:
                downloads = line.strip()
            elif line_index == 6:
                self.albums.append(Albumy(artist, title, tracks, year, downloads))

        for i in range(0, len(self.albums)):
            print(f"{i+1}. {self.albums[i].artist} - {self.albums[i].title} ({self.albums[i].year})")
if __name__ == "__main__":
    main_instance = main()