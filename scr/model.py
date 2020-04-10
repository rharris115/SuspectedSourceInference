from enum import IntEnum, auto, unique


@unique
class State(IntEnum):
    SUSCEPTIBLE = auto()
    INFECTED = auto()
    INFECTIOUS = auto()
    SYMPTOMATIC_INFECTIOUS = auto()
    REMOVED = auto()

    def infectious(self):
        return self == State.INFECTIOUS or self == State.SYMPTOMATIC_INFECTIOUS

    def susceptible(self):
        return self == State.SUSCEPTIBLE


class Agent:

    def __init__(self, name: str):
        self._name: str = name
        self._state: State = State.SUSCEPTIBLE

    @property
    def name(self) -> str:
        return self._name

    @property
    def state(self) -> State:
        return self._state

    @state.setter
    def state(self, value: State):
        assert self._state < value, f'Illegal state transition. {self._state} -> {value}'
        self._state = value

    def __repr__(self):
        return f'{self.name}: {self.state.name}'
