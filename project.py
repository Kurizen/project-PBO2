import wx
import wx.xrc

## Class Masuk

class Masuk ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Masuk QuickCheck", pos = wx.DefaultPosition, size = wx.Size( 449,204 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_username = wx.StaticText( self, wx.ID_ANY, u"Username :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_username.Wrap( -1 )
		gSizer4.Add( self.m_username, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_inputUsername = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_inputUsername, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer2.Add( gSizer4, 1, wx.EXPAND, 5 )
		
		self.m_buttonMasuk = wx.Button( self, wx.ID_ANY, u"Masuk", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_buttonMasuk, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_buttonMasuk.Bind( wx.EVT_BUTTON, self.m_buttonMasukOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_buttonMasukOnButtonClick( self, event ):
		event.Skip()
	
## Class Home

class Home ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Beranda", pos = wx.DefaultPosition, size = wx.Size( 700,278 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_inputPosisi = wx.StaticText( self, wx.ID_ANY, u"Bagian Tubuh yang Mengalami Keluhan :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_inputPosisi.Wrap( -1 )
		gSizer6.Add( self.m_inputPosisi, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		m_pilihPosisiChoices = [ u"Kepala", u"Dada", u"Kaki" ]
		self.m_pilihPosisi = wx.ComboBox( self, wx.ID_ANY, u"Pilih", wx.DefaultPosition, wx.Size( 150,-1 ), m_pilihPosisiChoices, 0 )
		gSizer6.Add( self.m_pilihPosisi, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_inputKondisi = wx.StaticText( self, wx.ID_ANY, u"Keluhan :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_inputKondisi.Wrap( -1 )
		gSizer6.Add( self.m_inputKondisi, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		m_pilihKondisiChoices = [ u"Bengkak", u"Nyeri" ]
		self.m_pilihKondisi = wx.ComboBox( self, wx.ID_ANY, u"Pilih", wx.DefaultPosition, wx.Size( 150,-1 ), m_pilihKondisiChoices, 0 )
		gSizer6.Add( self.m_pilihKondisi, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer3.Add( gSizer6, 1, wx.EXPAND, 5 )
		
		self.m_buttonDiagnosa = wx.Button( self, wx.ID_ANY, u"Diagnosa", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_buttonDiagnosa, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer7 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_teksHasil = wx.StaticText( self, wx.ID_ANY, u"Hasil Diagnosa :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_teksHasil.Wrap( -1 )
		gSizer7.Add( self.m_teksHasil, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_hasilDiagnosa = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY )
		gSizer7.Add( self.m_hasilDiagnosa, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer3.Add( gSizer7, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_pilihPosisi.Bind( wx.EVT_COMBOBOX, self.m_pilihPosisiOnCombobox )
		self.m_pilihPosisi.Bind( wx.EVT_TEXT, self.m_pilihPosisiOnText )
		self.m_pilihPosisi.Bind( wx.EVT_TEXT_ENTER, self.m_pilihPosisiOnTextEnter )
		self.m_pilihKondisi.Bind( wx.EVT_COMBOBOX, self.m_pilihKondisiOnCombobox )
		self.m_pilihKondisi.Bind( wx.EVT_TEXT, self.m_pilihKondisiOnText )
		self.m_pilihKondisi.Bind( wx.EVT_TEXT_ENTER, self.m_pilihKondisiOnTextEnter )
		self.m_buttonDiagnosa.Bind( wx.EVT_BUTTON, self.m_buttonDiagnosaOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_pilihPosisiOnCombobox( self, event ):
		event.Skip()
	
	def m_pilihPosisiOnText( self, event ):
		event.Skip()
	
	def m_pilihPosisiOnTextEnter( self, event ):
		event.Skip()
	
	def m_pilihKondisiOnCombobox( self, event ):
		event.Skip()
	
	def m_pilihKondisiOnText( self, event ):
		event.Skip()
	
	def m_pilihKondisiOnTextEnter( self, event ):
		event.Skip()
	
	def m_buttonDiagnosaOnButtonClick( self, event ):
		event.Skip()
	