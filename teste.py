from sap import sapgui

sap = sapgui.SapGui()
print("objeto instanciado")
sap.logon()
sap.session.findById('wnd[0]/tbar[0]/okcd').text = 'FBL3N'
