from datetime import datetime
import pandas as pd

from config import config


# Class for a Contact

class Contact ():

  def __check_mandatory_fields (self, data):
    if config['debug']:
      print ('[Checking for mandatory fields]')
    _missing = []
    # Check that no mandatory columns are missing
    for _key in config['contact_cols_mand']:
      if _key not in data.keys():
        print (f'[WARNING] Missing data for {_key}')
        _missing.append(_key)
      else:
        print (f'[Yay!] We wanted: {_key}')
    return _missing
  
  def __get_date_time_now (self):
    _dt = datetime.now()
    return _dt

  # Init Function
  def __init__(self):
    if config['debug']:
      print ("[INIT-Contact][Setting Empty Dataframe]")
    self.data = {}
    self.data['updated'] = self.__get_date_time_now()
    self.fields = []

    print (self.data)

  # Print me...
  def __str__(self):
    _string = str(self.data)
    return _string
  
  # New --> Amend
  def new (self, data):
    return (self.amend(data))
  
  # Amend
  def amend (self, data):
     
    if config['debug']:
        print ()
        print (f'[Amending Contact Object using: {list(data.keys())}')

    _missing = []
    print ("Current data keys", self.data.keys(), self.fields)
    #if 'updated' in self.fields:    # If we care about mandatory fields. :)
    _missing = self.__check_mandatory_fields(data)
    #if len(_missing) == 0:
    self.data |= data
    self.data['updated'] = self.__get_date_time_now()
    self.fields = self.data.keys()
    #else:
    return _missing



# Class for Contacts Database


class ContactsDB:
  
  # Init Function
  def __init__(self):

    contacts = pd.DataFrame(columns=config['contact_cols'])
    if config['debug']:
        print ("[INIT-ContactDB] [Setting Empty Dataframe]")

  # Print me...
  def __str__(self):
    _string = str(self.contacts.shape)
    return _string
  

  def add (self, data_dict):

    # Assue it's all good data for now :)
    _df = pd.DataFrame.from_dict(data_dict, orient='columns')
    self.contacts.append(_df)