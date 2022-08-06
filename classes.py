class Television:
    """
    A class representing details for a television object
    """

    MIN_CHANNEL: int = 0  # Minimum TV channel
    MAX_CHANNEL: int = 3  # Maximum TV channel

    MIN_VOLUME: int = 0  # Minimum TV volume
    MAX_VOLUME: int = 2  # Maximum TV volume

    def __init__(self) -> None:
        """
        Constructor to create initial state of a television object.
        param channel: the TV channel. It should be set to the minimum TV channel by default.
        param volume: the TV volume. It should be set to the minimum TV volume by default.
        param power: the TV power. The TV should start when it is off.
        """
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__power = False

    def power(self) -> None:
        """
        Method to access the TV power.
        :return: - If called on a TV object that is off, the TV object should be turned on.
                 - If called on a TV object that is on, the TV object should be turned off.
        """

        if not self.__power:
            self.__power = True
        else:
            self.__power = False

    def channel_up(self) -> None:
        """
        Method should be used to adjust the TV channel by incrementing its value.
        :return:
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_CHANNEL, it should take the TV channel back to the MIN_CHANNEL.
        """
        if self.__power:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Method should be used to adjust the TV channel by decrementing its value.
        :return:
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_CHANNEL, it should take the TV channel back to the MAX_CHANNEL.
        """
        if self.__power:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Method should be used to adjust the TV volume by incrementing its value.
        :return:
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_VOLUME, the volume should not be adjusted.
        """
        if self.__power:
            if self.__volume == Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
            else:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method should be used to adjust the TV volume by decrementing its value.
        :return:
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_VOLUME, the volume should not be adjusted.
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
