from robot.api import SuiteVisitor
from robot.parsing.model import _TestData


class _TestDataNameHelper(_TestData):
    """Remove the dependency on *_table's being defined, so that we can get name the same way as TestData"""
    def _get_tables(self, *args, **kwargs):
        # robot.utils NormalizedDict accepts None as a valid input
        return None


class SourceName(SuiteVisitor):
    """Set name based on the source regardless of name changes.

    Is the complement of name (-N, --name). Sets what would've been selected as the default name if name hadn't been
    used. Useful so external log data of original name isn't needed.
    """
    def start_suite(self, suite):
        if suite.source:
            suite.name = _TestDataNameHelper(source=suite.source).name
