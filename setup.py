import setuptools

setuptools.setup(
    name='gists_id',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
