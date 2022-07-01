# -*- coding: utf-8 -*-
import json
import requests
from typing import Dict
from dataclasses import dataclass
from random_username.generate import generate_username
import random
import string
from time import sleep



class Germail:
    def __init__(self,create=True,password=None):
        """
        create temporary email 
        
        **Parameters**
            - **create** : if create True we create new email 
            if False not create new email
            - **password** : user password if you want a password
            if not ... the password will generate randomly

        """

        self.user_password=password
        self.stat_login=False
        self.messages=None
        self.api_address = "https://api.mail.tm"
        if create==True:
            username = (generate_username(1)[0]).lower()
            domain = random.choice(list(map(lambda x: x["domain"],
            requests.get("{}/domains".format(self.api_address)).json()["hydra:member"])))
            address = "{}@{}".format(username, domain)
            if self.user_password is not None:
                self.password=self.user_password
            else:
                self.password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(6))

            self.address = address
            try:
                acco = self._make_account_request("accounts",
                                            self.address, self.password)
                self.id_=acco["id"]
                print("email : ",self.address ,"\n","password : ",self.password)
                print("")
                self.login()
            except:
                self.new_account()
            


    def renew_account(self):
        """
        delete the last account and renew an other account
        """

        if self.stat_login==True:
            self.delete_account()
            self.__init__(create=True)
            return True
        else:
            print("can not renew emty account !!\ntry new_account")
            return False

    def new_account(self):
        """
        create new account
        """

        self.__init__(create=True,password=self.user_password)
        return True
        
    def login(self,email=None,password=None):
        """
        login into account if email and password is None login
        automatique in the new email

        **Parameters**
            - **email** : email of your created account
            - **password** : password of your account
        """

        if email is not None:
            try:
                jwt = self._make_account_request("token",
                                           email, password)
                self.auth_headers = {
                    "accept": "application/ld+json",
                    "Content-Type": "application/json",
                    "Authorization": "Bearer {}".format(jwt["token"])
                    }
                self.address=email
                self.password=password
                r = requests.get("{}/me".format(self.api_address),
                headers=self.auth_headers)
                self.id_=r.json()["id"]
                self.stat_login=True
            
            except Exception as e:
                print(e,"or not true information login")
                self.stat_login=False
                return False
            

        jwt = self._make_account_request("token",
                                           self.address, self.password)
        self.auth_headers = {
            "accept": "application/ld+json",
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(jwt["token"])
        }
        self.stat_login=True
        return jwt

    def get_mail(self):
        """
        get the email of account
        """

        return self.address

    def get_password(self):
        """
        get the password of account
        """

        return self.password

    def get_info(self):
        """
        get the email and password and id of account
        """

        return (self.address,self.password,self.id_)

    def get_messages(self, page=1):
        """
        get all messages

        **Parameters**
            - **page** : page of inbox if page=1 return the new messages
        """

        if self.stat_login==True:
            r = requests.get("{}/messages?page={}".format(self.api_address, page),
                            headers=self.auth_headers)
            messages = []
            for message_data in r.json()["hydra:member"]:
                # recover full message
                r = requests.get(
                    f"{self.api_address}/messages/{message_data['id']}", headers=self.auth_headers)
                text = r.json()["text"]
                html = r.json()["html"]
                # prepare the mssage object
                messages.append(Message(
                    message_data["id"],
                    message_data["from"],
                    #message_data["to"],
                    message_data["subject"],
                    #message_data["intro"],
                    text,
                    html,
                    #message_data
                     ))
            self.messages=messages
            return messages
        else:
            print("cant read message without login")
            return False
            


    def delete_account(self):
        """
        delete your account

        """

        if self.stat_login==True:
            r = requests.delete("{}/accounts/{}".format(self.api_address,
                                                        self.id_), headers=self.auth_headers)
            print(self.address," Deleted !\n\n")
            self.id_=None
            self.auth_headers=None
            self.password=None
            self.stat_login=False
            self.messages=None
            return r.status_code == 204
        else:
            print("can not delete emty account !!")
            return False

    def read_message(self, id):
        """
        Read a message by id , you can get it with get_massages Function

        **Parameters**
            - **id** : ID of the message
        """

        if self.stat_login==True:
            r = requests.get(
                f"{self.api_address}/messages/{id}", headers=self.auth_headers)
            text = r.json()["text"]
            html = r.json()["html"]
            message_data=r.json()
            message=Message(
                    message_data["id"],
                    message_data["from"],
                    #message_data["to"],
                    message_data["subject"],
                    #message_data["intro"],
                    text,
                    html,
                    #message_data
                    )
            return message
        else:
            NoMessageFound()
            print("cant read message without login")
            return Message(None,None,None,None,None)
            
    def get_last_message(self,r=True):
        """
        Get the last message in the email

        **Parameters**
            - **r** : refresh all the messages if True 
        """

        if self.stat_login==True:
            if r==False:
                if self.messages is None:
                    self.get_messages()
                return self.messages[0]
            else:
                self.get_messages()
                return self.messages[0]
        else:
            print("cant read message without login")
            NoMessageFound()
            return Message(None,None,None,None,None)

    def monitor_account(self):
        """Keep waiting for new messages ."""
        
        if self.stat_login==True:
            k=False
            while k==False:
                print("\nWaiting for new messages...")
                start = len(self.get_messages())
                while len(self.get_messages()) == start:
                    sleep(1)
                print("New message arrived!")
                k=True
            return True
        else:
            print("cant waitting a message without login !!",
            "\ntry login in account for do that\n")
            return False

    def _make_account_request(self,endpoint, address, password):
        account = {"address": address, "password": password}
        headers = {
            "accept": "application/ld+json",
            "Content-Type": "application/json"
        }
        r = requests.post("{}/{}".format(self.api_address, endpoint),
                          data=json.dumps(account), headers=headers)
        if r.status_code not in [200, 201]:
            print(r.status_code,"Unprocessable entity")
            raise CouldNotGetAccountException()
        return r.json()




@dataclass
class Message:
    id_: str
    from_: Dict
    #to: Dict
    subject: str
    #intro: str
    text: str
    html: str
    #data: Dict



class CouldNotGetAccountException(Exception):
    """Raised if a POST on /accounts or /authorization_token return a failed status code."""

class NoMessageFound(Exception):
    """Raised if a POST on /accounts or /authorization_token return a failed status code."""
        
