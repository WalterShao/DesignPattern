#!/usr/bin/python
# -*- coding: UTF-8 -*-

""" Test programs.
"""

class Shape(object):
    """ Parent class for figure and article
    Public Attributes:
        name: article or figure's name
        objects: list of articles included
    Public Methods:
        add_object(article): add article to figure
        del_object(name) : delete article from figure by name
        handle_object: perform article's action
    """
    def __init__(self, name):
        self.name = name
        self.objects = []
        self._is_drawn = None
    def add_object(self, article):
        """ Add article to figure
        Args:
            article: article to be added
        Returns:
        Raises:
            Native exceptions.
        """
        pass
    def del_object(self, name):
        """ Delete article from figure
        Args:
            name: name of article to be deleted
        Returns:
        Raises:
            Native exceptions.
        """
        pass
    def handle_object(self):
        """ Delete article from figure
        Args:
        Returns:
        Raises:
            Native exceptions.
        """
        pass

class Figure(Shape):
    """ Class for Figure
    Public Attributes:
    Public Methods:
        add_object(article): add article to figure
        del_object(name) : delete article from figure by name
    """
    def add_object(self, article):
        self.objects.append(article)

    def del_object(self, name):
        for obj in self.objects:
            if obj.name is name:
                self.objects.remove(obj)
                break

    def handle_object(self):
        for article in self.objects:
            article.handle_object()

class Circle(Shape):
    """ Class for circle
    Public Attributes:
    Public Methods:
        handle_object: draw a circle
    """
    def handle_object(self):
        print("Draw a circle")
        self._is_drawn = True

class Triangle(Shape):
    """ Class for triangle
    Public Attributes:
    Public Methods:
        handle_object: draw a triangle
    """
    def handle_object(self):
        print("Draw a triangle")
        self._is_drawn = True

class Rectangle(Shape):
    """ Class for rectangle
    Public Attributes:
    Public Methods:
        handle_object: draw a rectangle
    """
    def handle_object(self):
        print("Draw a rectangle")
        self._is_drawn = True

def handle_all_article_object(figure):
    """ Perform all articles' action
    Args:
        figure: Figure object
    Returns:
    Raises:
        Native exceptions.
    """
    for article in figure.objects:
        article.handle_object()

def main():
    """ Main flow code.
    Args:
    Returns:
    Raises:
        Native exceptions.
    """
    figure = Figure('figure')
    circle1 = Circle('circle1')
    triangle1 = Triangle('triangle1')
    figure.add_object(circle1)
    figure.add_object(triangle1)

    subfigure = Figure('subfigure')
    rectangle1 = Rectangle('rectangle1')
    circle2 = Circle('circle2')
    subfigure.add_object(rectangle1)
    subfigure.add_object(circle2)
    figure.add_object(subfigure)

    handle_all_article_object(figure)


if __name__ == '__main__':
    main()
