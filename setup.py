from setuptools import find_packages, setup

setup(
    name='app',
    version='0.0.1',
    packages=find_packages(),
    license='MIT',
    install_requires=['tornado', 'prometheus-client'],
    author='Sergio Soto',
    description='Prometheus exporter for Tornado applications',
    classifiers=(
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'),
)
