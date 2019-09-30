from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import numpy, h5py, os

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

# Interface
class Ui_MainWindow(QtGui.QMainWindow):

    def setupUi(self, MainWindow):
        # Fonts
        font_headline = QtGui.QFont()
        font_headline.setPointSize(13)
        font_headline.setBold(True)

        font_graphs = QtGui.QFont()
        font_graphs.setPixelSize(12)
        font_graphs.setBold(False)

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
        MainWindow.setDockOptions(
            QtWidgets.QMainWindow.AllowNestedDocks | QtWidgets.QMainWindow.AllowTabbedDocks | QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setWindowTitle("pySAsum")
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
        self.lineEdit_scan_A_name = QtWidgets.QLineEdit(self.groupBox_scan_A)
        self.lineEdit_scan_A_name.setGeometry(QtCore.QRect(5, 22, 260, 20))
        self.lineEdit_scan_A_name.setObjectName("lineEdit_scan_A_name")
        self.lineEdit_scan_A_name.setFont(font_ee)
        self.toolButton_scan_A = QtWidgets.QToolButton(self.groupBox_scan_A)
        self.toolButton_scan_A.setGeometry(QtCore.QRect(275, 22, 20, 20))
        self.toolButton_scan_A.setObjectName("toolButton_scan_A")
        self.toolButton_scan_A.setText("...")
        self.toolButton_scan_A.setFont(font_ee)
        self.label_scan_A_type = QtWidgets.QLabel(self.groupBox_scan_A)
        self.label_scan_A_type.setFont(font_ee)
        self.label_scan_A_type.setGeometry(QtCore.QRect(5, 45, 40, 20))
        self.label_scan_A_type.setObjectName("label_scan_A_type")
        self.label_scan_A_type.setText("Type:")
        self.comboBox_scan_A_type = QtWidgets.QComboBox(self.groupBox_scan_A)
        self.comboBox_scan_A_type.setFont(font_ee)
        self.comboBox_scan_A_type.setGeometry(QtCore.QRect(45, 45, 150, 20))
        self.comboBox_scan_A_type.setObjectName("comboBox_scan_A_type")
        self.comboBox_scan_A_type.addItem("Single point")
        self.comboBox_scan_A_type.addItem("Integrated image")
        self.comboBox_scan_A_type.addItem("2D map")
        self.graphicsView_scan_A = pg.ImageView(self.groupBox_scan_A)
        self.graphicsView_scan_A.setGeometry(QtCore.QRect(3, 70, 295, 275))
        self.graphicsView_scan_A.setObjectName("graphicsView_scan_A")
        self.graphicsView_scan_A.ui.histogram.hide()
        self.graphicsView_scan_A.ui.menuBtn.hide()
        self.graphicsView_scan_A.ui.roiBtn.hide()
        self.label_scan_A_polarisation = QtWidgets.QLabel(self.groupBox_scan_A)
        self.label_scan_A_polarisation.setFont(font_ee)
        self.label_scan_A_polarisation.setGeometry(QtCore.QRect(5, 350, 75, 20))
        self.label_scan_A_polarisation.setObjectName("label_scan_A_polarisation")
        self.label_scan_A_polarisation.setText("Polarisation:")
        self.comboBox_scan_A_polarisation = QtWidgets.QComboBox(self.groupBox_scan_A)
        self.comboBox_scan_A_polarisation.setFont(font_ee)
        self.comboBox_scan_A_polarisation.setGeometry(QtCore.QRect(75, 350, 55, 20))
        self.comboBox_scan_A_polarisation.setObjectName("comboBox_scan_A_polarisation")
        self.label_scan_A_point_number = QtWidgets.QLabel(self.groupBox_scan_A)
        self.label_scan_A_point_number.setFont(font_ee)
        self.label_scan_A_point_number.setGeometry(QtCore.QRect(158, 350, 80, 20))
        self.label_scan_A_point_number.setObjectName("label_scan_A_point_number")
        self.label_scan_A_point_number.setText("Point number:")
        self.comboBox_scan_A_point_number = QtWidgets.QComboBox(self.groupBox_scan_A)
        self.comboBox_scan_A_point_number.setFont(font_ee)
        self.comboBox_scan_A_point_number.setGeometry(QtCore.QRect(240, 350, 55, 20))
        self.comboBox_scan_A_point_number.setObjectName("comboBox_scan_A_point_number")

        # Block: scan B
        self.label_scan_B = QtWidgets.QLabel(self.centralwidget)
        self.label_scan_B.setGeometry(QtCore.QRect(15, 385, 80, 20))
        self.label_scan_B.setObjectName("label_scan_B")
        self.label_scan_B.setText("Scan B")
        self.label_scan_B.setFont(font_headline)
        self.groupBox_scan_B = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_scan_B.setGeometry(QtCore.QRect(5, 390, 300, 375))
        self.groupBox_scan_B.setObjectName("groupBox_scan_B")
        self.lineEdit_scan_B_name = QtWidgets.QLineEdit(self.groupBox_scan_B)
        self.lineEdit_scan_B_name.setGeometry(QtCore.QRect(5, 22, 260, 20))
        self.lineEdit_scan_B_name.setObjectName("lineEdit_scan_B_name")
        self.lineEdit_scan_B_name.setFont(font_ee)
        self.toolButton_scan_B = QtWidgets.QToolButton(self.groupBox_scan_B)
        self.toolButton_scan_B.setGeometry(QtCore.QRect(275, 22, 20, 20))
        self.toolButton_scan_B.setObjectName("toolButton_scan_B")
        self.toolButton_scan_B.setText("...")
        self.toolButton_scan_B.setFont(font_ee)
        self.label_scan_B_type = QtWidgets.QLabel(self.groupBox_scan_B)
        self.label_scan_B_type.setFont(font_ee)
        self.label_scan_B_type.setGeometry(QtCore.QRect(5, 45, 40, 20))
        self.label_scan_B_type.setObjectName("label_scan_B_type")
        self.label_scan_B_type.setText("Type:")
        self.comboBox_scan_B_type = QtWidgets.QComboBox(self.groupBox_scan_B)
        self.comboBox_scan_B_type.setFont(font_ee)
        self.comboBox_scan_B_type.setGeometry(QtCore.QRect(45, 45, 150, 20))
        self.comboBox_scan_B_type.setObjectName("comboBox_scan_B_type")
        self.comboBox_scan_B_type.addItem("Single point")
        self.comboBox_scan_B_type.addItem("Integrated image")
        self.comboBox_scan_B_type.addItem("2D map")
        self.graphicsView_scan_B = pg.ImageView(self.groupBox_scan_B)
        self.graphicsView_scan_B.setGeometry(QtCore.QRect(3, 70, 295, 275))
        self.graphicsView_scan_B.setObjectName("graphicsView_scan_B")
        self.graphicsView_scan_B.ui.histogram.hide()
        self.graphicsView_scan_B.ui.menuBtn.hide()
        self.graphicsView_scan_B.ui.roiBtn.hide()
        self.label_scan_B_polarisation = QtWidgets.QLabel(self.groupBox_scan_B)
        self.label_scan_B_polarisation.setFont(font_ee)
        self.label_scan_B_polarisation.setGeometry(QtCore.QRect(5, 350, 75, 20))
        self.label_scan_B_polarisation.setObjectName("label_scan_B_polarisation")
        self.label_scan_B_polarisation.setText("Polarisation:")
        self.comboBox_scan_B_polarisation = QtWidgets.QComboBox(self.groupBox_scan_B)
        self.comboBox_scan_B_polarisation.setFont(font_ee)
        self.comboBox_scan_B_polarisation.setGeometry(QtCore.QRect(75, 350, 55, 20))
        self.comboBox_scan_B_polarisation.setObjectName("comboBox_scan_B_polarisation")
        self.label_scan_B_point_number = QtWidgets.QLabel(self.groupBox_scan_B)
        self.label_scan_B_point_number.setFont(font_ee)
        self.label_scan_B_point_number.setGeometry(QtCore.QRect(158, 350, 80, 20))
        self.label_scan_B_point_number.setObjectName("label_scan_B_point_number")
        self.label_scan_B_point_number.setText("Point number:")
        self.comboBox_scan_B_point_number = QtWidgets.QComboBox(self.groupBox_scan_B)
        self.comboBox_scan_B_point_number.setFont(font_ee)
        self.comboBox_scan_B_point_number.setGeometry(QtCore.QRect(240, 350, 55, 20))
        self.comboBox_scan_B_point_number.setObjectName("comboBox_scan_B_point_number")

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
        self.graphicsView_result_integrated_roi = pg.PlotWidget(self.groupBox_result)
        self.graphicsView_result_integrated_roi.setGeometry(QtCore.QRect(3, 431, 770, 275))
        self.graphicsView_result_integrated_roi.setObjectName("graphicsView_result_integrated_roi")
        self.graphicsView_result_integrated_roi.getAxis("bottom").tickFont = font_graphs
        self.graphicsView_result_integrated_roi.getAxis("bottom").setStyle(tickTextOffset=10)
        self.graphicsView_result_integrated_roi.getAxis("left").tickFont = font_graphs
        self.graphicsView_result_integrated_roi.getAxis("left").setStyle(tickTextOffset=10)
        self.graphicsView_result_integrated_roi.showAxis("top")
        self.graphicsView_result_integrated_roi.getAxis("top").setTicks([])
        self.graphicsView_result_integrated_roi.showAxis("right")
        self.graphicsView_result_integrated_roi.getAxis("right").setTicks([])
        self.label_result_roi_coorddinates = QtWidgets.QLabel(self.groupBox_result)
        self.label_result_roi_coorddinates.setGeometry(QtCore.QRect(10, 710, 400, 22))
        self.label_result_roi_coorddinates.setObjectName("label_result_roi_coorddinates")
        self.label_result_roi_coorddinates.setText(
            "ROI coordinates:  left                    right                    top                      bottom")
        self.label_result_roi_coorddinates.setFont(font_ee)
        self.lineEdit_result_roi_left = QtWidgets.QLineEdit(self.groupBox_result)
        self.lineEdit_result_roi_left.setGeometry(QtCore.QRect(127, 710, 40, 22))
        self.lineEdit_result_roi_left.setObjectName("lineEdit_result_roi_left")
        self.lineEdit_result_roi_left.setFont(font_ee)
        self.lineEdit_result_roi_left.setText("10")
        self.lineEdit_result_roi_right = QtWidgets.QLineEdit(self.groupBox_result)
        self.lineEdit_result_roi_right.setGeometry(QtCore.QRect(217, 710, 40, 22))
        self.lineEdit_result_roi_right.setObjectName("lineEdit_result_roi_right")
        self.lineEdit_result_roi_right.setFont(font_ee)
        self.lineEdit_result_roi_right.setText("20")
        self.lineEdit_result_roi_top = QtWidgets.QLineEdit(self.groupBox_result)
        self.lineEdit_result_roi_top.setGeometry(QtCore.QRect(297, 710, 40, 22))
        self.lineEdit_result_roi_top.setObjectName("lineEdit_result_roi_top")
        self.lineEdit_result_roi_top.setFont(font_ee)
        self.lineEdit_result_roi_top.setText("10")
        self.lineEdit_result_roi_bottom = QtWidgets.QLineEdit(self.groupBox_result)
        self.lineEdit_result_roi_bottom.setGeometry(QtCore.QRect(407, 710, 40, 22))
        self.lineEdit_result_roi_bottom.setObjectName("lineEdit_result_roi_bottom")
        self.lineEdit_result_roi_bottom.setFont(font_ee)
        self.lineEdit_result_roi_bottom.setText("20")
        self.pushButton_result_turn_roi = QtWidgets.QPushButton(self.groupBox_result)
        self.pushButton_result_turn_roi.setGeometry(QtCore.QRect(535, 710, 80, 22))
        self.pushButton_result_turn_roi.setObjectName("pushButton_result_turn_roi")
        self.pushButton_result_turn_roi.setText("Turn ROI")
        self.pushButton_result_turn_roi.setFont(font_headline)
        self.pushButton_result_export_integrated_roi = QtWidgets.QPushButton(self.groupBox_result)
        self.pushButton_result_export_integrated_roi.setGeometry(QtCore.QRect(620, 710, 151, 22))
        self.pushButton_result_export_integrated_roi.setObjectName("pushButton_result_export_integrated_roi")
        self.pushButton_result_export_integrated_roi.setText("Export int. ROI")
        self.pushButton_result_export_integrated_roi.setFont(font_headline)

        # This part of Result block is visible
        self.checkBox_result_divide_by_monitor = QtWidgets.QCheckBox(self.groupBox_result)
        self.checkBox_result_divide_by_monitor.setGeometry(QtCore.QRect(5, 22, 241, 22))
        self.checkBox_result_divide_by_monitor.setObjectName("checkBox_result_divide_by_monitor")
        self.checkBox_result_divide_by_monitor.setText("Divide by monitors")
        self.checkBox_result_divide_by_monitor.setFont(font_ee)
        self.label_result_aspect_ratio = QtWidgets.QLabel(self.groupBox_result)
        self.label_result_aspect_ratio.setFont(font_ee)
        self.label_result_aspect_ratio.setGeometry(QtCore.QRect(170, 22, 75, 20))
        self.label_result_aspect_ratio.setObjectName("label_result_aspect_ratio")
        self.label_result_aspect_ratio.setText("Aspect ratio:")
        self.horizontalSlider_result_aspect_ratio = QtWidgets.QSlider(self.groupBox_result)
        self.horizontalSlider_result_aspect_ratio.setGeometry(QtCore.QRect(250, 22, 140, 22))
        self.horizontalSlider_result_aspect_ratio.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_result_aspect_ratio.setObjectName("horizontalSlider_result_aspect_ratio")
        self.horizontalSlider_result_aspect_ratio.setMinimum(1)
        self.horizontalSlider_result_aspect_ratio.setMaximum(30)
        self.horizontalSlider_result_aspect_ratio.setValue(1)
        self.lineEdit_result_operation_sign = QtWidgets.QLineEdit(self.groupBox_result)
        self.lineEdit_result_operation_sign.setGeometry(QtCore.QRect(450, 22, 20, 22))
        self.lineEdit_result_operation_sign.setObjectName("lineEdit_result_operation_sign")
        self.lineEdit_result_operation_sign.setFont(font_ee)
        self.lineEdit_result_operation_sign.setText(" - ")
        self.lineEdit_result_operation = QtWidgets.QLineEdit(self.groupBox_result)
        self.lineEdit_result_operation.setGeometry(QtCore.QRect(475, 22, 200, 22))
        self.lineEdit_result_operation.setObjectName("lineEdit_result_operation")
        self.lineEdit_result_operation.setFont(font_ee)
        self.lineEdit_result_operation.setEnabled(False)
        self.lineEdit_result_operation.setStyleSheet("color:rgb(0,0,0)")
        self.pushButton_result_swap_ab = QtWidgets.QPushButton(self.groupBox_result)
        self.pushButton_result_swap_ab.setGeometry(QtCore.QRect(680, 22, 90, 22))
        self.pushButton_result_swap_ab.setObjectName("pushButton_result_swap_ab")
        self.pushButton_result_swap_ab.setText("(A<->B)")
        self.pushButton_result_swap_ab.setFont(font_headline)
        self.graphicsView_result = pg.ImageView(self.groupBox_result)
        self.graphicsView_result.setGeometry(QtCore.QRect(3, 48, 770, 684))
        self.graphicsView_result.setObjectName("graphicsView_result")
        self.graphicsView_result.ui.menuBtn.hide()
        self.graphicsView_result.ui.roiBtn.hide()
        self.graphicsView_result.ui.histogram.clickAccepted
        colmap = pg.ColorMap(numpy.array([0.4, 0.5, 0.6]),
                             numpy.array([[0, 0, 255, 255], [0, 0, 0, 255], [0, 255, 0, 255]], dtype=numpy.ubyte))
        self.graphicsView_result.setColorMap(colmap)

        self.label_result_reduce_number_of_pixels = QtWidgets.QLabel(self.groupBox_result)
        self.label_result_reduce_number_of_pixels.setGeometry(QtCore.QRect(10, 736, 250, 20))
        self.label_result_reduce_number_of_pixels.setObjectName("label_result_reduce_number_of_pixels")
        self.label_result_reduce_number_of_pixels.setText("Reduce number of pixels in each direction by:")
        self.label_result_reduce_number_of_pixels.setFont(font_ee)
        self.checkBox_result_reduce_number_of_pixels_by_2 = QtWidgets.QCheckBox(self.groupBox_result)
        self.checkBox_result_reduce_number_of_pixels_by_2.setGeometry(QtCore.QRect(270, 736, 241, 20))
        self.checkBox_result_reduce_number_of_pixels_by_2.setObjectName("checkBox_result_reduce_number_of_pixels_by_2")
        self.checkBox_result_reduce_number_of_pixels_by_2.setText("x2")
        self.checkBox_result_reduce_number_of_pixels_by_2.setFont(font_ee)
        self.checkBox_result_reduce_number_of_pixels_by_4 = QtWidgets.QCheckBox(self.groupBox_result)
        self.checkBox_result_reduce_number_of_pixels_by_4.setGeometry(QtCore.QRect(315, 736, 241, 20))
        self.checkBox_result_reduce_number_of_pixels_by_4.setObjectName("checkBox_result_reduce_number_of_pixels_by_4")
        self.checkBox_result_reduce_number_of_pixels_by_4.setText("x4")
        self.checkBox_result_reduce_number_of_pixels_by_4.setFont(font_ee)
        self.checkBox_result_reduce_number_of_pixels_by_8 = QtWidgets.QCheckBox(self.groupBox_result)
        self.checkBox_result_reduce_number_of_pixels_by_8.setGeometry(QtCore.QRect(360, 736, 241, 20))
        self.checkBox_result_reduce_number_of_pixels_by_8.setObjectName("checkBox_result_reduce_number_of_pixels_by_8")
        self.checkBox_result_reduce_number_of_pixels_by_8.setText("x8")
        self.checkBox_result_reduce_number_of_pixels_by_8.setFont(font_ee)
        self.pushButton_result_export = QtWidgets.QPushButton(self.groupBox_result)
        self.pushButton_result_export.setGeometry(QtCore.QRect(620, 735, 151, 22))
        self.pushButton_result_export.setObjectName("pushButton_clear_all")
        self.pushButton_result_export.setText("Export result (2D)")
        self.pushButton_result_export.setFont(font_headline)
        self.pushButton_result_ROI = QtWidgets.QPushButton(self.groupBox_result)
        self.pushButton_result_ROI.setGeometry(QtCore.QRect(535, 735, 80, 22))
        self.pushButton_result_ROI.setObjectName("pushButton_result_ROI")
        self.pushButton_result_ROI.setText("ROI")
        self.pushButton_result_ROI.setFont(font_headline)

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
        self.actionVersion.setText("Version 1.3.1")
        self.actionVersion.setFont(font_ee)
        self.menuHelp.addAction(self.actionVersion)
        self.menubar.addAction(self.menuHelp.menuAction())

# EE (Actions, drawing, math)
class GUI(Ui_MainWindow):

    current_dir = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")

    def __init__(self):

        super(GUI, self).__init__()
        self.setupUi(self)

        # Actions on clicks
        self.toolButton_scan_A.clicked.connect(self.button_import_scan)
        self.toolButton_scan_B.clicked.connect(self.button_import_scan)
        self.comboBox_scan_A_point_number.currentIndexChanged.connect(self.diff_line)
        self.comboBox_scan_A_polarisation.currentIndexChanged.connect(self.diff_line)
        self.comboBox_scan_A_type.currentIndexChanged.connect(self.change_interface)
        self.comboBox_scan_B_point_number.currentIndexChanged.connect(self.diff_line)
        self.comboBox_scan_B_polarisation.currentIndexChanged.connect(self.diff_line)
        self.comboBox_scan_B_type.currentIndexChanged.connect(self.change_interface)
        self.pushButton_result_export.clicked.connect(self.button_export_result)

        self.checkBox_result_reduce_number_of_pixels_by_2.stateChanged.connect(self.reduce_number_of_pixels)
        self.checkBox_result_reduce_number_of_pixels_by_4.stateChanged.connect(self.reduce_number_of_pixels)
        self.checkBox_result_reduce_number_of_pixels_by_8.stateChanged.connect(self.reduce_number_of_pixels)

        self.pushButton_result_swap_ab.clicked.connect(self.diff_line)
        self.checkBox_result_divide_by_monitor.stateChanged.connect(self.draw_res)
        self.horizontalSlider_result_aspect_ratio.valueChanged.connect(self.draw_res)
        self.pushButton_result_ROI.clicked.connect(self.button_roi_calculate_show_turn_square)
        self.pushButton_result_turn_roi.clicked.connect(self.button_roi_calculate_show_turn_square)
        self.pushButton_result_export_integrated_roi.clicked.connect(self.button_export_roi)
        self.lineEdit_result_roi_left.editingFinished.connect(self.button_roi_calculate_show_turn_square)
        self.lineEdit_result_roi_right.editingFinished.connect(self.button_roi_calculate_show_turn_square)
        self.lineEdit_result_roi_top.editingFinished.connect(self.button_roi_calculate_show_turn_square)
        self.lineEdit_result_roi_bottom.editingFinished.connect(self.button_roi_calculate_show_turn_square)
        self.lineEdit_result_operation_sign.editingFinished.connect(self.diff_line)
        self.actionVersion.triggered.connect(self.menu_info)

        # use arrays to keep old "lines" and redraw only if they are different from new ones
        self.line_A = ["", ""]
        self.line_B = ["", ""]
        self.show_roi = 0
        self.turn_roi = 0
        self.draw_roi_result = []

        self.detector_image_A = []
        self.detector_image_B = []
        self.res = []
        # I will use self.interface_A and self.interface_B to track what was
        # changed on the form and do changes without creating too many functions
        self.last_type_A = []
        self.last_type_B = []

        self.initial_roi = []

    def button_import_scan(self):
        if self.sender().objectName() == "toolButton_scan_A":

            self.lineEdit_scan_A_name.setText("")

            data_file = QtWidgets.QFileDialog().getOpenFileName(None, "FileNames", self.current_dir, ".h5 (*.h5)")
            if data_file[0] == "": return
            # Next "Import scans" will open last dir instead of the app location
            self.current_dir = data_file[0][0][:data_file[0][0].rfind("/")]

            self.lineEdit_scan_A_name.setText(data_file[0])
            if self.lineEdit_scan_A_name.text() == "": return

            self.comboBox_scan_A_point_number.clear()
            self.comboBox_scan_A_polarisation.clear()
            self.graphicsView_scan_A.clear()

            with h5py.File(self.lineEdit_scan_A_name.text(), 'r') as FILE:
                self.original_roi_A = numpy.array(FILE[list(FILE.keys())[0]].get("instrument").get('scalers').get('roi').get("roi"))
                self.lineEdit_result_roi_left.setText(str(self.original_roi_A[2])[:-2])
                self.lineEdit_result_roi_right.setText(str(self.original_roi_A[3])[:-2])
                self.lineEdit_result_roi_bottom.setText(str(self.original_roi_A[1])[:-2])
                self.lineEdit_result_roi_top.setText(str(self.original_roi_A[0])[:-2])

                for index, th in enumerate(FILE[list(FILE.keys())[0]].get("instrument").get('motors').get('th').get("value")):
                    self.comboBox_scan_A_point_number.addItem(str(index))

                for polarisation in FILE[list(FILE.keys())[0]].get("instrument").get('detectors'):

                    if polarisation in ("psd_uu", "psd_du", "psd_dd", "psd_ud"):
                        self.comboBox_scan_A_polarisation.addItem(str(polarisation)[-2:])
                    elif polarisation in ("psd"):
                        self.comboBox_scan_A_polarisation.addItem("np")

            self.comboBox_scan_A_point_number.setCurrentIndex(0)
            self.comboBox_scan_A_polarisation.setCurrentIndex(0)

            self.last_type_A = self.comboBox_scan_A_type.currentText()

        elif self.sender().objectName() == "toolButton_scan_B":
            self.lineEdit_scan_B_name.setText("")

            data_file = QtWidgets.QFileDialog().getOpenFileName(None, "FileNames", self.current_dir, ".h5 (*.h5)")
            if data_file[0] == "": return
            # Next "Import scans" will open last dir
            self.current_dir = data_file[0][0][:data_file[0][0].rfind("/")]

            self.lineEdit_scan_B_name.setText(data_file[0])
            if self.lineEdit_scan_B_name.text() == "": return

            self.comboBox_scan_B_point_number.clear()
            self.comboBox_scan_B_polarisation.clear()
            self.graphicsView_scan_B.clear()

            with h5py.File(self.lineEdit_scan_B_name.text(), 'r') as FILE:

                for index, th in enumerate(FILE[list(FILE.keys())[0]].get("instrument").get('motors').get('th').get("value")):
                    self.comboBox_scan_B_point_number.addItem(str(index))

                for polarisation in FILE[list(FILE.keys())[0]].get("instrument").get('detectors'):

                    if polarisation in ("psd_uu", "psd_du", "psd_dd", "psd_ud"):
                        self.comboBox_scan_B_polarisation.addItem(str(polarisation)[-2:])
                    elif polarisation in ("psd"):
                        self.comboBox_scan_B_polarisation.addItem("np")

            self.comboBox_scan_B_point_number.setCurrentIndex(0)
            self.comboBox_scan_B_polarisation.setCurrentIndex(0)

            self.last_type_B = self.comboBox_scan_B_type.currentText()

        self.diff_line()

    def button_export_result(self):
        # Export resulting picture as CSV
        dir = QtWidgets.QFileDialog().getExistingDirectory(None, "FileNames", self.current_dir)
        if dir == "": return

        with open(dir + "/2D_map (" + self.lineEdit_result_operation.text() + ").dat", "w") as new_file_2d_map:
            for line in self.res:
                for row in line:
                    new_file_2d_map.write(str(int(row)) + " ")
                new_file_2d_map.write("\n")

    def change_interface(self):

        if  not self.last_type_A == self.comboBox_scan_A_type.currentText():
            # if we have "Single point" as a mode and we just changet to it -> change "Point number" to the first one
            if self.comboBox_scan_A_type.currentText() == "Single point": self.comboBox_scan_A_point_number.setCurrentIndex(0)
            # if we have "2D map" as a mode and we just changet to it -> change Scan B Type to "2D map" also
            elif self.comboBox_scan_A_type.currentText() == "2D map": self.comboBox_scan_B_type.setCurrentIndex(2)
            # if we changed from "2D map" -> change B also
            if self.last_type_A == "2D map":
                if self.comboBox_scan_A_type.currentText() == "Single point": self.comboBox_scan_B_type.setCurrentIndex(0)
                elif self.comboBox_scan_A_type.currentText() == "Integrated image": self.comboBox_scan_B_type.setCurrentIndex(1)

        # same for B
        if not self.last_type_B == self.comboBox_scan_B_type.currentText():
            if self.comboBox_scan_B_type.currentText() == "Single point": self.comboBox_scan_B_point_number.setCurrentIndex(0)
            elif self.comboBox_scan_B_type.currentText() == "2D map": self.comboBox_scan_A_type.setCurrentIndex(2)
            if self.last_type_B == "2D map":
                if self.comboBox_scan_B_type.currentText() == "Single point": self.comboBox_scan_A_type.setCurrentIndex(0)
                elif self.comboBox_scan_B_type.currentText() == "Integrated image": self.comboBox_scan_A_type.setCurrentIndex(1)

        # show/hide some elements depends on the mode
        if self.comboBox_scan_A_type.currentText() == "2D map" or self.comboBox_scan_B_type.currentText() == "2D map":
            self.checkBox_result_reduce_number_of_pixels_by_2.setDisabled(True)
            self.checkBox_result_reduce_number_of_pixels_by_4.setDisabled(True)
            self.checkBox_result_reduce_number_of_pixels_by_8.setDisabled(True)
        else:
            self.checkBox_result_reduce_number_of_pixels_by_2.setDisabled(False)
            self.checkBox_result_reduce_number_of_pixels_by_4.setDisabled(False)
            self.checkBox_result_reduce_number_of_pixels_by_8.setDisabled(False)

        if self.comboBox_scan_A_type.currentText() in ["2D map", "Integrated image"]:
            self.comboBox_scan_A_point_number.setDisabled(True)
        else:
            self.comboBox_scan_A_point_number.setDisabled(False)

        if self.comboBox_scan_B_type.currentText() in ["2D map", "Integrated image"]:
            self.comboBox_scan_B_point_number.setDisabled(True)
        else:
            self.comboBox_scan_B_point_number.setDisabled(False)

        self.last_type_A = self.comboBox_scan_A_type.currentText()
        self.last_type_B = self.comboBox_scan_B_type.currentText()

        self.diff_line()

    # diff line
    def diff_line(self):

        if not self.sender().objectName() == "pushButton_result_swap_ab":
            line = ""

            if self.lineEdit_result_operation_sign.text() not in ["-", " -", "- ", "+", " +", "+ "]:
                self.lineEdit_result_operation_sign.setText(" - ")
            if self.comboBox_scan_A_type.currentText() == "Single point" and not self.comboBox_scan_A_point_number.currentText() == "":
                self.line_A[0] = "A(" + str(self.comboBox_scan_A_polarisation.currentText()) + ")(" + str(self.comboBox_scan_A_point_number.currentText()) + ")"
            elif self.comboBox_scan_A_type.currentText() == "Integrated image" and not self.comboBox_scan_A_polarisation.currentText() == "":
                self.line_A[0] = "A(" + str(self.comboBox_scan_A_polarisation.currentText()) + ")(All)"
            elif self.comboBox_scan_A_type.currentText() == "2D map" and not self.comboBox_scan_A_polarisation.currentText() == "":
                self.line_A[0] = "A(" + str(self.comboBox_scan_A_polarisation.currentText()) + ")(2D map)"

            if self.comboBox_scan_B_type.currentText() == "Single point" and not self.comboBox_scan_B_point_number.currentText() == "":
                self.line_B[0] = "B(" + str(self.comboBox_scan_B_polarisation.currentText()) + ")(" + str(self.comboBox_scan_B_point_number.currentText()) + ")"
            elif self.comboBox_scan_B_type.currentText() == "Integrated image" and not self.comboBox_scan_B_polarisation.currentText() == "":
                self.line_B[0] = "B(" + str(self.comboBox_scan_B_polarisation.currentText()) + ")(All)"
            elif self.comboBox_scan_B_type.currentText() == "2D map" and not self.comboBox_scan_B_polarisation.currentText() == "":
                self.line_B[0] = "B(" + str(self.comboBox_scan_B_polarisation.currentText()) + ")(2D map)"

            # fill one of the scans if it is the only one is imported
            if not self.line_A[0] == "" and self.line_B[0] == "": line = self.line_A[0]
            elif self.line_A[0] == "" and not self.line_B[0] == "": line = self.line_B[0]
            # otherwice check if a line is already presented and what is the first. Keep the same order
            else:
                if self.lineEdit_result_operation.text().find("A(") == 0:
                    line = self.line_A[0] + self.lineEdit_result_operation_sign.text() + self.line_B[0]
                else: line = self.line_B[0] + self.lineEdit_result_operation_sign.text() + self.line_A[0]

            self.lineEdit_result_operation.setText(line)

            if not self.line_A[0] == self.line_A[1]: self.draw_det_A_frame()
            self.line_A[1] = self.line_A[0]

            if not self.line_B[0] == self.line_B[1]: self.draw_det_B_frame()
            self.line_B[1] = self.line_B[0]

        else:

            if self.lineEdit_result_operation.text() == "": return

            if not self.lineEdit_result_operation.text().find(self.lineEdit_result_operation_sign.text()) > 0: return

            if self.lineEdit_result_operation.text().find(self.line_A[0]) == 0: # then A scan is first
                line = self.line_B[0] + self.lineEdit_result_operation_sign.text() + self.line_A[0]
            else: line = self.line_A[0] + self.lineEdit_result_operation_sign.text() + self.line_B[0]

            self.lineEdit_result_operation.setText(line)

        self.draw_res()

        self.button_roi_calculate_show_turn_square()

    # draw graphs
    def draw_det_A_frame(self):

        self.graphicsView_scan_A.clear()

        if self.lineEdit_scan_A_name.text() == "" or self.comboBox_scan_A_point_number.currentText() == "" or self.comboBox_scan_A_polarisation.currentText() == "": return

        # define "detector name" by polarisation
        if self.comboBox_scan_A_polarisation.currentText() == "np": SCAN_PSD_A = "psd"
        else: SCAN_PSD_A = "psd_" + self.comboBox_scan_A_polarisation.currentText()

        with h5py.File(self.lineEdit_scan_A_name.text(), 'r') as FILE:
            # sum all detector images
            if self.comboBox_scan_A_type.currentText() == "Integrated image":
                for i in range(0, self.comboBox_scan_A_point_number.count() - 1):
                    if i == 0: self.detector_image_A = FILE[list(FILE.keys())[0]].get("instrument").get('detectors').get(SCAN_PSD_A).get('data')[i]
                    else: self.detector_image_A = numpy.add(self.detector_image_A, FILE[list(FILE.keys())[0]].get("instrument").get('detectors').get(SCAN_PSD_A).get('data')[i])
            # sum each frame in Y axis
            elif self.comboBox_scan_A_type.currentText() == "2D map":
                self.detector_image_A = FILE[list(FILE.keys())[0]].get("instrument").get("detectors").get(SCAN_PSD_A).get('data')[:, :, :].sum(axis=1)
                self.detector_image_A = numpy.flip(self.detector_image_A, axis=0)
            # show specific frame
            else:
                self.detector_image_A = FILE[list(FILE.keys())[0]].get("instrument").get('detectors').get(SCAN_PSD_A).get('data')[int(self.comboBox_scan_A_point_number.currentText())]

            # seems to be a numpy bag - I cant draw out an array until I subtract zero array of the same size of it
            self.detector_image_A = numpy.around(self.detector_image_A, decimals=0).astype(int)
            self.detector_image_A = numpy.subtract(self.detector_image_A, numpy.zeros((self.detector_image_A.shape[0], self.detector_image_A.shape[1])))

            self.graphicsView_scan_A.setImage(self.detector_image_A, axes={'x':1, 'y':0}, levels=(0,0.1))

            colmap = pg.ColorMap(numpy.array([0.0, 0.1, 1.0]), numpy.array([[0, 0, 255, 255], [255, 0, 0, 255], [0, 255, 0, 255]], dtype=numpy.ubyte))
            self.graphicsView_scan_A.setColorMap(colmap)

    def draw_det_B_frame(self):
        # see comments in draw_det_A_frame
        self.graphicsView_scan_B.clear()

        if self.lineEdit_scan_B_name.text() == "" or self.comboBox_scan_B_point_number.currentText() == "" or self.comboBox_scan_B_polarisation.currentText() == "": return

        if self.comboBox_scan_B_polarisation.currentText() == "np": SCAN_PSD_B = "psd"
        else: SCAN_PSD_B = "psd_" + self.comboBox_scan_B_polarisation.currentText()

        with h5py.File(self.lineEdit_scan_B_name.text(), 'r') as FILE:

            if self.comboBox_scan_B_type.currentText() == "Integrated image":
                for i in range(0, self.comboBox_scan_B_point_number.count() - 1):
                    if i == 0: self.detector_image_B = FILE[list(FILE.keys())[0]].get("instrument").get('detectors').get(SCAN_PSD_B).get('data')[i]
                    else: self.detector_image_B = numpy.add(self.detector_image_B, FILE[list(FILE.keys())[0]].get("instrument").get('detectors').get(SCAN_PSD_B).get('data')[i])
            elif self.comboBox_scan_B_type.currentText() == "2D map":
                self.detector_image_B = FILE[list(FILE.keys())[0]].get("instrument").get("detectors").get(SCAN_PSD_B).get('data')[:, :, :].sum(axis=1)
                self.detector_image_B = numpy.flip(self.detector_image_B, axis=0)
            else:
                self.detector_image_B = FILE[list(FILE.keys())[0]].get("instrument").get('detectors').get(SCAN_PSD_B).get('data')[int(self.comboBox_scan_B_point_number.currentText())]

            self.detector_image_B = numpy.around(self.detector_image_B, decimals=0).astype(int)
            self.detector_image_B = numpy.subtract(self.detector_image_B, numpy.zeros((self.detector_image_B.shape[0], self.detector_image_B.shape[1])))

            self.graphicsView_scan_B.setImage(self.detector_image_B, axes={'x': 1, 'y': 0}, levels=(0, 0.1))

            colmap = pg.ColorMap(numpy.array([0.0, 0.1, 1.0]), numpy.array([[0, 0, 255, 255], [255, 0, 0, 255], [0, 255, 0, 255]], dtype=numpy.ubyte))
            self.graphicsView_scan_B.setColorMap(colmap)

    def draw_res(self):

        # Subtract 2D map only from other 2D map
        if (self.comboBox_scan_A_type.currentText() == "2D map" and not self.comboBox_scan_B_type.currentText() == "2D map") or (self.comboBox_scan_B_type.currentText() == "2D map" and not self.comboBox_scan_A_type.currentText() == "2D map"): return

        if self.lineEdit_result_operation.text().find("()") > -1 or self.lineEdit_result_operation.text() in ["", self.lineEdit_result_operation_sign.text()] : return
        if not self.lineEdit_scan_A_name.text() == "" and (self.comboBox_scan_A_point_number.currentText() == "" or self.comboBox_scan_A_polarisation.currentText() == ""): return
        if not self.lineEdit_scan_B_name.text() == "" and (self.comboBox_scan_B_point_number.currentText() == "" or self.comboBox_scan_B_polarisation.currentText() == ""): return

        # Get requested in the line A frame
        if not self.line_A[0] == "":

            if self.comboBox_scan_A_polarisation.currentText() == "np": SCAN_PSD_A = "psd"
            else: SCAN_PSD_A = "psd_" + self.comboBox_scan_A_polarisation.currentText()

            with h5py.File(self.lineEdit_scan_A_name.text(), 'r') as FILE:
                # seems to be a bug in numpy arrays imported from hdf5 files. Need to redefine array type to int.
                self.detector_image_A = numpy.around(self.detector_image_A, decimals=0).astype(int)
                self.detector_image_A = numpy.subtract(self.detector_image_A, numpy.zeros((self.detector_image_A.shape[0], self.detector_image_A.shape[1])))

                for index, scaler in enumerate(FILE[list(FILE.keys())[0]].get("instrument").get('scalers').get('SPEC_counter_mnemonics')):
                    if SCAN_PSD_A == "psd": monitor_A_identifier = "b'mon0'"
                    elif SCAN_PSD_A == "psd_uu": monitor_A_identifier = "b'm1'"
                    elif SCAN_PSD_A == "psd_dd": monitor_A_identifier = "b'm2'"
                    elif SCAN_PSD_A == "psd_du": monitor_A_identifier = "b'm3'"
                    elif SCAN_PSD_A == "psd_ud": monitor_A_identifier = "b'm4'"

                    if monitor_A_identifier in str(scaler):
                        if self.comboBox_scan_A_point_number.currentText() in ["All", "2D map"]:
                            monitor_A = numpy.sum(numpy.array(FILE[list(FILE.keys())[0]].get("instrument").get('scalers').get('data')).T[index])
                        else:
                            monitor_A = numpy.array(FILE[list(FILE.keys())[0]].get("instrument").get('scalers').get('data')).T[index][int(self.comboBox_scan_A_point_number.currentText())]

        # Get requested in the line B frame
        if not self.line_B[0] == "":

            if self.comboBox_scan_B_polarisation.currentText() == "np": SCAN_PSD_B = "psd"
            else: SCAN_PSD_B = "psd_" + self.comboBox_scan_B_polarisation.currentText()

            with h5py.File(self.lineEdit_scan_B_name.text(), 'r') as FILE:
                # seems to be a bug in numpy arrays imported from hdf5 files. Need to redefine array type to int.
                self.detector_image_B = numpy.around(self.detector_image_B, decimals=0).astype(int)
                self.detector_image_B = numpy.subtract(self.detector_image_B, numpy.zeros((self.detector_image_B.shape[0], self.detector_image_B.shape[1])))

                for index, scaler in enumerate(FILE[list(FILE.keys())[0]].get("instrument").get('scalers').get('SPEC_counter_mnemonics')):
                    if SCAN_PSD_B == "psd": monitor_B_identifier = "b'mon0'"
                    elif SCAN_PSD_B == "psd_uu": monitor_B_identifier = "b'm1'"
                    elif SCAN_PSD_B == "psd_dd": monitor_B_identifier = "b'm2'"
                    elif SCAN_PSD_B == "psd_du": monitor_B_identifier = "b'm3'"
                    elif SCAN_PSD_B == "psd_ud": monitor_B_identifier = "b'm4'"

                    if monitor_B_identifier in str(scaler):
                        if self.comboBox_scan_B_point_number.currentText() in ["All", "2D map"]:
                            monitor_B = numpy.sum(numpy.array(FILE[list(FILE.keys())[0]].get("instrument").get('scalers').get('data')).T[index])
                        else:
                            monitor_B = numpy.array(FILE[list(FILE.keys())[0]].get("instrument").get('scalers').get('data')).T[index][int(self.comboBox_scan_B_point_number.currentText())]

        # Do the subtraction
        if self.line_A[0] == "" and not self.line_B[0] == "": RES = self.detector_image_B
        elif not self.line_A[0] == "" and self.line_B[0] == "": RES = self.detector_image_A
        else:
            if not self.lineEdit_result_operation.text().find(self.line_A[0]) == 0:
                main = self.detector_image_B
                main_mon = monitor_B
                min = self.detector_image_A
                min_mon = monitor_A
            else:
                main = self.detector_image_A
                main_mon = monitor_A
                min = self.detector_image_B
                min_mon = monitor_B

            if self.checkBox_result_divide_by_monitor.isChecked():
                main = numpy.divide(main, main_mon/min_mon)

        scale_low = 0
        scale_high = 1

        if self.lineEdit_result_operation.text().find("+") > 0:
            RES = numpy.add(main, min)
        elif self.lineEdit_result_operation.text().find("-") > 0:
            RES = numpy.subtract(main, min)
            scale_low = -10
            scale_high = 10

            if self.checkBox_result_reduce_number_of_pixels_by_2.isChecked() or self.checkBox_result_reduce_number_of_pixels_by_4.isChecked() or self.checkBox_result_reduce_number_of_pixels_by_8.isChecked():
                scale_low = -20
                scale_high = 20

        if self.checkBox_result_reduce_number_of_pixels_by_2.isChecked(): RES = RES.reshape(int(RES.shape[0]/2), 2, int(RES.shape[1]/2), 2).sum(axis=1).sum(axis=2)
        elif self.checkBox_result_reduce_number_of_pixels_by_4.isChecked(): RES = RES.reshape(int(RES.shape[0]/4), 4, int(RES.shape[1]/4), 4).sum(axis=1).sum(axis=2)
        elif self.checkBox_result_reduce_number_of_pixels_by_8.isChecked(): RES = RES.reshape(int(RES.shape[0]/8), 8, int(RES.shape[0]/8), 8).sum(axis=1).sum(axis=2)

        RES = numpy.swapaxes(RES, 0,1)

        self.res = RES

        self.graphicsView_result.setImage(RES, scale=(1, self.horizontalSlider_result_aspect_ratio.value()))
        if not self.detector_image_A == []:
            self.graphicsView_scan_A.setImage(self.detector_image_A, axes={'x': 1, 'y': 0}, levels=(0, 0.1), scale=(1, self.horizontalSlider_result_aspect_ratio.value()))
        if not self.detector_image_B == []:
            self.graphicsView_scan_B.setImage(self.detector_image_B, axes={'x': 1, 'y': 0}, levels=(0, 0.1), scale=(1, self.horizontalSlider_result_aspect_ratio.value()))

        self.graphicsView_result.ui.histogram.setHistogramRange(scale_low, scale_high)
        self.graphicsView_result.ui.histogram.setLevels(scale_low, scale_high)

        self.statusbar.showMessage('Action "' + self.lineEdit_result_operation.text() + '" is performed.')

        self.button_roi_calculate_show_turn_square()

    # Reduce number of pixels
    def reduce_number_of_pixels(self):

        self.lineEdit_result_roi_left.setText(self.initial_roi[0])
        self.lineEdit_result_roi_right.setText(self.initial_roi[1])
        self.lineEdit_result_roi_bottom.setText(self.initial_roi[2])
        self.lineEdit_result_roi_top.setText(self.initial_roi[3])

        if self.sender().objectName() == "checkBox_result_reduce_number_of_pixels_by_2":
            if self.checkBox_result_reduce_number_of_pixels_by_2.isChecked():
                self.checkBox_result_reduce_number_of_pixels_by_4.setChecked(False)
                self.checkBox_result_reduce_number_of_pixels_by_8.setChecked(False)
                self.lineEdit_result_roi_left.setText(str(int(round(int(self.initial_roi[0])/2))))
                self.lineEdit_result_roi_right.setText(str(int(round(int(self.initial_roi[1])/2))))
                self.lineEdit_result_roi_bottom.setText(str(int(round(int(self.initial_roi[2])/2))))
                self.lineEdit_result_roi_top.setText(str(int(round(int(self.initial_roi[3])/2))))
            else:
                self.checkBox_result_reduce_number_of_pixels_by_2.setChecked(False)

        elif self.sender().objectName() == "checkBox_result_reduce_number_of_pixels_by_4":
            if self.checkBox_result_reduce_number_of_pixels_by_4.isChecked():
                self.checkBox_result_reduce_number_of_pixels_by_2.setChecked(False)
                self.checkBox_result_reduce_number_of_pixels_by_8.setChecked(False)
                self.lineEdit_result_roi_left.setText(str(int(round(int(self.initial_roi[0])/4))))
                self.lineEdit_result_roi_right.setText(str(int(round(int(self.initial_roi[1])/4))))
                self.lineEdit_result_roi_bottom.setText(str(int(round(int(self.initial_roi[2])/4))))
                self.lineEdit_result_roi_top.setText(str(int(round(int(self.initial_roi[3])/4))))
            else:
                self.checkBox_result_reduce_number_of_pixels_by_4.setChecked(False)
        elif self.sender().objectName() == "checkBox_result_reduce_number_of_pixels_by_8":
            if self.checkBox_result_reduce_number_of_pixels_by_8.isChecked():
                self.checkBox_result_reduce_number_of_pixels_by_2.setChecked(False)
                self.checkBox_result_reduce_number_of_pixels_by_4.setChecked(False)
                self.lineEdit_result_roi_left.setText(str(int(round(int(self.initial_roi[0])/8))))
                self.lineEdit_result_roi_right.setText(str(int(round(int(self.initial_roi[1])/8))))
                self.lineEdit_result_roi_bottom.setText(str(int(round(int(self.initial_roi[2])/8))))
                self.lineEdit_result_roi_top.setText(str(int(round(int(self.initial_roi[3])/8))))
            else:
                self.checkBox_result_reduce_number_of_pixels_by_8.setChecked(False)

        self.button_roi_calculate_show_turn_square()
        self.draw_res()

    def menu_info(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)).replace("\\", "/") + "\icon.png"))
        msgBox.setText("PySAsum V1.3.1\n\n"
                                                                                            "Alexey.Klechikov@gmail.com\n\n"
                                                                                            "Check new version at https://github.com/Alexey-Klechikov/pySAsum/releases")
        msgBox.exec_()

    # ROI
    def button_roi_calculate_show_turn_square(self):

        ####### turn roi
        if self.sender().objectName() == "pushButton_result_turn_roi":
            if self.turn_roi == 0: self.turn_roi = 1
            else: self.turn_roi = 0

        ####### show roi
        if self.sender().objectName() == "pushButton_result_ROI":
            # resize Result 2D map to show what is hidden
            if self.show_roi == 0:
                self.graphicsView_result.setGeometry(QtCore.QRect(3, 48, 770, 383))
                self.show_roi = 1
            else:
                self.graphicsView_result.setGeometry(QtCore.QRect(3, 48, 770, 684))
                self.show_roi = 0

        ####### calculate
        plot_x = []
        plot_y = []

        self.graphicsView_result_integrated_roi.getPlotItem().clear()

        # for some reason I cant just plot an array (might be the problem with export of 2d arrays from hdf5), I do it in lame way instead
        if self.turn_roi == 0:
            for index, i in enumerate(self.res):
                if index < int(self.lineEdit_result_roi_left.text()) or index > int(self.lineEdit_result_roi_right.text()): continue
                plot_x.append(index)
                plot_y.append(i[int(self.lineEdit_result_roi_top.text()) : int(self.lineEdit_result_roi_bottom.text())].sum())
        else:
            for index, i in enumerate(numpy.swapaxes(self.res, 0, 1)):
                if index < int(self.lineEdit_result_roi_top.text()) or index > int(self.lineEdit_result_roi_bottom.text()): continue
                plot_x.append(index)
                plot_y.append(i[int(self.lineEdit_result_roi_left.text()) : int(self.lineEdit_result_roi_right.text())].sum())

        self.roi_plot_export = [plot_x, plot_y]

        s1 = pg.PlotCurveItem(x=plot_x, y=plot_y, pen=pg.mkPen(0, 0, 0))
        self.graphicsView_result_integrated_roi.addItem(s1)

        ####### square
        if self.sender().objectName() in ["comboBox_scan_A_type", "comboBox_scan_B_type"]:
            if self.comboBox_scan_A_type.currentText() == "2D map" or self.comboBox_scan_B_type.currentText() == "2D map":
                self.lineEdit_result_roi_bottom.setText(str(self.res.shape[1]))
                self.lineEdit_result_roi_top.setText("0")
            elif not self.initial_roi == []:
                self.lineEdit_result_roi_bottom.setText(self.initial_roi[2])
                self.lineEdit_result_roi_top.setText(self.initial_roi[3])

        if not self.checkBox_result_reduce_number_of_pixels_by_2.isChecked() and not self.checkBox_result_reduce_number_of_pixels_by_4.isChecked() and not self.checkBox_result_reduce_number_of_pixels_by_8.isChecked() and not self.comboBox_scan_A_type.currentText() == "2D map" and not self.comboBox_scan_B_type.currentText() == "2D map":
            self.initial_roi = [self.lineEdit_result_roi_left.text(), self.lineEdit_result_roi_right.text(), self.lineEdit_result_roi_bottom.text(), self.lineEdit_result_roi_top.text()]

        spots = []
        if self.draw_roi_result:
            self.graphicsView_result.removeItem(self.draw_roi_result)

        for i in range(int(self.lineEdit_result_roi_left.text()), int(self.lineEdit_result_roi_right.text())):
            spots.append({'x': i, 'y': int(self.lineEdit_result_roi_top.text())*self.horizontalSlider_result_aspect_ratio.value()})
            spots.append({'x': i, 'y': int(self.lineEdit_result_roi_bottom.text())*self.horizontalSlider_result_aspect_ratio.value()})

        for j in range(int(self.lineEdit_result_roi_top.text()), int(self.lineEdit_result_roi_bottom.text())):
            spots.append({'x': int(self.lineEdit_result_roi_left.text()), 'y': j*self.horizontalSlider_result_aspect_ratio.value()})
            spots.append({'x': int(self.lineEdit_result_roi_right.text()), 'y': j*self.horizontalSlider_result_aspect_ratio.value()})

        self.draw_roi_result = pg.ScatterPlotItem(spots=spots, size=1.5, pen=pg.mkPen(255, 255, 255))

        if self.show_roi == 1:
            self.graphicsView_result.addItem(self.draw_roi_result)

    def button_export_roi(self):
        # Export ROI as simple 2 column dat
        dir = QtWidgets.QFileDialog().getExistingDirectory(None, "FileNames", self.current_dir)
        if dir == "": return

        with open(dir + "/ROI (" + self.lineEdit_result_operation.text() + ").dat", "w") as new_file_roi:
            for i in range(0, len(self.roi_plot_export[0])):
                new_file_roi.write(str(self.roi_plot_export[0][i]) + " " + str(int(round(self.roi_plot_export[1][i]))) )
                new_file_roi.write("\n")

if __name__ == "__main__":
    import sys
    QtWidgets.QApplication.setStyle("Fusion")
    app = QtWidgets.QApplication(sys.argv)
    prog = GUI()
    prog.show()
    sys.exit(app.exec_())
