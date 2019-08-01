from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import numpy, h5py, os

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
current_dir = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):

        # Fonts
        font_headline = QtGui.QFont()
        font_headline.setPointSize(8)
        font_headline.setBold(True)

        font_graphs = QtGui.QFont()
        font_graphs.setPixelSize(10)
        font_graphs.setBold(False)

        font_graphs_2 = QtGui.QFont()
        font_graphs_2.setPixelSize(1)
        font_graphs_2.setBold(False)

        font_ee = QtGui.QFont()
        font_ee.setPointSize(7)
        font_ee.setBold(False)

        # Graphs background
        pg.setConfigOption('background', (255, 255, 255))
        pg.setConfigOption('foreground', 'k')

        # Main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(665, 548)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(665, 548))
        MainWindow.setMaximumSize(QtCore.QSize(665, 548))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setWindowTitle("SuperADAM .h5 detector images subtractor")
        MainWindow.setWindowIcon(QtGui.QIcon(current_dir + "\icon.png"))
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Block: scan A
        self.label_scan_A = QtWidgets.QLabel(self.centralwidget)
        self.label_scan_A.setGeometry(QtCore.QRect(15, 0, 47, 13))
        self.label_scan_A.setObjectName("label_scan_A")
        self.label_scan_A.setText("Scan A")
        self.label_scan_A.setFont(font_headline)
        self.groupBox_scan_A = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_scan_A.setGeometry(QtCore.QRect(5, -3, 199, 254))
        self.groupBox_scan_A.setObjectName("groupBox_scan_A")
        self.lineEdit_name_scan_A = QtWidgets.QLineEdit(self.groupBox_scan_A)
        self.lineEdit_name_scan_A.setGeometry(QtCore.QRect(5, 22, 168, 16))
        self.lineEdit_name_scan_A.setObjectName("lineEdit_name_scan_B")
        self.lineEdit_name_scan_A.setFont(font_ee)
        self.toolButton_scan_A = QtWidgets.QToolButton(self.groupBox_scan_A)
        self.toolButton_scan_A.setGeometry(QtCore.QRect(175, 22, 20, 16))
        self.toolButton_scan_A.setObjectName("toolButton_scan_B")
        self.toolButton_scan_A.setText("...")
        self.toolButton_scan_A.setFont(font_ee)
        self.label_polarisation_A = QtWidgets.QLabel(self.groupBox_scan_A)
        self.label_polarisation_A.setFont(font_ee)
        self.label_polarisation_A.setGeometry(QtCore.QRect(5, 40, 21, 16))
        self.label_polarisation_A.setObjectName("label_polarisation_A")
        self.label_polarisation_A.setText("Pol.")
        self.comboBox_polarisation_A = QtWidgets.QComboBox(self.groupBox_scan_A)
        self.comboBox_polarisation_A.setFont(font_ee)
        self.comboBox_polarisation_A.setGeometry(QtCore.QRect(25, 40, 40, 16))
        self.comboBox_polarisation_A.setObjectName("comboBox_polarisation_A")
        self.label_point_number_A = QtWidgets.QLabel(self.groupBox_scan_A)
        self.label_point_number_A.setFont(font_ee)
        self.label_point_number_A.setGeometry(QtCore.QRect(100, 40, 70, 16))
        self.label_point_number_A.setObjectName("label_point_number_A")
        self.label_point_number_A.setText("Point num.")
        self.comboBox_point_number_A = QtWidgets.QComboBox(self.groupBox_scan_A)
        self.comboBox_point_number_A.setFont(font_ee)
        self.comboBox_point_number_A.setGeometry(QtCore.QRect(150, 40, 45, 16))
        self.comboBox_point_number_A.setObjectName("comboBox_point_number_A")
        self.graphicsView_scan_A = pg.ImageView(self.groupBox_scan_A)
        self.graphicsView_scan_A.setGeometry(QtCore.QRect(2, 59, 196, 194))
        self.graphicsView_scan_A.setObjectName("graphicsView_scan_B")
        self.graphicsView_scan_A.ui.histogram.hide()
        self.graphicsView_scan_A.ui.menuBtn.hide()
        self.graphicsView_scan_A.ui.roiBtn.hide()

        # Block: scan B
        self.label_scan_B = QtWidgets.QLabel(self.centralwidget)
        self.label_scan_B.setGeometry(QtCore.QRect(15, 255, 47, 13))
        self.label_scan_B.setObjectName("label_scan_B")
        self.label_scan_B.setText("Scan B")
        self.label_scan_B.setFont(font_headline)
        self.groupBox_scan_B = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_scan_B.setGeometry(QtCore.QRect(5, 252, 199, 254))
        self.groupBox_scan_B.setObjectName("groupBox_scan_B")
        self.lineEdit_name_scan_B = QtWidgets.QLineEdit(self.groupBox_scan_B)
        self.lineEdit_name_scan_B.setGeometry(QtCore.QRect(5, 22, 168, 16))
        self.lineEdit_name_scan_B.setObjectName("lineEdit_name_scan_B")
        self.lineEdit_name_scan_B.setFont(font_ee)
        self.toolButton_scan_B = QtWidgets.QToolButton(self.groupBox_scan_B)
        self.toolButton_scan_B.setGeometry(QtCore.QRect(175, 22, 20, 16))
        self.toolButton_scan_B.setObjectName("toolButton_scan_B")
        self.toolButton_scan_B.setText("...")
        self.toolButton_scan_B.setFont(font_ee)
        self.label_polarisation_B = QtWidgets.QLabel(self.groupBox_scan_B)
        self.label_polarisation_B.setFont(font_ee)
        self.label_polarisation_B.setGeometry(QtCore.QRect(5, 40, 21, 16))
        self.label_polarisation_B.setObjectName("label_polarisation_B")
        self.label_polarisation_B.setText("Pol.")
        self.comboBox_polarisation_B = QtWidgets.QComboBox(self.groupBox_scan_B)
        self.comboBox_polarisation_B.setFont(font_ee)
        self.comboBox_polarisation_B.setGeometry(QtCore.QRect(25, 40, 40, 16))
        self.comboBox_polarisation_B.setObjectName("comboBox_polarisation_B")
        self.label_point_number_B = QtWidgets.QLabel(self.groupBox_scan_B)
        self.label_point_number_B.setFont(font_ee)
        self.label_point_number_B.setGeometry(QtCore.QRect(100, 40, 70, 16))
        self.label_point_number_B.setObjectName("label_point_number_B")
        self.label_point_number_B.setText("Point num.")
        self.comboBox_point_number_B = QtWidgets.QComboBox(self.groupBox_scan_B)
        self.comboBox_point_number_B.setFont(font_ee)
        self.comboBox_point_number_B.setGeometry(QtCore.QRect(150, 40, 45, 16))
        self.comboBox_point_number_B.setObjectName("comboBox_point_number_B")
        self.graphicsView_scan_B = pg.ImageView(self.groupBox_scan_B)
        self.graphicsView_scan_B.setGeometry(QtCore.QRect(2, 59, 196, 194))
        self.graphicsView_scan_B.setObjectName("graphicsView_scan_B")
        self.graphicsView_scan_B.ui.histogram.hide()
        self.graphicsView_scan_B.ui.menuBtn.hide()
        self.graphicsView_scan_B.ui.roiBtn.hide()

        # Block: Difference
        self.label_difference = QtWidgets.QLabel(self.centralwidget)
        self.label_difference.setGeometry(QtCore.QRect(220, 0, 61, 16))
        self.label_difference.setObjectName("label_difference")
        self.label_difference.setText("Difference")
        self.label_difference.setFont(font_headline)
        self.groupBox_difference = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_difference.setGeometry(QtCore.QRect(210, -3, 450, 509))
        self.groupBox_difference.setObjectName("groupBox_difference")
        self.checkBox_dev_by_monitor = QtWidgets.QCheckBox(self.groupBox_difference)
        self.checkBox_dev_by_monitor.setGeometry(QtCore.QRect(5, 20, 241, 20))
        self.checkBox_dev_by_monitor.setObjectName("checkBox_dev_by_monitor")
        self.checkBox_dev_by_monitor.setText("Devide scans by monitors before substraction ")
        self.checkBox_dev_by_monitor.setFont(font_ee)
        self.lineEdit_difference = QtWidgets.QLineEdit(self.groupBox_difference)
        self.lineEdit_difference.setGeometry(QtCore.QRect(220, 22, 100, 16))
        self.lineEdit_difference.setObjectName("lineEdit_difference")
        self.lineEdit_difference.setFont(font_ee)
        self.lineEdit_difference.setEnabled(False)
        self.lineEdit_difference.setStyleSheet("color:rgb(0,0,0)")
        self.pushButton_swap_ab = QtWidgets.QPushButton(self.groupBox_difference)
        self.pushButton_swap_ab.setGeometry(QtCore.QRect(329, 22, 61, 16))
        self.pushButton_swap_ab.setObjectName("pushButton_swap_ab")
        self.pushButton_swap_ab.setText("(A<->B)")
        self.pushButton_swap_ab.setFont(font_headline)
        self.pushButton_load_difference = QtWidgets.QPushButton(self.groupBox_difference)
        self.pushButton_load_difference.setGeometry(QtCore.QRect(394, 22, 51, 16))
        self.pushButton_load_difference.setObjectName("pushButton_load_difference")
        self.pushButton_load_difference.setText("Load")
        self.pushButton_load_difference.setFont(font_headline)
        self.graphicsView_difference = pg.ImageView(self.groupBox_difference)
        self.graphicsView_difference.setGeometry(QtCore.QRect(6, 43, 440, 440))
        self.graphicsView_difference.setObjectName("graphicsView_difference")
        self.graphicsView_difference.ui.menuBtn.hide()
        self.graphicsView_difference.ui.roiBtn.hide()
        self.graphicsView_difference.ui.histogram.clickAccepted
        colmap = pg.ColorMap(numpy.array([0.4, 0.5, 0.6]),
                             numpy.array([[0, 0, 255, 255], [0, 0, 0, 255], [0, 255, 0, 255]], dtype=numpy.ubyte))
        self.graphicsView_difference.setColorMap(colmap)

        self.label_reduce_pix = QtWidgets.QLabel(self.groupBox_difference)
        self.label_reduce_pix.setGeometry(QtCore.QRect(10, 488, 190, 16))
        self.label_reduce_pix.setObjectName("label_reduce_pix")
        self.label_reduce_pix.setText("Reduce number of pixels in each direction by:")
        self.label_reduce_pix.setFont(font_ee)
        self.checkBox_reduce_2 = QtWidgets.QCheckBox(self.groupBox_difference)
        self.checkBox_reduce_2.setGeometry(QtCore.QRect(200, 488, 241, 16))
        self.checkBox_reduce_2.setObjectName("checkBox_reduce_2")
        self.checkBox_reduce_2.setText("x2")
        self.checkBox_reduce_2.setFont(font_ee)
        self.checkBox_reduce_4 = QtWidgets.QCheckBox(self.groupBox_difference)
        self.checkBox_reduce_4.setGeometry(QtCore.QRect(240, 488, 241, 16))
        self.checkBox_reduce_4.setObjectName("checkBox_sum_4_pix")
        self.checkBox_reduce_4.setText("x4")
        self.checkBox_reduce_4.setFont(font_ee)
        self.checkBox_reduce_8 = QtWidgets.QCheckBox(self.groupBox_difference)
        self.checkBox_reduce_8.setGeometry(QtCore.QRect(280, 488, 241, 16))
        self.checkBox_reduce_8.setObjectName("checkBox_sum_8_pix")
        self.checkBox_reduce_8.setText("x8")
        self.checkBox_reduce_8.setFont(font_ee)
        self.pushButton_clear_all = QtWidgets.QPushButton(self.groupBox_difference)
        self.pushButton_clear_all.setGeometry(QtCore.QRect(364, 488, 81, 16))
        self.pushButton_clear_all.setObjectName("pushButton_clear_all")
        self.pushButton_clear_all.setText("Clear all")
        self.pushButton_clear_all.setFont(font_headline)

        # Menu and statusbar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 717, 21))
        self.menubar.setObjectName("menubar")
        self.menubar.setFont(font_ee)
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuHelp.setTitle("Help")
        self.menuHelp.setFont(font_ee)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.actionVersion.setText("Version 1.0")
        self.actionVersion.setFont(font_ee)
        self.menuHelp.addAction(self.actionVersion)
        self.menubar.addAction(self.menuHelp.menuAction())

        # Actions on clicks
        self.toolButton_scan_A.clicked.connect(self.button_import_scan_A)
        self.toolButton_scan_B.clicked.connect(self.button_import_scan_B)
        self.pushButton_swap_ab.clicked.connect(self.button_swap_ab)
        self.pushButton_load_difference.clicked.connect(self.draw_diff)
        self.pushButton_clear_all.clicked.connect(self.button_clear_all)
        self.checkBox_dev_by_monitor.stateChanged.connect(self.draw_diff)
        self.checkBox_reduce_2.stateChanged.connect(self.reduce_x2)
        self.checkBox_reduce_4.stateChanged.connect(self.reduce_x4)
        self.checkBox_reduce_8.stateChanged.connect(self.reduce_x8)
        self.comboBox_point_number_A.currentIndexChanged.connect(self.draw_det_A_frame)
        self.comboBox_point_number_A.currentIndexChanged.connect(self.diff_line)
        self.comboBox_polarisation_A.currentIndexChanged.connect(self.draw_det_A_frame)
        self.comboBox_polarisation_A.currentIndexChanged.connect(self.diff_line)
        self.comboBox_point_number_B.currentIndexChanged.connect(self.draw_det_B_frame)
        self.comboBox_point_number_B.currentIndexChanged.connect(self.diff_line)
        self.comboBox_polarisation_B.currentIndexChanged.connect(self.draw_det_B_frame)
        self.comboBox_polarisation_B.currentIndexChanged.connect(self.diff_line)
        self.actionVersion.triggered.connect(self.menu_info)

    def button_import_scan_A(self):
        self.comboBox_point_number_A.clear()
        self.comboBox_polarisation_A.clear()
        self.graphicsView_scan_A.clear()
        self.lineEdit_name_scan_A.setText("")

        data_file = QtWidgets.QFileDialog().getOpenFileName(None, "FileNames", current_dir)
        self.lineEdit_name_scan_A.setText(data_file[0])

        if self.lineEdit_name_scan_A.text() == "": return

        self.comboBox_point_number_A.clear()
        self.comboBox_polarisation_A.clear()

        with h5py.File(self.lineEdit_name_scan_A.text(), 'r') as file:

            scan_data = file[list(file.keys())[0]]

            for index, th in enumerate(scan_data.get("instrument").get('motors').get('th').get("value")):
                self.comboBox_point_number_A.addItem(str(index))

            for polarisation in scan_data.get("instrument").get('detectors'):

                if polarisation in ("psd_uu", "psd_du", "psd_dd", "psd_ud"):
                    self.comboBox_polarisation_A.addItem(str(polarisation)[-2:])
                elif polarisation in ("psd"):
                    self.comboBox_polarisation_A.addItem("np")

            self.comboBox_point_number_A.setCurrentIndex(0)
            self.comboBox_polarisation_A.setCurrentIndex(0)

        self.draw_det_A_frame()

    def button_import_scan_B(self):
        self.comboBox_point_number_B.clear()
        self.comboBox_polarisation_B.clear()
        self.graphicsView_scan_B.clear()
        self.lineEdit_name_scan_B.setText("")

        data_file = QtWidgets.QFileDialog().getOpenFileName(None, "FileNames", current_dir)
        self.lineEdit_name_scan_B.setText(data_file[0])

        if self.lineEdit_name_scan_B.text() == "": return

        self.comboBox_point_number_B.clear()
        self.comboBox_polarisation_B.clear()

        with h5py.File(self.lineEdit_name_scan_B.text(), 'r') as file:

            scan_data = file[list(file.keys())[0]]

            for index, th in enumerate(scan_data.get("instrument").get('motors').get('th').get("value")):
                self.comboBox_point_number_B.addItem(str(index))

            for polarisation in scan_data.get("instrument").get('detectors'):

                if polarisation in ("psd_uu", "psd_du", "psd_dd", "psd_ud"):
                    self.comboBox_polarisation_B.addItem(str(polarisation)[-2:])
                elif polarisation in ("psd"):
                    self.comboBox_polarisation_B.addItem("np")

            self.comboBox_point_number_B.setCurrentIndex(0)
            self.comboBox_polarisation_B.setCurrentIndex(0)

        self.draw_det_B_frame()

    def button_clear_all(self):
        self.comboBox_point_number_A.clear()
        self.comboBox_polarisation_A.clear()
        self.graphicsView_scan_A.clear()
        self.lineEdit_name_scan_A.setText("")
        self.comboBox_point_number_B.clear()
        self.comboBox_polarisation_B.clear()
        self.graphicsView_scan_B.clear()
        self.lineEdit_name_scan_B.setText("")
        self.lineEdit_difference.setText("")
        self.graphicsView_difference.clear()

    def diff_line(self):
        line = ""

        if not (self.comboBox_point_number_A.currentText() == "" or self.comboBox_polarisation_A.currentText() == "" ): line = "A(" + str(self.comboBox_polarisation_A.currentText()) + ")(" + str(self.comboBox_point_number_A.currentText()) + ")"
        if not (self.comboBox_point_number_B.currentText() == "" or self.comboBox_polarisation_B.currentText() == "" ):
            if line == "": line = "B(" + str(self.comboBox_polarisation_B.currentText()) + ")(" + str(self.comboBox_point_number_B.currentText()) + ")"
            else: line += " - B(" + str(self.comboBox_polarisation_B.currentText()) + ")(" + str(self.comboBox_point_number_B.currentText()) + ")"

        self.lineEdit_difference.setText(line)

        self.draw_diff()

    def button_swap_ab(self):

        if self.lineEdit_difference.text() == "": return

        if not self.lineEdit_difference.text().find("-") > 0: return

        line = self.lineEdit_difference.text()[self.lineEdit_difference.text().find("-")+2:] + " - " + self.lineEdit_difference.text()[: self.lineEdit_difference.text().find("-")-1]

        self.lineEdit_difference.setText(line)

        self.draw_diff()

    def draw_det_A_frame(self):

        self.graphicsView_scan_A.clear()

        if self.lineEdit_name_scan_A.text() == "" or self.comboBox_point_number_A.currentText() == "" or self.comboBox_polarisation_A.currentText() == "": return

        if self.comboBox_polarisation_A.currentText() == "np": scan_psd_A = "psd"
        else: scan_psd_A = "psd_" + self.comboBox_polarisation_A.currentText()

        with h5py.File(self.lineEdit_name_scan_A.text(), 'r') as file:

            detector_image_A = file[list(file.keys())[0]].get("instrument").get('detectors').get(scan_psd_A).get('data')

            self.graphicsView_scan_A.setImage(detector_image_A[int(self.comboBox_point_number_A.currentText())], axes={'x':1, 'y':0}, levels=(0,0.1))

            colmap = pg.ColorMap(numpy.array([0.0, 0.1, 1.0]), numpy.array([[0, 0, 255, 255], [255, 0, 0, 255], [0, 255, 0, 255]], dtype=numpy.ubyte))
            self.graphicsView_scan_A.setColorMap(colmap)

    def draw_det_B_frame(self):

        self.graphicsView_scan_B.clear()

        if self.lineEdit_name_scan_B.text() == "" or self.comboBox_point_number_B.currentText() == "" or self.comboBox_polarisation_B.currentText() == "": return

        if self.comboBox_polarisation_B.currentText() == "np": scan_psd = "psd"
        else: scan_psd = "psd_" + self.comboBox_polarisation_B.currentText()

        with h5py.File(self.lineEdit_name_scan_B.text(), 'r') as file:

            detector_image_B = file[list(file.keys())[0]].get("instrument").get('detectors').get(scan_psd).get('data')

            self.graphicsView_scan_B.setImage(detector_image_B[int(self.comboBox_point_number_B.currentText())], axes={'x':1, 'y':0}, levels=(0,0.1))

            colmap = pg.ColorMap(numpy.array([0.0, 0.1, 1.0]), numpy.array([[0, 0, 255, 255], [255, 0, 0, 255], [0, 255, 0, 255]], dtype=numpy.ubyte))
            self.graphicsView_scan_B.setColorMap(colmap)

    def draw_diff(self):

        if self.lineEdit_difference.text() == "": return

        # Get requested in the line A frame
        if not self.lineEdit_difference.text().find("A(") == -1:
            line_scan_A = self.lineEdit_difference.text()[self.lineEdit_difference.text().find("A(") : self.lineEdit_difference.text().find("A(") + 10]

            if line_scan_A.find("np") > 0: scan_psd_A = "psd"
            else: scan_psd_A = "psd_" + line_scan_A[line_scan_A.find("(")+1 : line_scan_A.find(")")]

            index_psd_A = int(line_scan_A[line_scan_A.rfind("(")+1 : line_scan_A.rfind(")")])

            with h5py.File(self.lineEdit_name_scan_A.text(), 'r') as file:
                self.detector_image_A = file[list(file.keys())[0]].get("instrument").get('detectors').get(scan_psd_A).get('data')[index_psd_A]

                for index, scaler in enumerate(file[list(file.keys())[0]].get("instrument").get('scalers').get('SPEC_counter_mnemonics')):
                    if scan_psd_A == "psd": monitor_A_identifier = "b'mon0'"
                    elif scan_psd_A == "psd_uu": monitor_A_identifier = "b'm1'"
                    elif scan_psd_A == "psd_dd": monitor_A_identifier = "b'm2'"
                    elif scan_psd_A == "psd_du": monitor_A_identifier = "b'm3'"
                    elif scan_psd_A == "psd_ud": monitor_A_identifier = "b'm4'"
                    if monitor_A_identifier in str(scaler): monitor_A = numpy.array(file[list(file.keys())[0]].get("instrument").get('scalers').get('data')).T[index][index_psd_A]

        # Get requested in the line B frame
        if not self.lineEdit_difference.text().find("B(") == -1:
            line_scan_B = self.lineEdit_difference.text()[self.lineEdit_difference.text().find("B(") : self.lineEdit_difference.text().find("B(") + 10]

            if line_scan_B.find("np") > 0: scan_psd_B = "psd"
            else: scan_psd_B = "psd_" + line_scan_B[line_scan_B.find("(")+1 : line_scan_B.find(")")]

            index_psd_B = int(line_scan_B[line_scan_B.rfind("(")+1 : line_scan_B.rfind(")")])

            with h5py.File(self.lineEdit_name_scan_B.text(), 'r') as file:
                self.detector_image_B = file[list(file.keys())[0]].get("instrument").get('detectors').get(scan_psd_B).get('data')[index_psd_B]

                if scan_psd_B == "psd": monitor_B_identifier = "b'mon0'"
                elif scan_psd_B == "psd_uu": monitor_B_identifier = "b'm1'"
                elif scan_psd_B == "psd_dd": monitor_B_identifier = "b'm2'"
                elif scan_psd_B == "psd_du": monitor_B_identifier = "b'm3'"
                elif scan_psd_B == "psd_ud": monitor_B_identifier = "b'm4'"
                for index, scaler in enumerate(file[list(file.keys())[0]].get("instrument").get('scalers').get('SPEC_counter_mnemonics')):
                    if monitor_B_identifier in str(scaler): monitor_B = numpy.array(file[list(file.keys())[0]].get("instrument").get('scalers').get('data')).T[index][index_psd_B]

        # Do the substraction
        if self.lineEdit_difference.text().find("A(") == -1: res = self.detector_image_B
        elif self.lineEdit_difference.text().find("B(") == -1: res = self.detector_image_A
        else:
            if not self.lineEdit_difference.text().find(line_scan_A) == 0:
                main = self.detector_image_B
                main_mon = monitor_B
                min = self.detector_image_A
                min_mon = monitor_A
            else:
                main = self.detector_image_A
                main_mon = monitor_A
                min = self.detector_image_B
                min_mon = monitor_B

            if self.checkBox_dev_by_monitor.isChecked():
                main = numpy.divide(main, main_mon/min_mon)
            res = numpy.subtract(main, min)

        if self.checkBox_reduce_2.isChecked(): res = res.reshape(700, 2, 700, 2).sum(axis=1).sum(axis=2)
        elif self.checkBox_reduce_4.isChecked(): res = res.reshape(350, 4, 350, 4).sum(axis=1).sum(axis=2)
        elif self.checkBox_reduce_8.isChecked(): res = res.reshape(175, 8, 175, 8).sum(axis=1).sum(axis=2)

        res = numpy.around(res, decimals=0).astype(int)

        self.graphicsView_difference.setImage(res, axes={'x': 1, 'y': 0})
        if self.lineEdit_difference.text().find("A(") == -1 or self.lineEdit_difference.text().find("B(") == -1:
            self.graphicsView_difference.ui.histogram.setHistogramRange(0, 1)
            self.graphicsView_difference.ui.histogram.setLevels(0, 1)
        else:
            self.graphicsView_difference.ui.histogram.setHistogramRange(-10, 10)
            self.graphicsView_difference.ui.histogram.setLevels(-10, 10)
            if self.checkBox_reduce_2.isChecked() or self.checkBox_reduce_4.isChecked() or self.checkBox_reduce_8.isChecked():
                self.graphicsView_difference.ui.histogram.setHistogramRange(-20, 20)
                self.graphicsView_difference.ui.histogram.setLevels(-20, 20)

        self.statusbar.showMessage('Substraction "' + self.lineEdit_difference.text() + '" is performed.')

    def reduce_x2(self):
        if self.checkBox_reduce_2.isChecked():
            self.checkBox_reduce_4.setChecked(False)
            self.checkBox_reduce_8.setChecked(False)
        else: self.checkBox_reduce_2.setChecked(False)

        self.draw_diff()

    def reduce_x4(self):
        if self.checkBox_reduce_4.isChecked():
            self.checkBox_reduce_2.setChecked(False)
            self.checkBox_reduce_8.setChecked(False)
        else: self.checkBox_reduce_4.setChecked(False)

        self.draw_diff()

    def reduce_x8(self):
        if self.checkBox_reduce_8.isChecked():
            self.checkBox_reduce_2.setChecked(False)
            self.checkBox_reduce_4.setChecked(False)
        else: self.checkBox_reduce_8.setChecked(False)

        self.draw_diff()

    def menu_info(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)).replace("\\", "/") + "\icon.png"))
        msgBox.setText("SuperADAM .h5 scan subtractor. " + self.actionVersion.text() + "\n\n"
                                                                                            "Alexey.Klechikov@gmail.com\n\n"
                                                                                            "Check new version at https://github.com/Alexey-Klechikov/Scans-Subtractor/releases")
        msgBox.exec_()

if __name__ == "__main__":
    import sys
    QtWidgets.QApplication.setStyle("Fusion")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
