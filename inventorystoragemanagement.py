from tkinter import *
import mysql.connector as myp
from datetime import datetime

rt= Tk()
rt.title('AVRN Project')
rt.geometry('1000x400')
def add_pur():
    art= Tk() #Creates New Window for Adding Details
    art.title('Adding Purchase Order')
    
    def add_items():
        irt= Tk()
        irt.title('Add Items')
        def add_moreitems():
            #Connect To Database
            conn = myp.connect(
            host="localhost",
            user="root",
            passwd="1234",
            database="avrn_rfiddb"
            )
            #Create Cursor
            cur = conn.cursor()
            #Insert Into Table trn_itemdetails
            now = datetime.now()
            sql3= "INSERT INTO trn_itemdetails(I_POID, V_ItemCode, V_InvoiceNumber, N_Quantity, Dt_Created)  VALUES (%s,%s,%s,%s,%s)"
            val3= (poidno, V_ItemCode.get(), V_InvoiceNumber.get(), N_Quantity.get(), now) 
            cur.execute(sql3,val3) 

            #Commit Change
            conn.commit()
            #Close Connection
            conn.close()
            #Clear The Text Boxes
            refresh()
        
        addlab= Label(irt, text= 'Add Item Details', relief= SUNKEN, anchor=W)
        addlab.grid(row=0, column=1)
        #Connect To Database
        conn = myp.connect(
        host="localhost",
        user="root",
        passwd="1234",
        database="avrn_rfiddb"
        )
        #Create Cursor
        cur = conn.cursor()
        #Entry Boxes for trn_itemdtails
        V_ItemCode= Entry(irt, width=30)
        V_ItemCode.grid(row=14,column=1)
        V_InvoiceNumber= Entry(irt, width=30)
        V_InvoiceNumber.grid(row=15,column=1)
        N_Quantity= Entry(irt, width=30)
        N_Quantity.grid(row=16,column=1)
        #Create Text Box Labels for trn_itemdetails
        V_ItemCodelab= Label(irt, text='Item Code')
        V_ItemCodelab.grid(row=14,column=0)
        V_InvoiceNumberlab= Label(irt, text='Invoice Number')
        V_InvoiceNumberlab.grid(row=15,column=0)
        N_Quantitylab= Label(irt, text='Quantity')
        N_Quantitylab.grid(row=16,column=0)
        #Create Submit Button
        subbut= Button(irt, text= 'Submit & Close', command= lambda:[add_moreitems(), irt.destroy()])
        subbut.grid(row=17, column=0, columnspan=2, pady=10, padx=10) 
        #Create Add More Button
        addmoreitems= Button(irt, text='Submit & Add More Items', command= lambda:[add_moreitems(),irt.destroy(),add_items()])
        addmoreitems.grid(row= 18, column=0, columnspan=2, pady=10, padx=10)

        #Commit Change
        conn.commit()
        #Close Connection
        conn.close()
        #Clear The Text Boxes
        V_Code.delete(0, END)
        V_Name.delete(0, END)
        V_Address.delete(0, END)
        N_Mobile.delete(0, END)
        N_Phone.delete(0, END)
        V_Email.delete(0, END)
        V_PONumber.delete(0, END)
        V_RMCode.delete(0, END)
        I_QuantityOrdered.delete(0, END)
        irt.geometry('400x400')
        irt.mainloop()
    def submit():
        #Connect To Database
        conn = myp.connect(
        host="localhost",
        user="root",
        passwd="1234",
        database="avrn_rfiddb"
        )
        #Create Cursor
        cur = conn.cursor()
        now = datetime.now()
        #Insert Into Table mst_vendor
        sql1= "INSERT INTO mst_vendor(V_Code, V_Name, V_Address, N_Mobile, N_Phone, V_Email, Dt_Created)  VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val1= (V_Code.get(), V_Name.get(), V_Address.get(), N_Mobile.get(), N_Phone.get(), V_Email.get(), now)
        cur.execute(sql1,val1) 
        #Fetching auto generated I_VendorID from mst_vendor for trn_povendors
        venidf= "SELECT I_VendorID FROM mst_vendor WHERE V_Code= "+str(V_Code.get())
        cur.execute(venidf)
        venid= cur.fetchone()
        global venidno
        venidno= int(''.join(map(str, venid)))
        #Insert Into Table trn_povendors
        sql2= "INSERT INTO trn_povendors(I_VendorID, V_PONumber, V_RMCode, Dt_PODate, I_QuantityOrdered, Dt_Created)  VALUES (%s,%s,%s,%s,%s,%s)"
        val2= (venidno, V_PONumber.get(), V_RMCode.get(), now, I_QuantityOrdered.get(), now)
        cur.execute(sql2,val2) 
        #Fetching auto generated I_POID from trn_povendors for trn_itemdetails
        poidf= "SELECT I_POID FROM trn_povendors WHERE V_PONumber= "+str(V_PONumber.get())
        cur.execute(poidf)
        poid= cur.fetchone()
        global poidno
        poidno= int(''.join(map(str, poid))) #Converts Tupple data into integer
        #Commit Change
        conn.commit()
        #Close Connection
        conn.close()
        


    #Entry Boxes for trn_povendors
    txt2= Label(art, text= 'Add Purchase Order Details', relief= SUNKEN, anchor=W)
    txt2.grid(row=0,column=0, columnspan= 2)
    V_PONumber= Entry(art, width=30)
    V_PONumber.grid(row=1,column=1)
    V_RMCode= Entry(art, width=30)
    V_RMCode.grid(row=2,column=1)
    I_QuantityOrdered= Entry(art, width=30)
    I_QuantityOrdered.grid(row=3,column=1)

    #Entry Boxes for mst_vendor
    txt1= Label(art, text= 'Add Vendor Details', relief= SUNKEN, anchor=W)
    txt1.grid(row=5,column=0, columnspan= 2)
    V_Code= Entry(art, width=30)
    V_Code.grid(row=7,column=1)
    V_Name= Entry(art, width=30)
    V_Name.grid(row=8,column=1)
    V_Address= Entry(art, width=30)
    V_Address.grid(row=9,column=1)
    N_Mobile= Entry(art, width=30)
    N_Mobile.grid(row=10,column=1)
    N_Phone= Entry(art, width=30)
    N_Phone.grid(row=11,column=1)
    V_Email= Entry(art, width=30)
    V_Email.grid(row=12,column=1)

    #Entry Boxes for trn_itemdtails
    txt3= Label(art, text= 'Add Item Details', relief= SUNKEN, anchor=W)
    txt3.grid(row=13,column=0, columnspan= 2)
    addmore= Button(art, text= '+', command= lambda: [submit(),add_items()])
    addmore.grid(row= 13, column= 1)

    #Create Text Box Labels for trn_povendors
    V_PONumberlab= Label(art, text='PO Number')
    V_PONumberlab.grid(row=1,column=0)
    V_RMCodelab= Label(art, text='RM Code')
    V_RMCodelab.grid(row=2,column=0)
    I_QuantityOrderedlab= Label(art, text='Total Quantity Ordered')
    I_QuantityOrderedlab.grid(row=3,column=0)

    #Create Text Box Labels for mst_vendor
    V_Codelab= Label(art, text='Code')
    V_Codelab.grid(row=7,column=0)
    V_Namelab= Label(art, text='Name')
    V_Namelab.grid(row=8,column=0)
    V_Addresslab= Label(art, text='Address')
    V_Addresslab.grid(row=9,column=0)
    N_Mobilelab= Label(art, text='Mobile')
    N_Mobilelab.grid(row=10,column=0)
    N_Phonelab= Label(art, text='Phone')
    N_Phonelab.grid(row=11,column=0)
    V_Emaillab= Label(art, text='Email')
    V_Emaillab.grid(row=12,column=0)

    art.geometry('400x410')
