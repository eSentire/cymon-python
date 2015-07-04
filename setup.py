from distutils.core import setup

setup(
    name='cymon',
    packages=['cymon'],
    version='0.1',
    description='API wrapper for Cymon.io',
    author='Roy Firestein',
    author_email='info@cymon.io',
    url='https://github.com/eSentire/cymon-python',
    download_url='https://github.com/eSentire/cymon-python/tarball/0.1',
    keywords=['cymon', 'API', 'threat intelligence'],
    classifiers=[],
    requires=['requests']
)
