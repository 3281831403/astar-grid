"""网格 A*：堆、启发式与路径：待实现的核心模块。"""


def manhattan(a, b):
    """曼哈顿距离。"""
    raise NotImplementedError

def heap_push(heap, priority, node):
    """二叉堆插入。"""
    raise NotImplementedError

def heap_pop(heap):
    """二叉堆弹出最小项。"""
    raise NotImplementedError

def astar_path(grid, start, goal):
    """A* 路径。"""
    raise NotImplementedError

def astar_distance(grid, start, goal):
    """A* 距离，无路 -1。"""
    raise NotImplementedError
