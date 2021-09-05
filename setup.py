from setuptools import setup

setup(
    name='open_python',
    version='1.0.0',
    packages=['open_python'],
    license='MIT',
    install_requires=[
        'six',
        'importlib; python_version == "2.6"',
    ],
)
