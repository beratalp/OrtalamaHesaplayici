# -*- coding: utf-8 -*-
from __future__ import division

from Tkinter import *
from tkMessageBox import *

def calculaterror():
    showerror(title="Hata",message="Hesaplama işlemi sırasında bir sorun oluştu.",detail="Tüm notları doğru bir şekilde girdiğinizi kontrol edin ve tekrar deneyin.")

def setting():
    showerror(title="Hata",message="Bu program Pursaklar Fen Lisesi 9. sınıf öğrencileri için hazırlanmıştır",detail="Lütfen yeni sürümün çıkmasını bekleyiniz.")
def about():
    showinfo(title="Hakkında",message="Ortalama Hesaplayıcı v0.1WIN",detail="2012 Berat Alp Erbil-beratalp@goldos.org\nBu program GNU/GPLv3 Lisansıyla lisanslanmıştır.")
def calculate():
    try:
        matnot=float(mat.get())*4
        edenot=float(ede.get())*3
        tarnot=float(tar.get())*2
        dvanot=float(dva.get())*2
        cognot=float(cog.get())*2
        geonot=float(geo.get())*2
        ingnot=float(ing.get())*7
        almnot=float(alm.get())*2
        fiznot=float(fiz.get())*2
        biynot=float(biy.get())*2
        sagnot=float(sag.get())*1
        kimnot=float(kim.get())*2
        brmnot=float(brm.get())*2
        dkabnot=float(dkab.get())*1
        toplam=matnot+edenot+tarnot+dvanot+cognot+geonot+ingnot+almnot+fiznot+biynot+sagnot+kimnot+brmnot+dkabnot
        ort=toplam/34
        if ort>=85:
            belge = "Belge: Takdir"
        elif ort>=70:
            belge="Belge: Teşekkür"
        else:
            belge="Belge alamadınız."
        showinfo(title="Sonuç",message="Ortalamanız: %s"%ort,detail=belge)
    except:
        calculaterror()



MainWindow = Tk()
MainWindow.title("Ortalama Hesaplayıcı v0.1WIN")
MainWindow.geometry("310x315")
menu=Menu(MainWindow)
MainWindow.config(menu=menu)
file=Menu(menu)
menu.add_cascade(label="Dosya",menu=file)
file.add_command(label="Çık",command=MainWindow.quit)
settings=Menu(menu)
menu.add_cascade(label="Ayarlar",menu=settings)
settings.add_command(label="Ortalama Hesaplayıcı Ayarları",command=setting)
help=Menu(menu)
menu.add_cascade(label="Yardım",menu=help)
help.add_command(label="Hakkında",command=about)
mat=Entry()
mat.insert(END,"Matematik")
mat.pack()
ede=Entry()
ede.insert(END,"Edebiyat")
ede.pack()
tar=Entry()
tar.insert(END,"Tarih")
tar.pack()
dva=Entry()
dva.insert(END,"Dil ve Anlatım")
dva.pack()
cog=Entry()
cog.insert(END,"Coğrafya")
cog.pack()
geo=Entry()
geo.insert(END,"Geometri")
geo.pack()
ing=Entry()
ing.insert(END,"İngilizce")
ing.pack()
alm=Entry()
alm.insert(END,"Almanca")
alm.pack()
fiz=Entry()
fiz.insert(END,"Fizik")
fiz.pack()
biy=Entry()
biy.insert(END,"Biyoloji")
biy.pack()
sag=Entry()
sag.insert(END,"Sağlık")
sag.pack()
kim=Entry()
kim.insert(END,"Kimya")
kim.pack()
brm=Entry()
brm.insert(END,"BRM")
brm.pack()
dkab=Entry()
dkab.insert(END,"Din Kültürü")
dkab.pack()
calc=Button(text="Hesapla!",command=calculate)
calc.pack()
MainWindow.mainloop()