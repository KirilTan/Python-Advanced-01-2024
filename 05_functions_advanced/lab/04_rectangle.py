def rectangle(length: int, width: int) -> str:
    """
    Calculates the area and perimeter of a rectangle.

    Args:
        length (int): The length of the rectangle.
        width (int): The width of the rectangle.

    Returns:
        str: A string containing the area and perimeter of the rectangle.

    Raises:
        ValueError: If either the length or width is not an integer.

    """
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    def area() -> int:
        """
        Calculates the area of a rectangle.

        Returns:
            int: The area of the rectangle.

        """
        return length * width

    def perimeter() -> int:
        """
        Calculates the perimeter of a rectangle.

        Returns:
            int: The perimeter of the rectangle.

        """
        return 2 * (length + width)

    return (f"Rectangle area: {area()}\n"
            f"Rectangle perimeter: {perimeter()}")


print(rectangle(2, 10))
print(rectangle('2', 10))
