[] This algorithm will find the longest path of increasing integers in a torus.

[] Some details:

    --> If there are multiple paths of equal length, any of them may be returned.
    --> The path is a list of (x, y) tuples. (So the path is of the form [(x1, y1), (x2, y2), ... ] not [[x1, y1], [x2, y2], ...].)
    --> The path must start with the (x, y) coordinates with the lowest value in the path.
    --> A path must have at least two elements. If there are no valid paths, return [].
    --> If torus is None or has an m or n dimension that is 0, return [].
