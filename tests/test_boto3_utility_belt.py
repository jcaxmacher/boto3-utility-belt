import os
from pathlib import Path

import pytest
from moto import mock_sts

from boto3_utility_belt import __version__, get_refreshable_profile_session


def test_version():
    assert __version__ == "0.1.0"


@pytest.fixture(scope="module")
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    moto_credentials_file_path = (
        Path(__file__).parent.absolute() / "dummy_aws_credentials"
    )
    os.environ["AWS_SHARED_CREDENTIALS_FILE"] = str(moto_credentials_file_path)


@mock_sts
def test_refreshable_profile_session(aws_credentials):
    session = get_refreshable_profile_session(profile_name="test123")
