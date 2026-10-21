
import unittest

from event_scheduler import can_attend_all, min_rooms_required


class TestEventScheduler(unittest.TestCase):
    def test_no_overlapping_events(self):
        events = [(9, 10), (10, 11), (11, 12)]

        self.assertTrue(can_attend_all(events))

    def test_overlapping_events(self):
        events = [(9, 11), (10, 12)]

        self.assertFalse(can_attend_all(events))

    def test_empty_events(self):
        self.assertTrue(can_attend_all([]))

    def test_one_event(self):
        self.assertTrue(can_attend_all([(9, 10)]))

    def test_minimum_rooms_required(self):
        events = [(9, 10), (9, 11), (10, 12)]

        self.assertEqual(min_rooms_required(events), 2)

    def test_all_events_overlap(self):
        events = [(1, 5), (2, 6), (3, 7)]

        self.assertEqual(min_rooms_required(events), 3)

    def test_empty_schedule_needs_no_rooms(self):
        self.assertEqual(min_rooms_required([]), 0)

    def test_adjacent_events_reuse_room(self):
        events = [(9, 10), (10, 11), (11, 12)]

        self.assertEqual(min_rooms_required(events), 1)


if __name__ == "__main__":
    unittest.main()
