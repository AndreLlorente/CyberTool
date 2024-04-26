#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import processlogs
import exceltodb
import vtdatabase
import jupytergraphics
import processlogshttphttps
import portscanner3000
import activeconnections
import speech_recognition as sr
import subprocess
import socket
import ipaddress
import ALIENRAW
import os
from art import *
import VT
import vtfile

option=0

ascii_art = text2art("Cybertool")
by_ascii_art = text2art("by Andre Llorente")
def menu(option):
    while True:
        os.system('clear')
        print(ascii_art)
        print(by_ascii_art)
        print("\n----- Tool Menu -----")
        print("1. PortScanner3000")
        print("2. Show ActiveConnections on Host")
        print("3. Check [File, Database, or Manual IP] using VirusTotal")
        print("4. Check [Manual IP] using AlienVault")
        print("5. Process File Data")
        print("6. Jupyter-Notebooks Graphical integration")
        print("9. Exit Program.")

        option = input("Select the tool you want to use:\n-> ")
        match option:
            case "1":
                while True:
                    print("\n----- Port Scanner Menu -----")
                    portscanner3000.port_scanner_function()
                    input("Press Enter to continue...")
                    repeat = input("Do you want to repeat the Port Scanner? (Y/N) ")
                    if repeat.lower() != "y":
                        break
            case "2":
                while True:
                    print("\n----- Show Active Connections Menu -----")
                    activeconnections.activeconnectionsfunc()
                    input("Press Enter to continue...")
                    repeat = input("Do you want to repeat Show Active Connections? (Y/N) ")
                    if repeat.lower() != "y":
                        os.system('clear')
                        break
            case "3":
                while True:
                    ascii_vt = text2art("VirusTotal")
                    print(ascii_vt)
                    print("\n----- VirusTotal Menu -----")
                    print("What do you wish to analyze using the VirusTotal Platform?")
                    print("1. Analyze an IP")
                    print("2. Analyze a file")
                    print("3. Analyze IP from a Database")
                    vt_op = input("-> ")
                    if vt_op == "1":
                        VT.virustotalfunc()
                        input("Press Enter to continue...")
                    elif vt_op == "2":
                        vtfile.file_scan_function()
                        input("Press Enter to continue...")   
                    elif vt_op == "3":
                        vtdatabase.vtdatabasefunc()
                        input("Press Enter to continue...")
                    else:
                        print("Invalid Input. Try again.")
                    repeat = input("Do you want to repeat the VirusTotal Menu? (Y/N) ")
                    if repeat.lower() != "y":
                        os.system('clear')
                        break
            case "4":
                while True:
                    ALIENRAW.alienvaultipreportfunc()
                    input("Press Enter to continue...")
                    repeat = input("Do you want to repeat the AlienVault Menu? (Y/N) ")
                    if repeat.lower() != "y":
                        break
            case "5":
                while True:
                    print("\n----- Process File Data Menu -----")
                    print("Which type of file do you want to extract information from?")
                    print("1. Firewall Logs")
                    print("2. Excel Files")
                    print("3. Exit")
                    logs_op = input("-> ")
                    if logs_op == "1":
                        print("What type of data do you want to extract from your Firewall logs?")
                        print("\n----- Firewall Logs Menu -----")
                        print("1. HTTP & HTTPS access attempts")
                        print("2. SSH access attempts")
                        print("3. Exit to main menu")
                        logs_op2 = input("-> ")
                        if logs_op2 == "1":
                            processlogshttphttps.processlogshttphttps()
                            input("Press Enter to continue...")
                        elif logs_op2 == "2":
                            processlogs.process_ssh_log_filesfunc()
                            input("Press Enter to continue...")
                        
                        elif logs_op2 == "3":
                            break
                        else:
                            print("Invalid Input. Try again.")
                        repeat = input("Do you want to repeat the Process File Data Menu? (Y/N) ")
                        if repeat.lower() != "y":
                            break
                    if logs_op == "2":
                        exceltodb.exceltodbfunc()
                        input("Press Enter to continue...")
                    if logs_op == "3":
                        break
            case "6":
                while True:
                    jupytergraphics.jupyterfunc()
                    input("Press Enter to continue...")
                    repeat = input("Do you want to repeat the Jupyter-Notebooks Graphical integration? (Y/N) ")
                    if repeat.lower() != "y":
                        break
            case "9":
                print("See you on the other side...")
                return
            case _:
                print("Invalid Input. Try again.")

menu(option)