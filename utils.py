""" Utility functions used by the feeder package """

def shape(hmap):
    """ Given a dictionary return its approximate shape """
    _shape = {}

    if not isinstance(hmap, dict):
        return type(hmap)

    for key, val in hmap.items():
        if isinstance(val, dict):
            _shape[key] = shape(val) 
        elif isinstance(val, list):
            _shape[key] = [shape(val[0])] if val else []
        else: 
            _shape[key] = type(val)

    return _shape
