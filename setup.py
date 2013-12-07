from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='trem.passagens',
      version=version,
      description="Formulario para cadastro de locais e viagens de trem.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='trem',
      author='Matheus Pereira',
      author_email='matheper@gmail.com',
      url='https://github.com/matheper/trem.passagens',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['trem'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
#      setup_requires=["PasteScript"],
#      paster_plugins=["ZopeSkel"],
      )
