'''
This module exposes geometry data for World Country Boundaries.
'''

import csv
import codecs
import gzip
import xml.etree.cElementTree as et
from os.path import dirname, join, abspath

nan = float('NaN')

data = {}

with gzip.open(abspath('./data/World_Country_Boundaries.csv.gz')) as f:
    decoded = codecs.iterdecode(f, "utf-8")
    next(decoded)
    reader = csv.reader(decoded, delimiter=',', quotechar='"')
    for row in reader:
        geometry, code, name = row
        xml = et.fromstring(geometry)
        lats = []
        lons = []
        for i, poly in enumerate(xml.findall('.//outerBoundaryIs/LinearRing/coordinates')):
            if i > 0:
                lats.append(nan)
                lons.append(nan)
            coords = (c.split(',')[:2] for c in poly.text.split())
            lat, lon = list(zip(*[(float(lat), float(lon)) for lon, lat in
                coords]))
            lats.extend(lat)
            lons.extend(lon)
        data[code] = {
            'name'   : name,
            'lats'   : lats,
            'lons'   : lons,
        }
