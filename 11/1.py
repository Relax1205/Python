class MealyError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Mealy:
    def __init__(self):
        self.state = 'u3'
        self.output = 'D3'
        self.step_count = 0
        self.edge_history = set()
        self.last_action = None

        self.transitions = {
            'u3': {'reset': ('u3', 'D3'), 'init': ('u0', 'D2')},
            'u0': {'skip': ('u4', 'D1')},
            'u4': {'walk': ('u1', 'D4'), 'jog': ('u1', 'D4')},
            'u1': {'patch': ('u2', 'D0'), 'init': ('u2', 'D0')},
            'u2': {'skip': ('u5', 'D1')},
            'u5': {'skip': ('u6', 'D0')},
            'u6': {}
        }

        self.outputs = {
            'u3': 'D3',
            'u0': 'D2',
            'u4': 'D1',
            'u1': 'D4',
            'u2': 'D0',
            'u5': 'D1',
            'u6': 'D0'
        }

        self.in_edges_count = {
            'u3': 1,
            'u0': 1,
            'u4': 1,
            'u1': 2,
            'u2': 2,
            'u5': 1,
            'u6': 1
        }

        self.max_in_edges = max(self.in_edges_count.values())

    def run(self, action):
        if action not in ['reset', 'init', 'skip', 'walk', 'jog', 'patch']:
            return 'unknown'

        if action not in self.transitions[self.state]:
            return 'unsupported'

        prev_state = self.state
        self.state, _ = self.transitions[self.state][action]
        self.output = self.outputs[self.state]
        self.step_count += 1
        self.edge_history.add((prev_state, action, self.state))
        self.last_action = action
        return None

    def get_output(self):
        return self.output

    def has_max_in_edges(self):
        return self.in_edges_count[self.state] == self.max_in_edges

    def seen_edge(self, from_state, to_state):
        return any(src == from_state and dst == to_state
                   for (src, act, dst) in self.edge_history)

    def get_step(self):
        return self.step_count


def main():
    return Mealy()


def test_mealy_error():
    try:
        raise MealyError("test message")
    except MealyError as e:
        assert str(e) == "test message"


def test_initial_state():
    obj = main()
    assert obj.get_output() == 'D3'
    assert not obj.has_max_in_edges()
    assert not obj.seen_edge('u3', 'u3')
    assert obj.get_step() == 0


def test_reset_and_init():
    obj = main()
    assert obj.run('reset') is None
    assert obj.get_output() == 'D3'
    assert obj.seen_edge('u3', 'u3')
    assert obj.run('init') is None
    assert obj.get_output() == 'D2'
    assert obj.seen_edge('u3', 'u0')
    assert obj.get_step() == 2


def test_invalid_actions():
    obj = main()
    obj.run('init')
    assert obj.run('invalid') == 'unknown'
    assert obj.run('walk') == 'unsupported'
    assert obj.get_step() == 1


def test_full_path_with_patch():
    obj = main()
    obj.run('init')
    obj.run('skip')
    obj.run('walk')
    obj.run('patch')
    obj.run('skip')
    obj.run('skip')
    assert obj.get_output() == 'D0'
    assert obj.get_step() == 6
    assert obj.run('skip') == 'unsupported'


def test_full_path_with_init():
    obj = main()
    obj.run('init')
    obj.run('skip')
    obj.run('jog')
    obj.run('init')
    obj.run('skip')
    obj.run('skip')
    assert obj.get_output() == 'D0'
    assert obj.get_step() == 6
    assert obj.run('skip') == 'unsupported'


def test_jog_transition():
    obj = main()
    obj.run('init')
    obj.run('skip')
    assert obj.run('jog') is None
    assert obj.get_output() == 'D4'
    assert obj.seen_edge('u4', 'u1')
    assert obj.get_step() == 3


def test_all_seen_edges():
    obj = main()
    obj.run('init')
    obj.run('skip')
    obj.run('walk')
    obj.run('patch')
    obj.run('skip')
    obj.run('skip')
    assert obj.seen_edge('u3', 'u0')
    assert obj.seen_edge('u0', 'u4')
    assert obj.seen_edge('u4', 'u1')
    assert obj.seen_edge('u1', 'u2')
    assert obj.seen_edge('u2', 'u5')
    assert obj.seen_edge('u5', 'u6')
    assert not obj.seen_edge('u6', 'u6')
    assert not obj.seen_edge('u3', 'u4')


def test_has_max_in_edges():
    obj = main()
    obj.run('init')
    obj.run('skip')
    obj.run('walk')
    assert obj.has_max_in_edges()
    obj.run('patch')
    assert obj.has_max_in_edges()
    obj.run('skip')
    assert not obj.has_max_in_edges()
    obj.run('skip')
    assert not obj.has_max_in_edges()


def test_multiple_resets():
    obj = main()
    obj.run('reset')
    obj.run('reset')
    assert obj.seen_edge('u3', 'u3')
    assert obj.get_step() == 2


def test_no_transition_for_state():
    obj = main()
    obj.run('init')  # State u0
    assert obj.run('walk') == 'unsupported'
    assert obj.run('patch') == 'unsupported'
    assert obj.get_step() == 1


def test_no_action_for_state():
    obj = main()
    obj.run('init')  # State u0
    assert obj.run('invalid_action') == 'unknown'


def test_final_state_behavior():
    obj = main()
    obj.run('init')
    obj.run('skip')
    obj.run('walk')
    obj.run('patch')
    obj.run('skip')
    obj.run('skip')
    assert obj.run('reset') == 'unsupported'
    assert obj.run('init') == 'unsupported'
    assert obj.run('skip') == 'unsupported'
    assert obj.run('walk') == 'unsupported'
    assert obj.run('jog') == 'unsupported'
    assert obj.run('patch') == 'unsupported'
    assert obj.get_step() == 6


def run_tests():
    test_mealy_error()
    test_initial_state()
    test_reset_and_init()
    test_invalid_actions()
    test_full_path_with_patch()
    test_full_path_with_init()
    test_jog_transition()
    test_all_seen_edges()
    test_has_max_in_edges()
    test_multiple_resets()
    test_no_transition_for_state()
    test_no_action_for_state()
    test_final_state_behavior()


def test():
    run_tests()


test()