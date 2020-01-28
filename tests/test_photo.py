#!/usr/bin/env python
import pytest
from datetime import date
from photo import Photo

@pytest.fixture
def test_subject():
    return "TEST SUBJECT"


@pytest.fixture
def test_date():
    return date(2020, 1, 1)


@pytest.fixture
def test_photo(test_subject, test_date):
    return Photo(test_subject, test_date)


def test_object_matches_date_arg(test_photo, test_date):
    assert test_photo.date == test_date


def test_object_matches_subject_arg(test_photo, test_subject):
    assert test_photo.subject == test_subject
