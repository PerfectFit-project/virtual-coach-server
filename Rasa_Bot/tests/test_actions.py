"""Unit tests for the custom actions"""
import pytest

from rasa_sdk.events import SlotSet

from tests.conftest import WEEKLY_PLAN_TRACKER

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from actions import actions

# Update once the function tested here works correctly
@pytest.mark.asyncio
async def test_run_action_save_plan_week_calendar(dispatcher, domain):
    tracker = WEEKLY_PLAN_TRACKER
    action = actions.SavePlanWeekCalendar()
    events = await action.run(dispatcher, tracker, domain)
    expected_events = [
        SlotSet("success_save_calendar_plan_week", True),
    ]
    assert events == expected_events