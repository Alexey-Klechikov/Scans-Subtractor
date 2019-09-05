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
        font_headline.setPointSize(13)
        font_headline.setBold(True)

        font_graphs = QtGui.QFont()
        font_graphs.setPixelSize(12)
        font_graphs.setBold(False)

        font_graphs_2 = QtGui.QFont()
        font_graphs_2.setPixelSize(1)
        font_graphs_2.setBold(False)

        font_ee = QtGui.QFont()
        font_ee.setPointSize(11)
        font_ee.setBold(False)

        # Graphs background
        pg.setConfigOption('background', (255, 255, 255))
        pg.setConfigOption('foreground', 'k')

        # Main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 787)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 787))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 787))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setWindowTitle("pySAsum")
        MainWindow.setWindowIcon(QtGui.QIcon(current_dir + "\icon.png"))
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Block: scan A
        self.label_scan_A = QtWidgets.QLabel(self.centralwidget)
        self.label_scan_A.setGeometry(QtCore.QRect(15, 0, 80, 20))
        self.label_scan_A.setObjectName("label_scan_A")
        self.label_scan_A.setText("Scan A")
        self.label_scan_A.setFont(font_headline)
        self.groupBox_scan_A = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_scan_A.setGeometry(QtCore.QRect(5, 5, 300, 375))
        self.groupBox_scan_A.setObjectName("groupBox_scan_A")
        self.lineEdit_name_scan_A = QtWidgets.QLineEdit(self.groupBox_scan_A)
        self.lineEdit_name_scan_A.setGeometry(QtCore.QRect(5, 22, 260, 20))
        self.lineEdit_name_scan_A.setObjectName("lineEdit_name_scan_B")
        self.lineEdit_name_scan_A.setFont(font_ee)
        self.toolButton_scan_A = QtWidgets.QToolButton(self.groupBox_scan_A)
        self.toolButton_scan_A.setGeometry(QtCore.QRect(275, 22, 20, 20))
        self.toolButton_scan_A.setObjectName("toolButton_scan_B")
        self.toolButton_scan_A.setText("...")
        self.toolButton_scan_A.setFont(font_ee)
        self.label_polarisation_A = QtWidgets.QLabel(self.groupBox_scan_A)
        self.label_polarisation_A.setFont(font_ee)
        self.label_polarisation_A.setGeometry(QtCore.QRect(5, 45, 75, 20))
        self.label_polarisation_A.setObjectName("label_polarisation_A")
        self.label_polarisation_A.setText("Polarisation:")
        self.comboBox_polarisation_A = QtWidgets.QComboBox(self.groupBox_scan_A)
        self.comboBox_polarisation_A.setFont(font_ee)
        self.comboBox_polarisation_A.setGeometry(QtCore.QRect(75, 45, 55, 20))
        self.comboBox_polarisation_A.setObjectName("comboBox_polarisation_A")
        self.label_point_number_A = QtWidgets.QLabel(self.groupBox_scan_A)
        self.label_point_number_A.setFont(font_ee)
        self.label_point_number_A.setGeometry(QtCore.QRect(158, 45, 80, 20))
        self.label_point_number_A.setObjectName("label_point_number_A")
        self.label_point_number_A.setText("Point number:")
        self.comboBox_point_number_A = QtWidgets.QComboBox(self.groupBox_scan_A)
        self.comboBox_point_number_A.setFont(font_ee)
        self.comboBox_point_number_A.setGeometry(QtCore.QRect(240, 45, 55, 20))
        self.comboBox_point_number_A.setObjectName("comboBox_point_number_A")
        self.graphicsView_scan_A = pg.ImageView(self.groupBox_scan_A)
        self.graphicsView_scan_A.setGeometry(QtCore.QRect(3, 70, 295, 303))
        self.graphicsView_scan_A.setObjectName("graphicsView_scan_B")
        self.graphicsView_scan_A.ui.histogram.hide()
        self.graphicsView_scan_A.ui.menuBtn.hide()
        self.graphicsView_scan_A.ui.roiBtn.hide()

        # Block: scan B
        self.label_scan_B = QtWidgets.QLabel(self.centralwidget)
        self.label_scan_B.setGeometry(QtCore.QRect(15, 385, 80, 20))
        self.label_scan_B.setObjectName("label_scan_B")
        self.label_scan_B.setText("Scan B")
        self.label_scan_B.setFont(font_headline)
        self.groupBox_scan_B = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_scan_B.setGeometry(QtCore.QRect(5, 390, 300, 375))
        self.groupBox_scan_B.setObjectName("groupBox_scan_B")
        self.lineEdit_name_scan_B = QtWidgets.QLineEdit(self.groupBox_scan_B)
        self.lineEdit_name_scan_B.setGeometry(QtCore.QRect(5, 22, 260, 20))
        self.lineEdit_name_scan_B.setObjectName("lineEdit_name_scan_B")
        self.lineEdit_name_scan_B.setFont(font_ee)
        self.toolButton_scan_B = QtWidgets.QToolButton(self.groupBox_scan_B)
        self.toolButton_scan_B.setGeometry(QtCore.QRect(275, 22, 20, 20))
        self.toolButton_scan_B.setObjectName("toolButton_scan_B")
        self.toolButton_scan_B.setText("...")
        self.toolButton_scan_B.setFont(font_ee)
        self.label_polarisation_B = QtWidgets.QLabel(self.groupBox_scan_B)
        self.label_polarisation_B.setFont(font_ee)
        self.label_polarisation_B.setGeometry(QtCore.QRect(5, 45, 75, 20))
        self.label_polarisation_B.setObjectName("label_polarisation_B")
        self.label_polarisation_B.setText("Polarisation:")
        self.comboBox_polarisation_B = QtWidgets.QComboBox(self.groupBox_scan_B)
        self.comboBox_polarisation_B.setFont(font_ee)
        self.comboBox_polarisation_B.setGeometry(QtCore.QRect(75, 45, 55, 20))
        self.comboBox_polarisation_B.setObjectName("comboBox_polarisation_B")
        self.label_point_number_B = QtWidgets.QLabel(self.groupBox_scan_B)
        self.label_point_number_B.setFont(font_ee)
        self.label_point_number_B.setGeometry(QtCore.QRect(158, 45, 80, 20))
        self.label_point_number_B.setObjectName("label_point_number_B")
        self.label_point_number_B.setText("Point number:")
        self.comboBox_point_number_B = QtWidgets.QComboBox(self.groupBox_scan_B)
        self.comboBox_point_number_B.setFont(font_ee)
        self.comboBox_point_number_B.setGeometry(QtCore.QRect(240, 45, 55, 20))
        self.comboBox_point_number_B.setObjectName("comboBox_point_number_B")
        self.graphicsView_scan_B = pg.ImageView(self.groupBox_scan_B)
        self.graphicsView_scan_B.setGeometry(QtCore.QRect(3, 70, 295, 303))
        self.graphicsView_scan_B.setObjectName("graphicsView_scan_B")
        self.graphicsView_scan_B.ui.histogram.hide()
        self.graphicsView_scan_B.ui.menuBtn.hide()
        self.graphicsView_scan_B.ui.roiBtn.hide()


        # Block: Result
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(325, 0, 61, 20))
        self.label_result.setObjectName("label_result")
        self.label_result.setText("Result")
        self.label_result.setFont(font_headline)
        self.groupBox_result = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_result.setGeometry(QtCore.QRect(320, 5, 775, 760))
        self.groupBox_result.setObjectName("groupBox_result")

        # ROI part is hidden by default
        self.graphicsView_int_roi = pg.PlotWidget(self.groupBox_result)
        self.graphicsView_int_roi.setGeometry(QtCore.QRect(3, 431, 770, 275))
        self.graphicsView_int_roi.setObjectName("graphicsView_int_roi")
        self.graphicsView_int_roi.getAxis("bottom").tickFont = font_graphs
        self.graphicsView_int_roi.getAxis("bottom").setStyle(tickTextOffset=10)
        self.graphicsView_int_roi.getAxis("left").tickFont = font_graphs
        self.graphicsView_int_roi.getAxis("left").setStyle(tickTextOffset=10)
        self.graphicsView_int_roi.showAxis("top")
        self.graphicsView_int_roi.getAxis("top").tickFont = font_graphs_2
        self.graphicsView_int_roi.getAxis("top").setStyle(tickTextOffset=-2)
        self.graphicsView_int_roi.showAxis("right")
        self.graphicsView_int_roi.getAxis("right").tickFont = font_graphs_2
        self.graphicsView_int_roi.getAxis("right").setStyle(tickTextOffset=-2)
        self.label_roi_coord = QtWidgets.QLabel(self.groupBox_result)
        self.label_roi_coord.setGeometry(QtCore.QRect(10, 710, 400, 22))
        self.label_roi_coord.setObjectName("label_roi_coord")
        self.label_roi_coord.setText(
            "ROI coordinates: left                right                top                bottom")
        self.label_roi_coord.setFont(font_ee)
        self.lineEdit_roi_left = QtWidgets.QLineEdit(self.groupBox_result)
        self.lineEdit_roi_left.setGeometry(QtCore.QRect(127, 710, 40, 22))
        self.lineEdit_roi_left.setObjectName("lineEdit_roi_left")
        self.lineEdit_roi_left.setFont(font_ee)
        self.lineEdit_roi_left.setText("10")
        self.lineEdit_roi_right = QtWidgets.QLineEdit(self.groupBox_result)
        self.lineEdit_roi_right.setGeometry(QtCore.QRect(217, 710, 40, 22))
        self.lineEdit_roi_right.setObjectName("lineEdit_roi_right")
        self.lineEdit_roi_right.setFont(font_ee)
        self.lineEdit_roi_right.setText("20")
        self.lineEdit_roi_top = QtWidgets.QLineEdit(self.groupBox_result)
        self.lineEdit_roi_top.setGeometry(QtCore.QRect(297, 710, 40, 22))
        self.lineEdit_roi_top.setObjectName("lineEdit_roi_top")
        self.lineEdit_roi_top.setFont(font_ee)
        self.lineEdit_roi_top.setText("10")
        self.lineEdit_roi_bottom = QtWidgets.QLineEdit(self.groupBox_result)
        self.lineEdit_roi_bottom.setGeometry(QtCore.QRect(407, 710, 40, 22))
        self.lineEdit_roi_bottom.setObjectName("lineEdit_roi_bottom")
        self.lineEdit_roi_bottom.setFont(font_ee)
        self.lineEdit_roi_bottom.setText("20")
        self.pushButton_turn_ROI = QtWidgets.QPushButton(self.groupBox_result)
        self.pushButton_turn_ROI.setGeometry(QtCore.QRect(535, 710, 80, 22))
        self.pushButton_turn_ROI.setObjectName("pushButton_turn_ROI")
        self.pushButton_turn_ROI.setText("Turn ROI")
        self.pushButton_turn_ROI.setFont(font_headline)
        self.pushButton_export_int_roi = QtWidgets.QPushButton(self.groupBox_result)
        self.pushButton_export_int_roi.setGeometry(QtCore.QRect(620, 710, 151, 22))
        self.pushButton_export_int_roi.setObjectName("pushButton_export_int_roi")
        self.pushButton_export_int_roi.setText("Export int. ROI")
        self.pushButton_export_int_roi.setFont(font_headline)

        # This part of Result block is visible
        self.checkBox_dev_by_monitor = QtWidgets.QCheckBox(self.groupBox_result)
        self.checkBox_dev_by_monitor.setGeometry(QtCore.QRect(5, 22, 241, 22))
        self.checkBox_dev_by_monitor.setObjectName("checkBox_dev_by_monitor")
        self.checkBox_dev_by_monitor.setText("Devide by monitors")
        self.checkBox_dev_by_monitor.setFont(font_ee)
        self.lineEdit_operation_sign = QtWidgets.QLineEdit(self.groupBox_result)
        self.lineEdit_operation_sign.setGeometry(QtCore.QRect(450, 22, 20, 22))
        self.lineEdit_operation_sign.setObjectName("lineEdit_operation_sign")
        self.lineEdit_operation_sign.setFont(font_ee)
        self.lineEdit_operation_sign.setText(" - ")
        self.lineEdit_operation = QtWidgets.QLineEdit(self.groupBox_result)
        self.lineEdit_operation.setGeometry(QtCore.QRect(475, 22, 200, 22))
        self.lineEdit_operation.setObjectName("lineEdit_operation")
        self.lineEdit_operation.setFont(font_ee)
        self.lineEdit_operation.setEnabled(False)
        self.lineEdit_operation.setStyleSheet("color:rgb(0,0,0)")
        self.pushButton_swap_ab = QtWidgets.QPushButton(self.groupBox_result)
        self.pushButton_swap_ab.setGeometry(QtCore.QRect(680, 22, 90, 22))
        self.pushButton_swap_ab.setObjectName("pushButton_swap_ab")
        self.pushButton_swap_ab.setText("(A<->B)")
        self.pushButton_swap_ab.setFont(font_headline)
        self.graphicsView_result = pg.ImageView(self.groupBox_result)
        self.graphicsView_result.setGeometry(QtCore.QRect(3, 48, 770, 684))
        self.graphicsView_result.setObjectName("graphicsView_result")
        self.graphicsView_result.ui.menuBtn.hide()
        self.graphicsView_result.ui.roiBtn.hide()
        self.graphicsView_result.ui.histogram.clickAccepted
        colmap = pg.ColorMap(numpy.array([0.4, 0.5, 0.6]),
                             numpy.array([[0, 0, 255, 255], [0, 0, 0, 255], [0, 255, 0, 255]], dtype=numpy.ubyte))
        self.graphicsView_result.setColorMap(colmap)

        self.label_reduce_pix = QtWidgets.QLabel(self.groupBox_result)
        self.label_reduce_pix.setGeometry(QtCore.QRect(10, 736, 250, 20))
        self.label_reduce_pix.setObjectName("label_reduce_pix")
        self.label_reduce_pix.setText("Reduce number of pixels in each direction by:")
        self.label_reduce_pix.setFont(font_ee)
        self.checkBox_reduce_2 = QtWidgets.QCheckBox(self.groupBox_result)
        self.checkBox_reduce_2.setGeometry(QtCore.QRect(270, 736, 241, 20))
        self.checkBox_reduce_2.setObjectName("checkBox_reduce_2")
        self.checkBox_reduce_2.setText("x2")
        self.checkBox_reduce_2.setFont(font_ee)
        self.checkBox_reduce_4 = QtWidgets.QCheckBox(self.groupBox_result)
        self.checkBox_reduce_4.setGeometry(QtCore.QRect(315, 736, 241, 20))
        self.checkBox_reduce_4.setObjectName("checkBox_sum_4_pix")
        self.checkBox_reduce_4.setText("x4")
        self.checkBox_reduce_4.setFont(font_ee)
        self.checkBox_reduce_8 = QtWidgets.QCheckBox(self.groupBox_result)
        self.checkBox_reduce_8.setGeometry(QtCore.QRect(360, 736, 241, 20))
        self.checkBox_reduce_8.setObjectName("checkBox_sum_8_pix")
        self.checkBox_reduce_8.setText("x8")
        self.checkBox_reduce_8.setFont(font_ee)
        self.pushButton_export_result = QtWidgets.QPushButton(self.groupBox_result)
        self.pushButton_export_result.setGeometry(QtCore.QRect(620, 735, 151, 22))
        self.pushButton_export_result.setObjectName("pushButton_clear_all")
        self.pushButton_export_result.setText("Export result (2D)")
        self.pushButton_export_result.setFont(font_headline)
        self.pushButton_ROI = QtWidgets.QPushButton(self.groupBox_result)
        self.pushButton_ROI.setGeometry(QtCore.QRect(535, 735, 80, 22))
        self.pushButton_ROI.setObjectName("pushButton_ROI")
        self.pushButton_ROI.setText("ROI")
        self.pushButton_ROI.setFont(font_headline)

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
        self.actionVersion.setText("Version 1.2")
        self.actionVersion.setFont(font_ee)
        self.menuHelp.addAction(self.actionVersion)
        self.menubar.addAction(self.menuHelp.menuAction())

        # Actions on clicks
        self.toolButton_scan_A.clicked.connect(self.button_import_scan_A)
        self.toolButton_scan_B.clicked.connect(self.button_import_scan_B)
        self.pushButton_swap_ab.clicked.connect(self.button_swap_ab)
        self.pushButton_export_result.clicked.connect(self.button_export_result)
        self.checkBox_dev_by_monitor.stateChanged.connect(self.draw_res)
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

        self.pushButton_ROI.clicked.connect(self.button_roi)
        self.pushButton_ROI.clicked.connect(self.draw_roi)
        self.pushButton_turn_ROI.clicked.connect(self.button_turn_roi)
        self.pushButton_export_int_roi.clicked.connect(self.button_export_int_roi)
        self.lineEdit_roi_left.editingFinished.connect(self.draw_roi)
        self.lineEdit_roi_right.editingFinished.connect(self.draw_roi)
        self.lineEdit_roi_top.editingFinished.connect(self.draw_roi)
        self.lineEdit_roi_bottom.editingFinished.connect(self.draw_roi)
        self.lineEdit_operation_sign.editingFinished.connect(self.diff_line)
        self.actionVersion.triggered.connect(self.menu_info)

        self.line_A = ""
        self.line_B = ""
        self.show_roi = 0
        self.turn_roi = 0
        self.draw_roi_result = []
        self.res = []

    def button_import_scan_A(self):

        self.lineEdit_name_scan_A.setText("")
        data_file = QtWidgets.QFileDialog().getOpenFileName(None, "FileNames", current_dir)
        self.lineEdit_name_scan_A.setText(data_file[0])
        if self.lineEdit_name_scan_A.text() == "": return

        self.comboBox_point_number_A.clear()
        self.comboBox_polarisation_A.clear()
        self.graphicsView_scan_A.clear()

        with h5py.File(self.lineEdit_name_scan_A.text(), 'r') as file:

            scan_data = file[list(file.keys())[0]]

            for index, th in enumerate(scan_data.get("instrument").get('motors').get('th').get("value")):
                self.comboBox_point_number_A.addItem(str(index))

            self.comboBox_point_number_A.addItem("All")

            for polarisation in scan_data.get("instrument").get('detectors'):

                if polarisation in ("psd_uu", "psd_du", "psd_dd", "psd_ud"):
                    self.comboBox_polarisation_A.addItem(str(polarisation)[-2:])
                elif polarisation in ("psd"):
                    self.comboBox_polarisation_A.addItem("np")

        self.comboBox_point_number_A.setCurrentIndex(0)
        self.comboBox_polarisation_A.setCurrentIndex(0)

        self.draw_det_A_frame()
        self.diff_line()

    def button_import_scan_B(self):
        self.lineEdit_name_scan_B.setText("")
        data_file = QtWidgets.QFileDialog().getOpenFileName(None, "FileNames", current_dir)
        self.lineEdit_name_scan_B.setText(data_file[0])
        if self.lineEdit_name_scan_B.text() == "": return

        self.comboBox_point_number_B.clear()
        self.comboBox_polarisation_B.clear()
        self.graphicsView_scan_B.clear()

        with h5py.File(self.lineEdit_name_scan_B.text(), 'r') as file:

            scan_data = file[list(file.keys())[0]]

            for index, th in enumerate(scan_data.get("instrument").get('motors').get('th').get("value")):
                self.comboBox_point_number_B.addItem(str(index))

            self.comboBox_point_number_B.addItem("All")

            for polarisation in scan_data.get("instrument").get('detectors'):

                if polarisation in ("psd_uu", "psd_du", "psd_dd", "psd_ud"):
                    self.comboBox_polarisation_B.addItem(str(polarisation)[-2:])
                elif polarisation in ("psd"):
                    self.comboBox_polarisation_B.addItem("np")

        self.comboBox_point_number_B.setCurrentIndex(0)
        self.comboBox_polarisation_B.setCurrentIndex(0)

        self.draw_det_B_frame()
        self.diff_line()

    def button_export_result(self):

        # Export resulting picture as CSV
        current_dir = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
        dir = QtWidgets.QFileDialog().getExistingDirectory(None, "FileNames", current_dir)

        with open(dir + "/2D_map.dat", "w") as new_file_2d_map:
            for line in self.res:
                for row in line:
                    new_file_2d_map.write(str(int(row)) + " ")
                new_file_2d_map.write("\n")

    # diff line
    def diff_line(self):
        line = ""

        if self.lineEdit_operation_sign.text() not in ["-", " -", "- ", "+", " +", "+ "]:
            self.lineEdit_operation_sign.setText(" - ")

        if not self.comboBox_point_number_A.currentText() == "" and not self.comboBox_polarisation_A.currentText() == "":
            self.line_A = "A(" + str(self.comboBox_polarisation_A.currentText()) + ")(" + str(self.comboBox_point_number_A.currentText()) + ")"
        if not self.comboBox_point_number_B.currentText() == "" and not self.comboBox_polarisation_B.currentText() == "":
            self.line_B = "B(" + str(self.comboBox_polarisation_B.currentText()) + ")(" + str(self.comboBox_point_number_B.currentText()) + ")"

        # fill one of the scans if only one is imported
        if not self.line_A == "" and self.line_B == "": line = self.line_A
        elif self.line_A == "" and not self.line_B == "": line = self.line_B
        # otherwice check if a line is already presented and what is the first. Keep the same order
        else:
            if self.lineEdit_operation.text().find("A(") == 0:
                line = self.line_A + self.lineEdit_operation_sign.text() + self.line_B
            else: line = self.line_B + self.lineEdit_operation_sign.text() + self.line_A

        self.lineEdit_operation.setText(line)

        self.draw_res()

    def button_swap_ab(self):

        if self.lineEdit_operation.text() == "": return

        if not self.lineEdit_operation.text().find(self.lineEdit_operation_sign.text()) > 0: return

        if self.lineEdit_operation.text().find(self.line_A) == 0: # then A scan is first
            line = self.line_B + self.lineEdit_operation_sign.text() + self.line_A
        else: line = self.line_A + self.lineEdit_operation_sign.text() + self.line_B

        self.lineEdit_operation.setText(line)

        self.draw_res()

    # draw graphs
    def draw_det_A_frame(self):

        self.graphicsView_scan_A.clear()

        if self.lineEdit_name_scan_A.text() == "" or self.comboBox_point_number_A.currentText() == "" or self.comboBox_polarisation_A.currentText() == "": return

        if self.comboBox_polarisation_A.currentText() == "np": scan_psd_A = "psd"
        else: scan_psd_A = "psd_" + self.comboBox_polarisation_A.currentText()

        with h5py.File(self.lineEdit_name_scan_A.text(), 'r') as file:

            if not self.comboBox_point_number_A.currentText() == "All":
                self.detector_image_A = file[list(file.keys())[0]].get("instrument").get('detectors').get(scan_psd_A).get('data')[int(self.comboBox_point_number_A.currentText())]
            else:
                for i in range(0, self.comboBox_point_number_A.count() - 1):
                    if i == 0: self.detector_image_A = file[list(file.keys())[0]].get("instrument").get('detectors').get(scan_psd_A).get('data')[i]
                    else: self.detector_image_A = numpy.add(self.detector_image_A, file[list(file.keys())[0]].get("instrument").get('detectors').get(scan_psd_A).get('data')[i])

            self.detector_image_A = numpy.around(self.detector_image_A, decimals=0).astype(int)
            self.detector_image_A = numpy.subtract(self.detector_image_A, numpy.zeros((self.detector_image_A.shape[0], self.detector_image_A.shape[1])))

            self.graphicsView_scan_A.setImage(self.detector_image_A, axes={'x':1, 'y':0}, levels=(0,0.1))

            colmap = pg.ColorMap(numpy.array([0.0, 0.1, 1.0]), numpy.array([[0, 0, 255, 255], [255, 0, 0, 255], [0, 255, 0, 255]], dtype=numpy.ubyte))
            self.graphicsView_scan_A.setColorMap(colmap)

    def draw_det_B_frame(self):

        self.graphicsView_scan_B.clear()

        if self.lineEdit_name_scan_B.text() == "" or self.comboBox_point_number_B.currentText() == "" or self.comboBox_polarisation_B.currentText() == "": return

        if self.comboBox_polarisation_B.currentText() == "np": scan_psd_B = "psd"
        else: scan_psd_B = "psd_" + self.comboBox_polarisation_B.currentText()

        with h5py.File(self.lineEdit_name_scan_B.text(), 'r') as file:

            if not self.comboBox_point_number_B.currentText() == "All":
                self.detector_image_B = file[list(file.keys())[0]].get("instrument").get('detectors').get(scan_psd_B).get('data')[int(self.comboBox_point_number_B.currentText())]
            else:
                for i in range(0, self.comboBox_point_number_B.count() - 1):
                    if i == 0:
                        self.detector_image_B = file[list(file.keys())[0]].get("instrument").get('detectors').get(scan_psd_B).get('data')[i]
                    else:
                        self.detector_image_B = numpy.add(self.detector_image_B, file[list(file.keys())[0]].get("instrument").get('detectors').get(scan_psd_B).get('data')[i])

            self.detector_image_B = numpy.around(self.detector_image_B, decimals=0).astype(int)
            self.detector_image_B = numpy.subtract(self.detector_image_B, numpy.zeros((self.detector_image_B.shape[0], self.detector_image_B.shape[1])))

            self.graphicsView_scan_B.setImage(self.detector_image_B, axes={'x': 1, 'y': 0}, levels=(0, 0.1))

            colmap = pg.ColorMap(numpy.array([0.0, 0.1, 1.0]), numpy.array([[0, 0, 255, 255], [255, 0, 0, 255], [0, 255, 0, 255]], dtype=numpy.ubyte))
            self.graphicsView_scan_B.setColorMap(colmap)

    def draw_res(self):

        if self.lineEdit_operation.text().find("()") > -1 or self.lineEdit_operation.text() in ["", self.lineEdit_operation_sign.text()] : return

        if not self.lineEdit_name_scan_A.text() == "" and (self.comboBox_point_number_A.currentText() == "" or self.comboBox_polarisation_A.currentText() == ""): return
        if not self.lineEdit_name_scan_B.text() == "" and (self.comboBox_point_number_B.currentText() == "" or self.comboBox_polarisation_B.currentText() == ""): return
        # Get requested in the line A frame
        if not self.line_A == "":

            if self.comboBox_polarisation_A.currentText() == "np": scan_psd_A = "psd"
            else: scan_psd_A = "psd_" + self.comboBox_polarisation_A.currentText()

            with h5py.File(self.lineEdit_name_scan_A.text(), 'r') as file:
                # seems to be a bug in numpy arrays imported from hdf5 files. Need to redefine array type to int.
                self.detector_image_A = numpy.around(self.detector_image_A, decimals=0).astype(int)
                self.detector_image_A = numpy.subtract(self.detector_image_A, numpy.zeros((self.detector_image_A.shape[0], self.detector_image_A.shape[1])))

                for index, scaler in enumerate(file[list(file.keys())[0]].get("instrument").get('scalers').get('SPEC_counter_mnemonics')):
                    if scan_psd_A == "psd": monitor_A_identifier = "b'mon0'"
                    elif scan_psd_A == "psd_uu": monitor_A_identifier = "b'm1'"
                    elif scan_psd_A == "psd_dd": monitor_A_identifier = "b'm2'"
                    elif scan_psd_A == "psd_du": monitor_A_identifier = "b'm3'"
                    elif scan_psd_A == "psd_ud": monitor_A_identifier = "b'm4'"

                    if monitor_A_identifier in str(scaler):
                        if not self.comboBox_point_number_A.currentText() == "All":
                            monitor_A = numpy.array(file[list(file.keys())[0]].get("instrument").get('scalers').get('data')).T[index][int(self.comboBox_point_number_A.currentText())]
                        else:
                            monitor_A = numpy.sum(numpy.array(file[list(file.keys())[0]].get("instrument").get('scalers').get('data')).T[index])

        # Get requested in the line B frame
        if not self.line_B == "":

            if self.comboBox_polarisation_B.currentText() == "np": scan_psd_B = "psd"
            else: scan_psd_B = "psd_" + self.comboBox_polarisation_B.currentText()

            with h5py.File(self.lineEdit_name_scan_B.text(), 'r') as file:
                # seems to be a bug in numpy arrays imported from hdf5 files. Need to redefine array type to int.
                self.detector_image_B = numpy.around(self.detector_image_B, decimals=0).astype(int)
                self.detector_image_B = numpy.subtract(self.detector_image_B, numpy.zeros((self.detector_image_B.shape[0], self.detector_image_B.shape[1])))

                for index, scaler in enumerate(file[list(file.keys())[0]].get("instrument").get('scalers').get('SPEC_counter_mnemonics')):
                    if scan_psd_B == "psd": monitor_B_identifier = "b'mon0'"
                    elif scan_psd_B == "psd_uu": monitor_B_identifier = "b'm1'"
                    elif scan_psd_B == "psd_dd": monitor_B_identifier = "b'm2'"
                    elif scan_psd_B == "psd_du": monitor_B_identifier = "b'm3'"
                    elif scan_psd_B == "psd_ud": monitor_B_identifier = "b'm4'"

                    if monitor_B_identifier in str(scaler):
                        if not self.comboBox_point_number_B.currentText() == "All":
                            monitor_B = numpy.array(file[list(file.keys())[0]].get("instrument").get('scalers').get('data')).T[index][int(self.comboBox_point_number_B.currentText())]
                        else:
                            monitor_B = numpy.sum(numpy.array(file[list(file.keys())[0]].get("instrument").get('scalers').get('data')).T[index])

        # Do the subtraction
        if self.line_A == "" and not self.line_B == "": res = self.detector_image_B
        elif not self.line_A == "" and self.line_B == "": res = self.detector_image_A
        else:
            if not self.lineEdit_operation.text().find(self.line_A) == 0:
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

        scale_low = 0
        scale_high = 1

        if self.lineEdit_operation.text().find("+") > 0:
            res = numpy.add(main, min)
        elif self.lineEdit_operation.text().find("-") > 0:
            res = numpy.subtract(main, min)
            scale_low = -10
            scale_high = 10

            if self.checkBox_reduce_2.isChecked() or self.checkBox_reduce_4.isChecked() or self.checkBox_reduce_8.isChecked():
                scale_low = -20
                scale_high = 20

        if self.checkBox_reduce_2.isChecked(): res = res.reshape(int(res.shape[0]/2), 2, int(res.shape[1]/2), 2).sum(axis=1).sum(axis=2)
        elif self.checkBox_reduce_4.isChecked(): res = res.reshape(int(res.shape[0]/4), 4, int(res.shape[1]/4), 4).sum(axis=1).sum(axis=2)
        elif self.checkBox_reduce_8.isChecked(): res = res.reshape(int(res.shape[0]/8), 8, int(res.shape[0]/8), 8).sum(axis=1).sum(axis=2)

        res = numpy.swapaxes(res, 0,1)

        self.res = res

        self.graphicsView_result.setImage(res)

        self.graphicsView_result.ui.histogram.setHistogramRange(scale_low, scale_high)
        self.graphicsView_result.ui.histogram.setLevels(scale_low, scale_high)

        self.statusbar.showMessage('Action "' + self.lineEdit_operation.text() + '" is performed.')

        self.button_int_roi()

    # Reduce number of pixels
    def reduce_x2(self):
        if self.checkBox_reduce_2.isChecked():
            self.checkBox_reduce_4.setChecked(False)
            self.checkBox_reduce_8.setChecked(False)
        else:
            self.checkBox_reduce_2.setChecked(False)

        self.draw_res()

        if self.checkBox_reduce_2.isChecked() and not self.res == []:
            self.lineEdit_roi_bottom.setText(str(int(round(len(self.res[1]) *0.9))))
            self.lineEdit_roi_right.setText(str(int(round(len(self.res[0]) *0.9))))
            if self.show_roi == 1:
                self.draw_roi()

    def reduce_x4(self):
        if self.checkBox_reduce_4.isChecked():
            self.checkBox_reduce_2.setChecked(False)
            self.checkBox_reduce_8.setChecked(False)
        else:
            self.checkBox_reduce_4.setChecked(False)

        self.draw_res()

        if self.checkBox_reduce_4.isChecked() and not self.res == []:
            self.lineEdit_roi_bottom.setText(str(int(round(len(self.res[1]) *0.9))))
            self.lineEdit_roi_right.setText(str(int(round(len(self.res[0]) *0.9))))
            if self.show_roi == 1:
                self.draw_roi()

    def reduce_x8(self):
        if self.checkBox_reduce_8.isChecked():
            self.checkBox_reduce_2.setChecked(False)
            self.checkBox_reduce_4.setChecked(False)
        else:
            self.checkBox_reduce_8.setChecked(False)

        self.draw_res()

        if self.checkBox_reduce_8.isChecked() and not self.res == []:
            self.lineEdit_roi_bottom.setText(str(int(round(len(self.res[1]) *0.9))))
            self.lineEdit_roi_right.setText(str(int(round(len(self.res[0]) *0.9))))
            if self.show_roi == 1:
                self.draw_roi()

    def menu_info(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)).replace("\\", "/") + "\icon.png"))
        msgBox.setText("SuperADAM .h5 scan subtractor. " + self.actionVersion.text() + "\n\n"
                                                                                            "Alexey.Klechikov@gmail.com\n\n"
                                                                                            "Check new version at https://github.com/Alexey-Klechikov/pySAsum/releases")
        msgBox.exec_()

    # ROI
    def button_roi(self):
        # resize Result 2D map to show what is hidden
        if self.show_roi == 0:
            self.graphicsView_result.setGeometry(QtCore.QRect(3, 48, 770, 383))
            self.show_roi = 1
        else:
            self.graphicsView_result.setGeometry(QtCore.QRect(3, 48, 770, 684))
            self.show_roi = 0

        # default roi
        try:
            self.lineEdit_roi_right.setText(str(int(round(len(self.res[0])*0.9))))
            self.lineEdit_roi_bottom.setText(str(int(round(len(self.res[1])*0.9))))
        except:
            self.lineEdit_roi_right.setText("50")
            self.lineEdit_roi_bottom.setText("50")

    def draw_roi(self):
        spots = []

        if self.draw_roi_result:
            self.graphicsView_result.removeItem(self.draw_roi_result)

        for i in range(int(self.lineEdit_roi_left.text()), int(self.lineEdit_roi_right.text())):
            spots.append({'x': i, 'y': int(self.lineEdit_roi_top.text())})
            spots.append({'x': i, 'y': int(self.lineEdit_roi_bottom.text())})

        for j in range(int(self.lineEdit_roi_top.text()), int(self.lineEdit_roi_bottom.text())):
            spots.append({'x': int(self.lineEdit_roi_left.text()), 'y': j})
            spots.append({'x': int(self.lineEdit_roi_right.text()), 'y': j})

        self.draw_roi_result = pg.ScatterPlotItem(spots=spots, size=1.5, pen=pg.mkPen(255, 255, 255))
        if self.show_roi == 1: self.graphicsView_result.addItem(self.draw_roi_result)

        self.button_int_roi()

    def button_int_roi(self):

        plot_x = []
        plot_y = []

        self.graphicsView_int_roi.getPlotItem().clear()

        # for some reason I cant just plot array (might be the problem with export of 2d arrays from hdf5), I do it in lame way instead
        if self.turn_roi == 0:
            for index, i in enumerate(self.res):
                if index < int(self.lineEdit_roi_left.text()) or index > int(self.lineEdit_roi_right.text()): continue
                plot_x.append(index)
                plot_y.append(i[int(self.lineEdit_roi_top.text()) : int(self.lineEdit_roi_bottom.text())].sum())
        else:
            for index, i in enumerate(numpy.swapaxes(self.res, 0, 1)):
                if index < int(self.lineEdit_roi_top.text()) or index > int(self.lineEdit_roi_bottom.text()): continue
                plot_x.append(index)
                plot_y.append(i[int(self.lineEdit_roi_left.text()) : int(self.lineEdit_roi_right.text())].sum())

        self.roi_plot_export = [plot_x, plot_y]

        s1 = pg.PlotCurveItem(x=plot_x, y=plot_y, pen=pg.mkPen(0, 0, 0))
        self.graphicsView_int_roi.addItem(s1)

    def button_export_int_roi(self):
        # Export ROI as simple 2 column dat
        current_dir = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
        dir = QtWidgets.QFileDialog().getExistingDirectory(None, "FileNames", current_dir)

        with open(dir + "/ROI.dat", "w") as new_file_roi:
            for i in range(0, len(self.roi_plot_export[0])):
                new_file_roi.write(str(self.roi_plot_export[0][i]) + " " + str(int(round(self.roi_plot_export[1][i]))) )
                new_file_roi.write("\n")

    def button_turn_roi(self):
        if self.turn_roi == 0: self.turn_roi = 1
        else: self.turn_roi = 0

        self.button_int_roi()

if __name__ == "__main__":
    import sys
    QtWidgets.QApplication.setStyle("Fusion")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
