class Colors:
    dark_grey = (26,31,40)  #0
    green = (47, 230, 23)   #1
    red = (232, 18, 18)     #2
    orange = (226, 116, 17) #3
    yellow = (237, 234, 4)  #4
    purple = (166, 0, 247)  #5
    cyan = (21, 204, 209)   #6
    blue = (13, 64, 216)    #7
    white = (255, 255, 255) 
    dark_blue = (44, 44, 127)
    light_blue = (59, 85, 162)

    """A python decorator that allows you to call a method on 
       a class rather than on an instance of that class."""
    @classmethod 
    def get_cell_colors(cls): # cls is reference to class and allows to access class level attributes.
            return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]
        