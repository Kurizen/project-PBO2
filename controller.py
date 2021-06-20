from os import error
import wx
import project
import sqlite3
import pathlib

con = sqlite3.connect(r"D:\Documents\SEMESTER 4\PBO2\project\dbproject.db")

wxframe = project.Masuk
class MyGui(wxframe) :
    def __init__(self, parent) :
        wxframe.__init__(self, parent)
    
    def m_buttonMasukOnButtonClick(self, event):
        self.Close()
        frame1 = MyGui1(None)
        frame1.Show()

wxframe1 = project.Home
class MyGui1(wxframe1) :
    def __init__(self, parent) :
        wxframe1.__init__(self, parent)
        self.con = sqlite3.connect(r"D:\Documents\SEMESTER 4\PBO2\project\dbproject.db")
        self.cursor = self.con.cursor()

    def executeQuery(self, query, retVal=False) :
        self.cursor.execute(query)
        all_results = self.cursor.fetchall()
        self.con.commit()
        if retVal :
            return all_results
    
    def sql_fetch(self, posisi, kondisi) :
        sql = 'SELECT diagnosa FROM Penyakit WHERE posisi=? AND kondisi=?'
        cursorObj = con.cursor()
        cursorObj.execute(sql, (posisi, kondisi,))
        rows = cursorObj.fetchall()
        for row in rows :
            return(row)

    def m_buttonDiagnosaOnButtonClick(self, event) :
        posisi = self.m_pilihPosisi.GetValue()
        kondisi = self.m_pilihKondisi.GetValue()
        hasil = MyGui1.sql_fetch(con, posisi, kondisi)
        self.m_hasilDiagnosa.SetValue(str(hasil))
