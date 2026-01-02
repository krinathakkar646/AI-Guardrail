from setuptools import setup

setup(
    name='ai-guardrail',
    version='1.0.0',
    description='A CLI tool to detect and block prompt injection attacks on LLMs.',
    author='Your Name',
    py_modules=['guardrail'],  # This assumes your script is named guardrail.py
    install_requires=[
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'guardrail=guardrail:main',
        ],
    },
)
