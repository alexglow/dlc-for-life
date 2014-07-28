dlc-for-life
============

Little scripts that may or may not enhance your experience.

ke.py -
Used in conjunction with GeekTool ( http://projects.tynsoe.org/en/geektool/ ), this little script places a display of the current time in ke ( http://en.wikipedia.org/wiki/Ke_(unit) ) on your desktop. It can give you a sense of urgency, or modify your perception of time in other ways. Really interesting!

screenshot.py -
This Selenium WebDriver script ( http://www.seleniumhq.org/projects/webdriver/ ) captures a screenshot to the same directory from which you run the command to launch the script.
It captures the entire loaded canvas - including content that's currently off-screen - which is useful if you need a screenshot of EVERYTHING on a page. For example, I write instructables that are sometimes featured. It's nice to have a screenshot of this, but sometimes I forget until a few hours after it's featured - at which point it may be partially offscreen. This takes the fuss out of capturing the page header AND my instructable; no cropping, stitching, or whatever.
To launch, run: python screenshot.py