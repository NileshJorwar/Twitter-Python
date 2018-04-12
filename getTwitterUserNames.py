# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 14:59:09 2018

@author: niles
"""

import pandas as pd
from bs4 import BeautifulSoup
import urllib
import csv

def main():
    
    coname_twitter_account_file = pd.read_excel('coname_twitter_account.xlsx', sheetname='coname')
    getUserName(coname_twitter_account_file)
    print('Work Done...')
def getUserName(coname_twitter_account_file):
    
    k=1
    with open('coname_twitter_account_users.csv', 'a',newline='') as myFile:
        writer = csv.writer(myFile)
        writer.writerow(["Company Name", "Main Twitter Handle", "Other Twitter Handles"])
        for i in coname_twitter_account_file.index:
            twitterHandleCollections=[]
            coname=coname_twitter_account_file['coname'][i]
            twitterMainHandle=coname_twitter_account_file['twitter main account'][i]        
            twitterHandleCollections.append(coname_twitter_account_file['twitterOtherHandle1'][i])
            twitterHandleCollections.append(coname_twitter_account_file['twitterOtherHandle2'][i])
            twitterHandleCollections.append(coname_twitter_account_file['twitterOtherHandle3'][i])
            twitterHandleCollections.append(coname_twitter_account_file['twitterOtherHandle4'][i])
            twitterHandleCollections.append(coname_twitter_account_file['twitterOtherHandle5'][i])
            twitterHandleCollections.append(coname_twitter_account_file['twitterOtherHandle6'][i])
            twitterHandleCollections.append(coname_twitter_account_file['twitterOtherHandle7'][i])
            twitterHandleCollections.append(coname_twitter_account_file['twitterOtherHandle8'][i])
            twitterHandleCollections.append(coname_twitter_account_file['twitterOtherHandle9'][i])
            twitterUserMainHandle=None
            twitterUserOtherHandle=None
            writeCSVTwitterData=[]
            if pd.isnull(twitterMainHandle):
                twitterMainHandle=None
                writeCSVTwitterData.append(coname)
                writeCSVTwitterData.append(twitterUserMainHandle)            
                #writeCSVTwitterUserNames=[[coname, twitterUserMainHandle]]
            else:
                home_url=twitterMainHandle
                html = urllib.request.urlopen(home_url).read()    
                soup_sub_html=BeautifulSoup(html,'html.parser')
                twitterUserMainHandle = soup_sub_html.find('a',attrs={'class':'ProfileHeaderCard-screennameLink u-linkComplex js-nav'}).get('href')
                #print(twitterUserMainHandle)
                writeCSVTwitterData.append(coname)
                writeCSVTwitterData.append(twitterUserMainHandle.replace('/','@'))
                #writeCSVTwitterUserNames=[[coname, twitterUserMainHandle]]
            for handle in twitterHandleCollections:
                if pd.isnull(handle):
                    temp=handle
                    #print(handle)
                else:
                    try:                    
                        home_url=handle
                        html = urllib.request.urlopen(home_url).read()    
                        soup_sub_html=BeautifulSoup(html,'html.parser')
                        twitterUserOtherHandle = soup_sub_html.find('a',attrs={'class':'ProfileHeaderCard-screennameLink u-linkComplex js-nav'}).get('href')
                        #writeCSVTwitterUserNames=[[coname, twitterUserOtherHandle]]
                        writeCSVTwitterData.append(twitterUserOtherHandle.replace('/','@'))
                    except Exception as e:
                        twitterUserOtherHandle=e
                        continue
                    #print(twitterUserOtherHandle)
            print(writeCSVTwitterData)
            print(k)
            writer.writerow(writeCSVTwitterData)        
            writeCSVTwitterData=None
            k=k+1                
                    
if __name__ == '__main__':
    main()        