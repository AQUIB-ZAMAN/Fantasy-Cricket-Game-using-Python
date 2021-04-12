# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fantasy_CricketP.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from New_Team import Ui_NewTeam
from Open_Team import Ui_Dialog
from Team_Evaluation import Ui_evaluate_team
import sqlite3

Team_name = 'Enter name here'
PointsAvailable = 1000
PointsUsed = 0
no_of_bat = 0
no_of_bwl = 0
no_of_ar = 0
no_of_wk = 0
AllPlayers = []
AvailablePlayers = []
SelectedPlayers = []
CurrentPlayers = []
CurrentCategory = ''


conn = sqlite3.connect('Matches.db')
c = conn.cursor()
c.execute("SELECT * from PlayerDetails")
AllPlayers = c.fetchall()
c.close()
conn.close()


class Ui_MainWindow(object):
    def New_Team(self):
        self.window = QtWidgets.QMainWindow()
        self.new = Ui_NewTeam()
        self.new.setupUi(self.window)
        self.window.show()
        self.EnableButtons()
        self.Initialize()
        self.DisplayAll()
        self.ClearDB()
        
        
        
    def EnableButtons(self):
        self.bat_btn.setEnabled(True)
        self.bow_btn.setEnabled(True)
        self.ar_btn.setEnabled(True)
        self.wk_btn.setEnabled(True)
        
        
        
    def Initialize(self):
        #INITIALIZE THE MAIN WINDOW
        global Team_name
        global PointsAvailable
        global PointsUsed
        global no_of_bat
        global no_of_bwl
        global no_of_ar
        global no_of_wk
        global CurrentPlayers
        global SelectedPlayers
        global AvailablePlayers
        Team_name = 'Enter name here'
        PointsAvailable = 1000
        PointsUsed = 0
        no_of_bat = 0
        no_of_bwl = 0
        no_of_ar = 0
        no_of_wk = 0
        SelectedPlayers = []
        AvailablePlayers = []
        CurrentPlayers = []
        for i in AllPlayers:
            name = i[0]
            AvailablePlayers.append(name)
            CurrentPlayers.append(name)
        _translate = QtCore.QCoreApplication.translate
        self.batsmen.setText(_translate("MainWindow", "0"))
        self.bowlers.setText(_translate("MainWindow", "0"))
        self.allrounders.setText(_translate("MainWindow", "0"))
        self.wicketkeeper.setText(_translate("MainWindow", "0"))
        self.points_available.setText(_translate("MainWindow", "1000"))
        self.points_used.setText(_translate("MainWindow", "0"))
        
        
        
    def DisplayAll(self):
        #DISPLAY ALL PLAYERS IN THE SELECTION LIST
        self.listWidget.clear()
        self.listWidget_2.clear()
        self.listWidget.addItem("")
        self.listWidget.addItem("")
        self.listWidget_2.addItem("")
        self.listWidget_2.addItem("")
        for i in AllPlayers:
                s = i[0]
                ls = len(s)
                t = str(i[2]).rjust(35 - ls)
                s = s + t
                self.listWidget.addItem("{}".format(s));


        
    def ClearDB(self):
        conn = sqlite3.connect('Matches.db')
        c = conn.cursor()
        c.execute("DELETE FROM Teams WHERE player1 = ''")
        conn.commit()
        c.close()
        conn.commit()
        
        
        
    def Open_Team(self):
        self.ClearDB()
        self.window = QtWidgets.QMainWindow()
        self.new = Ui_Dialog()
        self.new.setupUi(self.window)
        self.window.show()
    
    
    
    def DisableButtons(self):
        self.bat_btn.setEnabled(False)
        self.bow_btn.setEnabled(False)
        self.ar_btn.setEnabled(False)
        self.wk_btn.setEnabled(False)
        
        
        
    def Handle_TeamNotCreated(self):
            self.Reset()
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Please create a new team first.")
            msg.setWindowTitle("Team Not Created")
            msg.exec_()
        
        
        
    def Save_Team(self):
        global Team_name
        if Team_name == 'Enter name here':
            self.Handle_TeamNotCreated()
        elif(len(SelectedPlayers) < 11):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Select atleast 11 players.")
            msg.setWindowTitle("Team formation error")
            msg.exec_()
        else:
            if no_of_bat == 0:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("You must select atleast 1 batsman!!!")
                msg.setWindowTitle("Not Enough Batsmen")
                msg.exec_()
                return
            if no_of_bwl == 0:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("You must select atleast 1 bowler!!!")
                msg.setWindowTitle("Not Enough Bowlers")
                msg.exec_()
                return
            if no_of_ar == 0:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("You must select atleast 1 allrounder!!!")
                msg.setWindowTitle("Not Enough Allrounders")
                msg.exec_()
                return
            if no_of_wk == 0:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("You must select atleast 1 wicket-keeper!!!")
                msg.setWindowTitle("Not Enough Wicket-keepers")
                msg.exec_()
                return
            conn = sqlite3.connect('Matches.db')
            c = conn.cursor()
            Team = ()
            Team += (Team_name,)
            for i in SelectedPlayers:
                Team += (i,)
            c.execute("INSERT INTO Teams VALUES {}".format(Team))
            conn.commit()
            c.close()
            conn.close()
            self.Reset()
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Team saved successfully!!")
            msg.setWindowTitle("Team Creation Successful")
            msg.exec_()
        
        
        
    def Reset(self):
        global Team_name
        Team_name = 'Enter name here'
        self.DisableButtons()
        self.listWidget.clear()
        self.listWidget_2.clear()
        _translate = QtCore.QCoreApplication.translate
        self.batsmen.setText(_translate("MainWindow", "##"))
        self.bowlers.setText(_translate("MainWindow", "##"))
        self.allrounders.setText(_translate("MainWindow", "##"))
        self.wicketkeeper.setText(_translate("MainWindow", "##"))
        self.points_available.setText(_translate("MainWindow", "####"))
        self.points_used.setText(_translate("MainWindow", "####"))
        self.team_name.setText(_translate("MainWindow", "Displayed Here"))

            
        
    def Evaluate_Team(self):
        self.ClearDB()
        self.window = QtWidgets.QMainWindow()
        self.new = Ui_evaluate_team()
        self.new.setupUi(self.window)
        self.window.show()
        


    def bat(self):
        try:
            global Team_name
            global AllPlayers
            global CurrentCategory
            global CurrentPlayers
            _translate = QtCore.QCoreApplication.translate
            conn = sqlite3.connect('Matches.db')
            c = conn.cursor()
            if Team_name == 'Enter name here':
                c.execute("SELECT * FROM Teams WHERE player1 = ''")
                Team_name = c.fetchone()
                Team_name = Team_name[0]
            else:
                pass
        except:
            self.Handle_TeamNotCreated()
        else:
            if self.team_name.text() == "Displayed Here":
                c.execute("DELETE FROM Teams WHERE player1 = ''")
                self.team_name.setText(_translate("MainWindow", "{}".format(Team_name)))
            CurrentCategory = 'BAT'
            self.listWidget.clear()
            self.listWidget.addItem("")
            self.listWidget.addItem("")
            CurrentPlayers = []
            for i in AllPlayers:
                if i[1] == 'BAT' and i[0] in AvailablePlayers:
                    s = i[0]
                    CurrentPlayers.append(s)
                    ls = len(s)
                    t = str(i[2]).rjust(35 - ls)
                    s = s + t
                    self.listWidget.addItem("{}".format(s));
        finally:
            conn.commit()
            c.close()
            conn.close()
            
    
    
    def bwl(self):
        try:
            global Team_name
            global AllPlayers
            global CurrentCategory
            global CurrentPlayers
            _translate = QtCore.QCoreApplication.translate
            conn = sqlite3.connect('Matches.db')
            c = conn.cursor()
            if Team_name == 'Enter name here':
                c.execute("SELECT * FROM Teams WHERE player1 = ''")
                Team_name = c.fetchone()
                Team_name = Team_name[0]
            else:
                pass
        except:
            self.Handle_TeamNotCreated()
        else:
            if self.team_name.text() == "Displayed Here":
                c.execute("DELETE FROM Teams WHERE player1 = ''")
                self.team_name.setText(_translate("MainWindow", "{}".format(Team_name)))
            CurrentCategory = 'BWL'
            self.listWidget.clear()
            self.listWidget.addItem("")
            self.listWidget.addItem("")
            CurrentPlayers = []
            for i in AllPlayers:
                if i[1] == 'BWL' and i[0] in AvailablePlayers:
                    s = i[0]
                    CurrentPlayers.append(s)
                    ls = len(s)
                    t = str(i[2]).rjust(35 - ls)
                    s = s + t
                    self.listWidget.addItem("{}".format(s));
        finally:
            conn.commit()
            c.close()
            conn.close()
            
            
            
    def ar(self):
        try:
            global Team_name
            global AllPlayers
            global CurrentCategory
            global CurrentPlayers
            _translate = QtCore.QCoreApplication.translate
            conn = sqlite3.connect('Matches.db')
            c = conn.cursor()
            if Team_name == 'Enter name here':
                c.execute("SELECT * FROM Teams WHERE player1 = ''")
                Team_name = c.fetchone()
                Team_name = Team_name[0]
            else:
                pass
        except:
            self.Handle_TeamNotCreated()
        else:
            if self.team_name.text() == "Displayed Here":
                c.execute("DELETE FROM Teams WHERE player1 = ''")
                self.team_name.setText(_translate("MainWindow", "{}".format(Team_name)))
            CurrentCategory = 'AR'
            self.listWidget.clear()
            self.listWidget.addItem("")
            self.listWidget.addItem("")
            CurrentPlayers = []
            for i in AllPlayers:
                if i[1] == 'AR' and i[0] in AvailablePlayers:
                    s = i[0]
                    CurrentPlayers.append(s)
                    ls = len(s)
                    t = str(i[2]).rjust(35 - ls)
                    s = s + t
                    self.listWidget.addItem("{}".format(s));
        finally:
            conn.commit()
            c.close()
            conn.close()
            
            
            
    def wk(self):
        try:
            global Team_name
            global AllPlayers
            global CurrentCategory
            global CurrentPlayers
            _translate = QtCore.QCoreApplication.translate
            conn = sqlite3.connect('Matches.db')
            c = conn.cursor()
            if Team_name == 'Enter name here':
                c.execute("SELECT * FROM Teams WHERE player1 = ''")
                Team_name = c.fetchone()
                Team_name = Team_name[0]
            else:
                pass
        except:
            self.Handle_TeamNotCreated()
        else:
            if self.team_name.text() == "Displayed Here":
                c.execute("DELETE FROM Teams WHERE player1 = ''")
                self.team_name.setText(_translate("MainWindow", "{}".format(Team_name)))
            CurrentCategory = 'WK'
            self.listWidget.clear()
            self.listWidget.addItem("")
            self.listWidget.addItem("")
            CurrentPlayers = []
            for i in AllPlayers:
                if i[1] == 'WK' and i[0] in AvailablePlayers:
                    s = i[0]
                    CurrentPlayers.append(s)
                    ls = len(s)
                    t = str(i[2]).rjust(35 - ls)
                    s = s + t
                    self.listWidget.addItem("{}".format(s));
        finally:
            conn.commit()
            c.close()
            conn.close()



    def AddPlayer(self, item):
        try:
            global Team_name
            global AllPlayers
            global CurrentCategory
            global CurrentPlayers
            _translate = QtCore.QCoreApplication.translate
            conn = sqlite3.connect('Matches.db')
            c = conn.cursor()
            if Team_name == 'Enter name here':
                c.execute("SELECT * FROM Teams WHERE player1 = ''")
                Team_name = c.fetchone()
                Team_name = Team_name[0]
            else:
                pass
        except:
            self.Handle_TeamNotCreated()
        else:
            if self.team_name.text() == "Displayed Here":
                c.execute("DELETE FROM Teams WHERE player1 = ''")
                self.team_name.setText(_translate("MainWindow", "{}".format(Team_name)))
            global CurrentPlayers
            global SelectedPlayers
            global AvailablePlayers
            global PointsAvailable
            global PointsUsed
            global no_of_bat
            global no_of_bwl
            global no_of_ar
            global no_of_wk
            t = item.text()
            t = t.rstrip("1234567890 ")
            if(t == ''):
                return
            for i in AllPlayers:
                if t == i[0]:
                    category = i[1]
                    value = i[2]
                    break
            total_no_of_players = no_of_bat + no_of_bwl + no_of_ar + no_of_wk
            if total_no_of_players == 11:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("You have already selected 11 players!!!\nNow save your team.")
                msg.setWindowTitle("All Players Selected")
                msg.exec_()
                return
            if PointsAvailable - value < 0:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("You dont have enough points to buy this player!!!")
                msg.setWindowTitle("Not Enough Points")
                msg.exec_()
                return
            if category == 'BAT' and no_of_bat == 4:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("You cannot select more than 4 batsmen!!!")
                msg.setWindowTitle("Invalid Choice")
                msg.exec_()
                return
            if category == 'BWL' and no_of_bwl == 3:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("You cannot select more than 3 bowlers!!!")
                msg.setWindowTitle("Invalid Choice")
                msg.exec_()
                return
            if category == 'AR' and no_of_ar == 3:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("You cannot select more than 3 allrounders!!!")
                msg.setWindowTitle("Invalid Choice")
                msg.exec_()
                return
            if category == 'WK' and no_of_wk == 1:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("You cannot select more than 1 wicket-keeper!!!")
                msg.setWindowTitle("Invalid Choice")
                msg.exec_()
                return
            if category == 'BAT':
                no_of_bat += 1
            elif category == 'BWL':
                no_of_bwl +=1
            elif category == 'AR':
                no_of_ar += 1
            elif category == 'WK':
                no_of_wk += 1
            PointsAvailable -= value
            PointsUsed += value
            CurrentPlayers.remove(t)
            AvailablePlayers.remove(t)
            SelectedPlayers.append(t)
            self.listWidget_2.addItem(t)
            r = self.listWidget.row(item)
            self.listWidget.takeItem(r)
            _translate = QtCore.QCoreApplication.translate
            self.batsmen.setText(_translate("MainWindow", "{}".format(no_of_bat)))
            self.bowlers.setText(_translate("MainWindow", "{}".format(no_of_bwl)))
            self.allrounders.setText(_translate("MainWindow", "{}".format(no_of_ar)))
            self.wicketkeeper.setText(_translate("MainWindow", "{}".format(no_of_wk)))
            self.points_available.setText(_translate("MainWindow", "{}".format(PointsAvailable)))
            self.points_used.setText(_translate("MainWindow", "{}".format(PointsUsed)))
        finally:
            conn.commit()
            c.close()
            conn.close()
        
        
        
    def RemovePlayer(self, item):
        global CurrentPlayers
        global SelectedPlayers
        global AvailablePlayers
        global PointsAvailable
        global CurrentCategory
        global PointsUsed
        global no_of_bat
        global no_of_bwl
        global no_of_ar
        global no_of_wk
        t = item.text()
        t = t.rstrip("1234567890 ")
        if(t == ''):
            return
        for i in AllPlayers:
            if t == i[0]:
                category = i[1]
                value = i[2]
                break
        if category == 'BAT':
            no_of_bat -= 1
        elif category == 'BWL':
            no_of_bwl -=1
        elif category == 'AR':
            no_of_ar -= 1
        elif category == 'WK':
            no_of_wk -= 1
        PointsAvailable += value
        PointsUsed -= value
        if category == CurrentCategory:
            CurrentPlayers.append(t)
            for i in AllPlayers:
                if i[0] == t:
                    lt = len(t)
                    s = str(i[2]).rjust(35 - lt)
                    s = t + s
                    self.listWidget.addItem("{}".format(s))
                    break
        AvailablePlayers.append(t)
        SelectedPlayers.remove(t)
        lt = len(t)
        t = t + str(value).rjust(35 - lt)
        r = self.listWidget_2.row(item)
        self.listWidget_2.takeItem(r)
        _translate = QtCore.QCoreApplication.translate
        self.batsmen.setText(_translate("MainWindow", "{}".format(no_of_bat)))
        self.bowlers.setText(_translate("MainWindow", "{}".format(no_of_bwl)))
        self.allrounders.setText(_translate("MainWindow", "{}".format(no_of_ar)))
        self.wicketkeeper.setText(_translate("MainWindow", "{}".format(no_of_wk)))
        self.points_available.setText(_translate("MainWindow", "{}".format(PointsAvailable)))
        self.points_used.setText(_translate("MainWindow", "{}".format(PointsUsed)))


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(937, 656)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bowlers = QtWidgets.QLabel(self.centralwidget)
        self.bowlers.setGeometry(QtCore.QRect(370, 80, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bowlers.setFont(font)
        self.bowlers.setStyleSheet("color: rgb(3, 190, 159);\n"
"background-color: rgb(240, 240, 240);")
        self.bowlers.setObjectName("bowlers")
        self.wicketkeeper = QtWidgets.QLabel(self.centralwidget)
        self.wicketkeeper.setGeometry(QtCore.QRect(780, 80, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.wicketkeeper.setFont(font)
        self.wicketkeeper.setStyleSheet("color: rgb(3, 190, 159);\n"
"background-color: rgb(240, 240, 240);")
        self.wicketkeeper.setObjectName("wicketkeeper")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(230, 80, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(50, 80, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label_9.setObjectName("label_9")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(410, 80, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label_12.setObjectName("label_12")
        self.batsmen = QtWidgets.QLabel(self.centralwidget)
        self.batsmen.setGeometry(QtCore.QRect(190, 80, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.batsmen.setFont(font)
        self.batsmen.setStyleSheet("color: rgb(3, 190, 159);\n"
"background-color: rgb(240, 240, 240);")
        self.batsmen.setObjectName("batsmen")
        self.allrounders = QtWidgets.QLabel(self.centralwidget)
        self.allrounders.setGeometry(QtCore.QRect(550, 80, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.allrounders.setFont(font)
        self.allrounders.setStyleSheet("color: rgb(3, 190, 159);\n"
"background-color: rgb(240, 240, 240);")
        self.allrounders.setObjectName("allrounders")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(600, 80, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label_13.setObjectName("label_13")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(40, 20, 791, 111))
        self.label_11.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 30, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label_8.setObjectName("label_8")
        self.bat_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.bat_btn.setEnabled(False)
        self.bat_btn.setGeometry(QtCore.QRect(130, 250, 61, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.bat_btn.setFont(font)
        self.bat_btn.setObjectName("bat_btn")
        ''''''
        self.bat_btn.toggled.connect(self.bat)
        ''''''
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(510, 250, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("")
        self.label_16.setObjectName("label_16")
        self.wk_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.wk_btn.setEnabled(False)
        self.wk_btn.setGeometry(QtCore.QRect(330, 250, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.wk_btn.setFont(font)
        self.wk_btn.setObjectName("wk_btn")
        ''''''
        self.wk_btn.toggled.connect(self.wk)
        ''''''
        self.points_available = QtWidgets.QLabel(self.centralwidget)
        self.points_available.setGeometry(QtCore.QRect(260, 210, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.points_available.setFont(font)
        self.points_available.setStyleSheet("color: rgb(3, 190, 159);")
        self.points_available.setObjectName("points_available")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(120, 240, 271, 311))
        self.listWidget.setLineWidth(1)
        self.listWidget.setObjectName("listWidget")
        ''''''
        self.listWidget.itemDoubleClicked.connect(self.AddPlayer)
        ''''''
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(430, 370, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.team_name = QtWidgets.QLabel(self.centralwidget)
        self.team_name.setGeometry(QtCore.QRect(610, 250, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.team_name.setFont(font)
        self.team_name.setStyleSheet("color: rgb(3, 190, 159);")
        self.team_name.setObjectName("team_name")
        self.bow_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.bow_btn.setEnabled(False)
        self.bow_btn.setGeometry(QtCore.QRect(200, 250, 71, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.bow_btn.setFont(font)
        self.bow_btn.setObjectName("bow_btn")
        ''''''
        self.bow_btn.toggled.connect(self.bwl)
        ''''''
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(500, 240, 271, 311))
        self.listWidget_2.setObjectName("listWidget_2")
        ''''''
        self.listWidget_2.itemDoubleClicked.connect(self.RemovePlayer)
        ''''''
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(120, 210, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(500, 210, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("")
        self.label_15.setObjectName("label_15")
        self.points_used = QtWidgets.QLabel(self.centralwidget)
        self.points_used.setGeometry(QtCore.QRect(610, 210, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.points_used.setFont(font)
        self.points_used.setStyleSheet("color: rgb(3, 190, 159);")
        self.points_used.setObjectName("points_used")
        self.ar_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.ar_btn.setEnabled(False)
        self.ar_btn.setGeometry(QtCore.QRect(270, 250, 51, 17))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.ar_btn.setFont(font)
        self.ar_btn.setObjectName("ar_btn")
        ''''''
        self.ar_btn.toggled.connect(self.ar)
        ''''''
        self.listWidget.raise_()
        self.listWidget_2.raise_()
        self.label_16.raise_()
        self.label_11.raise_()
        self.bowlers.raise_()
        self.wicketkeeper.raise_()
        self.label_10.raise_()
        self.label_9.raise_()
        self.label_12.raise_()
        self.batsmen.raise_()
        self.allrounders.raise_()
        self.label_13.raise_()
        self.label_8.raise_()
        self.bat_btn.raise_()
        self.wk_btn.raise_()
        self.points_available.raise_()
        self.label_17.raise_()
        self.team_name.raise_()
        self.bow_btn.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.points_used.raise_()
        self.ar_btn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 937, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.menuBar.setFont(font)
        self.menuBar.setAutoFillBackground(False)
        self.menuBar.setStyleSheet("")
        self.menuBar.setObjectName("menuBar")
        self.manage_teams = QtWidgets.QMenu(self.menuBar)
        self.manage_teams.setGeometry(QtCore.QRect(270, 157, 237, 174))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.manage_teams.setFont(font)
        self.manage_teams.setStyleSheet("background-color: rgb(190, 190, 190);")
        self.manage_teams.setObjectName("manage_teams")
        MainWindow.setMenuBar(self.menuBar)
        self.new_team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.new_team.setFont(font)
        self.new_team.setObjectName("new_team")
        ''''''
        self.new_team.triggered.connect(self.New_Team)
        ''''''
        self.open_team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.open_team.setFont(font)
        self.open_team.setObjectName("open_team")
        ''''''
        self.open_team.triggered.connect(self.Open_Team)
        ''''''
        self.save_team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.save_team.setFont(font)
        self.save_team.setObjectName("save_team")
        ''''''
        self.save_team.triggered.connect(self.Save_Team)
        ''''''
        self.evaluate_team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.evaluate_team.setFont(font)
        self.evaluate_team.setObjectName("evaluate_team")
        ''''''
        self.evaluate_team.triggered.connect(self.Evaluate_Team)
        ''''''
        self.manage_teams.addAction(self.new_team)
        self.manage_teams.addAction(self.open_team)
        self.manage_teams.addAction(self.save_team)
        self.manage_teams.addAction(self.evaluate_team)
        self.menuBar.addAction(self.manage_teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fantasy Cricket"))
        self.bowlers.setText(_translate("MainWindow", "##"))
        self.wicketkeeper.setText(_translate("MainWindow", "##"))
        self.label_10.setText(_translate("MainWindow", "Bowlers (BOW)"))
        self.label_9.setText(_translate("MainWindow", "Batsmen (BAT)"))
        self.label_12.setText(_translate("MainWindow", "Allrounders (AR)"))
        self.batsmen.setText(_translate("MainWindow", "##"))
        self.allrounders.setText(_translate("MainWindow", "##"))
        self.label_13.setText(_translate("MainWindow", "Wicket-keeper (WK)"))
        self.label_8.setText(_translate("MainWindow", "Your Selections"))
        self.bat_btn.setText(_translate("MainWindow", "BAT"))
        self.label_16.setText(_translate("MainWindow", "Team Name"))
        self.wk_btn.setText(_translate("MainWindow", "WK"))
        self.points_available.setText(_translate("MainWindow", "####"))
        self.label_17.setText(_translate("MainWindow", ">"))
        self.team_name.setText(_translate("MainWindow", "Displayed Here"))
        self.bow_btn.setText(_translate("MainWindow", "BOW"))
        self.label_14.setText(_translate("MainWindow", "Points Available"))
        self.label_15.setText(_translate("MainWindow", "Points Used"))
        self.points_used.setText(_translate("MainWindow", "####"))
        self.ar_btn.setText(_translate("MainWindow", "AR"))
        self.manage_teams.setTitle(_translate("MainWindow", "&     Manage Teams     "))
        self.new_team.setText(_translate("MainWindow", "&       NEW Team"))
        self.open_team.setText(_translate("MainWindow", "  &     OPEN Team"))
        self.save_team.setText(_translate("MainWindow", "&       SAVE Team"))
        self.evaluate_team.setText(_translate("MainWindow", "&       EVALUATE Team"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
