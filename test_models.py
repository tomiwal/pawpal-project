import pytest
from models import Owner, Pet, Task, Schedule, Scheduler


def test_task_priority_values():
    """Test that priority values map correctly"""
    task_high = Task("Walk", "high", 30, "daily")
    task_medium = Task("Feed", "medium", 10, "daily")
    task_low = Task("Play", "low", 60, "daily")

    assert task_high.get_priority_value() == 3
    assert task_medium.get_priority_value() == 2
    assert task_low.get_priority_value() == 1


def test_sort_by_priority():
    """Test that tasks are sorted by priority correctly"""
    tasks = [
        Task("Play", "low", 60, "daily"),
        Task("Walk", "high", 30, "daily"),
        Task("Feed", "medium", 10, "daily"),
    ]

    owner = Owner("James", [], 480)
    pet = Pet("Mochi", "dog", 3, [])
    scheduler = Scheduler(owner, pet, tasks)

    sorted_tasks = scheduler.sort_tasks_by_priority(tasks)

    assert sorted_tasks[0].priority.lower() == "high"
    assert sorted_tasks[1].priority.lower() == "medium"
    assert sorted_tasks[2].priority.lower() == "low"


def test_generate_plan_fits_in_time():
    """Test that scheduler only includes tasks that fit in available time"""
    tasks = [
        Task("Walk", "high", 200, "daily"),
        Task("Feed", "high", 200, "daily"),
        Task("Play", "medium", 200, "daily"),  # Won't fit
    ]

    owner = Owner("James", [], 400)  # Only 400 minutes available
    pet = Pet("Mochi", "dog", 3, [])
    scheduler = Scheduler(owner, pet, tasks)

    schedule = scheduler.generate_plan()

    assert len(schedule.tasks) == 2  # Only first two tasks fit
    assert schedule.total_time_minutes == 400


def test_add_preference():
    """Test adding preferences to owner"""
    owner = Owner("James", [], 480)
    owner.add_preference("early morning")
    owner.add_preference("evening")

    prefs = owner.get_preferences()
    assert len(prefs) == 2
    assert "early morning" in prefs


def test_is_due_today():
    """Test is_due_today for daily tasks"""
    task_daily = Task("Walk", "high", 30, "daily")
    task_weekly = Task("Bath", "low", 60, "weekly")

    assert task_daily.is_due_today() == True
    assert task_weekly.is_due_today() == False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
