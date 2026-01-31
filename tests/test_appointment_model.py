from models.appointment import Appointment
from datetime import datetime, timedelta, timezone


def test_end_time_property():
    start = datetime(2026, 1, 1, 10, 0, tzinfo=timezone.utc)

    appt = Appointment(
        start_time=start,
        duration_minutes=30,
    )

    assert appt.end_time == start + timedelta(minutes=30)
