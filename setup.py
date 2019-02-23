from setuptools import setup, find_packages

setup(
    name='AAAAAA',
    description='A VVVVVV inspired arcade game.',
    version='0.0.1',
    author='ROYALBEFF',
    license='MIT',
    platforms='ALL',
    install_requires=['pygame>=1.9.4'],
    packages=find_packages(),
    package_data={'': ['*.png']},
    entry_points={'console_scripts': ['aaaaaa = aaaaaa:main']}
)
