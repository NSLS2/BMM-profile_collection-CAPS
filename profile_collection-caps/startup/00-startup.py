from bluesky import RunEngine
from bluesky.callbacks.tiled_writer import TiledWriter
from tiled.client import from_uri
from bluesky.callbacks.best_effort import BestEffortCallback

import bluesky.plans as bp

bec = BestEffortCallback()

cat = from_uri('http://127.0.0.1:8000', api_key='capscaps')
tw = TiledWriter(cat)
RE = RunEngine({})
RE.subscribe(tw)
RE.subscribe(bec)
