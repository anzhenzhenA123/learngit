# -*- coding:cp936 -*-
__author__ = 'Administrator'
# ����webdriver��time ���

from selenium import webdriver
import time

print ("------��������Զ�������¼�����������------")
# ����Logintest ��

class Logintest():

        def openB(self):
            """ ������� """
            global browser  # ����browserΪȫ�ֱ���
            browser = webdriver.Firefox()   # ʵ����Firefox��
            time.sleep(2)   # ʹ������ͣ2�룬��ͬ
            return "\n �Ѵ�"

        def keyinfo(self, url,telephone,password):
            """��λ�û��������������д������"""
            browser.get(url)    # get()password������url
            time.sleep(2)
            browser.find_element_by_id('telephone').send_keys(telephone)  # ��λ�ֻ��ŵ������ʹ��send_keys()����д������
            time.sleep(2)
            browser.find_element_by_id('password').send_keys(password)  # ��λ����������ʹ��send_keys()����д������
            time.sleep(2)
            

        def keyyzm(self, verCode, imgValidateCode):
            """��λ��֤��������ͼƬ�����û�Э����������֤�룬�ɸ�����Ҫ�л�ͼƬ"""
            ChangeReq = input("��������֤��ͼƬ�����л�?(Y/N): ")    # ѯ���û��Ƿ��ܿ�����֤��ͼƬ
            while ChangeReq == "Y":
                browser.find_element_by_id(imgValidateCode).click()    # ���û��޷����壬��λ��֤��ͼƬԪ�ز����ֱ���û�����
                clearPic = input("���Կ���ͼƬ��?(Y/N): ", )   # ѯ���û��Ƿ��ܿ���
                if clearPic == "Y":     # ���ܿ��壬�����л�ͼƬ
                    ChangeReq = "N"
            yzm = input("�����뿴������֤��:")     # �û�������֤��
            browser.find_element_by_id(verCode).send_keys(yzm)  # ��λ��֤�������д������
            return yzm

        def verifylogin(self, loginSub1, title):
            """�����¼��ť������֤�Ƿ��¼�ɹ�����֤���ݣ���¼���ҳ��Դ����title�������ַ���Ϣ��"""
            browser.find_element_by_id(loginSub1).click()  # ��λ��¼��ť�����
            time.sleep(1)
            try:
                assert title in browser.title  # ʹ��assert����ҳ��title��ĳ�ַ�
            except AssertionError:  # ��ҳ��title����ĳ�ַ�������¼ʧ�ܣ���������AssertionError
                print ("%>_<% ...��½ʧ��")  # AssertionError �Ĵ���ʽ
                screenshot = raw_input("��Ҫ��ͼ�Ա���fail������?(Y/N)(ͼƬ��LoginErro.jpg������C:\): ")  # ѯ���Ƿ����ͼ
                if screenshot == "Y":
                    browser.save_screenshot("C:\LoginErro.jpg")     # ʹ��save_screenshot������ͼ����LoginErro����
            else:   # ��ҳ��title��ĳ�ַ�������¼�ɹ�������ִ��else���
                print ("��¼�ɹ�")
            return "������֤"

        def closeB(self):
            """�ر������"""
            CloseB = input("�ر�?(Y/N): ")  # ѯ���Ƿ���Ҫ�ر�
            if CloseB == "Y":
                browser.quit()      # ʹ��quit()�ر�
            return "\n ------���β����������н�������лʹ�ã��ټ�"
            time.sleep(5)

# ʵ����testClassΪ SucLogin��������ȷ���û��������룬��֤���¼

SucLogin = Logintest()
print ("1.�������", SucLogin.openB())
print ("2.�򿪲���url���������û���������\n", \
    SucLogin.keyinfo("http://www.rongzi.com/account/login", "15821865916","123456a"))
print ("3.�����������֤��\n", SucLogin.keyyzm("verCode", "imgValidateCode"))
print ("4.��֤��½�Ƿ�ɹ�\n", SucLogin.verifylogin("loginSub1", U"����������"))
print ("5.�ر������\n", SucLogin.closeB())

# ������Ҫʵ����testClassΪXXXX���޸��������


# ����

