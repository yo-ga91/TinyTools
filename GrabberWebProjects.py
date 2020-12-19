#! /usr/bin/python3.5
# -*- coding: utf-8 -*-

import os
import tarfile
import subprocess
import pathlib

class ProJec:
    def __init__(self, Mydir):
        self.name =  Mydir[(Mydir.rindex('/', 1, (- 1)) + 1):(-1)]
        self.Dir = Mydir[:(-1)]
        os.mkdir=('/home/BUP/'+self.name)
        self.BUP = '/home/BUP/'
        #+self.name

    def create_tar(self):
        with tarfile.open(self.BUP+self.name  + '.tar.gz', "w:gz") as tar:
             tar.add(self.Dir)
             print('{0} not CMS is Archiver'.format(self.name))
    def __del__(self):
        ' '

class DataBase:
    def __init__(self, BdName, Bdhoast, BduName, BdPass, BupDir):
        self.Dir=str(BupDir)
        self.Name=str(BdName)
        self.User=str(BduName)
        self.Pass=str(BdPass)
        self.host=str(Bdhoast)

    def BDdumps(self):
        print('DBDumped')
        try:
            dump = self.Dir + self.Name + '.sql'
            # return dump
            p = subprocess.Popen(
                'mysqldump -h' + self.host + ' -u' + self.User + ' -p' + self.Pass + ' --databases ' + self.Name + ' > ' + dump,
                shell=True)
           # Wait for completion
            p.communicate()
            # Check for errors
            if p.returncode != 0:
                raise p.returncode
            print('Backup done for', self.Name)
            return dump
        except:
            print('Backup DB failed for ', self.Name)

    def __del__(self):
        ' '

class MyBitrix:
    def __init__(self, Mydir):
        self.name =  Mydir[(Mydir.rindex('/', 1, (- 1)) + 1):(-1)]
        self.Dir = Mydir[:(-1)]
        os.mkdir=('/home/BUP/'+self.name)
        self.BUP = str('/home/BUP/'+self.name)

    def extractBD(self):
        if pathlib.Path(self.Dir + '/bitrix').is_symlink():
            print(self.name+'\n' + str(pathlib.Path(self.Dir + '/bitrix')))
            BdHost = BduName = BdPass = BdName = 'symlink'
            self.MyDB=DataBase(BdName,BdHost,BduName,BdPass,self.BUP)
        elif pathlib.Path(self.Dir + '/bitrix').is_dir():
            if pathlib.Path(self.Dir + '/bitrix/php_interface/dbconn.php').exists():
                with open(self.Dir + '/bitrix/php_interface/dbconn.php') as File:
                    for line in File:
                        if line.find('$DBHost') > -1 and (line.find('#') == (-1) or line.find('#') > 1):
                            BdHost = line[(line.find('= "') + 3):(len(line) - 3)]
                        elif line.find('$DBLogin') > -1 and (line.find('#') == (-1) or line.find('#') > 1):
                            BduName = line[(line.find('= "') + 3): (len(line) - 3)]
                        elif line.find('$DBPassword') > -1 and (line.find('#') == (-1) or line.find('#') > 1):
                            BdPass = line[(line.find('= "') + 3): (len(line) - 3)]
                        elif line.find('$DBName') > -1 and (line.find('#') == (-1) or line.find('#') > 1):
                            BdName = line[(line.find('= "') + 3): (len(line) - 3)]
                self.MyDB=DataBase(BdName,BdHost,BduName,BdPass,self.BUP)
            elif pathlib.Path(self.Dir + '/bitrix/.settings.php').exists():
                with open(self.Dir + '/bitrix/.settings.php') as File:
                    for line in File:
                        if line.find('host') > -1 and (line.find('#') == (-1) or line.find('#') > 1):
                            BdHost = line[(line.find("=> '") + 4):(len(line) - 3)]
                        elif line.find('login') > -1 and (line.find('#') == (-1) or line.find('#') > 1):
                            BduName = line[(line.find("=> '") + 4): (len(line) - 3)]
                        elif line.find('password') > -1 and (line.find('#') == (-1) or line.find('#') > 1):
                            BdPass = line[(line.find("=> '") + 4): (len(line) - 3)]
                        elif line.find('database') > -1 and (line.find('#') == (-1) or line.find('#') > 1):
                            BdName = line[(line.find("=> '") + 4): (len(line) - 3)]
                self.MyDB=DataBase(BdName,BdHost,BduName,BdPass,self.BUP)
            else:
                print('{0} is Bad database config!'.format(self.name))
                BdHost = BduName = BdPass = BdName = '*****'
                self.MyDB=DataBase(BdName,BdHost,BduName,BdPass,self.BUP)
        else:
           print('{0} is symlink database config!'.format(self.name))
           BdHost = BduName = BdPass = BdName = 'symlink'
           self.MyDB=DataBase(BdName, BdHost, BduName, BdPass, self.BUP)

    def create_tar(self):
        self.MyDB.BDdumps()
        with tarfile.open(self.BUP + '.tar.gz', "w:gz") as tar:
             tar.add(self.Dir)
             print('{0} on Bitrix is Archiver'.format(self.name))

    def __del__(self):
        ' '

class MyWP:
    def __init__(self, Mydir):
        self.name =  Mydir[(Mydir.rindex('/', 1, (- 1)) + 1):(-1)]
        self.Dir = Mydir[:(-1)]
        os.mkdir=('/home/BUP/'+self.name)
        self.BUP = '/home/BUP/'+self.name

    def extractBD(self):
        if pathlib.Path(self.Dir + '/wp-config.php').exists():
            with open(self.Dir + '/wp-config.php') as File:
                for line in File:
                    if line.find('DB_HOST') > -1 and line.find('#') == (-1):
                        BdHost = line[(line.find(",") + 3):(len(line) - 4)]
                    elif line.find('DB_USER') > -1 and line.find('#') == (-1):
                        BduName = line[(line.find(",") + 3): (len(line) - 4)]
                    elif line.find('DB_PASSWORD') > -1 and line.find('#') == (-1):
                        BdPass = line[(line.find(",") + 3): (len(line) - 4)]
                    elif line.find('DB_NAME') > -1 and line.find('#') == (-1):
                        BdName = line[(line.find(",") + 3): (len(line) - 4)]
            self.MyDB=DataBase(str(BdName),str(BdHost),str(BduName),str(BdPass), self.BUP)
        else:
            print('{0} is Bad database config!'.format(self.name))
            BdHost=BduName=BdPass=BdName='*****'
            self.MyDB=DataBase(str(BdName),str(BdHost),str(BduName),str(BdPass), self.BUP)


    def create_tar(self):
        self.MyDB.BDdumps()
        with tarfile.open(self.BUP + '.tar.gz', "w:gz") as tar:
             tar.add(self.Dir)
             print('{0} on WordPress is Archiver'.format(self.name))

    def __del__(self):
        ' '

class MyJoomla:
    def __init__(self, Mydir):
        self.name =  Mydir[(Mydir.rindex('/', 1, (- 1)) + 1):(-1)]
        self.Dir = Mydir[:(-1)]
        os.mkdir=('/home/BUP/'+self.name)
        self.BUP = '/home/BUP/'+self.name

    def extractBD(self):
        if pathlib.Path(self.Dir + '/configuration.php').exists():
            with open(self.Dir + '/configuration.php') as File:
                for line in File:
                    if line.find('$host') > -1 and line.find('#') == (-1):
                        BdHost = line[(line.find("'") + 1):(len(line) - 2)]
                    elif line.find('$user') > -1 and line.find('#') == (-1):
                        BduName = line[(line.find("'") + 1): (len(line) - 2)]
                    elif line.find('$password') > -1 and line.find('#') == (-1):
                        BdPass = line[(line.find("'") + 1): (len(line) - 2)]
                    elif line.find('$db') > -1 and line.find('#') == (-1):
                        BdName = line[(line.find("'") + 1): (len(line) - 2)]
            self.MyDB=DataBase(str(BdName),str(BdHost),str(BduName),str(BdPass), self.BUP)
        else:
            print('{0} is Bad database config!'.format(self.name))
            BdHost = BduName = BdPass = BdName = '*****'
            self.MyDB=DataBase(str(BdName),str(BdHost),str(BduName),str(BdPass), self.BUP)

    def create_tar(self):
        self.MyDB.BDdumps()
        with tarfile.open(self.BUP  + '.tar.gz', "w:gz") as tar:
             tar.add(self.Dir)
             print('{0} on Joomla is Archiver'.format(self.name))

    def __del__(self):
        ' '

def MyList(List, MyType, DBList):
    if MyType.find('All') < 0:
        DBList.write(str(MyType)+'\n')
        for Obj in List:
            Obj.extractBD()
            Obj.create_tar()
            DBList.write(str(Obj.name) + '\n')
            DBList.write('\t DataBase \n')
            DBList.write(str(Obj.MyDB.Name) + '\n')
            DBList.write(str(Obj.MyDB.User) + '\n')
            DBList.write(str(Obj.MyDB.Pass) + '\n')
            DBList.write(str(Obj.MyDB.host) + '\n')
            DBList.write('\n')
    else:
        DBList.write(str(MyType)+'\n')
        for Obj in List:
            DBList.write(str(Obj.name) + '\n')
            Obj.create_tar()
            
    print('\n Project {0} is compressed \n'.format(str(MyType)))
    
def PrList(List, MyType, DBList):
    if MyType.find('All') < 0:
        DBList.write(str(MyType)+'\n')
        for Obj in List:
            DBList.write(str(Obj.name) + '\n')
            #DBList.write('\t DataBase \n')
            #DBList.write(str(Obj.MyDB.Name) + '\n')
            #DBList.write(str(Obj.MyDB.User) + '\n')
            #DBList.write(str(Obj.MyDB.Pass) + '\n')
            #DBList.write(str(Obj.MyDB.host) + '\n')
            #DBList.write('\n')
        else:
            DBList.write(str(MyType)+' '+str(len(List))+'\n\n')
    else:
        DBList.write(str(MyType)+'\n')
        for Obj in List:
            DBList.write(str(Obj.name) + '\n')
        else:
            DBList.write(str(MyType)+' '+str(len(List))+'\n\n')

            
    print('\n Project {0} add in List \n'.format(str(MyType)))


def FindFiles(catalog, FindFilename):
#    '''Поиск заданных файлов по дереву
#    на глубину до первого вхождения'''
    Myfind_files = []

    currentDirectory = pathlib.Path(catalog)
    for currentFile in currentDirectory.iterdir():
        if (currentFile.name.find(FindFilename)>=0) and (currentFile.is_file()):
            Myfind_files.append(currentFile)
            return Myfind_files
    else:
        for currentFile in currentDirectory.iterdir():
            if currentFile.is_dir():
                Myfind_files.extend(FindFiles(currentFile, FindFilename))

    return Myfind_files

def main():
    DirFind = '/var/www/'
    FileCheck = 'index'

    ProJectList = FindFiles(DirFind, FileCheck)
    Bitr = []
    WP = []
    AllPRJ = []

    for Obj in ProJectList:
        Obj = str(Obj)
        #Obj = Obj[:Obj.find('index')]
        Obj = Obj[:(Obj.rindex('/', 1, (-2))+1)]
        # Bitr=pathlib.Path(str(Obj+'/bitrix')
        if pathlib.Path(Obj + '/bitrix').exists():
            Bitr.append(MyBitrix(Obj))
        elif pathlib.Path(Obj + '/wp-config.php').exists():
            WP.append(MyWP(Obj))
        else:
            AllPRJ.append(ProJec(Obj))

    print('Bitrix project {0}'.format(str(len(Bitr))))
    print('WP project {0}'.format(str(len(WP))))
    print('All project {0}'.format(str(len(AllPRJ))))

    PreDB_List = open('/home/BUP/PrList.txt', 'w')
    PrList(Bitr, 'Bitr', PreDB_List)
    PrList(WP, 'WP', PreDB_List)
    PrList(AllPRJ, 'All', PreDB_List)
    PreDB_List.close()

    DB_List = open('/home/BUP/dbList.txt', 'w')
    MyList(Bitr, 'Bitr', DB_List)
    MyList(WP, 'WP', DB_List)
    MyList(AllPRJ, 'All', DB_List)
    DB_List.close()

    print('\n Program is complite \n')


main()

