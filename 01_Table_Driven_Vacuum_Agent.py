                      # Practical 1: Table-Driven Vacuum Agent
class TableDrivenVacuumAgent:
    def __init__(self):
        # The percept history of the agent
        self.percept_history = []

        # Look-up table: maps a sequence of percepts to a specific action
        # Percept format: (Location, Status)
        self.table = {
            # Time step 1: Single percept sequences
            ((('A', 'Clean'),),): 'Right',
            ((('A', 'Dirty'),),): 'Suck',
            ((('B', 'Clean'),),): 'Left',
            ((('B', 'Dirty'),),): 'Suck',

            # Time step 2: Two percept sequences
            ((('A', 'Clean'),), (('B', 'Dirty'),)): 'Suck',
            ((('A', 'Clean'),), (('B', 'Clean'),)): 'Right',
            ((('A', 'Dirty'),), (('A', 'Clean'),)): 'Right',
            ((('B', 'Dirty'),), (('B', 'Clean'),)): 'Left',

            # Time step 3: Three percept sequences
            ((('A', 'Dirty'),), (('A', 'Clean'),), (('B', 'Dirty'),)): 'Suck',
            ((('A', 'Dirty'),), (('A', 'Clean'),), (('B', 'Clean'),)): 'Left',
        }

    def act(self, current_percept):
        """Append the current percept to history and look up the next action."""
        self.percept_history.append(current_percept)
        history_key = tuple(self.percept_history)
        return self.table.get(history_key, 'Right')


if __name__ == "__main__":
    agent = TableDrivenVacuumAgent()

    percept_1 = ('A', 'Dirty')
    print(f"Percept: {percept_1} -> Action: {agent.act(percept_1)}")

    percept_2 = ('A', 'Clean')
    print(f"Percept: {percept_2} -> Action: {agent.act(percept_2)}")

    percept_3 = ('B', 'Dirty')
    print(f"Percept: {percept_3} -> Action: {agent.act(percept_3)}")
