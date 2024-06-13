# Load in Application Config

#import logger

config = {}

config['debug'] = True

config['logbook_cols'] = ['owner', 'call_sign', 'date_start','mode','freq_tx', 'freq_rx', 'updated']
config['logbook_cols_mand'] = ['owner', 'call_sign', 'date_start','mode', 'freq_tx']
config['contact_cols'] = ['owner', 'call_sign', 'qth','first_name','grid_square', 'updated']
config['contact_cols_mand'] = ['owner', 'call_sign', 'first_name']
