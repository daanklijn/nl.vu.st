"""Tests for `heartmonitor.entity` package."""
import pytest
import heartbeatmonitor
import datetime


def test_help(capsys):
    """Correct name argument and printing"""
    heartbeatmonitor.print_help()
    captured = capsys.readouterr()
    lines = captured.out.split("\n")
    assert "Usage: HB-Sim2020 [options]" == lines[0]
    assert "Options:" == lines[1]
    assert "\t--path <file>" == lines[2]
    assert (
        "Where file is a CSV file containing the headers oxygen, pulse, blood_pressure_systolic, blood_pressure_diastolic in any order."
        == lines[3]
    )
    assert "" == lines[4]
    assert (
        "The system will generate a status for each measurement, these statuses should be interpreted as follows:"
        == lines[5]
    )
    assert "OK:               A reading that is not considered dangerous." == lines[6]
    assert (
        "MISSING:          A reading that is not considered a valid reading."
        == lines[7]
    )
    assert (
        "MINOR:            A reading that is of interest to medical personnel but cannot be considered a threat yet."
        == lines[8]
    )
    assert (
        "MAJOR:            A reading that is of interest to medical personnel and has to be considered a threat."
        == lines[9]
    )
    assert (
        "LIFE_THREATENING: A reading that is of interest to medical personnel because it can have severe effects on the chance of survival of the patient."
        == lines[10]
    )


def test_MEASUREMENT_INTERVAL_IN_MS(capsys):
    """Testing MEASUREMENT_INTERVAL_IN_MS"""
    assert heartbeatmonitor.MEASUREMENT_INTERVAL_IN_MS == 1000


def test_MILLISECONDS_IN_SECOND(capsys):
    """Testing MILLISECONDS_IN_SECOND"""
    assert heartbeatmonitor.MILLISECONDS_IN_SECOND == 1000


def test_wait_on_new_measurement(capsys):
    """Testing wait_on_new_measurement"""
    before_timestamp = datetime.datetime.now().timestamp()
    assert heartbeatmonitor.wait_on_new_measurement() is None
    difference = (datetime.datetime.now().timestamp() - before_timestamp) * 1000
    assert difference - 10 <= heartbeatmonitor.MEASUREMENT_INTERVAL_IN_MS
    assert difference + 10 >= heartbeatmonitor.MEASUREMENT_INTERVAL_IN_MS
