from distutils.core import setup
setup(
  name = 'LibSerial23',       
  packages = ['LibSerial23'],   
  version = '0.1',      
  license='MIT',       
  description = 'Biblioteca LibSerial23 ',   
  author = 'Andre Moreira',                  
  author_email = 'almsantana@bol.com.br',     
  url = 'https://github.com/AMOREIRA23/LibSerial23',  
  download_url = 'https://github.com/AMOREIRA23/LibSerial23/archive/0.1.tar.gz',    
  keywords = ['Serial', 'Senai', 'ComPort'],  
  install_requires=[           
          'datetime',
          'random',         
      ],
  classifiers=[
    #"3 - Alpha", "4 - Beta" or "5 - Production/Stable"   
    'Development Status :: 5 - Production/Stable',   
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
  ],
)