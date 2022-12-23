from PyQt5 import QtWidgets, uic


lista=[]

class Ventanaregistrop(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Ventanaregistrop, self).__init__(parent)
        uic.loadUi("UI_GRUPO5/UI/REGISTROPERSONAL.ui", self)

        self.btnSalir_3.clicked.connect(self.salir)
        self.btnRegistrar_3.clicked.connect(self.registrar)
        self.btnBorrar.clicked.connect(self.borrar)



    def registrar(self):
        nombres=self.txtNombre.text()
        apellidos=self.txtApellido.text()
        dni=self.txtDni.text()
        direccion=self.txtDireccion.text()
        ciudad=self.txtCiudad.text()
        telefono=self.txtTelefono.text()
        telefono2=self.txtTelefono2.text()
        whatsapp=self.cboWhatsaap.currentText()
        correo=self.txtCorreo.text()
        cargo=self.cboCargo.currentText()
       

    
        datos=(str(nombres), str(apellidos),str(dni),str(direccion),str(ciudad),
        str(telefono),str(telefono2),whatsapp,str(correo),cargo) ##Estos datos se añaden a la lista 
        lista.append(datos)
        self.listar()


    def listar(self): ##Este metodo permitira listar los datos de la lista a la tabla
        self.tblDatos_3.setRowCount(50)
        for i in range(len(lista)):
            self.tblDatos_3.setItem(i,0, QtWidgets.QTableWidgetItem(lista[i][0]))
            self.tblDatos_3.setItem(i,1, QtWidgets.QTableWidgetItem(lista[i][1]))
            self.tblDatos_3.setItem(i,2, QtWidgets.QTableWidgetItem(lista[i][2]))
            self.tblDatos_3.setItem(i,3, QtWidgets.QTableWidgetItem(lista[i][3]))
            self.tblDatos_3.setItem(i,4, QtWidgets.QTableWidgetItem(lista[i][4]))
            self.tblDatos_3.setItem(i,5, QtWidgets.QTableWidgetItem(lista[i][5]))
            self.tblDatos_3.setItem(i,6, QtWidgets.QTableWidgetItem(lista[i][6]))
            self.tblDatos_3.setItem(i,7, QtWidgets.QTableWidgetItem(lista[i][7]))
            self.tblDatos_3.setItem(i,8, QtWidgets.QTableWidgetItem(lista[i][8]))
            self.tblDatos_3.setItem(i,9, QtWidgets.QTableWidgetItem(lista[i][9]))




    def borrar(self):
        self.txtNombre.clear()
        self.txtApellido.clear()
        self.txtDni.clear()
        self.txtDireccion.clear()
        self.txtCiudad.clear()
        self.txtTelefono.clear()
        self.txtTelefono2.clear()
        self.cboWhatsaap.clear()
        self.txtCorreo.clear()
        self.cboCargo.clear()
        self.tblDatos_3.clear()
        

    def salir(self):
        self.close()


       