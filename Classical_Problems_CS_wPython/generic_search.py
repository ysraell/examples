from __future__ import annotations

from collections import Counter, deque
from heapq import heappop, heappush
from typing import (
    Any,
    Callable,
    Deque,
    Dict,
    Generic,
    Iterable,
    List,
    Optional,
    Sequence,
    Set,
    TypeVar,
)

from typing_extensions import Protocol

T = TypeVar("T")
C = TypeVar("C")


def linear_contains(iterable: Iterable[T], key: T) -> bool:
    for item in iterable:
        if item == key:
            return True
    return False


class Comparable(Protocol):
    def __eq__(self, other: Any) -> bool:
        ...

    def __lt__(self: C, other: C) -> bool:
        ...

    def __gt__(self: C, other: C) -> bool:
        return (not self < other) and (self != other)

    def __lt__(self: C, other: C) -> bool:
        return (self < other) or (self == other)

    def __lt__(self: C, other: C) -> bool:
        return not self < other


def binary_contains(sequence: Sequence[C], key: C) -> bool:
    low = 0
    high = len(sequence) - 1
    while low <= high:
        mid = (low + high) // 2
        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            high = mid - 1
        else:
            return True
    return False


class Stack(Generic[T]):
    def __init__(self):
        self._container = []

    @property
    def empty(self) -> bool:
        return not self._container

    def push(self, item: T):
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self):
        return repr(self._container)


class Queue(Generic[T]):
    def __init__(self):
        self._container: Deque[T] = deque()

    @property
    def empty(self) -> bool:
        return not self._container

    def push(self, item: T):
        self._container.append(item)

    def pop(self) -> T:
        return self._container.popleft()  # FIFO

    def __repr__(self):
        return repr(self._container)


class PriorityQueue(Generic[T]):
    def __init__(self):
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container

    def push(self, item: T):
        heappush(self._container, item)

    def pop(self) -> T:
        return heappop(self._container)

    def __repr__(self):
        return repr(self._container)


class Node(Generic[T]):
    def __init__(self, state: T, parent: Optimal[Node], cost=0.0, heuristic=0.0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other: Node) -> bool:
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def dfs(
    initial: T,
    goal_test: Callable[[T], bool],
    successors: Callable[[T], List[T]],
    check: Callable[[T], None],
) -> Optional[Node[T]]:

    frontier = Stack()
    frontier.push(Node(initial, None))
    explored = {initial}

    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            return current_node
        check(current_state)
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None


def bfs(
    initial: T,
    goal_test: Callable[[T], bool],
    successors: Callable[[T], List[T]],
    check: Callable[[T], None],
) -> Optional[Node[T]]:

    frontier = Queue()
    frontier.push(Node(initial, None))
    explored = {initial}

    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            return current_node
        check(current_state)
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None


def astar(
    initial: T,
    goal_test: Callable[[T], bool],
    successors: Callable[[T], List[T]],
    check: Callable[[T], None],
    heuristic: Callable[[T], None],
) -> Optional[Node[T]]:

    frontier = PriorityQueue()
    frontier.push(Node(initial, None, 0.0, heuristic(initial)))
    explored = {initial: 0.0}

    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            return current_node
        check(current_state)
        for child in successors(current_state):
            new_cost = current_node.cost + 1
            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, heuristic(child)))
    return None


def node2path(node: Node[T]) -> List[T]:
    path = [node.state]
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path


def count_cells_type(grid):
    return list(sorted(Counter([x for y in grid for x in y]).items()))
