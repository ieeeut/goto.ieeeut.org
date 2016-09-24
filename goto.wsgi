import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/ieeeut.org/goto/public_html')

from goto import app as application