#Create Menu Bar
menubar= Menu(rt)
rt.config(menu= menubar)
#Create Submenu
submenu= Menu(menubar, tearoff= 0)
menubar.add_cascade(label= "File", menu=submenu)
submenu.add_command(label= 'Add PO', command= add_pur)
submenu.add_command(label= 'Exit', command= rt.destroy)

def search_id():
    ert= Tk() #Creates new window for search display
    ert.title('Record Search')
    #Connect To Database
    conn = myp.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="avrn_rfiddb"
    )
    #Create Cursor
    cur = conn.cursor()
    #Fetches Record by comparing search id with V_PONumber
    sql4="SELECT a.V_PONumber, b.V_Name, a.V_RMCode, a.Dt_PODate, a.I_QuantityOrdered, a.I_QuantityReceived, a.Dt_LastUpdated FROM trn_povendors a LEFT JOIN mst_vendor b on a.I_VendorID=b.I_VendorID WHERE a.DisplayFlag = '1' AND a.V_PONumber= "+str(searchpo.get())
    cur.execute(sql4) 
    tabpovend1= cur.fetchall()
    #Creates Labels for Table Display
    polab1= Label(ert, text= 'PO Number')
    polab1.grid(row=2, column=0)
    polab2= Label(ert, text= 'Vendor Name')
    polab2.grid(row=2, column=1)
    polab3= Label(ert, text= 'RM Code')
    polab3.grid(row=2, column=2)
    polab4= Label(ert, text= 'Creation Date')
    polab4.grid(row=2, column=3)
    polab5= Label(ert, text= 'Total Quantity Ordered')
    polab5.grid(row=2, column=4)
    polab6= Label(ert, text= 'Total Quantity Recieved')
    polab6.grid(row=2, column=5)
    polab7= Label(ert, text= 'Last Entry')
    polab7.grid(row=2, column=6)
    #Loop through results
    printpo=[]
    for tabs in tabpovend1:
        for i in range(7):
            printpo.append(str(tabs[i]))
            poprint= Label(ert, text= printpo[i])
            poprint.grid(row=3, column=0+i)
    #Create Entry Labels for updating values
    polab1Ent= Entry(ert, width=20)
    polab1Ent.grid(row=4,column=0)
    polab1Ent.insert(INSERT, printpo[0])
    polab2Ent= Entry(ert, width=20)
    polab2Ent.grid(row=4,column=1)
    polab2Ent.insert(INSERT, printpo[1])
    polab3Ent= Entry(ert, width=20)
    polab3Ent.grid(row=4,column=2)
    polab3Ent.insert(INSERT, printpo[2])

    polab5Ent= Entry(ert, width=20)
    polab5Ent.grid(row=4,column=4)
    polab5Ent.insert(INSERT, printpo[4])
    polab6Ent= Entry(ert, width=20)
    polab6Ent.grid(row=4,column=5)
    polab6Ent.insert(INSERT, printpo[5])
    
    #Creating an Update Records Function
    def upd():
        #Connect To Database
        conn = myp.connect(
        host="localhost",
        user="root",
        passwd="1234",
        database="avrn_rfiddb"
        )
        #Create Cursor
        cur = conn.cursor()
        #Updating records
        now = datetime.now()
        sql5= "UPDATE trn_povendors tp, mst_vendor mv SET tp.V_PONumber= %s, mv.V_Name= %s, tp.V_RMCode= %s, tp.I_QuantityOrdered= %s, tp.I_QuantityReceived= %s, tp.Dt_LastUpdated= %s WHERE tp.I_VendorID=mv.I_VendorID AND tp.V_PONumber= %s AND tp.DisplayFlag = '1'"
        val5=(str(polab1Ent.get()), str(polab2Ent.get()), str(polab3Ent.get()), str(polab5Ent.get()), str(polab6Ent.get()), now, str(searchpo.get()))
        cur.execute(sql5,val5)
        #Commit Change
        conn.commit()
        #Close Connection
        conn.close()
        #Destroy Window & Restart
        ert.destroy()
        refresh()
        search_id()
    #Creating Del Function. This Function does'nt actually delete record but rather turns DisplayFlag to 0
    def delrec():
        #Connect To Database
        conn = myp.connect(
        host="localhost",
        user="root",
        passwd="1234",
        database="avrn_rfiddb"
        )
        #Create Cursor
        cur = conn.cursor()
        #Deleting records
        now = datetime.now()
        sql5= "UPDATE trn_povendors tp SET tp.DisplayFlag= '0', tp.Dt_LastUpdated= %s WHERE tp.V_PONumber= %s AND tp.DisplayFlag = '1'"
        val5=(now, str(searchpo.get()))
        cur.execute(sql5,val5)
        #Commit Change
        conn.commit()
        #Close Connection
        conn.close()
        #Destroy Window 
        ert.destroy()
        refresh()
        
    #Creating an Update Button
    update_but= Button(ert, text= 'Update Records', command= upd)
    update_but.grid(row=6, column=2, padx= 20, pady=20)
    #Creating a Delete Button
    del_but= Button(ert, text= 'Delete Records', command= delrec)
    del_but.grid(row=6, column= 4, padx= 20, pady=20)
    ert.geometry('900x400')
    #Commit Change
    conn.commit()
    #Close Connection
    conn.close()
    ert.mainloop()

