class Card:
    def __init__(self, value):
        self.__value: int = value  # -5, 0 through 12
        self.__face_up: bool = False

    def get_value(self) -> int:
        return self.__value

    def is_face_up(self) -> bool:
        return self.__face_up

    def set_face_up(self) -> None:
        self.__face_up = True

    def set_face_down(self) -> None:
        self.__face_up = False

    def print(self) -> None:
        print(str(self))

    def to_str(self, add_newlines: bool) -> str:
        if self.is_face_up():
            return "/----\\\n|    |\n| {:02d} |\n|    |\n\\----/".format(self.__value)
        else:
            return "/----\\\n|    |\n| -- |\n|    |\n\\----/"
