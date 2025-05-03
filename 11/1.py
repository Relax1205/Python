class MachineError(Exception):
    pass

class MooreMachine:
    def __init__(self):
        self.cur_state = 'u3'
        self.step_count = 0
        self.visited_edges = set()

        self.outputs = {
            'u0': 'D2',
            'u1': 'D4',
            'u2': 'D0',
            'u3': 'D3',
            'u4': 'D1',
            'u5': 'D1',
            'u6': 'D0',
        }

        self.transitions = {
            'u3': {'reset': 'u3', 'init': 'u0'},
            'u0': {'jog': 'u2', 'skip': 'u4'},
            'u4': {'jog': 'u1'},
            'u1': {'patch': 'u1', 'init': 'u2'},
            'u2': {'walk': 'u3', 'jog': 'u0', 'skip': 'u5'},
            'u5': {'skip': 'u6'},
            'u6': {}
        }

        # Compute incoming edge counts, ignoring self-loops
        self.in_edges_count = {state: 0 for state in self.transitions}
        for src, methods in self.transitions.items():
            for method, dst in methods.items():
                if dst != src:
                    self.in_edges_count[dst] += 1

        self.max_in_edges = max(self.in_edges_count.values())

    def run(self, name):
        if name not in self._all_known_methods():
            return 'unknown'
        next_state = self.transitions.get(self.cur_state, {}).get(name)
        if not next_state:
            return 'unsupported'
        self.visited_edges.add((self.cur_state, next_state))
        self.cur_state = next_state
        self.step_count += 1
        return None

    def _all_known_methods(self):
        return {method for trans in self.transitions.values() for method in trans}

    def get_output(self):
        return self.outputs[self.cur_state]

    def has_max_in_edges(self):
        return self.in_edges_count[self.cur_state] == self.max_in_edges

    def seen_edge(self, f, t):
        return (f, t) in self.visited_edges

    def get_step(self):
        return self.step_count


def main():
    return MooreMachine()



def test():
    obj = main()
    tests = [
        (obj.has_max_in_edges(), False),
        (obj.seen_edge('u4', 'u1'), False),
        (obj.run('init'), None),
        (obj.get_output(), 'D2'),
        (obj.run('mask'), 'unknown'),
        (obj.has_max_in_edges(), True),
        (obj.run('skip'), None),
        (obj.seen_edge('u2', 'u5'), False),
        (obj.get_output(), 'D1'),
        (obj.seen_edge('u3', 'u3'), False),
        (obj.get_step(), 2),
        (obj.has_max_in_edges(), False),
        (obj.run('jog'), None),
        (obj.get_output(), 'D4'),
        (obj.run('patch'), None),
        (obj.seen_edge('u0', 'u4'), True),
        (obj.get_output(), 'D4'),
        (obj.run('pan'), 'unknown'),
        (obj.run('init'), None),
        (obj.get_output(), 'D0'),
        (obj.seen_edge('u1', 'u1'), True),
        (obj.run('skip'), None),
        (obj.get_output(), 'D1'),
        (obj.run('paint'), 'unknown'),
        (obj.run('skip'), None),
        (obj.get_step(), 7),
        (obj.seen_edge('u3', 'u2'), False),
        (obj.get_output(), 'D0')
    ]

    for i, (res, exp) in enumerate(tests, 1):
        print(f"{i:2}. {'PASS' if res == exp else 'FAIL'}: Expected {exp}, got {res}")
    passed = sum(1 for res, exp in tests if res == exp)
    print(f"\nPassed: {passed}/{len(tests)}")

if __name__ == "__main__":
    test()
