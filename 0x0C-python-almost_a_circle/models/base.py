#!/usr/bin/python3
"""this module contains a class Base.
"""
import json
import turtle
import time


class Base:
    """Class Base that sets the instance id.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor that sets the instance id.

        Args:
            id (Int, None): id value. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): list of dictionaries

        Returns:
            json str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is not None or len(list_dictionaries) > 0:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances who inherits of Base.
        """
        li = []
        filename = "{}.json".format(cls.__name__)
        if list_objs is not None:
            for obj in list_objs:
                li.append(obj.to_dictionary())
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(li))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.

        Args:
            json_string (str): a string representing a list of dictionaries.

        Returns:
            [type]: the list represented by json_string.
        """
        if json_string is None or len(json_string) < 1:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Returns:
            obj: instance with all new attributes.
        """
        new = cls(1, 1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances.

        Returns:
            list: list of instances.
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                pylist = cls.from_json_string(file.read())
        except Exception:
            return []
        return [cls.create(**i) for i in pylist]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw all rectangles and squares

        Args:
            list_rectangles (list): list of rectangles.
            list_squares (list): list of squares.
        """
        t = turtle.Turtle()
        style = ("Arial", 11, 'normal', 'bold')
        for i in list_rectangles:
            if "rectangle" in str(type(i)):
                t.penup()
                x = i.x
                y = i.y
                h = i.height
                w = i.width
                t.setposition(x+w/2, y-30)
                t.color('#4a661a')
                t.write(i, font=style, align="center")
                t.color('black')
                t.setposition(x, y)
                t.pendown()
                t.fillcolor("#4a661a")
                t.begin_fill()
                for j in range(2):
                    t.forward(w)
                    t.left(90)
                    t.forward(h)
                    t.left(90)
                t.end_fill()
                time.sleep(2)
                turtle.resetscreen()
        for i in list_squares:
            if "square" in str(type(i)):
                t.penup()
                s = i.size
                x = i.x
                y = i.y
                t.setposition(x+s/2, y-30)
                t.color('#c75038')
                t.write(i, font=style, align="center")
                t.color('black')
                t.setposition(x, y)
                t.pendown()
                t.fillcolor("#c75038")
                t.begin_fill()
                for j in range(4):
                    t.forward(s)
                    t.left(90)
                t.end_fill()
                time.sleep(2)
                turtle.resetscreen()
