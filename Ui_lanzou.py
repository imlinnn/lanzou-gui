# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/rachpt/Documents/work_sp/lanzou-gui/lanzou.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1000, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.share_tab = QtWidgets.QWidget()
        self.share_tab.setObjectName("share_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.share_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_share_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_share_1.setObjectName("horizontalLayout_share_1")
        self.label_share_url = QtWidgets.QLabel(self.share_tab)
        self.label_share_url.setObjectName("label_share_url")
        self.horizontalLayout_share_1.addWidget(self.label_share_url)
        self.line_share_url = QtWidgets.QLineEdit(self.share_tab)
        self.line_share_url.setObjectName("line_share_url")
        self.horizontalLayout_share_1.addWidget(self.line_share_url)
        self.btn_extract = QtWidgets.QPushButton(self.share_tab)
        self.btn_extract.setObjectName("btn_extract")
        self.horizontalLayout_share_1.addWidget(self.btn_extract)
        self.verticalLayout_4.addLayout(self.horizontalLayout_share_1)
        self.table_share = QtWidgets.QTableView(self.share_tab)
        self.table_share.setObjectName("table_share")
        self.verticalLayout_4.addWidget(self.table_share)
        self.horizontalLayout_share_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_share_2.setObjectName("horizontalLayout_share_2")
        self.btn_share_select_all = QtWidgets.QPushButton(self.share_tab)
        self.btn_share_select_all.setObjectName("btn_share_select_all")
        self.horizontalLayout_share_2.addWidget(self.btn_share_select_all)
        self.label_dl_path = QtWidgets.QLabel(self.share_tab)
        self.label_dl_path.setObjectName("label_dl_path")
        self.horizontalLayout_share_2.addWidget(self.label_dl_path)
        self.btn_share_dl = QtWidgets.QPushButton(self.share_tab)
        self.btn_share_dl.setObjectName("btn_share_dl")
        self.horizontalLayout_share_2.addWidget(self.btn_share_dl)
        self.verticalLayout_4.addLayout(self.horizontalLayout_share_2)
        self.tabWidget.addTab(self.share_tab, "")
        self.disk_tab = QtWidgets.QWidget()
        self.disk_tab.setEnabled(True)
        self.disk_tab.setMinimumSize(QtCore.QSize(620, 0))
        self.disk_tab.setObjectName("disk_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.disk_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.disk_locs = QtWidgets.QHBoxLayout()
        self.disk_locs.setObjectName("disk_locs")
        self.disk_loc = QtWidgets.QHBoxLayout()
        self.disk_loc.setObjectName("disk_loc")
        self.label_disk_loc = QtWidgets.QLabel(self.disk_tab)
        self.label_disk_loc.setObjectName("label_disk_loc")
        self.disk_loc.addWidget(self.label_disk_loc)
        self.disk_locs.addLayout(self.disk_loc)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.disk_locs.addItem(spacerItem)
        self.btn_disk_mkdir = QtWidgets.QPushButton(self.disk_tab)
        self.btn_disk_mkdir.setObjectName("btn_disk_mkdir")
        self.disk_locs.addWidget(self.btn_disk_mkdir)
        self.verticalLayout_3.addLayout(self.disk_locs)
        self.table_disk = QtWidgets.QTableView(self.disk_tab)
        self.table_disk.setObjectName("table_disk")
        self.verticalLayout_3.addWidget(self.table_disk)
        self.horizontalLayout_disk_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_disk_2.setObjectName("horizontalLayout_disk_2")
        self.btn_disk_select_all = QtWidgets.QPushButton(self.disk_tab)
        self.btn_disk_select_all.setObjectName("btn_disk_select_all")
        self.horizontalLayout_disk_2.addWidget(self.btn_disk_select_all)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_disk_2.addItem(spacerItem1)
        self.btn_disk_delete = QtWidgets.QPushButton(self.disk_tab)
        self.btn_disk_delete.setObjectName("btn_disk_delete")
        self.horizontalLayout_disk_2.addWidget(self.btn_disk_delete)
        self.btn_disk_dl = QtWidgets.QPushButton(self.disk_tab)
        self.btn_disk_dl.setObjectName("btn_disk_dl")
        self.horizontalLayout_disk_2.addWidget(self.btn_disk_dl)
        self.verticalLayout_3.addLayout(self.horizontalLayout_disk_2)
        self.tabWidget.addTab(self.disk_tab, "")
        self.rec_tab = QtWidgets.QWidget()
        self.rec_tab.setObjectName("rec_tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.rec_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_rec = QtWidgets.QHBoxLayout()
        self.horizontalLayout_rec.setObjectName("horizontalLayout_rec")
        self.btn_rec_select_all = QtWidgets.QPushButton(self.rec_tab)
        self.btn_rec_select_all.setObjectName("btn_rec_select_all")
        self.horizontalLayout_rec.addWidget(self.btn_rec_select_all)
        self.btn_recovery = QtWidgets.QPushButton(self.rec_tab)
        self.btn_recovery.setObjectName("btn_recovery")
        self.horizontalLayout_rec.addWidget(self.btn_recovery)
        self.btn_rec_delete = QtWidgets.QPushButton(self.rec_tab)
        self.btn_rec_delete.setObjectName("btn_rec_delete")
        self.horizontalLayout_rec.addWidget(self.btn_rec_delete)
        self.btn_rec_clean = QtWidgets.QPushButton(self.rec_tab)
        self.btn_rec_clean.setObjectName("btn_rec_clean")
        self.horizontalLayout_rec.addWidget(self.btn_rec_clean)
        self.btn_recovery_all = QtWidgets.QPushButton(self.rec_tab)
        self.btn_recovery_all.setObjectName("btn_recovery_all")
        self.horizontalLayout_rec.addWidget(self.btn_recovery_all)
        self.expire_files_btn = QtWidgets.QPushButton(self.rec_tab)
        self.expire_files_btn.setObjectName("expire_files_btn")
        self.horizontalLayout_rec.addWidget(self.expire_files_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_rec)
        self.table_rec = QtWidgets.QTableView(self.rec_tab)
        self.table_rec.setObjectName("table_rec")
        self.verticalLayout.addWidget(self.table_rec)
        self.tabWidget.addTab(self.rec_tab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 30))
        self.menubar.setObjectName("menubar")
        self.acount = QtWidgets.QMenu(self.menubar)
        self.acount.setObjectName("acount")
        self.files = QtWidgets.QMenu(self.menubar)
        self.files.setObjectName("files")
        self.help = QtWidgets.QMenu(self.menubar)
        self.help.setObjectName("help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolbar = QtWidgets.QToolBar(MainWindow)
        self.toolbar.setObjectName("toolbar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar)
        self.login = QtWidgets.QAction(MainWindow)
        self.login.setObjectName("login")
        self.logout = QtWidgets.QAction(MainWindow)
        self.logout.setObjectName("logout")
        self.upload = QtWidgets.QAction(MainWindow)
        self.upload.setObjectName("upload")
        self.download = QtWidgets.QAction(MainWindow)
        self.download.setObjectName("download")
        self.delete = QtWidgets.QAction(MainWindow)
        self.delete.setObjectName("delete")
        self.how = QtWidgets.QAction(MainWindow)
        self.how.setObjectName("how")
        self.about = QtWidgets.QAction(MainWindow)
        self.about.setObjectName("about")
        self.acount.addSeparator()
        self.acount.addAction(self.login)
        self.acount.addAction(self.logout)
        self.files.addAction(self.upload)
        self.files.addAction(self.download)
        self.files.addAction(self.delete)
        self.help.addAction(self.how)
        self.help.addAction(self.about)
        self.menubar.addAction(self.acount.menuAction())
        self.menubar.addAction(self.files.menuAction())
        self.menubar.addAction(self.help.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_share_url.setText(_translate("MainWindow", "蓝奏链接"))
        self.btn_extract.setText(_translate("MainWindow", "提取"))
        self.btn_share_select_all.setText(_translate("MainWindow", "全选"))
        self.label_dl_path.setText(_translate("MainWindow", "文件下载路径"))
        self.btn_share_dl.setText(_translate("MainWindow", "下载选中文件"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.share_tab), _translate("MainWindow", "蓝奏云链接提取"))
        self.label_disk_loc.setText(_translate("MainWindow", "位置"))
        self.btn_disk_mkdir.setText(_translate("MainWindow", "新建文件夹"))
        self.btn_disk_select_all.setText(_translate("MainWindow", "全选"))
        self.btn_disk_delete.setText(_translate("MainWindow", "删除"))
        self.btn_disk_dl.setText(_translate("MainWindow", "下载"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.disk_tab), _translate("MainWindow", "我的蓝奏云"))
        self.btn_rec_select_all.setText(_translate("MainWindow", "全选"))
        self.btn_recovery.setText(_translate("MainWindow", "还原"))
        self.btn_rec_delete.setText(_translate("MainWindow", "彻底删除"))
        self.btn_rec_clean.setText(_translate("MainWindow", "清空回收站"))
        self.btn_recovery_all.setText(_translate("MainWindow", "全部还原"))
        self.expire_files_btn.setText(_translate("MainWindow", "过期文件"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rec_tab), _translate("MainWindow", "回收站"))
        self.acount.setTitle(_translate("MainWindow", "登录"))
        self.files.setTitle(_translate("MainWindow", "文件"))
        self.help.setTitle(_translate("MainWindow", "帮助"))
        self.toolbar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.login.setText(_translate("MainWindow", "登录"))
        self.logout.setText(_translate("MainWindow", "登出"))
        self.upload.setText(_translate("MainWindow", "上传"))
        self.download.setText(_translate("MainWindow", "下载"))
        self.delete.setText(_translate("MainWindow", "删除"))
        self.how.setText(_translate("MainWindow", "使用说明"))
        self.about.setText(_translate("MainWindow", "关于"))
