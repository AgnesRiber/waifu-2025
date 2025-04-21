from setuptools import setup, find_packages

setup(
    name="waifu_agnes",
    version="1.0.0",
    author="Agnes",
    description="Waifu2x Version 2025",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AgnesRiber/waifu-2025",
    packages=find_packages(),
    install_requires=[
        "numpy==1.24.0",
        "Pillow==10.0.0",
        "Wand==0.6.10",
        "chainer==7.4.0"
    ],
    python_requires=">=3.8",
)
