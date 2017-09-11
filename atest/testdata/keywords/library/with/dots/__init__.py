from __future__ import print_function
from robot.api.deco import keyword


class dots(object):

    @keyword(name='In.name.conflict')
    def keyword(self):
        print("Executing keyword 'In.name.conflict'.")
