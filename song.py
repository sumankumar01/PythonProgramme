class song:
    """class to represt the song
    Attribute:
    title(str): the title of songs
    artist(Artist): an artist object represent  the song creator.
    duration(int): the duration of the songs  in sec. may be  Zero
    """

    def __init__(self, title, article, duration=0):
        """song init method
        Args:
            title(str): Intitialize the 'title' attribute
            artist(Artist): At artist object represent the song's creator
            duration (optional[int]: initil value for duration attribute.
              will default to zero if not specified
        """

        self.title = title
        self.article = article
        self.duration = duration


# help(song.__init__)
help(song.__doc__)
# help(song.__init__.__doc__)
