import pygame


class Text(pygame.sprite.DirtySprite):
    def __init__(
        self,
        text,
        pos=(0, 0),
        color=(255, 255, 255),
        font=None,
        size=35,
        antialias=1,
        background=None,
    ):
        super().__init__()

        try:
            self._font = pygame.font.Font(font, size)
        except FileNotFoundError as e:
            print(e, "uses default pygame font instead.")
            self._font = pygame.font.Font(None, size)

        self.image = self._font.render(text, antialias, color, background)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    @property
    def position(self):
        """Return text position."""
        return self.rect.topleft

    @position.setter
    def position(self, pos):
        """Update text position."""
        self.rect.topleft = pos

    @property
    def linesize(self):
        """Return linesize for text with this font."""
        return self._font.get_linesize()

    @property
    def size(self):
        """Return text surface size."""
        return self.rect.size

    @property
    def width(self):
        """Return text surface width."""
        return self.rect.width

    @property
    def height(self):
        """Return text surface height."""
        return self.rect.height

    def update(self):
        self.dirty = 1