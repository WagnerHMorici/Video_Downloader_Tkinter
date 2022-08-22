from pytube import YouTube, Playlist


class Download:

    def __init__(self, link) -> None:
        self.link = link

    def download_video(self):
        # save_path = ''
        yt = YouTube(f'{self}')
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

    def download_audio(self):
        # save_path = ''
        yt = YouTube(f'{self}')
        yt.streams.filter(adaptive=True, only_audio=True, file_extension='mp4').desc().first().download()

    def download_playlist_v(self):
        # save_path = ''
        yt = Playlist(f'{self}')
        for video in yt:
            video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().\
            download()

    def download_playlist_a(self):
        # save_path = ''
        yt = Playlist(f'{self}')
        for music in yt:
            music.streams.filter(adaptive=True, only_audio=True, file_extension='mp4').desc().first().download()