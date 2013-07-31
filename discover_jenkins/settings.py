from django.conf import settings


TASKS = getattr(settings, 'TEST_TASKS', (
    'discover_jenkins.tasks.run_pylint',
    'discover_jenkins.tasks.with_coverage',
))
OUTPUT_DIR = getattr(settings, 'TEST_OUTPUT_DIR', 'reports')
PYLINT_RCFILE = getattr(settings, 'TEST_PYLINT_RCFILE', 'pylint.rc')
PROJECT_APPS = getattr(settings, 'TEST_PROJECT_APPS', ())

COVERAGE_WITH_MIGRATIONS = getattr(settings, 'TEST_COVERAGE_WITH_MIGRATIONS', False)
COVERAGE_REPORT_HTML_DIR = getattr(settings, 'TEST_COVERAGE_REPORT_HTML_DIR', '')
COVERAGE_MEASURE_BRANCH = getattr(settings, 'TEST_COVERAGE_MEASURE_BRANCH', True)
COVERAGE_EXCLUDES = getattr(settings, 'TEST_COVERAGE_EXCLUDES', [])
COVERAGE_EXCLUDES_FOLDERS = getattr(settings, 'TEST_COVERAGE_EXCLUDES_FOLDERS', [])
COVERAGE_RCFILE = getattr(settings, 'TEST_COVERAGE_RCFILE', 'coverage.rc')
