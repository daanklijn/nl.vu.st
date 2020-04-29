"""Tests for heartmonitor.logger package."""
import pytest
import heartbeatmonitor
import logger
from datetime import datetime
import pathlib
import os

LOG_FOLDER_NAME = (
    str(pathlib.Path(__file__).parent.absolute().parent.absolute())
    + os.path.sep
    + "test_logs"
)
logger.LOG_FOLDER_NAME = (
    str(pathlib.Path(__file__).parent.absolute().parent.absolute())
    + os.path.sep
    + "test_logs"
)
PARENT_FOLDER = (
    str(pathlib.Path(__file__).parent.absolute().parent.absolute()) + os.path.sep
)


def test_logger1(capsys):
    """Log folder doesn't exist"""
    """MAKE SURE LOG FOLDER DOESN'T EXIST"""
    assert not os.path.exists(LOG_FOLDER_NAME)
    date = datetime.now().strftime("%d-%m-%y")
    logger.log("abc" + os.linesep)
    assert os.path.exists(LOG_FOLDER_NAME)
    logfilename = LOG_FOLDER_NAME + os.path.sep + date
    assert os.path.exists(logfilename)
    logfile = open(logfilename, "r")
    lines = logfile.readlines()
    assert lines[0] == "abc\n"


def test_logger2(capsys):
    """Log folder does exist"""
    """MAKE SURE LOG FOLDER DOES EXIST"""
    assert os.path.exists(LOG_FOLDER_NAME)
    date = datetime.now().strftime("%d-%m-%y")
    logfilename = LOG_FOLDER_NAME + os.path.sep + date
    logger.log("abc")
    assert os.path.exists(LOG_FOLDER_NAME)
    logfile = open(logfilename, "r")
    lines = logfile.readlines()
    assert lines[0] == "abc\n"
    assert lines[1] == "abc"
    os.remove(logfilename)
    os.rmdir(LOG_FOLDER_NAME)