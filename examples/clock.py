from datetime import datetime

from fluepdot import Fluepdot
from PIL import ImageFont

"""
Renders the current time. For up-to-date information, run once per minute using e.g. cron.
Centering and y offset depends on chosen font.
Run as a module using `python3 -m examples.clock`.
"""

current_time = datetime.now().strftime('%-H:%M')
centered = current_time.center(10)

fluepdot = Fluepdot('127.0.0.1', rendering_mode=Fluepdot.RenderingMode.DIFFERENTIAL)
fluepdot.render_text(centered, font=ImageFont.truetype('Starjedi', 22), x=0, y=-11)
fluepdot.update()
