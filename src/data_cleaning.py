import pandas as pd
import numpy as np

def read_data(file):
    df = pd.read_csv(file)
    return df

def column_cleaner(df):
    df.drop(['Unnamed: 23','Unnamed: 24','Unnamed: 25','Unnamed: 26','Unnamed: 27'],axis=1,inplace=True)
    df.columns = ['interview_date','client_name', 'industry', 'location',
       'interview_position', 'skillset', 'interview_type', 'name', 'gender',
       'candidate_current_location', 'candidate_job_location',
       'interview_venue', 'candidate_native_location', 'start_time_permission',
       'hope_no_unscheduled', 'call_3_hours_prior', 'alternative_number',
       'printed_resume_read_jd', 'can_find_interview', 'call_letter_shared',
       'expected_attendance', 'actual_attendance', 'marital_status']
    return df


def date_converter(df):
    df['interview_date'].replace(['25 – Apr-16'],'25.04.2016',inplace=True)
    df['interview_date'] = df['interview_date'].str[:10]
    df['interview_date'] = pd.to_datetime(df['interview_date'])
    return df

def fillnas(df):
    df.fillna("empty", inplace= True)
    return df


def lower_all_data(df):
    columns = ['client_name', 'industry', 'location',
       'interview_position', 'skillset', 'interview_type', 'name', 'gender',
       'candidate_current_location', 'candidate_job_location',
       'interview_venue', 'candidate_native_location', 'start_time_permission',
       'hope_no_unscheduled', 'call_3_hours_prior', 'alternative_number',
       'printed_resume_read_jd', 'can_find_interview', 'call_letter_shared',
       'expected_attendance', 'actual_attendance', 'marital_status']

    for ind_col in columns: 
        df[ind_col] = df[ind_col].apply(lambda x: str(x).lower())
    return df

def clean_data_values(df):
    # drop where gender is Nan
    df = df.drop(index=1233)

    # synthesize to consistent names for current loc
    df['candidate_current_location'] = df['candidate_current_location'].replace({'chennai':'Chennai', 'chennai ':'Chennai', 'CHENNAI':'Chennai', '- Cochin- ':'Cochin'})

    # consistent names for job loc
    df['candidate_job_location'] = df['candidate_job_location'].replace({'- Cochin- ':'Cochin'})

    # consistent names for interview venue
    df['interview_venue'] = df['interview_venue'].replace({'- Cochin- ':'Cochin'})

    # consistent locations for native loc
    df['candidate_native_location'] = df['candidate_native_location'].replace({'- Cochin- ':'Cochin', 'Dehli/ NCR': 'NCR'})

    df['can_find_interview'] = df['can_find_interview'].replace({"yes": "yes", "na": "no", "no- i need to check": "no", "na": "no"})
    df['call_letter_shared'] = df['call_letter_shared'].replace({'yes': 'yes', 'nan':'no', 'havent checked':'no', 'need to check': 'no', 'not sure': 'no','yet to check': 'no', 'not yet': 'no', 'na': 'no'})
    df['expected_attendance'] = df['expected_attendance'].replace({"yes": "yes", "uncertain": "no", "nan": "no", "11:00 am": "yes", "10.30 am": "yes"})
    df['actual_attendance'] = df['actual_attendance'].apply(lambda x: x.strip())

    df['printed_resume_read_jd'].replace(['yes '],'yes',inplace=True)
    df['printed_resume_read_jd'].replace(['no- will take it soon','not yet','na'],'no',inplace=True)

    df['call_3_hours_prior'].replace(['no dont','na'],'no',inplace=True)

    df['alternative_number'].replace(['no i have only thi number','na'],'no',inplace=True)

    df['hope_no_unscheduled'].replace(['not sure','na','cant say','not sure'],'no',inplace=True)

    df['start_time_permission'].replace(['yet to confirm','na','not yet'],'no',inplace=True)

    df['interview_type'].replace(['scheduled walk in', 'sceduled walkin'], 'scheduled walkin', inplace=True)
    df['interview_type'].replace('walkin ', 'walkin', inplace=True)
    df['interview_type'].replace('scheduled ', 'scheduled', inplace=True)

    df['skillset'].loc[df['skillset'].str.contains('java')] = 'java'
    df['skillset'].loc[df['skillset'].str.contains('sccm')] = 'sccm'
    df['skillset'].loc[df['skillset'].str.contains('lead')] = 'technical lead'
    df['skillset'].loc[df['skillset'].str.contains('cots')] = 'cots'
    df['skillset'].loc[df['skillset'].str.contains('kyc')] = 'kyc'
    df['skillset'].loc[df['skillset'].str.contains('lending')] = 'l & l'
    df['skillset'].loc[df['skillset'].str.contains('analytical')] = 'analytical r&d'
    df['skillset'].replace(['9.00 am', '10.00 am', '11.30 am', '12.30 pm', '9.30 am'], 'None', inplace=True)
    return df

def dummy_data(df):
    new_df = df.drop(columns=['interview_date','name'], axis=1)
    new_df = pd.get_dummies(new_df, drop_first=True)
    return new_df

if __name__ == '__main__':
    file = '../data/Interview.csv'
    df = read_data(file)
    df = column_cleaner(df)
    df = date_converter(df)
    df = fillnas(df)
    df = lower_all_data(df)
    df = clean_data_values(df)
    new_df = dummy_data(df)