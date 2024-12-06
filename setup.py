from setuptools import setup, find_packages
import os

# Install fluidsynth using apt
# os.system('apt-get update && apt-get install -y fluidsynth')

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="giantmusictransformer",
    version="24.12.2",
    description="Fast multi-instrumental music transformer with true full MIDI instruments range, efficient encoding, octo-velocity and outro tokens",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Alex Lev",
    author_email="alexlev61@proton.me",
    url="https://github.com/asigalov61/giantmusictransformer",
    project_urls={
        "Examples": "https://github.com/asigalov61/giantmusictransformer/tegridymidi/example",
        "Issues": "https://github.com/asigalov61/giantmusictransformer/issues",
        "Documentation": "https://github.com/asigalov61/giantmusictransformer/docs",
        "Discussions": "https://github.com/asigalov61/giantmusictransformer/discussions",
        "Source Code": "https://github.com/asigalov61/giantmusictransformer",
        "Official GitHub Repo": "https://github.com/asigalov61/Giant-Music-Transformer",
        "Hugging Face Models Repo": "https://huggingface.co/asigalov61/Giant-Music-Transformer",
        "Hugging Face Spaces Deom": "https://huggingface.co/spaces/asigalov61/Giant-Music-Transformer"
    },
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'giantmusictransformer': ['/', 'seed_midis/', 'examples/'],
    },
    keywords=['MIDI', 'music', 'music ai', 'music transformer'],
    python_requires='>=3.6',
    license='Apache Software License 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',  
        'Operating System :: OS Independent',        
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12"
    ],
)