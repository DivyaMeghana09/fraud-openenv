from dataclasses import dataclass

@dataclass
class FraudObservation:
    duration: int
    frequency: int

@dataclass
class FraudAction:
    action: int

@dataclass
class FraudState:
    step_count: int