#Function To Refresh Mainpage
def refresh():
    #Connect To Database
    conn = myp.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="avrn_rfiddb"
    )
    #Create Cursor
    cur = conn.cursor()
    #Display Tables for last 10 purchase orders
    cur.execute("SELECT a.V_PONumber, b.V_Name, a.V_RMCode, a.Dt_PODate, a.I_QuantityOrdered, a.I_QuantityReceived, a.Dt_LastUpdated FROM trn_povendors a LEFT JOIN mst_vendor b on (a.I_VendorID=b.I_VendorID) WHERE a.DisplayFlag = '1'") #Can change query code here to bring last 10 records according to desc order of date stamp
    tabpovend= cur.fetchmany(10)
    polab1= Label(rt, text= 'PO Number')
    polab1.grid(row=2, column=0)
    polab2= Label(rt, text= 'Vendor Name')
    polab2.grid(row=2, column=1)
    polab3= Label(rt, text= 'RM Code')
    polab3.grid(row=2, column=2)
    polab4= Label(rt, text= 'Creation Date')
    polab4.grid(row=2, column=3)
    polab5= Label(rt, text= 'Total Quantity Ordered')
    polab5.grid(row=2, column=4)
    polab6= Label(rt, text= 'Total Quantity Recieved')
    polab6.grid(row=2, column=5)
    polab7= Label(rt, text= 'Last Entry')
    polab7.grid(row=2, column=6)
    #Clear Screen
    a=-1
    for j in range(10):
        a=a+1
        for i in range(7):
            poprint= Label(rt, text= '                                           ')
            poprint.grid(row=3+a, column=0+i)
    #Loop through results
    a=-1
    for tab in tabpovend:
        a=a+1
        for i in range(7):
            printpo= str(tab[i])
            poprint= Label(rt, text= printpo)
            poprint.grid(row=3+a, column=0+i)

    #Commit Change
    conn.commit()
    #Close Connection
    conn.close()

