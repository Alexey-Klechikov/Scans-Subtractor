'''
Install with:
* Windows - pyinstaller --onefile --noconsole -i"C:\icon.ico" --add-data C:\icon.ico;images C:\pySAsum_V1.4.py
* MacOS - pyinstaller --onefile --windowed pySAsum_V1.4.py

Requirements for a nice interface:
* PyQt<=5.12.2
'''

from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import numpy as np
import h5py, os, sys, pkgutil, platform

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

# Interface
class Ui_MainWindow(QtGui.QMainWindow):

    groupbox_os_displ = 0 if platform.system() == 'Windows' else 2 # PyQt version/OS fix

    def __create_element(self, object, geometry, objectName, text=None, font=None, placeholder=None, visible=None, stylesheet=None, checked=None, checkable=None, title=None, combo=None, enabled=None):
        object.setObjectName(objectName)

        if not geometry == [999, 999, 999, 999]:
            object.setGeometry(QtCore.QRect(geometry[0], geometry[1], geometry[2], geometry[3]))

        if not text == None: object.setText(text)
        if not title == None: object.setTitle(title)
        if not font == None: object.setFont(font)
        if not placeholder == None: object.setPlaceholderText(placeholder)
        if not visible == None: object.setVisible(visible)
        if not checked == None: object.setChecked(checked)
        if not checkable == None: object.setCheckable(checked)
        if not enabled == None: object.setEnabled(enabled)

        if not stylesheet == None: object.setStyleSheet(stylesheet)

        if not combo == None:
            for i in combo: object.addItem(str(i))

    def setupUi(self, MainWindow):
        # Fonts
        font_headline = QtGui.QFont()
        font_headline.setPointSize(11 if platform.system() == 'Windows' else 13)
        font_headline.setBold(True)

        font_graphs = QtGui.QFont()
        font_graphs.setPixelSize(12)
        font_graphs.setBold(False)

        font_ee = QtGui.QFont()
        font_ee.setPointSize(9  if platform.system() == 'Windows' else 11)
        font_ee.setBold(False)

        # Graphs background
        pg.setConfigOption('background', (255, 255, 255))
        pg.setConfigOption('foreground', 'k')

        # Main window
        MainWindow_size = [1100, 809]  if platform.system() == 'Windows' else [1100, 789]
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(MainWindow_size[0], MainWindow_size[1])
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(MainWindow_size[0], MainWindow_size[1]))
        MainWindow.setMaximumSize(QtCore.QSize(MainWindow_size[0], MainWindow_size[1]))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks | QtWidgets.QMainWindow.AllowTabbedDocks | QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setWindowTitle("pySAsum")
        # when we create .exe with pyinstaller, we need to store icon inside it. Then we find it inside unpacked temp directory.
        for i in pkgutil.iter_importers():
            path = str(i).split("'")[1].replace("\\\\", "\\") if str(i).find('FileFinder')>=0 else None
            if path != None: self.iconpath = path + "\\images\\icon.ico"
        MainWindow.setWindowIcon(QtGui.QIcon(self.iconpath))
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Block: scan A
        self.label_scan_A = QtWidgets.QLabel(self.centralwidget)
        self.__create_element(self.label_scan_A, [15, 0, 80, 20], "label_scan_A", text="Scan A", font=font_headline, stylesheet="QLabel { color : blue; }")
        self.groupBox_scan_A = QtWidgets.QGroupBox(self.centralwidget)
        self.__create_element(self.groupBox_scan_A, [5, 6-self.groupbox_os_displ, 300, 375+self.groupbox_os_displ], "groupBox_scan_A")
        self.lineEdit_scan_A_name = QtWidgets.QLineEdit(self.groupBox_scan_A)
        self.__create_element(self.lineEdit_scan_A_name, [5, 22+self.groupbox_os_displ, 260, 20], "lineEdit_scan_A_name", font=font_ee)
        self.toolButton_scan_A = QtWidgets.QToolButton(self.groupBox_scan_A)
        self.__create_element(self.toolButton_scan_A, [275, 22+self.groupbox_os_displ, 20, 20], "toolButton_scan_A", text="...", font=font_ee)
        self.label_scan_A_type = QtWidgets.QLabel(self.groupBox_scan_A)
        self.__create_element(self.label_scan_A_type, [5, 45+self.groupbox_os_displ, 40, 20], "label_scan_A_type", text="Type:", font=font_ee)
        self.comboBox_scan_A_type = QtWidgets.QComboBox(self.groupBox_scan_A)
        self.__create_element(self.comboBox_scan_A_type, [45, 45+self.groupbox_os_displ, 150, 20], "comboBox_scan_A_type", combo=["Single point", "Integrated image", "2D map"], font=font_ee)
        self.graphicsView_scan_A = pg.ImageView(self.groupBox_scan_A)
        self.__create_element(self.graphicsView_scan_A, [3, 70+self.groupbox_os_displ, 295, 275], "graphicsView_scan_A")
        self.graphicsView_scan_A.ui.histogram.hide()
        self.graphicsView_scan_A.ui.menuBtn.hide()
        self.graphicsView_scan_A.ui.roiBtn.hide()
        self.label_scan_A_polarisation = QtWidgets.QLabel(self.groupBox_scan_A)
        self.__create_element(self.label_scan_A_polarisation, [5, 350+self.groupbox_os_displ, 75, 20], "label_scan_A_polarisation", text="Polarisation:", font=font_ee)
        self.comboBox_scan_A_polarisation = QtWidgets.QComboBox(self.groupBox_scan_A)
        self.__create_element(self.comboBox_scan_A_polarisation, [75, 350+self.groupbox_os_displ, 55, 20], "comboBox_scan_A_polarisation", font=font_ee)
        self.label_scan_A_pointNumber = QtWidgets.QLabel(self.groupBox_scan_A)
        self.__create_element(self.label_scan_A_pointNumber, [158, 350+self.groupbox_os_displ, 80, 20], "label_scan_A_pointNumber", text="Point number:", font=font_ee)
        self.comboBox_scan_A_pointNumber = QtWidgets.QComboBox(self.groupBox_scan_A)
        self.__create_element(self.comboBox_scan_A_pointNumber, [240, 350+self.groupbox_os_displ, 55, 20], "comboBox_scan_A_pointNumber", font=font_ee)

        # Block: scan B
        self.label_scan_B = QtWidgets.QLabel(self.centralwidget)
        self.__create_element(self.label_scan_B, [15, 385, 80, 20], "label_scan_B", text="Scan B", font=font_headline, stylesheet="QLabel { color : blue; }")
        self.groupBox_scan_B = QtWidgets.QGroupBox(self.centralwidget)
        self.__create_element(self.groupBox_scan_B, [5, 391-self.groupbox_os_displ, 300, 375+self.groupbox_os_displ], "groupBox_scan_B")
        self.lineEdit_scan_B_name = QtWidgets.QLineEdit(self.groupBox_scan_B)
        self.__create_element(self.lineEdit_scan_B_name, [5, 22+self.groupbox_os_displ, 260, 20], "lineEdit_scan_B_name", font=font_ee)
        self.toolButton_scan_B = QtWidgets.QToolButton(self.groupBox_scan_B)
        self.__create_element(self.toolButton_scan_B, [275, 22+self.groupbox_os_displ, 20, 20], "toolButton_scan_B", text="...", font=font_ee)
        self.label_scan_B_type = QtWidgets.QLabel(self.groupBox_scan_B)
        self.__create_element(self.label_scan_B_type, [5, 45+self.groupbox_os_displ, 40, 20], "label_scan_B_type", text="Type:", font=font_ee)
        self.comboBox_scan_B_type = QtWidgets.QComboBox(self.groupBox_scan_B)
        self.__create_element(self.comboBox_scan_B_type, [45, 45+self.groupbox_os_displ, 150, 20], "comboBox_scan_B_type", combo=["Single point", "Integrated image", "2D map"], font=font_ee)
        self.graphicsView_scan_B = pg.ImageView(self.groupBox_scan_B)
        self.__create_element(self.graphicsView_scan_B, [3, 70+self.groupbox_os_displ, 295, 275], "graphicsView_scan_B")
        self.graphicsView_scan_B.ui.histogram.hide()
        self.graphicsView_scan_B.ui.menuBtn.hide()
        self.graphicsView_scan_B.ui.roiBtn.hide()
        self.label_scan_B_polarisation = QtWidgets.QLabel(self.groupBox_scan_B)
        self.__create_element(self.label_scan_B_polarisation, [5, 350+self.groupbox_os_displ, 75, 20], "label_scan_B_polarisation", text="Polarisation:", font=font_ee)
        self.comboBox_scan_B_polarisation = QtWidgets.QComboBox(self.groupBox_scan_B)
        self.__create_element(self.comboBox_scan_B_polarisation, [75, 350+self.groupbox_os_displ, 55, 20], "comboBox_scan_B_polarisation", font=font_ee)
        self.label_scan_B_pointNumber = QtWidgets.QLabel(self.groupBox_scan_B)
        self.__create_element(self.label_scan_B_pointNumber, [158, 350+self.groupbox_os_displ, 80, 20], "label_scan_B_pointNumber", text="Point number:", font=font_ee)
        self.comboBox_scan_B_pointNumber = QtWidgets.QComboBox(self.groupBox_scan_B)
        self.__create_element(self.comboBox_scan_B_pointNumber, [240, 350+self.groupbox_os_displ, 55, 20], "comboBox_scan_B_pointNumber", font=font_ee)

        # Block: Result
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.__create_element(self.label_result, [325, 0, 61, 20], "label_result", text="Result", font=font_headline, stylesheet="QLabel { color : blue; }")
        self.groupBox_result = QtWidgets.QGroupBox(self.centralwidget)
        self.__create_element(self.groupBox_result, [320, 6-self.groupbox_os_displ, 775, 760+self.groupbox_os_displ], "groupBox_result")
        # ROI part is hidden by default
        self.graphicsView_result_integratedRoi = pg.PlotWidget(self.groupBox_result)
        self.__create_element(self.graphicsView_result_integratedRoi, [13, 440+self.groupbox_os_displ, 770, 265], "graphicsView_result_integratedRoi")
        self.graphicsView_result_integratedRoi.getAxis("bottom").tickFont = font_graphs
        self.graphicsView_result_integratedRoi.getAxis("bottom").setStyle(tickTextOffset=10)
        self.graphicsView_result_integratedRoi.getAxis("left").tickFont = font_graphs
        self.graphicsView_result_integratedRoi.getAxis("left").setStyle(tickTextOffset=5)
        self.graphicsView_result_integratedRoi.showAxis("top")
        self.graphicsView_result_integratedRoi.getAxis("top").setStyle(showValues=False)
        self.graphicsView_result_integratedRoi.showAxis("right")
        self.graphicsView_result_integratedRoi.getAxis("right").setStyle(showValues=False)
        self.label_result_roi_left = QtWidgets.QLabel(self.groupBox_result)
        self.__create_element(self.label_result_roi_left, [10, 710+self.groupbox_os_displ, 130, 22], "label_result_roi_left", text="ROI coordinates: left", font=font_ee)
        self.lineEdit_result_roi_left = QtWidgets.QLineEdit(self.groupBox_result)
        self.__create_element(self.lineEdit_result_roi_left, [127, 710+self.groupbox_os_displ, 40, 22], "lineEdit_result_roi_left", text="10", font=font_ee)
        self.label_result_roi_right = QtWidgets.QLabel(self.groupBox_result)
        self.__create_element(self.label_result_roi_right, [183, 710+self.groupbox_os_displ, 40, 22], "label_result_roi_right", text="right", font=font_ee)
        self.lineEdit_result_roi_right = QtWidgets.QLineEdit(self.groupBox_result)
        self.__create_element(self.lineEdit_result_roi_right, [217, 710+self.groupbox_os_displ, 40, 22], "lineEdit_result_roi_right", text="20", font=font_ee)
        self.label_result_roi_top = QtWidgets.QLabel(self.groupBox_result)
        self.__create_element(self.label_result_roi_top, [270, 710+self.groupbox_os_displ, 40, 22], "label_result_roi_top", text="top", font=font_ee)
        self.lineEdit_result_roi_top = QtWidgets.QLineEdit(self.groupBox_result)
        self.__create_element(self.lineEdit_result_roi_top, [297, 710+self.groupbox_os_displ, 40, 22], "lineEdit_result_roi_top", text="10", font=font_ee)
        self.label_result_roi_bottom = QtWidgets.QLabel(self.groupBox_result)
        self.__create_element(self.label_result_roi_bottom, [348, 710+self.groupbox_os_displ, 42, 22], "label_result_roi_bottom", text="bottom", font=font_ee)
        self.lineEdit_result_roi_bottom = QtWidgets.QLineEdit(self.groupBox_result)
        self.__create_element(self.lineEdit_result_roi_bottom, [397, 710+self.groupbox_os_displ, 40, 22], "lineEdit_result_roi_bottom", text="20", font=font_ee)
        self.pushButton_result_roi_turn = QtWidgets.QPushButton(self.groupBox_result)
        self.__create_element(self.pushButton_result_roi_turn, [535, 710+self.groupbox_os_displ, 80, 22], "pushButton_result_roi_turn", text="Turn ROI", font=font_headline)
        self.pushButton_result_integratedRoi_export = QtWidgets.QPushButton(self.groupBox_result)
        self.__create_element(self.pushButton_result_integratedRoi_export, [620, 710+self.groupbox_os_displ, 151, 22], "pushButton_result_integratedRoi_export", text="Export int. ROI", font=font_headline)

        # This part of Result block is visible
        self.checkBox_result_devideByMonitor = QtWidgets.QCheckBox(self.groupBox_result)
        self.__create_element(self.checkBox_result_devideByMonitor, [5, 22+self.groupbox_os_displ, 241, 22], "checkBox_result_devideByMonitor", text="Devide by monitors", font=font_ee)
        self.label_result_aspectRatio = QtWidgets.QLabel(self.groupBox_result)
        self.__create_element(self.label_result_aspectRatio, [165, 22+self.groupbox_os_displ, 75, 20], "label_result_aspectRatio", text="Aspect ratio:", font=font_ee)
        self.horizontalSlider_result_aspectRatio = QtWidgets.QSlider(self.groupBox_result)
        self.__create_element(self.horizontalSlider_result_aspectRatio, [245, 22+self.groupbox_os_displ, 120, 22], "horizontalSlider_result_aspectRatio")
        self.horizontalSlider_result_aspectRatio.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_result_aspectRatio.setMinimum(1)
        self.horizontalSlider_result_aspectRatio.setMaximum(30)
        self.horizontalSlider_result_aspectRatio.setValue(1)
        self.label_result_2Dmap_View_scale = QtWidgets.QLabel(self.groupBox_result)
        self.__create_element(self.label_result_2Dmap_View_scale, [395, 22+self.groupbox_os_displ, 40, 22], "label_result_2Dmap_View_scale", text="View", font=font_ee)
        self.comboBox_result_2Dmap_scale = QtWidgets.QComboBox(self.groupBox_result)
        self.__create_element(self.comboBox_result_2Dmap_scale, [425, 22+self.groupbox_os_displ, 50, 22], "comboBox_result_2Dmap_scale", font=font_ee, combo=["Log", "Lin"])
        self.comboBox_result_operation_sign = QtWidgets.QComboBox(self.groupBox_result)
        self.__create_element(self.comboBox_result_operation_sign, [500, 22 + self.groupbox_os_displ, 40, 22], "comboBox_result_operation_sign", font=font_ee, combo=["-", "+"])

        self.lineEdit_result_operation = QtWidgets.QLineEdit(self.groupBox_result)
        self.__create_element(self.lineEdit_result_operation, [545, 22+self.groupbox_os_displ, 130, 22], "lineEdit_result_operation", stylesheet="color:rgb(0,0,0)", enabled=False, font=font_ee)
        self.pushButton_result_swapAB = QtWidgets.QPushButton(self.groupBox_result)
        self.__create_element(self.pushButton_result_swapAB, [680, 22+self.groupbox_os_displ, 90, 22], "pushButton_result_swapAB", text="(A<->B)", font=font_headline)
        self.graphicsView_result = pg.ImageView(self.groupBox_result)
        self.__create_element(self.graphicsView_result, [3, 48+self.groupbox_os_displ, 770, 684], "graphicsView_result")
        self.graphicsView_result.ui.menuBtn.hide()
        self.graphicsView_result.ui.roiBtn.hide()
        self.graphicsView_result.ui.histogram.clickAccepted
        colmap = pg.ColorMap(np.array([0.4, 0.5, 0.6]),
                             np.array([[0, 0, 255, 255], [0, 0, 0, 255], [0, 255, 0, 255]], dtype=np.ubyte))
        self.graphicsView_result.setColorMap(colmap)

        self.label_result_f_numberOfPixels_reduce = QtWidgets.QLabel(self.groupBox_result)
        self.__create_element(self.label_result_f_numberOfPixels_reduce, [10, 736+self.groupbox_os_displ, 250, 20], "label_result_f_numberOfPixels_reduce", text="Reduce number of pixels in each direction by:", font=font_ee)
        self.checkBox_result_f_numberOfPixels_reduce_by2 = QtWidgets.QCheckBox(self.groupBox_result)
        self.__create_element(self.checkBox_result_f_numberOfPixels_reduce_by2, [270, 736+self.groupbox_os_displ, 241, 20], "checkBox_result_f_numberOfPixels_reduce_by2", text="x2", font=font_ee)
        self.checkBox_result_f_numberOfPixels_reduce_by4 = QtWidgets.QCheckBox(self.groupBox_result)
        self.__create_element(self.checkBox_result_f_numberOfPixels_reduce_by4, [315, 736+self.groupbox_os_displ, 241, 20], "checkBox_result_f_numberOfPixels_reduce_by4", text="x4", font=font_ee)
        self.checkBox_result_f_numberOfPixels_reduce_by8 = QtWidgets.QCheckBox(self.groupBox_result)
        self.__create_element(self.checkBox_result_f_numberOfPixels_reduce_by8, [360, 736+self.groupbox_os_displ, 241, 20], "checkBox_result_f_numberOfPixels_reduce_by8", text="x8", font=font_ee)
        self.pushButton_result_export = QtWidgets.QPushButton(self.groupBox_result)
        self.__create_element(self.pushButton_result_export, [620, 735+self.groupbox_os_displ, 151, 22], "pushButton_result_export", text="Export result (2D)", font=font_headline)
        self.pushButton_result_ROI = QtWidgets.QPushButton(self.groupBox_result)
        self.__create_element(self.pushButton_result_ROI, [535, 735+self.groupbox_os_displ, 80, 22], "pushButton_result_ROI", text="ROI", font=font_headline)
        self.pushButton_result_Clear = QtWidgets.QPushButton(self.groupBox_result)
        self.__create_element(self.pushButton_result_Clear, [450, 735 + self.groupbox_os_displ, 80, 22], "pushButton_result_Clear", text="Clear", font=font_headline)

        # Menu and statusbar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.__create_element(self.menubar, [0, 0, 717, 21], "menubar", font=font_ee)
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.__create_element(self.menu_help, [999, 999, 999, 999], "menu_help", title="Help", font=font_ee)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_version = QtWidgets.QAction(MainWindow)
        self.__create_element(self.action_version, [999, 999, 999, 999], "action_version", text="Version 1.4", font=font_ee)
        self.menu_help.addAction(self.action_version)
        self.menubar.addAction(self.menu_help.menuAction())

