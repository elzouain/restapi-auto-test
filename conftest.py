import pytest


def pytest_runtest_makereport(item, call):
    if item.iter_markers(name='must_pass'):
        if call.excinfo is not None:
            parent = item.parent
            parent._mpfailed = item


def pytest_runtest_setup(item):
    must_pass_failed = getattr(item.parent, '_mpfailed', None)
    if must_pass_failed is not None:
        pytest.skip('must pass test failed (%s)' % must_pass_failed.name)
