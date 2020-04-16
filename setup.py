from setuptools import setup, find_packages

setup(
    name="accel-code", packages=find_packages(),
    entry_points={
        "console_scripts": [
            "accel_transform = accel_code.run:main",
        ],
    },
)
