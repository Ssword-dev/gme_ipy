"""
# Redirect 
A package for browsers
"""
import webbrowser
import sys

DEFAULT_BROWSER = 'chrome' # Dont push it, i aint setting this to edge lmfao
#chrome_controller = webbrowser.register(DEFAULT_BROWSER) # ight, dont like how long it takes to do this so not doing it

def redirect(link):
    """
    Opens a browser then goes to the link 
    """
    webbrowser.open(link)
def open_tab(link):
    """
    Make a new tab
    """
    return webbrowser.open_new_tab(link) # return whether it was opened. also cuz i dont wanna make another thingy its just
# gonna make it unreadable

def redirect_to_domain(link):
    """
    Uhh i made this just for readability, you can use redirect instead lmao
    """
    return redirect(link) # ok so return this too

def help():
    """
    A help function that displays a tutorial
    """
    print("Uhh, hello there user! so... you want a tutorial? hmm... ok so\n basically you can use the `redirect` function to open a site... not really a redirect but\n good for tutorials or opening links")
    print("so to use it you would type `redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')`\n and it would open the link in your default browser")
    print("you can also use the `help` function to get a list of all the functions (only 1 right now)")
    print("and you can also use the `exit` function to exit the program")

def exit(code):
    """
    Not related to browser, but useful for debugging
    """
    sys.exit(code)
