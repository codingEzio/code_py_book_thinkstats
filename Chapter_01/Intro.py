
__doc__ = \
""" 
    Simple idea: <CODE-AS-NOTES>.
    
    The '.ipynb' could accomplish this, 
    but ... Well, I wanna use this one :p 
"""

class AboutThisBook:
    """ Quotes from author 

        If you have never studied statistics, 
            I think this book is a good place to start. 
        
        And 
            if you have taken a traditional statistics class, 
            I hope this book will help repair the damage.
    """

    def __init__(self, freeOrNot, py3):
        self.freeOrNot  = "yes"
        self.py3        = "yes"

    @staticmethod
    def get_resource():
        """ The author suggests that 
            run 'nsfg.py' for testing before u start.
        """
        
        book_src, book_pdf = (
            "https://github.com/AllenDowney/ThinkStats2/tree/master/code",
            "http://greenteapress.com/thinkstats2/thinkstats2.pdf"
        )


class AnecdotalEvidence:
    """
        Sometimes we call it 'prejudice'. 
        I prefer the word "F dumb".
    """

    def ___init__(self, features):
        self.features = [
            "Inaccuracy",
            "Selection bias",
            "Confirmation bias ",
            "Small num of observations",
        ]

    @staticmethod 
    def how_can_we_do_better():
        data_collection     = "real, large, reliable dataset"
        descriptive_stat    = "visualize it"
        expl_data_analysis  = "look for patterns, differences and .."
        estimation          = "use ... to estimate characteristics of the general .."
        hypothesis_testing  = "evaluate the diff might've happend by chance, or not"
