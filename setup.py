from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='clean folder from trash',
    url='http://github.com/dummy_user/useful',
    author='Alena Mishchenko',
    author_email='a_mertel@ukr.net',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts':['clean-folder = clean_folder.clean:main']
    },
)
    
    