from setuptools import setup

setup(
    name='humanhash',
    version='1.0.0',
    description='Algorithm for generating natural-language-based cryptographic hashes',
    author='Nima Khazaei',
    author_email='nima@khazaei.net',
    url='http://khazaei.net/projects/humanhash/',
    packages=['hhlib'],
    long_description="""\
        An algorithm for generating cryptographic hashes in the form of English sentences.
        """,
    classifiers=[
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Internet",
        "Topic :: Security :: Cryptography",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Natural Language :: English"
    ],
    keywords='cryptography hash checksum natural-language',
    license='ISC',
    install_requires=[
        'setuptools'
    ],
)
