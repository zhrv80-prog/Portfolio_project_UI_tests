from time import sleep

import pytest
from selene import browser, have, be


def test_draft(username, password):
    assert False