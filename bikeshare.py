import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

"""
Introduction and User Name
"""
name = input('How is your name? ')
print('Hello',name.title(),', welcome to the Bikeshare Analysis. I can give many insights into our bikeshare usage. Would you like to see data for Chicago, New York or Washington?')

"""
Asking for the city input
"""
city_input = input('Please type in Chicago, New York City or Washington: ')
while city_input.lower() not in ('washington', 'new york city', 'chicago'):
    print('Sorry, I did not get the answer. Can you repeat the input and type in \'Chicago\', \'Washington\' or \'New York City\'?')
    city_input = input()

"""
Asking for the month
"""
month_input = input('For which month shall I do the analysis? Please type in \'January, February, March, April, May, June\'or \'all\' if you prefer the analysis without filters: ')
while month_input.lower() not in ('january, february, march, april, may, june, all'):
    print('Sorry, I did not get the answer. Can you repeat the input and type in \'January, February, March, April, May, June\'or \'all\'')
    month_input = input()
"""
Asking for the day selection
"""
day_input = input('Do you have a preferred day of week? Please type in \'Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday\' or \'all\' if you prefer the analysis without filters: ')
while day_input.lower() not in ('monday, tuesday, wednesday, thursday, friday, saturday, sunday, all'):
    print('Sorry, I did not get the answer. Can you repeat the input and type in \'January, February, March, April, May, June\'or \'all\'')
    day_input = input()

def get_filters (city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
       months = ['january', 'february', 'march', 'april', 'may', 'june']
       month = months.index(month) + 1

        # filter by month to create the new dataframe
       df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """
    Display the mean travel time """
    print('\n' 'Information about the mean travel time:')
    popular_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', popular_hour)
    popular_month = df['month'] = df['month'].mode()[0]
    print('Most Common Month:', calendar.month_name[popular_month])
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most Common Day of week:', popular_day_of_week)

def station_stats(df):
    """
    Display the mean stations and spots """
    print('\n' 'Information about the mean stations and spots:')
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station: ', popular_start_station)
    popular_end_station = df['End Station'].mode()[0]
    print('Most Common End Station: ', popular_end_station)

    #Create an additional column to combine start and end information
    df['Whole Trip'] = df['Start Station'] + ' - ' + df['End Station']
    popular_trip = df['Whole Trip'].mode()[0]
    print('Most Common Trip From Start to End: ', popular_trip)

def trip_duration_stats(df):
    """
    Display information about trip duration """
    print('\n' 'Information about the trip duration:')
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time: ', total_travel_time)
    avg_travel_time = df['Trip Duration'].mean()
    print('Average Travel Time: ', avg_travel_time)

def user_stats(df):
    """
    Display user information """
    print('\n' 'Information about the users:')
    user_type_counts = df['User Type'].value_counts()
    print('Counts of each user type: ', user_type_counts)
    if city_input in ('Chicago', 'New York City', 'chicago', 'new york city'):
        gender_counts = df['Gender'].value_counts()
        print('Counts of each gender: ', gender_counts)
        earliest_birth_year = df['Birth Year'].min()
        print('Earliest Year of Birth: ', int(earliest_birth_year))
        recent_birth_year = df['Birth Year'].max()
        print('Most recent Year of Birth: ', int(recent_birth_year))
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('Most common Year of Birth: ', int(most_common_birth_year))
    elif city_input in ('Washington', 'washington'):
        print ('I don\'t have any further user information for Washington')

def raw_data(df):
    """
    Giving raw data based on user feedback """
    raw_data = input('\n' 'Do you want to have a look into the raw data? Please type in Yes or No: ')
    while raw_data.lower() != 'no':
        print(df.head())
        raw_data = input('\n' 'Do you want to see five additional rows of the data?')

def main():
    while True:
        city_input.lower() in ('washington', 'chicago', 'new york city') and day_input.lower() in ('monday', 'tuesday','wednesday','thursday','friday', 'all',) and month_input.lower() in ('','january', 'february', 'march', 'april', 'may', 'june', 'all')

        df = get_filters(city_input.lower(), month_input.lower(), day_input.lower())

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\n' 'Would you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
