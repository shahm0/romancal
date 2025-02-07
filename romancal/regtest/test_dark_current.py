"""Regression test for the Dark current subtraction step."""
import pytest

from romancal.stpipe import RomanStep
from .regtestdata import compare_asdf


@pytest.mark.bigdata
def test_dark_current_subtraction_step(rtdata, ignore_asdf_paths):
    """ Function to run and compare Dark Current subtraction files. Note: This
        should include tests for overrides etc. """
    rtdata.get_data(
        "WFI/image/r0000101001001001001_01101_0001_WFI01_linearity.asdf")
    rtdata.input = "r0000101001001001001_01101_0001_WFI01_linearity.asdf"

    args = ["romancal.step.DarkCurrentStep", rtdata.input]
    RomanStep.from_cmdline(args)
    output =\
        "r0000101001001001001_01101_0001_WFI01_linearity_darkcurrentstep.asdf"
    rtdata.output = output
    rtdata.get_truth(f"truth/WFI/image/{output}")
    assert (compare_asdf(rtdata.output, rtdata.truth,
            **ignore_asdf_paths) is None)


@pytest.mark.bigdata
def test_dark_current_outfile_step(rtdata, ignore_asdf_paths):
    """ Function to run and compare Dark Current subtraction files. Here the
        test is for renaming the output file. """
    rtdata.get_data(
        "WFI/image/r0000101001001001001_01101_0001_WFI01_linearity.asdf")
    rtdata.input = "r0000101001001001001_01101_0001_WFI01_linearity.asdf"

    args = ["romancal.step.DarkCurrentStep", rtdata.input,
            '--output_file=Test_dark']
    RomanStep.from_cmdline(args)
    output = "Test_dark_darkcurrentstep.asdf"
    rtdata.output = output
    rtdata.get_truth(f"truth/WFI/image/{output}")
    assert (compare_asdf(rtdata.output, rtdata.truth,
            **ignore_asdf_paths) is None)


@pytest.mark.bigdata
def test_dark_current_outfile_suffix(rtdata, ignore_asdf_paths):
    """ Function to run and compare Dark Current subtraction files. Here the
        test is for renaming the output file. """
    rtdata.get_data(
        "WFI/image/r0000101001001001001_01101_0001_WFI01_linearity.asdf")
    rtdata.input = "r0000101001001001001_01101_0001_WFI01_linearity.asdf"

    args = ["romancal.step.DarkCurrentStep", rtdata.input,
            '--output_file=Test_dark', '--suffix="suffix_test"']
    RomanStep.from_cmdline(args)
    output = "Test_dark_suffix_test.asdf"
    rtdata.output = output
    rtdata.get_truth(f"truth/WFI/image/{output}")
    assert (compare_asdf(rtdata.output, rtdata.truth,
            **ignore_asdf_paths) is None)


@pytest.mark.xfail(reason='RCAL-285 should address this failure')
@pytest.mark.bigdata
def test_dark_current_output(rtdata, ignore_asdf_paths):
    """ Function to run and compare Dark Current subtraction files. Here the
        test for overriding the CRDS dark reference file. """

    rtdata.get_data(
        "WFI/image/r0000101001001001001_01101_0001_WFI01_linearity.asdf")
    rtdata.input = "r0000101001001001001_01101_0001_WFI01_linearity.asdf"
    dark_output_name = \
        "r0000101001001001001_01101_0001_WFI01_linearity_darkcurrentstep.asdf"

    args = ["romancal.step.DarkCurrentStep",
            rtdata.input,
            f"--dark_output={dark_output_name}"]
    RomanStep.from_cmdline(args)
    output =\
        "r0000101001001001001_01101_0001_WFI01_linearity_darkcurrentstep.asdf"
    rtdata.output = output
    rtdata.get_truth(f"truth/WFI/image/{output}")
    assert (compare_asdf(rtdata.output, rtdata.truth,
            **ignore_asdf_paths) is None)
