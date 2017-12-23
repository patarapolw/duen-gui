# -*- mode: python -*-

block_cipher = None


a = Analysis(['duen-gui.pyw'],
             pathex=['/Users/patarapolw/Dropbox/Uploads/duendecat'],
             binaries=[],
             datas=[('duendecat.xlsx', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='duen-gui',
          debug=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='duen-gui')
app = BUNDLE(coll,
             name='duen-gui.app',
             icon=None,
             bundle_identifier=None)
