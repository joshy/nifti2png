from setuptools import setup, find_packages

setup(
    name="nifti2png",
    version="0.0.1",
    url="https://github.com/joshy/nifti2png.git",
    author="Joshy Cyriac",
    author_email="j.cyriac@gmail.com",
    description="Converts nifti to png, _not_ a general purpose converter",
    packages=find_packages(),
    install_requires=[
        "tqdm>=4.24"
    ],
    entry_points={"console_scripts": ["nifti2png = nifti2png.__main__:main"]},
)
