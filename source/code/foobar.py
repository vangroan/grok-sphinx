# MIT License
#
# Copyright (c) [year] [fullname]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""
Module doc
==========

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec consectetur enim
eget nibh accumsan commodo. In tempor lacus a ipsum lobortis fermentum. Duis et
pulvinar lectus, et commodo orci. Morbi lobortis dictum risus, et imperdiet justo.
Aenean a mollis eros. Cras sed sem dapibus, convallis purus in, aliquet felis.
Fusce condimentum cursus nisi at sodales. Cras commodo odio ut tortor faucibus,
non vulputate nunc dictum.

.. code-block:: html
    :linenos:

    <h1>code block example</h1>
"""

def fibonacci(n: int) -> int:
    """
    Sequence where each number is the sum of the two preceding numbers.
    
    .. code-block:: python
        :linenos:

        fibonacci(5)

    .. doctest::

        >>> from foobar import fibonacci
        >>> fibonacci(5)
        5
    
    """
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
 

def func(arg1, arg2):
    """Summary line.

    Extended description of function.

    Args:
        arg1 (int): Description of arg1
        arg2 (str): Description of arg2

    Returns:
        bool: Description of return value

    """
    return True


def func2(arg1, arg2):
    """Summary line.

    Extended description of function.

    :param arg1: Description of arg1
    :type arg1: int
    :param arg2: Description of arg2
    :type arg2: str
    :returns: Description of return value
    :rtype: bool

    """
    return True

def func3(arg1: int, arg2: str) -> bool:
    """Summary line.

    Extended description of function.

    Args:
        arg1 : Description of arg1
        arg2 : Description of arg2

    Returns:
        Description of return value

    """
    return True

class Base:
    """
    Abstract base
    """
    pass


class FileDerive(Base):
    """
    Filesystem deriver
    """
    pass

class TcpDerive(Base):
    """
    TCP network deriver
    """
    pass
