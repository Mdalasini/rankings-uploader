from dataclasses import dataclass


@dataclass
class Team:
    team_name: str
    off_rank: int
    def_rank: int
