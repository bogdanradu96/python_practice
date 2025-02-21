from email import message_from_binary_file

import pytest
from pathlib import Path

@pytest.fixture
def memberships_file():

    project_root = Path(__file__).resolve().parent.parent  # Gets the root directory three levels up from "scripts"
    # Defines the output directory and file path
    folder_path = project_root / 'data'
    file_path = folder_path / 'memberships.csv'
    return file_path

def test_memberships_file_exists(memberships_file):
    assert memberships_file.exists(), f"Expected file {memberships_file} does not exist!"

def test_memberships_file_not_empty(memberships_file):
    with open(memberships_file, 'r') as csvfile:
        content = csvfile.read().strip()
    assert content, f"File {memberships_file} is empty!"