# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['transform_tk.py'],
             pathex=['C:\\Users\\Joy\\El\\Projects\\Python\\Py\\Computer graphics Transformation\\py\\gui\\tk'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries+ [('flow.ico', 'flow.ico', 'DATA')],
          a.zipfiles,
          a.datas,  
          [],
          name='TransformationApp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='flow.ico')
