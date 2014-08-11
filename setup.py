from setuptools import setup, find_packages

version = '0.1'

setup(
    name='shadowsocks-gtk',
    version=version,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    author='apporc',
    author_email='apporc@gmail.com',
    url='https://github.com/apporc/shadowsocks-gtk',
    license='http://opensource.org/licenses/MIT',
    description='ShadowSocks Gtk Client',
    install_requires=[],
    classifiers=[
        'Environment :: Desktop',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Internet :: Proxy'
        ],
    entry_points={
        'console_scripts': [
            'sslocal = shadowsocks_gtk.local:main',
        ],
        'gui_scripts': [
            'shadowsocks-gtk = shadowsocks_gtk.shadowsocks:main',
        ]
    }
)
