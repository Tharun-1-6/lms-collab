# loan_management.py (Student C - Issue #3)

from datetime import timedelta

LOAN_DAYS = 14
FINE_PER_DAY = 2  # rupees


def due_date(issue_date):
    """Return the due date, 14 days after the issue date."""
    return issue_date + timedelta(days=LOAN_DAYS)


def calculate_fine(issue_date, return_date):
    """Calculate the fine for a late returned book."""

    if return_date < issue_date:
        raise ValueError("Return date cannot be before issue date")

    days_late = (return_date - due_date(issue_date)).days

    return max(0, days_late) * FINE_PER_DAY
