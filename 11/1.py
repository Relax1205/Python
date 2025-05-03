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
            'u3': {'reset': 'u3', 'init': 'u0', 'walk': 'u2'},
            'u0': {'skip': 'u4'},
            'u4': {'jog': 'u1'},
            'u1': {'patch': 'u1', 'init': 'u2'},
            'u2': {'jog': 'u0', 'skip': 'u5'},
            'u5': {'skip': 'u6'},
            'u6': {}
        }

        self.in_edges_count = {state: 0 for state in self.transitions}
        for src, edges in self.transitions.items():
            for _, dst in edges.items():
                self.in_edges_count[dst] += 1

        self.max_in_edges = max(self.in_edges_count.values())

    def run(self, name):
        if name not in self._all_known_methods():
            return 'unknown'

        next_state = self.transitions.get(self.cur_state, {}).get(name)
        if next_state is None:
            return 'unsupported'

        self.visited_edges.add((self.cur_state, next_state))
        self.cur_state = next_state
        self.step_count += 1
        return None

    def _all_known_methods(self):
        return {
            method
            for trans in self.transitions.values()
            for method in trans
        }

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


def test_run():
    obj = main()
    obj.run('init')
    assert obj.get_output() == 'D2'
    obj.run('skip')
    assert obj.get_output() == 'D1'


def test_unsupported():
    obj = main()
    result = obj.run('skip')
    assert result == 'unsupported'


def test_unknown():
    obj = main()
    result = obj.run('non_existent')
    assert result == 'unknown'


def test_seen_edge():
    obj = main()
    obj.run('init')
    obj.run('skip')
    assert obj.seen_edge('u0', 'u4')


def test_max_in_edges():
    obj = main()
    assert not obj.has_max_in_edges()


def test_get_step():
    obj = main()
    obj.run('init')
    obj.run('skip')
    assert obj.get_step() == 2


def test():
    test_run()
    test_unsupported()
    test_unknown()
    test_seen_edge()
    test_max_in_edges()
    test_get_step()