#Connect To Database
conn = myp.connect(
  host="localhost",
  user="root",
  passwd="1234",
  database="avrn_rfiddb"
)
#Create Cursor
cur = conn.cursor()
#Search PO Number Label and Entry Field
searchpolab= Label(rt, text='Enter PO Number')
searchpolab.grid(row=0, column=0)
searchpo= Entry(rt, width= 30)
searchpo.grid(row=0, column= 1)
#Create Search PO Number Button
search_but= Button(rt, text="Search", command= search_id) 
search_but.grid(row=0, column=2)
#Create Refresh Button
ref_but= Button(rt, text= 'Refresh', command= refresh)
ref_but.grid(row=0, column= 3)

#Display Tables for last 10 purchase orders
cur.execute("SELECT a.V_PONumber, b.V_Name, a.V_RMCode, a.Dt_PODate, a.I_QuantityOrdered, a.I_QuantityReceived, a.Dt_LastUpdated FROM trn_povendors a LEFT JOIN mst_vendor b on a.I_VendorID=b.I_VendorID WHERE a.DisplayFlag = '1'") #Can change query code here to bring last 10 records according to desc order of date stamp
tabpovend= cur.fetchmany(10)
polab1= Label(rt, text= 'PO Number')
polab1.grid(row=2, column=0)
polab2= Label(rt, text= 'Vendor Name')
polab2.grid(row=2, column=1)
polab3= Label(rt, text= 'RM Code')
polab3.grid(row=2, column=2)
polab4= Label(rt, text= 'Creation Date')
polab4.grid(row=2, column=3)
polab5= Label(rt, text= 'Total Quantity Ordered')
polab5.grid(row=2, column=4)
polab6= Label(rt, text= 'Total Quantity Recieved')
polab6.grid(row=2, column=5)
polab7= Label(rt, text= 'Last Entry')
polab7.grid(row=2, column=6)
#Loop through results
a=0
for tab in tabpovend:
    a=a+1
    for i in range(7):
        printpo= str(tab[i])
        poprint= Label(rt, text= printpo)
        poprint.grid(row=3+a, column=0+i)

#Commit Change
conn.commit()
#Close Connection
conn.close()

rt.mainloop()