# EE (Actions, drawing, math)
class GUI(Ui_MainWindow):

    dir_current = ""
    if platform.system() == 'Windows': dir_current = os.getcwd().replace("\\", "/") + "/"
    else:
        for i in sys.argv[0].split("/")[:-4]: dir_current += i + "/"

    def __init__(self):

        super(GUI, self).__init__()
        self.setupUi(self)

        # Actions on clicks
        self.toolButton_scan_A.clicked.connect(self.f_button_importScan)
        self.toolButton_scan_B.clicked.connect(self.f_button_importScan)

        self.comboBox_scan_A_pointNumber.currentIndexChanged.connect(self.f_diffLine)
        self.comboBox_scan_A_polarisation.currentIndexChanged.connect(self.f_diffLine)
        self.comboBox_scan_A_type.currentIndexChanged.connect(self.f_interface_change)
        self.comboBox_scan_B_pointNumber.currentIndexChanged.connect(self.f_diffLine)
        self.comboBox_scan_B_polarisation.currentIndexChanged.connect(self.f_diffLine)
        self.comboBox_scan_B_type.currentIndexChanged.connect(self.f_interface_change)
        self.comboBox_result_2Dmap_scale.currentIndexChanged.connect(self.f_res_draw)
        self.comboBox_result_2Dmap_scale.currentIndexChanged.connect(self.f_buttons_roi)
        self.comboBox_result_operation_sign.currentIndexChanged.connect(self.f_diffLine)

        self.pushButton_result_export.clicked.connect(self.f_button_exportResult)
        self.pushButton_result_ROI.clicked.connect(self.f_buttons_roi)
        self.pushButton_result_roi_turn.clicked.connect(self.f_buttons_roi)
        self.pushButton_result_integratedRoi_export.clicked.connect(self.f_button_roi_export)
        self.pushButton_result_swapAB.clicked.connect(self.f_diffLine)
        self.pushButton_result_Clear.clicked.connect(self.f_button_clear)


        self.checkBox_result_f_numberOfPixels_reduce_by2.stateChanged.connect(self.f_numberOfPixels_reduce)
        self.checkBox_result_f_numberOfPixels_reduce_by4.stateChanged.connect(self.f_numberOfPixels_reduce)
        self.checkBox_result_f_numberOfPixels_reduce_by8.stateChanged.connect(self.f_numberOfPixels_reduce)
        self.checkBox_result_devideByMonitor.stateChanged.connect(self.f_res_draw)

        self.horizontalSlider_result_aspectRatio.valueChanged.connect(self.f_res_draw)

        self.lineEdit_result_roi_left.editingFinished.connect(self.f_buttons_roi)
        self.lineEdit_result_roi_right.editingFinished.connect(self.f_buttons_roi)
        self.lineEdit_result_roi_top.editingFinished.connect(self.f_buttons_roi)
        self.lineEdit_result_roi_bottom.editingFinished.connect(self.f_buttons_roi)

        self.action_version.triggered.connect(self.f_menu_info)

        self.f_button_clear()

    def f_button_importScan(self):
        if self.sender().objectName() == "toolButton_scan_A":

            self.lineEdit_scan_A_name.setText("")

            file_data = QtWidgets.QFileDialog().getOpenFileName(None, "FileNames", self.dir_current, ".h5 (*.h5)")
            if file_data[0] == "": return
            # Next "Import scans" will open last dir instead of the app location
            self.dir_current = file_data[0][0][:file_data[0][0].rfind("/")]

            self.lineEdit_scan_A_name.setText(file_data[0])
            if self.lineEdit_scan_A_name.text() == "": return

            for element in (self.comboBox_scan_A_pointNumber, self.comboBox_scan_A_polarisation, self.graphicsView_scan_A): element.clear()

            with h5py.File(self.lineEdit_scan_A_name.text(), 'r') as FILE:
                self.original_roi_A = np.array(FILE[list(FILE.keys())[0]].get("instrument").get('scalers').get('roi').get("roi"))
                self.lineEdit_result_roi_left.setText(str(self.original_roi_A[2])[:-2])
                self.lineEdit_result_roi_right.setText(str(self.original_roi_A[3])[:-2])
                self.lineEdit_result_roi_bottom.setText(str(self.original_roi_A[1])[:-2])
                self.lineEdit_result_roi_top.setText(str(self.original_roi_A[0])[:-2])

                for index, th in enumerate(FILE[list(FILE.keys())[0]].get("instrument").get('motors').get('th').get("value")): self.comboBox_scan_A_pointNumber.addItem(str(index))

                for polarisation in FILE[list(FILE.keys())[0]].get("instrument").get('detectors'):

                    if polarisation in ("psd_uu", "psd_du", "psd_dd", "psd_ud"): self.comboBox_scan_A_polarisation.addItem(str(polarisation)[-2:])
                    elif polarisation in ("psd"): self.comboBox_scan_A_polarisation.addItem("np")

            self.comboBox_scan_A_pointNumber.setCurrentIndex(0)
            self.comboBox_scan_A_polarisation.setCurrentIndex(0)

            self.lastType_A = self.comboBox_scan_A_type.currentText()

        elif self.sender().objectName() == "toolButton_scan_B":
            self.lineEdit_scan_B_name.setText("")

            file_data = QtWidgets.QFileDialog().getOpenFileName(None, "FileNames", self.dir_current, ".h5 (*.h5)")
            if file_data[0] == "": return
            # Next "Import scans" will open last dir
            self.dir_current = file_data[0][0][:file_data[0][0].rfind("/")]

            self.lineEdit_scan_B_name.setText(file_data[0])
            if self.lineEdit_scan_B_name.text() == "": return

            for element in (self.comboBox_scan_B_pointNumber, self.comboBox_scan_B_polarisation, self.graphicsView_scan_B): element.clear()

            with h5py.File(self.lineEdit_scan_B_name.text(), 'r') as FILE:

                for index, th in enumerate(FILE[list(FILE.keys())[0]].get("instrument").get('motors').get('th').get("value")):
                    self.comboBox_scan_B_pointNumber.addItem(str(index))

                for polarisation in FILE[list(FILE.keys())[0]].get("instrument").get('detectors'):

                    if polarisation in ("psd_uu", "psd_du", "psd_dd", "psd_ud"): self.comboBox_scan_B_polarisation.addItem(str(polarisation)[-2:])
                    elif polarisation in ("psd"): self.comboBox_scan_B_polarisation.addItem("np")

            self.comboBox_scan_B_pointNumber.setCurrentIndex(0)
            self.comboBox_scan_B_polarisation.setCurrentIndex(0)

            self.lastType_B = self.comboBox_scan_B_type.currentText()

        self.f_diffLine()

    def f_button_exportResult(self):
        # Export resulting picture as CSV
        dir = QtWidgets.QFileDialog().getExistingDirectory(None, "FileNames", self.dir_current)
        if dir == "": return

        exportFile_name = f"A({self.lineEdit_scan_A_name.text()[self.lineEdit_scan_A_name.text().rfind('/') + 1:]})_B({self.lineEdit_scan_B_name.text()[self.lineEdit_scan_B_name.text().rfind('/') + 1:]}) --- {self.lineEdit_result_operation.text()}"
        with open(dir + "/" + exportFile_name.replace(" ", "") + "--- 2Dmap).dat", "w") as new_file_2d_map:
            for line in np.swapaxes(self.res_lin, 0,1):
                for row in line: new_file_2d_map.write(str(int(row)) + " ")
                new_file_2d_map.write("\n")

    def f_button_clear(self):
        # use arrays to keep old "lines" and redraw only if they are different from new ones
        self.line_A, self.line_B = ["", ""], ["", ""]
        self.roi_show, self.roi_turn, self.roi_draw_result, self.roi_initial = 0, 0, [], []
        self.detectorImage_A, self.detectorImage_B = [], []
        self.res_lin, self.res_draw = [], []

        # I will use self.interface_A and self.interface_B to track what was
        # changed on the form and do changes without creating too many functions
        self.lastType_A, self.lastType_B = [], []

        [i.clear() for i in [self.lineEdit_scan_A_name, self.lineEdit_scan_B_name, self.graphicsView_scan_A, self.graphicsView_scan_B, self.graphicsView_result, self.graphicsView_result_integratedRoi]]
        self.statusbar.clearMessage()

    def f_interface_change(self):

        if  not self.lastType_A == self.comboBox_scan_A_type.currentText():
            # if we have "Single point" as a mode and we just changet to it -> change "Point number" to the first one
            if self.comboBox_scan_A_type.currentText() == "Single point": self.comboBox_scan_A_pointNumber.setCurrentIndex(0)
            # if we have "2D map" as a mode and we just changet to it -> change Scan B Type to "2D map" also
            elif self.comboBox_scan_A_type.currentText() == "2D map": self.comboBox_scan_B_type.setCurrentIndex(2)
            # if we changed from "2D map" -> change B also
            if self.lastType_A == "2D map":
                if self.comboBox_scan_A_type.currentText() == "Single point": self.comboBox_scan_B_type.setCurrentIndex(0)
                elif self.comboBox_scan_A_type.currentText() == "Integrated image": self.comboBox_scan_B_type.setCurrentIndex(1)

        # same for B
        if not self.lastType_B == self.comboBox_scan_B_type.currentText():
            if self.comboBox_scan_B_type.currentText() == "Single point": self.comboBox_scan_B_pointNumber.setCurrentIndex(0)
            elif self.comboBox_scan_B_type.currentText() == "2D map": self.comboBox_scan_A_type.setCurrentIndex(2)
            if self.lastType_B == "2D map":
                if self.comboBox_scan_B_type.currentText() == "Single point": self.comboBox_scan_A_type.setCurrentIndex(0)
                elif self.comboBox_scan_B_type.currentText() == "Integrated image": self.comboBox_scan_A_type.setCurrentIndex(1)

        # show/hide some elements depends on the mode
        for element in (self.checkBox_result_f_numberOfPixels_reduce_by2, self.checkBox_result_f_numberOfPixels_reduce_by4, self.checkBox_result_f_numberOfPixels_reduce_by8):
            element.setDisabled(True if self.comboBox_scan_A_type.currentText() == "2D map" or self.comboBox_scan_B_type.currentText() == "2D map" else False)

        self.comboBox_scan_A_pointNumber.setDisabled(True if self.comboBox_scan_A_type.currentText() in ["2D map", "Integrated image"] else False)
        self.comboBox_scan_B_pointNumber.setDisabled(True if self.comboBox_scan_B_type.currentText() in ["2D map", "Integrated image"] else False)

        self.lastType_A, self.lastType_B = self.comboBox_scan_A_type.currentText(), self.comboBox_scan_B_type.currentText()

        self.f_diffLine()

    # diff line
    def f_diffLine(self):

        if not self.sender().objectName() == "pushButton_result_swapAB":

            if self.comboBox_scan_A_type.currentText() == "Single point" and not self.comboBox_scan_A_pointNumber.currentText() == "":
                self.line_A[0] = "A(" + str(self.comboBox_scan_A_polarisation.currentText()) + ")(" + str(self.comboBox_scan_A_pointNumber.currentText()) + ")"
            elif self.comboBox_scan_A_type.currentText() == "Integrated image" and not self.comboBox_scan_A_polarisation.currentText() == "":
                self.line_A[0] = "A(" + str(self.comboBox_scan_A_polarisation.currentText()) + ")(All)"
            elif self.comboBox_scan_A_type.currentText() == "2D map" and not self.comboBox_scan_A_polarisation.currentText() == "":
                self.line_A[0] = "A(" + str(self.comboBox_scan_A_polarisation.currentText()) + ")(2D map)"

            if self.comboBox_scan_B_type.currentText() == "Single point" and not self.comboBox_scan_B_pointNumber.currentText() == "":
                self.line_B[0] = "B(" + str(self.comboBox_scan_B_polarisation.currentText()) + ")(" + str(self.comboBox_scan_B_pointNumber.currentText()) + ")"
            elif self.comboBox_scan_B_type.currentText() == "Integrated image" and not self.comboBox_scan_B_polarisation.currentText() == "":
                self.line_B[0] = "B(" + str(self.comboBox_scan_B_polarisation.currentText()) + ")(All)"
            elif self.comboBox_scan_B_type.currentText() == "2D map" and not self.comboBox_scan_B_polarisation.currentText() == "":
                self.line_B[0] = "B(" + str(self.comboBox_scan_B_polarisation.currentText()) + ")(2D map)"

            # fill one of the scans if it is the only one is imported
            if not self.line_A[0] == "" and self.line_B[0] == "": line = self.line_A[0]
            elif self.line_A[0] == "" and not self.line_B[0] == "": line = self.line_B[0]
            # otherwice check if a line is already presented and what is the first. Keep the same order
            else:
                if self.lineEdit_result_operation.text().find("A(") == 0: line = self.line_A[0] + self.comboBox_result_operation_sign.currentText() + self.line_B[0]
                else: line = self.line_B[0] + self.comboBox_result_operation_sign.currentText() + self.line_A[0]

            self.lineEdit_result_operation.setText(line)

            if not self.line_A[0] == self.line_A[1]: self.f_detA_frame_draw()
            self.line_A[1] = self.line_A[0]

            if not self.line_B[0] == self.line_B[1]: self.f_detB_frame_draw()
            self.line_B[1] = self.line_B[0]

        else:
            if self.lineEdit_result_operation.text() == "": return
            if not self.lineEdit_result_operation.text().find(self.comboBox_result_operation_sign.currentText()) > 0: return
            if self.lineEdit_result_operation.text().find(self.line_A[0]) == 0: # then A scan is first
                line = self.line_B[0] + self.comboBox_result_operation_sign.currentText() + self.line_A[0]
            else: line = self.line_A[0] + self.comboBox_result_operation_sign.currentText() + self.line_B[0]

            self.lineEdit_result_operation.setText(line)

        self.f_res_draw()

        if self.roi_show == 1: self.f_buttons_roi()

    # draw graphs
    def f_detA_frame_draw(self):

        self.graphicsView_scan_A.clear()

        if self.lineEdit_scan_A_name.text() == "" or self.comboBox_scan_A_pointNumber.currentText() == "" or self.comboBox_scan_A_polarisation.currentText() == "": return

        # define "detector name" by polarisation
        SCAN_PSD_A = "psd" if self.comboBox_scan_A_polarisation.currentText() == "np" else str("psd_" + self.comboBox_scan_A_polarisation.currentText())

        with h5py.File(self.lineEdit_scan_A_name.text(), 'r') as FILE:
            # sum all detector images
            if self.comboBox_scan_A_type.currentText() == "Integrated image":
                for i in range(0, self.comboBox_scan_A_pointNumber.count() - 1):
                    if i == 0: self.detectorImage_A = FILE[list(FILE.keys())[0]].get("instrument").get('detectors').get(SCAN_PSD_A).get('data')[i]
                    else: self.detectorImage_A = np.add(self.detectorImage_A, FILE[list(FILE.keys())[0]].get("instrument").get('detectors').get(SCAN_PSD_A).get('data')[i])
            # sum each frame in Y axis
            elif self.comboBox_scan_A_type.currentText() == "2D map":
                self.detectorImage_A = FILE[list(FILE.keys())[0]].get("instrument").get("detectors").get(SCAN_PSD_A).get('data')[:, :, :].sum(axis=1)
                self.detectorImage_A = np.flip(self.detectorImage_A, axis=0)
            # show specific frame
            else: self.detectorImage_A = FILE[list(FILE.keys())[0]].get("instrument").get('detectors').get(SCAN_PSD_A).get('data')[int(self.comboBox_scan_A_pointNumber.currentText())]

            # seems to be a np bag - I cant draw out an array until I subtract zero array of the same size of it
            self.detectorImage_A = np.around(self.detectorImage_A, decimals=0).astype(int)
            self.detectorImage_A = np.subtract(self.detectorImage_A, np.zeros((self.detectorImage_A.shape[0], self.detectorImage_A.shape[1])))

            self.graphicsView_scan_A.setImage(self.detectorImage_A, axes={'x':1, 'y':0}, levels=(0,0.1))

            colmap = pg.ColorMap(np.array([0.0, 0.1, 1.0]), np.array([[0, 0, 255, 255], [255, 0, 0, 255], [0, 255, 0, 255]], dtype=np.ubyte))
            self.graphicsView_scan_A.setColorMap(colmap)

    def f_detB_frame_draw(self):

        # see comments in f_detA_frame_draw
        self.graphicsView_scan_B.clear()

        if self.lineEdit_scan_B_name.text() == "" or self.comboBox_scan_B_pointNumber.currentText() == "" or self.comboBox_scan_B_polarisation.currentText() == "": return

        SCAN_PSD_B = "psd" if self.comboBox_scan_B_polarisation.currentText() == "np" else str("psd_" + self.comboBox_scan_B_polarisation.currentText())

        with h5py.File(self.lineEdit_scan_B_name.text(), 'r') as FILE:

            if self.comboBox_scan_B_type.currentText() == "Integrated image":
                for i in range(0, self.comboBox_scan_B_pointNumber.count() - 1):
                    if i == 0: self.detectorImage_B = FILE[list(FILE.keys())[0]].get("instrument").get('detectors').get(SCAN_PSD_B).get('data')[i]
                    else: self.detectorImage_B = np.add(self.detectorImage_B, FILE[list(FILE.keys())[0]].get("instrument").get('detectors').get(SCAN_PSD_B).get('data')[i])
            elif self.comboBox_scan_B_type.currentText() == "2D map":
                self.detectorImage_B = FILE[list(FILE.keys())[0]].get("instrument").get("detectors").get(SCAN_PSD_B).get('data')[:, :, :].sum(axis=1)
                self.detectorImage_B = np.flip(self.detectorImage_B, axis=0)
            else: self.detectorImage_B = FILE[list(FILE.keys())[0]].get("instrument").get('detectors').get(SCAN_PSD_B).get('data')[int(self.comboBox_scan_B_pointNumber.currentText())]

            self.detectorImage_B = np.around(self.detectorImage_B, decimals=0).astype(int)
            self.detectorImage_B = np.subtract(self.detectorImage_B, np.zeros((self.detectorImage_B.shape[0], self.detectorImage_B.shape[1])))

            self.graphicsView_scan_B.setImage(self.detectorImage_B, axes={'x': 1, 'y': 0}, levels=(0, 0.1))

            colmap = pg.ColorMap(np.array([0.0, 0.1, 1.0]), np.array([[0, 0, 255, 255], [255, 0, 0, 255], [0, 255, 0, 255]], dtype=np.ubyte))
            self.graphicsView_scan_B.setColorMap(colmap)

    def f_res_draw(self):

        dict_monitorIdentifier = {"psd":"b'mon0'", "psd_uu":"b'm1'", "psd_dd": "b'm2'", "psd_du": "b'm3'", "psd_ud": "b'm4'"}

        # Subtract 2D map only from other 2D map
        if (self.comboBox_scan_A_type.currentText() == "2D map" and not self.comboBox_scan_B_type.currentText() == "2D map") or (self.comboBox_scan_B_type.currentText() == "2D map" and not self.comboBox_scan_A_type.currentText() == "2D map"): return

        if self.lineEdit_result_operation.text().find("()") > -1 or self.lineEdit_result_operation.text() in ["", self.comboBox_result_operation_sign.currentText()] : return
        if not self.lineEdit_scan_A_name.text() == "" and (self.comboBox_scan_A_pointNumber.currentText() == "" or self.comboBox_scan_A_polarisation.currentText() == ""): return
        if not self.lineEdit_scan_B_name.text() == "" and (self.comboBox_scan_B_pointNumber.currentText() == "" or self.comboBox_scan_B_polarisation.currentText() == ""): return

        # Get requested in the line A frame
        if not self.line_A[0] == "":

            if self.comboBox_scan_A_polarisation.currentText() == "np": SCAN_PSD_A = "psd"
            else: SCAN_PSD_A = "psd_" + self.comboBox_scan_A_polarisation.currentText()

            with h5py.File(self.lineEdit_scan_A_name.text(), 'r') as FILE:
                # seems to be a bug in np arrays imported from hdf5 files. Need to redefine array type to int.
                self.detectorImage_A = np.around(self.detectorImage_A, decimals=0).astype(int)
                self.detectorImage_A = np.subtract(self.detectorImage_A, np.zeros((self.detectorImage_A.shape[0], self.detectorImage_A.shape[1])))

                for index, scaler in enumerate(FILE[list(FILE.keys())[0]].get("instrument").get('scalers').get('SPEC_counter_mnemonics')):
                    monitor_A_identifier = dict_monitorIdentifier[SCAN_PSD_A]
                    if monitor_A_identifier in str(scaler):
                        if self.comboBox_scan_A_pointNumber.currentText() in ["All", "2D map"]:
                            monitor_A = np.sum(np.array(FILE[list(FILE.keys())[0]].get("instrument").get('scalers').get('data')).T[index])
                        else: monitor_A = np.array(FILE[list(FILE.keys())[0]].get("instrument").get('scalers').get('data')).T[index][int(self.comboBox_scan_A_pointNumber.currentText())]

        # Get requested in the line B frame
        if not self.line_B[0] == "":

            if self.comboBox_scan_B_polarisation.currentText() == "np": SCAN_PSD_B = "psd"
            else: SCAN_PSD_B = "psd_" + self.comboBox_scan_B_polarisation.currentText()

            with h5py.File(self.lineEdit_scan_B_name.text(), 'r') as FILE:
                # seems to be a bug in np arrays imported from hdf5 files. Need to redefine array type to int.
                self.detectorImage_B = np.around(self.detectorImage_B, decimals=0).astype(int)
                self.detectorImage_B = np.subtract(self.detectorImage_B, np.zeros((self.detectorImage_B.shape[0], self.detectorImage_B.shape[1])))

                for index, scaler in enumerate(FILE[list(FILE.keys())[0]].get("instrument").get('scalers').get('SPEC_counter_mnemonics')):
                    monitor_B_identifier = dict_monitorIdentifier[SCAN_PSD_B]
                    if monitor_B_identifier in str(scaler):
                        if self.comboBox_scan_B_pointNumber.currentText() in ["All", "2D map"]:
                            monitor_B = np.sum(np.array(FILE[list(FILE.keys())[0]].get("instrument").get('scalers').get('data')).T[index])
                        else: monitor_B = np.array(FILE[list(FILE.keys())[0]].get("instrument").get('scalers').get('data')).T[index][int(self.comboBox_scan_B_pointNumber.currentText())]

        # Do the subtraction
        if self.line_A[0] == "" and not self.line_B[0] == "": RES = self.detectorImage_B
        elif not self.line_A[0] == "" and self.line_B[0] == "": RES = self.detectorImage_A
        else:
            if not self.lineEdit_result_operation.text().find(self.line_A[0]) == 0:
                main, main_mon, min, min_mon = self.detectorImage_B, monitor_B, self.detectorImage_A, monitor_A
            else: main, main_mon, min, min_mon = self.detectorImage_A, monitor_A, self.detectorImage_B, monitor_B

            if self.checkBox_result_devideByMonitor.isChecked(): main = np.divide(main, main_mon/min_mon)

        if self.lineEdit_result_operation.text().find("+") > 0: RES = np.add(main, min)
        elif self.lineEdit_result_operation.text().find("-") > 0: RES = np.subtract(main, min)

        if self.checkBox_result_f_numberOfPixels_reduce_by2.isChecked(): RES = RES.reshape(int(RES.shape[0]/2), 2, int(RES.shape[1]/2), 2).sum(axis=1).sum(axis=2)
        elif self.checkBox_result_f_numberOfPixels_reduce_by4.isChecked(): RES = RES.reshape(int(RES.shape[0]/4), 4, int(RES.shape[1]/4), 4).sum(axis=1).sum(axis=2)
        elif self.checkBox_result_f_numberOfPixels_reduce_by8.isChecked(): RES = RES.reshape(int(RES.shape[0]/8), 8, int(RES.shape[0]/8), 8).sum(axis=1).sum(axis=2)

        RES = np.swapaxes(RES, 0,1)

        self.res_lin = RES
        self.res_draw = RES if self.comboBox_result_2Dmap_scale.currentText() == "Lin" else np.log10(np.where(RES < 1, 1, RES))

        scale_low, scale_high = np.min(self.res_draw), np.max(self.res_draw)
        self.graphicsView_result.setImage(self.res_draw, scale=(1, self.horizontalSlider_result_aspectRatio.value()))

        if not self.detectorImage_A == []:
            self.graphicsView_scan_A.setImage(self.detectorImage_A, axes={'x': 1, 'y': 0}, levels=(0, 0.1), scale=(1, self.horizontalSlider_result_aspectRatio.value()))
        if not self.detectorImage_B == []:
            self.graphicsView_scan_B.setImage(self.detectorImage_B, axes={'x': 1, 'y': 0}, levels=(0, 0.1), scale=(1, self.horizontalSlider_result_aspectRatio.value()))

        self.graphicsView_result.ui.histogram.setHistogramRange(scale_low*[2 if scale_low < 0 else 0.5][0], scale_high*0.7)
        self.graphicsView_result.ui.histogram.setLevels(scale_low*[2 if scale_low < 0 else 0.5][0], scale_high*0.7)

        self.statusbar.showMessage('Action "' + self.lineEdit_result_operation.text() + '" is performed.')

        self.f_buttons_roi()

    # Reduce number of pixels
    def f_numberOfPixels_reduce(self):

        ROI = [self.lineEdit_result_roi_left, self.lineEdit_result_roi_right, self.lineEdit_result_roi_bottom, self.lineEdit_result_roi_top]

        roi_lowerBy = 1
        if self.sender().objectName() == "checkBox_result_f_numberOfPixels_reduce_by2":
            if self.checkBox_result_f_numberOfPixels_reduce_by2.isChecked():
                self.checkBox_result_f_numberOfPixels_reduce_by4.setChecked(False)
                self.checkBox_result_f_numberOfPixels_reduce_by8.setChecked(False)
                roi_lowerBy = 2
            else: self.checkBox_result_f_numberOfPixels_reduce_by2.setChecked(False)
        elif self.sender().objectName() == "checkBox_result_f_numberOfPixels_reduce_by4":
            if self.checkBox_result_f_numberOfPixels_reduce_by4.isChecked():
                self.checkBox_result_f_numberOfPixels_reduce_by2.setChecked(False)
                self.checkBox_result_f_numberOfPixels_reduce_by8.setChecked(False)
                roi_lowerBy = 4
            else: self.checkBox_result_f_numberOfPixels_reduce_by4.setChecked(False)
        elif self.sender().objectName() == "checkBox_result_f_numberOfPixels_reduce_by8":
            if self.checkBox_result_f_numberOfPixels_reduce_by8.isChecked():
                self.checkBox_result_f_numberOfPixels_reduce_by2.setChecked(False)
                self.checkBox_result_f_numberOfPixels_reduce_by4.setChecked(False)
                roi_lowerBy = 8
            else: self.checkBox_result_f_numberOfPixels_reduce_by8.setChecked(False)

        for index, element in enumerate(ROI): element.setText(str(int(round(int(self.roi_initial[index])/roi_lowerBy))))

        self.f_buttons_roi()
        self.f_res_draw()

    def f_menu_info(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowIcon(QtGui.QIcon(self.iconpath))
        msgBox.setText("PySAsum. " + self.action_version.text() + "\n\n" + "Alexey.Klechikov@gmail.com\n\n" + "Check new version at https://github.com/Alexey-Klechikov/pySAsum/releases")
        msgBox.exec_()

    # ROI
    def f_buttons_roi(self):

        ####### turn roi
        if self.sender().objectName() == "pushButton_result_roi_turn": self.roi_turn = 1 if self.roi_turn == 0 else 0

        ####### show roi
        if self.sender().objectName() == "pushButton_result_ROI":
            # resize Result 2D map to show what is hidden
            if self.roi_show == 0:
                self.graphicsView_result.setGeometry(QtCore.QRect(3, 48+self.groupbox_os_displ, 770, 390))
                self.roi_show = 1
            else:
                self.graphicsView_result.setGeometry(QtCore.QRect(3, 48+self.groupbox_os_displ, 770, 684))
                self.roi_show = 0

        ####### calculate
        plot_x, plot_y = [], []

        self.graphicsView_result_integratedRoi.getPlotItem().clear()

        # for some reason I cant just plot an array (might be the problem with export of 2d arrays from hdf5), I do it in lame way instead
        if self.roi_turn == 0:
            for index, i in enumerate(self.res_lin):
                if index < int(self.lineEdit_result_roi_left.text()) or index > int(self.lineEdit_result_roi_right.text()): continue
                plot_x.append(index)
                plot_y.append(i[int(self.lineEdit_result_roi_top.text()) : int(self.lineEdit_result_roi_bottom.text())].sum())
        else:
            for index, i in enumerate(np.swapaxes(self.res_lin, 0, 1)):
                if index < int(self.lineEdit_result_roi_top.text()) or index > int(self.lineEdit_result_roi_bottom.text()): continue
                plot_x.append(index)
                plot_y.append(i[int(self.lineEdit_result_roi_left.text()) : int(self.lineEdit_result_roi_right.text())].sum())

        plot_y = plot_y if self.comboBox_result_2Dmap_scale.currentText() == "Lin" else np.log10(np.where(np.array(plot_y) < 1, 1, plot_y))

        self.roi_plot_export = [plot_x, plot_y]

        s1 = pg.PlotCurveItem(x=plot_x, y=plot_y, pen=pg.mkPen(0, 0, 0))
        self.graphicsView_result_integratedRoi.addItem(s1)

        ####### square
        if self.sender().objectName() in ["comboBox_scan_A_type", "comboBox_scan_B_type"]:
            if self.comboBox_scan_A_type.currentText() == "2D map" or self.comboBox_scan_B_type.currentText() == "2D map":
                self.lineEdit_result_roi_bottom.setText(str(self.res_lin.shape[1]))
                self.lineEdit_result_roi_top.setText("0")
            elif not self.roi_initial == []:
                self.lineEdit_result_roi_bottom.setText(self.roi_initial[2])
                self.lineEdit_result_roi_top.setText(self.roi_initial[3])

        if not self.checkBox_result_f_numberOfPixels_reduce_by2.isChecked() and not self.checkBox_result_f_numberOfPixels_reduce_by4.isChecked() and not self.checkBox_result_f_numberOfPixels_reduce_by8.isChecked() and not self.comboBox_scan_A_type.currentText() == "2D map" and not self.comboBox_scan_B_type.currentText() == "2D map":
            self.roi_initial = [self.lineEdit_result_roi_left.text(), self.lineEdit_result_roi_right.text(), self.lineEdit_result_roi_bottom.text(), self.lineEdit_result_roi_top.text()]

        if self.roi_draw_result: self.graphicsView_result.removeItem(self.roi_draw_result)

        spots = {'x': (int(self.lineEdit_result_roi_left.text()), int(self.lineEdit_result_roi_right.text()), int(self.lineEdit_result_roi_right.text()), int(self.lineEdit_result_roi_left.text()), int(self.lineEdit_result_roi_left.text())),
                'y': (int(self.lineEdit_result_roi_top.text()) * self.horizontalSlider_result_aspectRatio.value(), int(self.lineEdit_result_roi_top.text()) * self.horizontalSlider_result_aspectRatio.value(), int(self.lineEdit_result_roi_bottom.text()) * self.horizontalSlider_result_aspectRatio.value(), int(self.lineEdit_result_roi_bottom.text()) * self.horizontalSlider_result_aspectRatio.value(),int(self.lineEdit_result_roi_top.text()) * self.horizontalSlider_result_aspectRatio.value())}

        self.roi_draw_result = pg.PlotDataItem(spots, pen=pg.mkPen(255, 255, 255), connect="all")

        if self.roi_show == 1: self.graphicsView_result.addItem(self.roi_draw_result)

    def f_button_roi_export(self):
        # Export ROI as simple 2 column dat
        dir = QtWidgets.QFileDialog().getExistingDirectory(None, "FileNames", self.dir_current)
        if dir == "": return

        exportFile_name = f"A({self.lineEdit_scan_A_name.text()[self.lineEdit_scan_A_name.text().rfind('/')+1:]})_B({self.lineEdit_scan_B_name.text()[self.lineEdit_scan_B_name.text().rfind('/')+1:]}) --- {self.lineEdit_result_operation.text()}"
        with open(dir + "/" + exportFile_name.replace(" ", "") + "--- ROI).dat", "w") as new_file_roi:
            for i in range(0, len(self.roi_plot_export[0])):
                new_file_roi.write(str(self.roi_plot_export[0][i]) + " " + str(self.roi_plot_export[1][i]) )
                new_file_roi.write("\n")

if __name__ == "__main__":
    QtWidgets.QApplication.setStyle("Fusion")
    app = QtWidgets.QApplication(sys.argv)
    prog = GUI()
    prog.show()
    sys.exit(app.exec_())
