import unittest
from GYM import Gym, action_status, not_found
from Member import Member
from Trainer import Trainer, not_found as trainer_not_found
from Membership import Membership, not_found as membership_not_found
from Payment import Payment
from Attendance import Attendance


class TestGym(unittest.TestCase):

    # ==========================================
    # SUCCESS TESTS - 3
    # ==========================================

    def test_add_member(self):
        gym = Gym()

        member = Member(
            "M001",
            "01012345678",
            "Ahmed",
            "ahmed@gmail.com"
        )

        gym.add_member(member)

        self.assertEqual(len(gym.members), 1)

    def test_add_trainer(self):
        gym = Gym()

        trainer = Trainer(
            "T001",
            "01098765432",
            "Mohamed",
            "fitness"
        )

        gym.add_trainer(trainer)

        self.assertEqual(len(gym.trainers), 1)

    def test_add_payment(self):
        gym = Gym()

        member = Member(
            "M001",
            "01012345678",
            "Ahmed",
            "ahmed@gmail.com"
        )

        payment = Payment(
            "P001",
            member,
            500,
            (2026, 9, 28)
        )

        gym.add_payment(payment)

        self.assertEqual(len(gym.payments), 1)

    # ==========================================
    # INVALID INPUT TESTS - 3
    # ==========================================

    def test_invalid_trainer_specialty(self):
        with self.assertRaises(trainer_not_found):
            Trainer(
                "T001",
                "01098765432",
                "Mohamed",
                "swimming"
            )

    def test_invalid_membership_type(self):
        member = Member(
            "M001",
            "01012345678",
            "Ahmed",
            "ahmed@gmail.com"
        )

        with self.assertRaises(membership_not_found):
            Membership(
                "MS001",
                (2026, 9, 1),
                (2026, 10, 1),
                "weekly",
                member
            )

    def test_invalid_payment_amount(self):
        member = Member(
            "M001",
            "01012345678",
            "Ahmed",
            "ahmed@gmail.com"
        )

        with self.assertRaises(ValueError):
            Payment(
                "P001",
                member,
                0,
                (2026, 9, 28)
            )

    # ==========================================
    # BUSINESS RULE VIOLATIONS - 2
    # ==========================================

    def test_member_cannot_have_two_active_memberships(self):
        gym = Gym()

        member = Member(
            "M001",
            "01012345678",
            "Ahmed",
            "ahmed@gmail.com"
        )

        gym.add_member(member)

        first_membership = Membership(
            "MS001",
            (2026, 9, 1),
            (2026, 12, 1),
            "quarterly",
            member
        )

        second_membership = Membership(
            "MS002",
            (2026, 9, 10),
            (2026, 12, 10),
            "quarterly",
            member
        )

        gym.add_membership(first_membership)

        with self.assertRaises(action_status):
            gym.add_membership(second_membership)

    def test_expired_member_cannot_attend(self):
        gym = Gym()

        member = Member(
            "M001",
            "01012345678",
            "Ahmed",
            "ahmed@gmail.com"
        )

        gym.add_member(member)

        expired_membership = Membership(
            "MS001",
            (2025, 1, 1),
            (2025, 2, 1),
            "monthly",
            member
        )

        gym.memberships.append(expired_membership)

        attendance = Attendance(
            "A001",
            member,
            (2026, 9, 28)
        )

        self.assertEqual(attendance.member, member)

        with self.assertRaises(action_status):
            gym.member_attendace(
                attendance,
                expired_membership
            )

    # ==========================================
    # EDGE CASES - 2
    # ==========================================

    def test_search_non_existing_member(self):
        gym = Gym()

        with self.assertRaises(not_found):
            gym.search_member("M999")

    def test_empty_gym_dashboard(self):
        gym = Gym()

        dashboard = gym.dashboard()

        self.assertEqual(dashboard["total_members"], 0)
        self.assertEqual(dashboard["total_trainers"], 0)
        self.assertEqual(dashboard["active_memberships"], 0)
        self.assertEqual(dashboard["expired_memberships"], 0)
        self.assertEqual(dashboard["total_payments"], 0)
        self.assertEqual(dashboard["total_attendance"], 0)


# ==========================================
# RUN TESTS
# ==========================================

if __name__ == "__main__":
    unittest.main()

