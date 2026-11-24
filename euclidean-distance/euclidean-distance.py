import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    a=np.array(x)
    b=np.array(y)
    return float(np.linalg.norm(a-b))