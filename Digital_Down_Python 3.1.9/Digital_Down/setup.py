from setuptools import setup, find_packages

setup(
    name="Digital_Down",
    version="3.1.9",
    # Project URLs
    url="https://github.com/Digital-Down/Digital_Down_Python",
    description="Multimedia Programs",
    long_description='Audio Processing, Video Animation',
    platforms=["any"],
    keywords=["Digital Down", "Audio Processing", "Animation"],
    license="Custom (See Package for Details)",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'soundfile',
        'opencv-python',
        'moviepy',
    ],
)