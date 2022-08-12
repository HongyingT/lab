class Television:
    """
    A class representing details for a television object
    """

    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self) -> None:
        """
        Constructor to create initial state of a television object.
        """
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__power = False

    def power(self) -> None:
        """
        Method to access the TV power.
        """

        if not self.__power:
            self.__power = True
        else:
            self.__power = False

    def channel_up(self) -> None:
        """
        Method should be used to adjust the TV channel by incrementing its value.
        """
        if self.__power:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Method should be used to adjust the TV channel by decrementing its value.
        """
        if self.__power:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Method should be used to adjust the TV volume by incrementing its value.
        """
        if self.__power:
            if self.__volume == Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
            else:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method should be used to adjust the TV volume by decrementing its value.
        """
        if self.__power:
            if self.__volume == Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
            else:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method should be used to the format shown in the comments of main.py
        :return: the TV status
        """
        return f'TV status: Is on = {self.__power}, Channel = {self.__channel}, Volume = {self.__volume}'
