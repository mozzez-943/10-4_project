from setuptools import setup, find_packages

setup(
    name='montecarlo_ode_solver',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
    ],
    author='Moeez Omair',
    author_email='moeez.omair@example.com',
    description='Monte Carlo ODE Solver using Importance Sampling and Quasi-Monte Carlo',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
